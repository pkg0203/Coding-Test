"""
https://www.acmicpc.net/problem/2064
[ Implement ]
"""

import sys

def make_octet(string):
    while len(string)<8 :
        string = "0" + string
    return string

def fill_zero(j):
    for idx in range(j,4):
        mask[idx] = "0"
        network[idx] = "0"
    return None

N = int(sys.stdin.readline())
address = []
network = [None for _ in range(4)]
mask = [None for _ in range(4)]
for i in range(N):
    address.append(sys.stdin.readline().strip())

for j in range(4):
    is_all_same = True
    standard = address[0].split('.')[j]
    for ip in address :
        if standard!=ip.split('.')[j] :
            is_all_same = False
            break
    
    if is_all_same :
        mask[j]="255"
        network[j] = standard
    else :
        break

for k in range(j,4):
    standard_adr=make_octet(bin(int(address[0].split('.')[j]))[2:])
    mask_bit = ''
    network_bit = ''
    for idx in range(8) :
        standard_bit = standard_adr[idx]
        is_all_same = True
        for ip in address :
            if standard_bit != make_octet(bin(int(ip.split('.')[k]))[2:])[idx] :
                is_all_same = False
                break
        
        if is_all_same :
            mask_bit =mask_bit + '1'
            network_bit = network_bit + standard_bit
        
        else :
            while len(mask_bit) < 8 :
                mask_bit = mask_bit + '0'
            mask[j] = str(int(mask_bit,2))
            while len(network_bit) < 8 :
                network_bit = network_bit + '0'
            network[j] = str(int(network_bit,2))
            break
    if j<3 and is_all_same == False :
        fill_zero(j+1)
        break

sys.stdout.write(f"{'.'.join(network)}\n")
sys.stdout.write(f"{'.'.join(mask)}\n")