# Trích xuất và Xử lý Dữ liệu Bản đồ OpenStreetMap trên Đồ thị.

## 1. Mô tả.
* Đây là dự án sử dụng python đọc file .osm được download từ nền tảng OpenStreetMap (là bản đồ mở được đóng góp bởi cộng đồng) thông qua thư viện có sẵn xml.
* Những object được đọc sẽ được lưu vào database bằng logic thuần python, tạo ra script sql, sử dụng PostgreSQL để đọc file `.sql` để hoàn thành lưu trữ data bản đồ vào database.
* Sử dụng các lệnh truy vấn cơ bản của SQL lọc ra các node và way của một vùng bản đồ để trích xuất data ra object python, lưu chúng theo cấu trúc đồ thị (node và list các node kề). Phương pháp thực hiện thông qua thư viện `psycopg2`.
* Sử dụng thuật toán `DFS` trên đồ thị để thực hiện bài toán "**Tìm thành phần liên thông lớn nhất (Find the largest connected component)**"
> **Ý nghĩa**: Bài toán này có ý nghĩa tiền xử lí bản đồ trước khi thực hiện các thuật toán tìm đường phức tạp hơn (Dijkstra, A*, ...). Nó giúp loại bỏ các node "rác" trong bản đồ, là những con đường lỗi, đường cụt không kết nối với ai hay các "hòn đảo" trôi nổi. 

## 2. Cấu trúc thư mục.
```text
Map/
├── build_graph.py               # Xây dựng hàm lưu database vào cấu trúc đồ thị
├── command.sql                  # File SQL viết script để lưu data vào database (tạo bởi write_script_data.py)
├── find_lcc.py                  # Xây dựng hàm tìm thành phần liên thông lớn nhất bằng thuật toán DFS
├── intermediate.json            # Lưu trữ các object có data của bản đồ dưới dạng json (tạo bởi read_data.py)
├── map.osm                      # File .osm là file raw tải từ nền tảng OpenStreetMap
├── read_data.py                 # Đọc data từ map.osm và chuyển object sang định dạng json
└── write_script_data.py         # Đọc object từ intermediate.json và viết script lưu chúng vào database
```