print()

allowed_ips = []

allow_list = open("allow_list.txt", "r")
for line in allow_list:
    allowed_ips.append(line.strip())
allow_list.close()

alerts_file = open("alerts.csv", "r")

for line in alerts_file:

    alert = line.strip().split(",")

    source_ip = alert[0]
    target_ip = alert[1]
    attempts = int(alert[2])

    print("Security policy engine working...")
    print()

    print("Source IP:", source_ip)
    print("Target IP:", target_ip)
    print("Failed attempts:", attempts)

    if source_ip in allowed_ips:
        print("POLICY: Trusted IP in allow-list - Do not block")
    else:
        print("POLICY: Untrusted IP not in allow-list - Review for blocking")

    print()

alerts_file.close()
