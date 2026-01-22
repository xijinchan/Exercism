class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if records == []: return None
    records.sort(key=lambda x: x.record_id)

    if records[0].record_id != 0: raise ValueError("Record id is invalid or out of order.")
    for k in range(len(records)):
        if k < len(records)-1:
            if records[k].record_id != (records[k+1].record_id - 1): raise ValueError('Record id is invalid or out of order.')
        if all([records[k].parent_id == records[k].record_id, records[k].record_id != 0]): raise ValueError("Only root should have equal record and parent id.")
        if records[k].parent_id > records[k].record_id: raise ValueError("Node parent_id should be smaller than it's record_id.")    
    
    all_nodes = [Node(k.record_id) for k in records]
    records_by_parent_id = [k for k in records]
    records_by_parent_id.sort(key=lambda x: x.parent_id, reverse=True)

    for record in records_by_parent_id:
        if record.record_id == 0: continue
        for node in all_nodes:
            if record.parent_id == node.node_id:
                node.children.append(all_nodes[record.record_id])
                break

    return all_nodes[0]
    