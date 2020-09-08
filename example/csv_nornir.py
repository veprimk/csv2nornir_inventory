from nornir import InitNornir
from csv2nornir_inventory import Csv2NornirSimple


csv2n = Csv2NornirSimple("inventory.csv")
inventory_list = csv2n.inventory_converter()
csv2n.make_nornir_inventory()

# Verify that the inventory file is readable

nr = InitNornir(inventory={"plugin": "nornir.plugins.inventory.simple.SimpleInventory", "options": {"host_file": "csv_inventory.yaml"}})
for host in nr.inventory.hosts:
    print(f"""
    hostname: {nr.inventory.hosts[host].hostname}
    platform: {nr.inventory.hosts[host].platform}
    port:     {nr.inventory.hosts[host].port}
    username: {nr.inventory.hosts[host].username}
    password: {nr.inventory.hosts[host].password}
    groups:   {nr.inventory.hosts[host].groups}
    """)
