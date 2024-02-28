import yaml
import requests
import logging
import base64

class ProxyConf:
    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.namespace = ""
        self.zkAddr = []
        self.algoAddr = ""
        self.zkPath = ""
        self.ctrlName = ""
        self.ctrlUserName = ""
        self.ctrlPwd = ""
        self.timeout = ""
        self.log = ""

    def set_conf(self):
        f_yaml = open("am.yaml", 'r', encoding='UTF-8')
        conf = yaml.load(f_yaml.read(), Loader=yaml.FullLoader)
        f_yaml.close()
        namespace = conf['client']['proxy']['namespace']
        name = conf['client']['proxy']['controller']['name']
        username = conf['client']['proxy']['controller']['username']
        pwd = conf['client']['proxy']['controller']['password']
        zkUrl = conf['client']['proxy']['zk']
        algoAddr = conf['client']['proxy']['algo']
        timeout = conf['client']['proxy']['timeout']
        log = conf['plugins']['log']['default'][0]['level'] # console log
        self.namespace = namespace
        self.ctrlName = name
        self.ctrlUserName = username
        self.ctrlPwd = pwd
        self.algoAddr = algoAddr
        self.timeout = timeout

        idx = zkUrl.index("/")
        if idx <= 0:
            zkAddr = ""
            zkPath = zkUrl
        else:
            zkAddr = zkUrl[:idx].split(",")
            zkPath = zkUrl[idx:]

        self.zkPath = zkPath
        self.zkAddr = zkAddr
        self.zkAddr = ','.join(self.zkAddr)
        self.log = log

        if log == "debug":
            logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -%(message)s')
        elif log == "info":
            logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s -%(message)s')
        elif log == "warning":
            logging.basicConfig(level=logging.WARNING, format=' %(asctime)s - %(levelname)s -%(message)s')
        elif log == "error":
            logging.basicConfig(level=logging.ERROR, format=' %(asctime)s - %(levelname)s -%(message)s')
        elif log == "critical":
            logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s -%(message)s')
        else:
            logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -%(message)s')


def do_get(url, name, pwd):
    logging.debug(name+" : "+pwd)
    # header = {"Authorization": "Basic " + str(base64.b64encode(bytes(name + ":" + pwd, encoding="UTF-8")))}
    header = {"Authorization": "Basic YWRtaW46VG9vcEAxMjM="}
    logging.debug(header)
    req = requests.request(url=url, method="Get", headers=header)
    # print(req.text)
    return req.text
