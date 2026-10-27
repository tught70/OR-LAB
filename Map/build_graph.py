import psycopg2
from collections import defaultdict

def build_graph_pure_python():
    # 1. Kết nối database
    try:
        conn = psycopg2.connect(
            dbname='extract_map',
            user='postgres',
            password='hathanhtung',
            host='localhost',
            port='5432'
        )
    except Exception as e:
        print(f'Lỗi kết nối: {e}')
        return

    # 2. Truy vấn dữ liệu: Lấy tất cả các node thuộc các way, sắp xếp theo thứ tự (sequence)
    query = """
        SELECT wayid, nodeid, ordernode 
        FROM ways_nodes 
        ORDER BY wayid, ordernode ASC;
    """
    
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall() # Dữ liệu trả về là list of tuples: [(way_id, node_id, seq), ...]
    conn.close()

    # 3. XÂY DỰNG ĐỒ THỊ BẰNG PYTHON THUẦN
    # Cấu trúc đồ thị (Danh sách kề): Dictionary chứa key là node_id, 
    # value là 1 list chứa các node kề với nó và thông tin way_id
    # VD: { node_A: [{'neighbor': node_B, 'way_id': 1}, ...], ... }
    
    graph = defaultdict(list)
    
    current_way_id = None
    prev_node_id = None

    for row in rows:
        way_id, node_id, seq_order = row
        
        # Đảm bảo đỉnh luôn tồn tại trong dictionary (ngay cả khi nó chưa có cạnh kề)
        if node_id not in graph:
            graph[node_id] = []

        # Nếu đang xét cùng một way và đã có node trước đó, ta tạo một cạnh (edge)
        if current_way_id == way_id and prev_node_id is not None:
            # Thêm node hiện tại vào danh sách kề của node trước đó
            graph[prev_node_id].append({
                'neighbor': node_id,
                'way_id': way_id
            })
            
            # GIẢ ĐỊNH ĐƯỜNG 2 CHIỀU: Thêm node trước đó vào danh sách kề của node hiện tại
            # (Nếu database của bạn có lưu thông tin đường 1 chiều, bạn cần kiểm tra logic ở đây để quyết định có add dòng này không)
            graph[node_id].append({
                'neighbor': prev_node_id,
                'way_id': way_id
            })

        # Cập nhật lại node và way hiện tại để vòng lặp tiếp tục
        prev_node_id = node_id
        current_way_id = way_id

    # 4. In thử kết quả để kiểm tra
    print(f"Đã xây dựng đồ thị với {len(graph)} đỉnh.")
    
    # Lấy thử 1 node bất kỳ để xem danh sách kề
    sample_node = list(graph.keys())[0]
    print(f"Các đỉnh kề với node {sample_node}:")
    for edge in graph[sample_node]:
        print(f" - Đi tới node {edge['neighbor']} thông qua way {edge['way_id']}")

    return graph

if __name__ == '__main__':
    my_graph = build_graph_pure_python()