data=[
    {'id':1,'parentId':None},
    {'id':2,'parentId':1},
    {'id':3,'parentId':1},
    {'id':4,'parentId':2},
]

# Step 1: Identify the root node(s)
root_nodes = [node for node in data if node['parentId'] is None]

# Step 2: Traverse the tree and assign levels
node_levels = {}
stack = [node['id'] for node in root_nodes]
level = 0
while stack:
    node_id = stack.pop()
    if node_id not in node_levels:
        node_levels[node_id] = level
        for child in data:
            if child['parentId'] == node_id:
                stack.append(child['id'])
    level += 1
# Assign levels to nodes in the original data list
for node in data:
    node['node_level'] = node_levels.get(node['id'], 0)

# Step 3: Print the final list
print(data)

##############################################################################
data = [
    {'id': 1, 'parentId': None, 'node_level': 0},
    {'id': 2, 'parentId': 1, 'node_level': 1},
    {'id': 3, 'parentId': 1, 'node_level': 1},
    {'id': 4, 'parentId': 2, 'node_level': 2},
]

def create_final_entry(node_id, data, node_levels):
    entry = {}
    node = next((n for n in data if n['id'] == node_id), None)
    if node:
        entry[f'level_{node_levels[node_id]}'] = node['id']
        for child_id in [child['id'] for child in data if child['parentId'] == node_id]:
            child_entry = create_final_entry(child_id, data, node_levels)
            if child_entry:
                entry.update(child_entry)
        return entry
    return None
final = [create_final_entry(node['id'], data, {node['id']: node['node_level'] for node in data}) for node in data if node['parentId'] is None]

print(final)
