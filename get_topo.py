import logging
from mod_cache import *
OSC_LINK_TYPE = "ots-link"
IMPLEMENT_STATE = "implement"


def get_new_topo(topology):
    # {string: PhyNode}
    nodes = {}
    newTopo = {}
    for v in topology.node:
        if v.physical.implement_state != IMPLEMENT_STATE:
            continue
        nodes[v.node_id] = v

    # 修改link
    for v in topology.link:
        if v.physical.link_type != OSC_LINK_TYPE or v.physical.implement_state != IMPLEMENT_STATE:
            continue
        d_node = v.destination.dest_node
        s_node = v.source.source_node
        link = Link(link_id=v.link_id, src_node=s_node,
                    dst_node=d_node, src_tp_name=v.source.source_tp,
                    dst_tp_name=v.destination.dest_tp
                    )
        if nodes[link.src_node]:
            link.src_node_ip = nodes[link.src_node].physical.ip
        else:
            logging.debug("not found src node of link{}".format(v.link_id))
            continue

        if nodes[link.dst_node]:
            link.dst_node_ip = nodes[link.dst_node].physical.ip
        else:
            logging.debug("not found dst node of link{}".format(v.link_id))
            continue
        newTopo[v.link_id] = link
    return newTopo