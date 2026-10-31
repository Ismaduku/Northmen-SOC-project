print()
print()
print("NORTHMEN SOC - Security Monitoring Program")
print()
print()
print()
print("Asset inventory:")

inventory_file = "asset_inventory.csv"

asset_inventory = []
file = open(inventory_file, "r")
for line in file:
    asset = line.strip().split(",")
    asset_inventory.append(asset)

for asset in asset_inventory:
    print("Hostname:", asset[0], "– IP Address:", asset[1], "– Owner:", asset[2], "– Criticality:", asset[3])

print()
print()
print(f"High criticality assets:") 
for asset in asset_inventory:
    if asset[3] == "High": 
        print(f"Hostname: {asset[0]} – IP Address: {asset[1]}")
print()

print("Processing login attempts...")
print()
print("Failed attempts:")

log_file = "logs/auth.log"

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            print(line.strip())

print()

failed_attempts = 0
successful_attempts = 0


file = open(log_file, "r")
for line in file:
    if "Failed password" in line: 

        failed_attempts += 1
                    
    elif "Accepted password" in line:
        successful_attempts += 1

print(f"Total login attempts: {failed_attempts + successful_attempts}")
print("Successful attempts:", successful_attempts)
print(f"Suspicious attempts: {failed_attempts}")
      

print()



failed_ips = {}

file = open(log_file, "r")
for line in file:
    if "Failed password" in line:
        ip = line.split(" – ")[2].strip()

        if ip in failed_ips:    
            failed_ips[ip] += 1
        else: 
            failed_ips[ip] = 1

for ip, attempts in failed_ips.items(): 
    if attempts >= 3: # threshold for alerting the SOC team (if it is 3 or more login attempts)
    
        print(f"ALERT: {ip} has {attempts} failed login attempts! Potential brute-force attack detected. ALERT the SOC team immediately!")

print()
















