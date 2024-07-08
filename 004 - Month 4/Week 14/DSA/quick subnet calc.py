#! python3
# not originally my code, I just formatted it
# source: https://www.reddit.com/r/Python/comments/vxwfzk/stupid_simple_subnet_calculator/


import ipaddress


def get_subnet_details(ip):
    ip_addr = ipaddress.ip_interface(ip)
    net_addr = ip_addr.network
    pref_len = ip_addr.with_prefixlen
    mask = ip_addr.with_netmask
    wildcard = ip_addr.hostmask
    broadcast_address = net_addr.broadcast_address

    print('Network Address     :', str(net_addr).split('/')[0])
    print('Broadcast Address   :', broadcast_address)
    print('CIDR Notation       :', pref_len.split('/')[1])
    print('Subnet Mask         :', mask.split('/')[1])
    print('Wildcard Mask       :', wildcard)
    print('First IP            :', list(net_addr.hosts())[0])
    print('Last IP             :', list(net_addr.hosts())[-1])


# Main function
def main():
    ip = input('Enter IP address in IP/Mask Form: ')
    try:
        get_subnet_details(ip)
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
