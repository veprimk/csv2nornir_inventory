import csv
import sys


# Reads the CSV File and returns a list which will be using to create the yaml file

def inventory_converter(filename):
    inventory_data = []
    try:
        with open(filename) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                inventory_data.append([
                    row["name"],
                    row["hostname"],
                    row["platform"],
                    row["port"],
                    row["username"],
                    row["password"],
                    row["groups"]
                    ])
            return inventory_data
    except FileNotFoundError:
        print(f"Please make sure that {filename} is correct and exists...")
        sys.exit(1)


# Iterates over the list and creates the csv_inventory.yaml based on the Nornir model

def make_nornir_inventory(inventory_data_list):
    if len(inventory_data_list) < 1:
        print("The list argument doesn't have any records! Cannot create an inventory file out of an empty list!")
        return ValueError
    try:

        with open("csv_inventory.yaml", "w") as out_file:
            out_file.write("---\n")
            for host in inventory_data_list:
                out_file.write(f"{host[0]}:\n")
                out_file.write(f"  hostname: {host[1]}\n")
                out_file.write(f"  platform: {host[2]}\n")
                out_file.write(f"  port: {host[3]}\n")
                out_file.write(f"  username: {host[4]}\n")
                out_file.write(f"  password: {host[5]}\n")
                if len(host[6].split("_")) > 0:
                    out_file.write(f"  groups:\n")
                    for group in host[6].split("__"):
                        out_file.write(f"    - {group}\n")
                else:
                    out_file.write("\n")
            
            print("Inventory file created...")
    except PermissionError:
        print("An error occurred whilst trying to write into the file... Please make sure that there are enough permission assigned to the user executing the script...")
        sys.exit(1)


def main():

    csv_inventory_file = "inventory.csv"
    inventory_list = inventory_converter(csv_inventory_file)
    make_nornir_inventory(inventory_list)


if __name__ == "__main__":
    main()


