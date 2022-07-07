ip = '255.024.01.01'


def remove_leading(ip):
    ip_list = ip.split('.')    # ['255', '024', '01', '01']
    nip = []
    
    for i in ip_list:
        if i == '0' or i == '00' or i == '000' or i == '0000':
            nip.append('0')    # nip = ['0','0','0','0']
        else:
            nip.append(i.lstrip('0'))
                
                
    output = '.'.join(nip)
    return output

print(remove_leading(ip))