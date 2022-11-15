param = {'current_stage': 1, 
        'count_stage': 1,
        'param_coast': 0,
        'param_stage': 1,
        'param_factor': [2],
        'param_avalible': [5],
        'param_status': ['идёт в данный момент'],
        'param_sale': [3],
        'coast': 35}

row = [{'type': 'Common'}, {'type': 'E'}, {'type': 'X'}, {'type': 'Common'}]

# print(row.count({'type': 'Common'}))
# print(row.count({'type': 'E'}))
# print(row.count({'type': 'X'}))
# print(row.count({'type': 'G'}))

name = ['Common', 'Rare', 'Epic', 'Legedary', 'Exclusive']

count_nft = []

for elem in name:
    count_nft.append(row.count({'type': elem}))

print(count_nft)