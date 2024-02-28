from zk_proxy import ZkProxy
from proxy_common import do_get
from mod_toop import *
import logging
from Json import *
GET_PHY_TOPO_URL = "http://{}:8181/restconf/operational/network-topology:network-topology" //ODL topo
GET_PHY_LINK_URL = GET_PHY_TOPO_URL + "/link/{}"


class CtrlProxy:
    def __init__(self, conf):
        self.conf = conf
        pass

    # 从controller获取物理拓扑
    def ctrl_get_phy_topo(self):
        zp = ZkProxy(self.conf)
        # 获取controller所在主机
        host = zp.get_ctrl_addr()
        logging.debug("The host addr: ")
        logging.debug(host)
        data = do_get(url=GET_PHY_TOPO_URL.format(host), name=self.conf.ctrlUserName, pwd=self.conf.ctrlPwd)
        logging.debug("The topo data: ")
        zp.zk.stop()
        pt = PhyTopoRep()
        json_deserialize(data, pt)
        return pt.topology[0]



