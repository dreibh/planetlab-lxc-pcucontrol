from pcucontrol.reboot import *
import time

class DRAC(BasicPCUControl):
    supported_ports = [22,443,5869]
    def run_drac(self, node_port, dryrun):
        return self.run_expect_script("DRAC.exp racadm", dryrun=dryrun, model="None", ip=True)

    def run_ssh(self, node_port, dryrun):
        return self.run_expect_script("DRAC.exp ssh", dryrun=dryrun, model="None")

    def pcu_run(self, node_port, dryrun=False):
        r = self.run_ssh(node_port, dryrun=False)
        if "No error" in r:
            return r
        r2 = self.run_drac(node_port, dryrun=False)
        if "No error" in r2:
            return r2
        return r + " :: " +r2

    def pcu_test(self, node_port, dryrun=True):
        r = self.run_ssh(node_port, dryrun=True)
        if "No error" in r:
            return r
        r2 = self.run_drac(node_port, dryrun=True)
        if "No error" in r2:
            return r2
        return r + " :: " +r2
