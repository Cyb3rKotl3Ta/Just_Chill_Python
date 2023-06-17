from ipaddress import IPv4Address


ip = 2149583361

def int32_to_ip(int32):
    bin_str = f'{int32:b}'.rjust(32, '0')
    print(bin_str)
    return '.'.join([str(int(bin_str[idx:idx + 8], 2)) for idx in range(0, len(bin_str), 8)])

print(int32_to_ip(ip))


def int32_to_ip_2(int32):
    return str(IPv4Address(int32))

def int32_to_ip_3(int32):
    return '{}.{}.{}.{}'.format(*int32.to_bytes(4, 'big'))