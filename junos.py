from ncclient import manager
from ncclient.xml_ import *

# set device configs
switches = [
    {"host": "192.168.122.100", "port": "22",
             "username": "root", "password": "Chevron@123"}
]
for switch in switches:
    # make initial connection and save session as variable m
    with manager.connect(host=switch["host"], port=switch["port"], username=switch["username"], password=switch["password"], hostkey_verify=False, device_params={"name": "junos"}) as m:
        # retrieve config in XML format
        response = m.get_configuration(format='xml')
        host = response.xpath('configuration/system/host-name')[0].text
        interfaces = response.xpath('configuration/interfaces/interface')
        print('='*15)
        print(host)
        print('='*15)
        for interface in interfaces:
            int_name = interface.xpath('name')[0].text
            int_unit = interface.xpath('unit/name')[0].text
            ip = []
            for name in interface.xpath('unit/family/inet/address/name'):
                ip.append(name.text)
           # print("Interfaces are {} and unit is {} and its ip is {}".format(int_name,int_unit,ip))
            print(response)
