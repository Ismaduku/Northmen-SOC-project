print()
print("– NORTHMEN SOC - Policy Engine –")
print()

allowed_ips = []

allow_list = open("allow_list.txt", "r")
for line in allow_list:
    allowed_ips.append(line.strip())


log_file = open("logs/auth.log", "r")
for line in log_file:
    if "Failed password" in line:
        source_ip = line.split(" – ")[2]

print("Going through security policy engine...")

if source_ip in allowed_ips:
    print("POLICY: Trusted IP - Do not block")
else:
    print("POLICY: Untrusted IP - Block recommended")