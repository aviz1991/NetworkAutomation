from jnpr.junos import Device
from pprint import pprint

device = Device(host='192.168.122.100', user='root', password='Chevron@123',port= '22')
device.open()
pprint(device.facts)
#print(device.facts['hostname'])
