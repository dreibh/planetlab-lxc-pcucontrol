from pcucontrol.reboot import *
from distutils.sysconfig import get_python_lib; 
import subprocess

class HPiLO(BasicPCUControl):
    supported_ports = [443,22]
    def run(self, node_port, dryrun):
        if self.type == Transport.SSH:
            return self.run_ssh(node_port, dryrun)
        elif self.type == Transport.HTTP or self.type == Transport.HTTPS:
            return self.run_https(node_port, dryrun)
        else:
            raise ExceptionNoTransport("Unimplemented Transport for HPiLO %s" % self.type)

    def pcu_run(self, node_port, dryrun=False):
        r = self.run_https(node_port, dryrun=False)
        if "No error" in r:
            return r
        r2 = self.run_ssh(node_port, dryrun=False)
        if "No error" in r2:
            return r2
        return r + " :: " +r2

    def pcu_test(self, node_port, dryrun=True):
        r = self.run_https(node_port, dryrun=True)
        if "No error" in r:
            return r
        r2 = self.run_ssh(node_port, dryrun=True)
        if "No error" in r2:
            return r2
        return r + " :: " +r2

    def run_ssh(self, node_port, dryrun):
        return self.run_expect_script("HPiLO.exp ssh", dryrun=dryrun, model="None")
        
    def run_https(self, node_port, dryrun):
        return self.run_expect_script("HPiLO.exp https", dryrun=dryrun, model="None")
