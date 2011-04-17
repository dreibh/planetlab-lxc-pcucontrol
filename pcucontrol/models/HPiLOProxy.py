from pcucontrol.reboot import *
import subprocess
import urllib

class HPiLOProxy(BasicPCUControl):
    supported_ports = [80]

    def pcu_run(self, node_port):
        return self.proxy(node_port, False)
        
    def pcu_test(self, node_port):
        return self.proxy(node_port, True)

    def proxy(self, node_port, dryrun):
        return self.run_expect_script("HPiLO.exp proxy", 
                                    dryrun=dryrun, 
                                    model=self.__class__.__name__)

