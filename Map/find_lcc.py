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
