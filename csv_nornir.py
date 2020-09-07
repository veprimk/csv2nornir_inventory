from nornir import InitNornir

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
