# from build_graph import build_graph_pure_python

# def lcc(graph):
#     max_connect_comp = set()
#     for nodeID in graph:
#         stack = []
#         stack.append(nodeID)
#         while len(stack) > 0:
#             current_node = stack.pop()
#             if current_node not in max_connect_comp:
#                 max_connect_comp.add(current_node)
#             else:
#                 continue
#             for nei_info in graph[current_node]:
#                 stack.append(nei_info['neighbor'])

#     return max_connect_comp

# if __name__ == '__main__':
#     graph = build_graph_pure_python()
#     print('bắt đầu tìm thành phần liên thông lớn nhất')
#     l = lcc(graph)
#     print('thành phần liên thông lớn nhất bao gồm')
#     for i in l:
#         print(f'node id: {i}')
#     ll = len(l)
#     print(f'thành phần liên thông lớn nhất có {ll} node')
#     lll = len(graph) - ll
#     print(f'vậy ta lọc được {lll} node rác')

from build_graph import build_graph_pure_python

def lcc(graph):
    max_connect_comp = []
    max_number_of_comp = float('-inf')
    
    global_visited = set() 
    
    for nodeID in graph:
        if nodeID in global_visited:
            continue
            
        current_comp = []
        stack = [nodeID]
        
        while len(stack) > 0:
            current_node = stack.pop()
            
            if current_node not in global_visited:
                global_visited.add(current_node)
                current_comp.append(current_node)
                
                for nei_info in graph.get(current_node, []):
                    neighbor_id = nei_info['neighbor']

                    if neighbor_id not in global_visited:
                        stack.append(neighbor_id)
        
        if max_number_of_comp < len(current_comp):
            max_number_of_comp = len(current_comp)
            max_connect_comp = current_comp
            
    return max_connect_comp

if __name__ == '__main__':
    graph = build_graph_pure_python()
    print('Bắt đầu tìm kiếm thành phần liên thông lớn nhất...')
    l = lcc(graph)
    for i in l:
        print(f'Thành phần liên thông lớn nhất bao gồm node có id: {i}.')
    print('Ta đã lọc được', len(graph)-len(l), 'node rác.')
