import ipaddress as ip

CLASS_C = "192.168.0.0"
original_prefix = 24

if __name__ == "__main__":
    net_addr = f"{CLASS_C}/{original_prefix}"
    print(f"Network: {net_addr}")

    try:
        network = ip.ip_network(net_addr)
    except ValueError as e:
        raise Exception(f"Failed to create network: {e}")

    print("Network Configuration")
    print(f"\tNetwork Address: {network.network_address}")
    print(f"\tNumber of IP Addresses: {network.num_addresses}")
    print(f"\tSubnet Mask: {network.netmask}")
    print(f"\tBroadcast Address: {network.broadcast_address}")

    # Chia mạng con với các prefix mới từ 24 đến 30 và hiển thị first IP và last IP
    for new_prefix in range(24, 31):
        print(f"\nSubnets with new prefix /{new_prefix}:")
        for subnet in network.subnets(new_prefix=new_prefix):
            subnet_ips = list(subnet.hosts())
            if subnet_ips:
                print(f"Subnet: {subnet}")
                print(f"\tFirst IP: {subnet_ips[0]}")
                print(f"\tLast IP: {subnet_ips[-1]}")
            else:
                print(f"Subnet: {subnet}")
                print("\tNo usable IP addresses in this subnet.")