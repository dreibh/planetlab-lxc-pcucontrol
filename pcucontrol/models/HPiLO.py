from pcucontrol.reboot import *
from distutils.sysconfig import get_python_lib; 
import subprocess

class HPiLO(PCUControl):
    supported_ports = [22,443]
    def run(self, node_port, dryrun):
        if self.type == Transport.SSH:
            return self.run_ssh(node_port, dryrun)
        elif self.type == Transport.HTTP or self.type == Transport.HTTPS:
            return self.run_https(node_port, dryrun)
        else:
            raise ExceptionNoTransport("Unimplemented Transport for HPiLO %s" % self.type)

    def run_ssh(self, node_port, dryrun):

        self.transport.open(self.host, self.username)
        self.transport.sendPassword(self.password)

        # </>hpiLO-> 
        self.transport.ifThenSend("</>hpiLO->", "cd system1")

        # Reboot Outlet  N      (Y/N)?
        if dryrun:
            self.transport.ifThenSend("</system1>hpiLO->", "POWER")
        else:
            # Reset this machine
            self.transport.ifThenSend("</system1>hpiLO->", "reset")

        self.transport.ifThenSend("</system1>hpiLO->", "exit")

        self.transport.close()

        # NOTE: if an error occurs earlier, an exception should be thrown
        return 0
        
    def run_https(self, node_port, dryrun):

        locfg = command.CMD()

        cmd_str = get_python_lib(1) + "/pcucontrol/models/hpilo/"
        
        cmd = cmd_str + "locfg.pl -s %s -f %s -u %s -p '%s' "  % (
                    self.host, cmd_str+"iloxml/Get_Network.xml", 
                    self.username, self.password)
        cmd_out, cmd_err = locfg.run_noexcept(cmd)

        if locfg.s.returncode != 0:
            return cmd_out.strip() + cmd_err.strip()

        cmd = "grep 'MESSAGE' | grep -v 'No error'"
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
                            stderr=subprocess.STDOUT, close_fds=True)
        (grep_in, grep_out ) = (p.stdin, p.stdout)
        grep_in.write(cmd_out)
        grep_in.close()         # close so read does not block
        output = grep_out.read()
        if output.strip() != "":
            print "grep_out: %s" % output.strip()
            return output.strip()

        # NOTE: if an error occurs earlier, an exception should be thrown
        return 0
