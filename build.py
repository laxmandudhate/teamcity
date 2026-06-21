import sys

# 1. Get the parameter passed from TeamCity runtime
try:
    environment = sys.argv[1]
except IndexError:
    environment = "Local-Dev"

print(f"--- Python Script Starting for Environment: {environment} ---")

# 2. Read your existing index.html file
with open("index.html", "r") as file:
    html_content = file.read()

# 3. Simulate a simple modification or check
print("Successfully read index.html!")
print(f"Simulating deployment preparation to {environment}...")

# 4. Create an output log file as an artifact
with open("deployment_report.txt", "w") as report:
    report.write(f"Build was processed successfully for: {environment}\n")
    report.write("Status: PASS\n")

print("--- Python Script Finished ---")
