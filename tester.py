# local_kattis_runner.py
# Run your TSP solution locally with the Kattis sample input.
# It feeds input via stdin and prints your program's stdout (exactly as Kattis would).
# För att köra den gör följande i terminalen
# cd KTH/Algo/AlgoSpanningTree/
# python3 tester.py solution.py 
import subprocess
import sys

# --- Sample Input from the problem description ---
SAMPLE_INPUT = """10
95.0129 61.5432
23.1139 79.1937
60.6843 92.1813
48.5982 73.8207
89.1299 17.6266
76.2097 40.5706
45.6468 93.5470
1.8504 91.6904
82.1407 41.0270
44.4703 89.3650
"""

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 local_kattis_runner.py your_solution.py")
        sys.exit(1)

    solution_file = sys.argv[1]

    # Run your program as a subprocess, sending SAMPLE_INPUT to stdin
    process = subprocess.Popen(
        [sys.executable, solution_file],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate(input=SAMPLE_INPUT)

    print("=== Program output (stdout) ===")
    print(stdout)

    if stderr.strip():
        print("=== stderr (for debugging) ===")
        print(stderr)

    print("=== Exit code:", process.returncode, "===")

if __name__ == "__main__":
    main()
