# csv2nornir_inventory

A simple converter from CSV format inventory to Nornir model YAML File

 
## Use Case Description

Nornir currently supports Netbox, Ansible, NSOT and (Nornir) SimpleInventory as inventory plugins. This program intends to extend the flexibility by allowing users to use CSV Inventory file and convert it to YAML, which then can be used as native SimpleInventory host_file.
This can come to aid if you have multiple devices for which creating the inventory file in YAML format can be time consuming.

Currently this only creates the hosts file as well as will give you an example on how to include this file into your Nornir object as configuration parameter.

## Installation

Copy the file into your nornir working environment and then call import it into your script. 
This uses csv library which is included with python installation so no dependency installation required

## Configuration

If the code is configurable, describe it in detail, either here or in other documentation that you reference.

## Usage

Usage for the code is really simple.

```
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

```

CSV File should follow the format below:
```
name,hostname,platform,port,username,password,groups
rtr1, rtr1.somedomain.net,cisco_ios,22,devnet,n0tc1sc0,wan__us
rtr2, 10.2.2.2,juniper_junos, 22, root, secret1235,juniper
rtr3, rtr3.anotherdomain.com, cisco_iosxe, 822, admin, pass321,cisco__uk
```

As you can see, you can pass multiple groups as long as you concatinate them using '__' as they will be converted to list using split() function.

*Note* If you pass groups details, make sure you create the groups.yaml to satisfy the groups listed under hosts inventory

### DevNet Sandbox

This code can be used in [DevNet Sandbox](https://developer.cisco.com/site/sandbox/) by copying it and incorporating it within your code as per  usage instructions.

## How to test the software

Provide details on steps to test, versions of components/dependencies against which code was tested, date the code was last tested, etc. 
If the repo includes automated tests, detail how to run those tests.
If the repo is instrumented with a continuous testing framework, that is even better.


## Known issues
If you have questions, concerns, bug reports, etc., please create an issue against this [GitHub Repo](https://github.com/veprimk/csv2nornir_inventory/issues) and please make sure to include your code and the error log/traceback.


## TODO

1. Support for data core attribute
2. Support connection_options
3. Support creation of the groups.yaml if it's required

## Getting involved

If you would like to get involved, please create a pull requests and make your changes.

## Author(s)

This project was written and is maintained by the following individuals:

* Veprim Krasnici <veprimk@gmail.com>
