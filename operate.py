import sys
import csv
import math

if len(sys.argv)<2:
    print("Usage: python3 operate.py infile [infile...]")

else:
    for a in sys.argv[1:]:
        with open(a, newline='\n') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                try:
                    print(row[0], int(math.log(int(row[2]),2)))
                except Exception:
                    pass