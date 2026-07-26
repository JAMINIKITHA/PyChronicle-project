import sys
import subprocess

print("========== PyChronicle ==========")

if len(sys.argv) < 2:
    print("Usage: python main.py <python_file>")
    sys.exit()

target = sys.argv[1]

print(f"Analyzing: {target}")
print("--------------------------------")

subprocess.run(["python", "ast_parser.py", target])

print("--------------------------------")
print("Analysis Completed Successfully")