# Автор В.Н. Шубинкин

from ipaddress import ip_network

count = 0
for address in ip_network('158.132.161.128/255.255.255.128', False):
    bin_address = f'{address:b}'  # Python 3.9+
    #  bin_address = f'{int(address):b}' в ранних версиях
    count += bin_address[-1] == '1'
print(count)