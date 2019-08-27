# http://www.pythonchallenge.com/pc/return/disproportional.html

# Steps i used to solve challenge:
# 1. 

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(proxy, end="\n\n")
print(proxy.system.listMethods(), end="\n\n")
print(proxy.system.methodSignature('phone'), end="\n\n")
print(proxy.phone("Bert"), end="\n\n")


# ['phone', 'system.listethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']