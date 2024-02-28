

class PhyProvider:
	def __init__(self):
		self.attenuation_az = None
		self.attenuation_za = None


# // PhyProvider
# type PhyProvider struct {
# 	Positive float32 `json:"attenuation-az"`
# 	Reverse  float32 `json:"attenuation-za"`
# }

class Physical:
	def __init__(self):
		self.ip = None
		self.link_type = None
		self.implement_state = None
		self.provider = PhyProvider()
# // 物理属性
# type Physical struct {
# 	Ip       string      `json:"ip"`
# 	LinkType string      `json:"link-type"`
# 	State    string      `json:"implement-state"`
# 	Provider PhyProvider `json:"provider"`
# }


class PhySrc:
	def __init__(self):
		self.source_node = None
		self.source_tp = None
		self.node_ip = None

# // source terminal point
# type PhySrc struct {
# 	SrcNode string `json:"source-node"`
# 	SrcTp   string `json:"source-tp"`
# 	NodeIp  string `json:"-"`
# }


class PhyDst:
	def __init__(self):
		self.dest_node = None
		self.dest_tp = None
		self.node_ip = None


# // destination terminal point
# type PhyDst struct {
# 	DstNode string `json:"dest-node"`
# 	DstTp   string `json:"dest-tp"`
# 	NodeIp  string `json:"-"`
# }


class PhyNode:
	def __init__(self):
		self.node_id = None
		self.physical = Physical()

# // node
# type PhyNode struct {
# 	NodeId   string   `json:"node-id"`
# 	Physical Physical `json:"otn-phy-topology:physical"`
# }


class PhyLink:
	def __init__(self):
		self.link_id = None
		self.physical = Physical()
		self.source = PhySrc()
		self.destination = PhyDst()


# // link
# type PhyLink struct {
# 	LinkId   string   `json:"link-id"`
# 	Physical Physical `json:"otn-phy-topology:physical"`
# 	Src      PhySrc   `json:"source"`
# 	Dst      PhyDst   `json:"destination"`
# }


class PhyTopology:
	def __init__(self):
		self.link = [PhyLink()]
		self.node = [PhyNode()]
# // topology
# type PhyTopology struct {
# 	Link []PhyLink `json:"link"`
# 	Node []PhyNode `json:"node"`
# }


class PhyTopoRep:
	def __init__(self):
		self.topology = [PhyTopology()]
# // reply
# type PhyTopoRep struct {
# 	Topology []PhyTopology `json:"topology"`
# }


class InstanceDetails:
	def __init__(self):
		self.moduleName = None
		self.myIp = None
		self.user = None
		self.passwd = None
		self.namespace = None
# // zk InstanceDetails
# type InstanceDetails struct {
# 	ModuleName string `json:"moduleName"`
# 	MyIp       string `json:"myIp"`
# 	User       string `json:"user"`
# 	Pwd        string `json:"passwd"`
# 	Namespace  string `json:"namespace"`
# }
