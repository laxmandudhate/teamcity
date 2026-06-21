import sys
import time
import os

# 1. Grab the target environment from TeamCity runtime parameters
try:
    target_env = sys.argv[1]
except IndexError:
    target_env = "Local-Test"

print(f"--- Starting Infrastructure Backup Job for: {target_env} ---")

# 2. Simulate connecting to a network device (e.g., using Netmiko)
print(f"Connecting to {target_env} routers via SSH...")
time.sleep(2) # Simulating network delay

# Mock configuration data that we "downloaded" from the router
mock_router_config = f"""
hostname {target_env}-core-router
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
"""
print("Configuration successfully pulled from device.")

# 3. Save the configuration to a file so TeamCity can capture it as an Artifact
backup_folder = "backups"
os.makedirs(backup_folder, exist_ok=True)
filename = f"{backup_folder}/{target_env}_config_backup.txt"

with open(filename, "w") as file:
    file.write(mock_router_config)

print(f"Backup saved securely to: {filename}")
print("--- Job Complete ---")
