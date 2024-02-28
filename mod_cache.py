# package mod


class Attenuation:
    def __init__(self):
        self.timestamp = None
        self.positive_attenuation = None
        self.reverse_attenuation = None
# // 衰耗数据
# type Attenuation struct {
# 	Ts       uint64  `json:"timestamp"`
# 	Positive float32 `json:"positive-attenuation"`
# 	Reverse  float32 `json:"reverse-attenuation"`
# }


class Link:
    def __init__(self, link_id, src_node, dst_node, src_tp_name, dst_tp_name):
        self.link_id = link_id
        self.src_node = src_node
        self.dst_node = dst_node
        self.src_tp_name = src_tp_name
        self.dst_tp_name = dst_tp_name
        self.src_node_ip = None
        self.dst_node_ip = None
# // link
# type Link struct {
# 	Id        string `json:"link-id"`
# 	SrcNode   string `json:"src-node"`
# 	SrcNodeIp string `json:"-"`
# 	SrcTpName string `json:"-"`
# 	DstNode   string `json:"dst-node"`
# 	DstNodeIp string `json:"-"`
# 	DstTpName string `json:"-"`
# }


class Threshold:
    def __init__(self):
        self.timestamp = None
        self.positive_threshold = None
        self.reverse_threshold = None

# // 历史阈值
# type Threshold struct {
# 	Ts       uint64  `json:"timestamp,omitempty"`
# 	Positive float32 `json:"positive-threshold,omitempty"`
# 	Reverse  float32 `json:"reverse-threshold,omitempty"`
# }


class LinkPm:
    def __init__(self):
        self.pm = [Attenuation()]
        self.history = [Threshold()]

# // link性能数据
# type LinkPm struct {
# 	Link
# 	Pm      []Attenuation `json:"pm"`
# 	History []Threshold   `json:"history"`
# }


class LinkHistoryThres:
    def __init__(self):
        self.id = None
        self.link_id = None
        self.thresholds = [Threshold()]


# // link history threshold
# type LinkHistoryThres struct {
# 	Id         string      `json:"id,omitempty"`
# 	LinkId     string      `json:"link-id,omitempty"`
# 	Thresholds []Threshold `json:"thresholds,omitempty"`
# }