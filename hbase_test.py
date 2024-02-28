# import hbase
# from hbase.client.filters import *
import happybase
from flask import Flask
from proxy_common import ProxyConf
from ctrl_proxy import *
from get_topo import *
import struct
import os
import json
import time
from kazoo.client import KazooClient
app = Flask(__name__)
app.debug = True
zk = 'xx:xx'


# @app.route('/calc-attenuation', methods=['GET', 'POST'])
# def calc():
#     fs = open("hbase", 'w')
#     count = 100
#     with hbase.ConnectionPool(zk).connect() as conn:
#         print(conn.namespaces())
#         tables = conn.namespace('toop').tables()
#         print(tables)
#         table = conn['toop']['supervisory_channel']
#         fil = Filter("SingleColumnValueFilter ('PM', 'name', =, 'binary:INTERFACE-1-1-LINEOSC')")
#         # fil = KeyOnlyFilter("timestamp")
#         for row in table.scan(filter_=fil):
#             count -= 1
#             if count < 0:
#                 break
#             print(row)
#             fs.write(str(row)+"\n")
#         # supervisory_channel
#         # for t in tables:
#         #     for row in
#         print(conn['toop'])
#     fs.close()

@app.route('/calc-topo', methods=['GET', 'POST'])
def cal_topo():
    conf = ProxyConf("am.yaml")
    conf.set_conf()
    cp = CtrlProxy(conf)
    topology = cp.ctrl_get_phy_topo()
    # f_json = open("data", 'r')
    # json_data = f_json.read()
    # f_json.close()
    # pt = PhyTopoRep()
    # json_deserialize(json_data, pt)
    # topology = pt.topology[0]
    newTopo = get_new_topo(topology)
    print("hello")
    # f_data = open("data.json", 'w')
    # f_data.write(str(data))
    # f_data.close()


@app.route('/calc-happy', methods=['GET', 'POST'])
def cal_happy():
    connection = happybase.Connection('ip', port=6004, autoconnect=False)
    # before first use:
    connection.open()
    print("dhsiuhgfiudshfiuds")
    print(connection.tables())
    table = connection.table('toop:supervisory_channel')
    t1 = time.time()
    print(t1)
    # query_str = "ColumnPrefixFilter('your_prsifx_str') AND TimestampsFilter(your_timestamp)"
    try:
        query_str = "SingleColumnValueFilter('PM', 'timestamp', =, 'binary:1605756592000')"
        # for k, v in table.scan():
        #     print(k, v)
        #     break
        for k, v in table.scan(filter=query_str):
            print(k, v)
        # fs.close()
    except Exception as e:
        print(e)
    t2 = time.time()
    print(t2)
    print(t2-t1)
    print("dhsuifdhiudfhsiu")
    connection.close()

@app.route('/calc-happy', methods=['GET', 'POST'])
def get_hbase_addr():
    zk = KazooClient(hosts="xxx:2181")
    zk.start()
    zk_walk(zk, '/', printZNode)
    # for c in children:
    #     # logging.debug(c)
    #     data = zk.get("xxx:2181/" + c)
    #     print(data)
    #     # logging.debug(data)
    #     # detail = InstanceDetails()
    #     # detail.__dict__ = data
    #     # if detail.namespace == self.conf.namespace and detail.myIp != "":
    #     #     return detail.myIp
    #
    # zk.stop()

#
def zk_walk(_zk, node, func):
    data, stat = _zk.get(node)
    children = _zk.get_children(node)
    func(node, data, stat, children)
    if len(children) > 0:
        for sub in children:
            sub_node = ''
            if node != '/':
                sub_node = node + '/' + sub
            else:
                sub_node = '/' + sub
            zk_walk(_zk, sub_node, func)


def printZNode(node, data, stat, children):
    print("node  : " + node)
    print("data  : " + str(data))
    # print(json.dumps(data))
    print("stat  : " + str(stat))
    print("child : " + str(children))
    print("\n")


if __name__ == '__main__':
    print("hellodgdsufdsgif")
    print(happybase.__version__)
    get_hbase_addr()
    # cal_topo()
    # cal_happy()
    app.run(host='0.0.0.0', port=8080, threaded=True)
