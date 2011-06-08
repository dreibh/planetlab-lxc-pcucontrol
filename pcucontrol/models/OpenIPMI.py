
from pcucontrol.reboot import *
import subprocess

class OpenIPMI(PCUControl):

	supported_ports = [80,443,623]

	# TODO: get exit codes to determine success or failure...
	def run_http(self, node_port, dryrun):
		return self.run_ipmi(node_port, dryrun)
	def run_https(self, node_port, dryrun):
		return self.run_ipmi(node_port, dryrun)

	def run_ipmi(self, node_port, dryrun):

		if not dryrun:
			ipmi_cmd = "power cycle"
		else:
			ipmi_cmd = "user list"

		cmd = "ipmitool -I lanplus -H %s -U %s -P '%s' %s"
		cmd = cmd % ( self.host, self.username, self.password, ipmi_cmd )
		p = subprocess.Popen(cmd, shell=True, 
					   stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
					   stderr=subprocess.STDOUT, close_fds=True)
		(i,p) = (p.stdin, p.stdout)
		result = p.read()
		#print "RESULT: ", result

		if "Error" in result:
			return result
		else:
			return 0
