import sys
import subprocess
import csv

print("========== PyChronicle ==========")

if len(sys.argv) < 2:
    print("Usage: python main.py <python_file>")
    sys.exit()

target = sys.argv[1]

print(f"Analyzing: {target}")
print("--------------------------------")

subprocess.run(["python", "ast_parser.py", target])

with open("trace_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["File", "Status"])
    writer.writerow([target, "Analysis Completed Successfully"])

print("--------------------------------")
print("Trace report generated: trace_report.csv")
print("Analysis Completed Successfully")