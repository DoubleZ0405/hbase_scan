from kazoo.client import KazooClient
from mod_toop import *
import logging


class ZkProxy:
    def __init__(self, conf):
        self.conf = conf
        logging.debug("The zk Addr is ")
        logging.debug(self.conf.zkAddr)
        zk = KazooClient(hosts=self.conf.zkAddr)
        zk.start()
        self.zk = zk
        pass

    def get_ctrl_addr(self):
        return "10.255.0.11"
        # children = self.zk.get_children(path=self.conf.zkPath + "/" + self.conf.ctrlName)
        # for c in children:
        #     logging.debug(c)
        #     data = self.zk.get(path=self.conf.zkPath + "/" + self.conf.ctrlName + "/" + c)
        #     logging.debug(data)
        #     detail = InstanceDetails()
        #     detail.__dict__ = data
        #     if detail.namespace == self.conf.namespace and detail.myIp != "":
        #         return detail.myIp
        # return ""

