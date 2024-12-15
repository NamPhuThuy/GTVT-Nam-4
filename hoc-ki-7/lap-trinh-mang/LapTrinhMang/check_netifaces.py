import netifaces
from tabulate import tabulate

interfaces = netifaces.interfaces()
my_interfaces = dict()

def get_interface():
    for i in interfaces:
        addr = netifaces.ifaddresses(i)
        my_addr = dict()
        # Kiểm tra và lưu địa chỉ IPv4 nếu có
        if netifaces.AF_INET in addr.keys():
            my_addr["ipv4"] = addr[netifaces.AF_INET]
        # Kiểm tra và lưu địa chỉ IPv6 nếu có
        if netifaces.AF_INET6 in addr.keys():
            my_addr["ipv6"] = addr[netifaces.AF_INET6]
        
        # Lưu thông tin địa chỉ vào dictionary
        my_interfaces[i] = my_addr
    
    # Chuyển đổi dữ liệu thành danh sách các hàng để in bảng
    table_data = []
    for interface, addresses in my_interfaces.items():
        ipv4 = addresses.get("ipv4", [{}])[0].get("addr", "N/A")
        ipv6 = addresses.get("ipv6", [{}])[0].get("addr", "N/A")
        table_data.append([interface, ipv4, ipv6])
    
    # Định nghĩa tiêu đề của bảng
    headers = ["Interface", "IPv4 Address", "IPv6 Address"]
    
    # In bảng sử dụng tabulate
    print(tabulate(table_data, headers, tablefmt="grid"))

def get_broadcast_address():
    # Tạo danh sách để lưu địa chỉ broadcast
    broadcast_addr = []
    # Lặp qua từng giao diện mạng
    for interface in interfaces:
        # Lấy địa chỉ của giao diện
        ifaddresses = netifaces.ifaddresses(interface)
        # Kiểm tra nếu có địa chỉ IPv4
        if netifaces.AF_INET in ifaddresses:
            addr_info = ifaddresses[netifaces.AF_INET]
            # Lặp qua từng thông tin địa chỉ
            for info in addr_info:
                # Kiểm tra và lưu địa chỉ broadcast nếu có
                if "broadcast" in info:
                    broadcast_addr.append(info["broadcast"])
    # Trả về danh sách địa chỉ broadcast
    return broadcast_addr

if __name__=='__main__':
    # Gọi hàm get_interface và in kết quả
    print(get_interface())

    # Gọi hàm get_broadcast_address và in kết quả
    print(get_broadcast_address())