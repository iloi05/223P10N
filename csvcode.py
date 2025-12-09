# Name: Ivy Loi
# Project 10
# Purpose of file: Program reads and writes csv file

import csv

import os

counters = {"fresh": 0, "soph": 0, "jr": 0, "sen": 0}

students = {}

try:
    with open('Students.csv', mode='r') as file1, open('course enrollment.csv', mode= 'r') as file2:

        s = csv.DictReader(file1)
        for row in s:
            level = row["Level"].strip().upper()
            sid = row["ID"]

            if level == "FRESH":
                counters["fresh"] += 1
            elif level == "SOPH":
                counters["soph"] += 1
            elif level == "JR":
                counters["jr"] += 1
            elif level == "SR":
                counters["sen"] += 1

            students[sid] = {"Total_Units": 0, "CPSC_Units": 0}

        print(f'{counters["fresh"]} freshmen')
        print(f'{counters["soph"]} sophomores')
        print(f'{counters["jr"]} juniors')
        print(f'{counters["sen"]} seniors')

        e = csv.DictReader(file2)
        for row in e:
            eid = row["ID"]
            course = row["Course"].strip()
            units = int(row["Units"])

            if eid in students:
                students[eid]["Total_Units"] += units
                if course.startswith("CPSC"):
                    students[eid]["CPSC_Units"] += units
            else:
                students[eid] = {
                    "Total_Units": units,
                    "CPSC_Units": units if course.startswith("CPSC") else 0
                }

except FileNotFoundError:
    print("Error: The file 'course enrollment.csv' or 'Students.csv' not found.")
except Exception as e:
    print(f"An error occurred while reading the CSV: {e}")

try:
    with open('outputfile.csv', mode='w', newline='') as file3:
      
            writer = csv.writer(file3)
            writer.writerow(["ID", "Total Units", "CPSC Units"])
            for sid, data in students.items():
                writer.writerow([sid, data["Total_Units"], data["CPSC_Units"]])
except FileNotFoundError:
    print("Directory for 'outputfile.csv' does not exist.")
except Exception as e:
    print("Error writing to outputfile.csv:", e)

if os.path.exists('outputfile.csv') and os.path.getsize('outputfile.csv') > 0:
    print("Output file exists and has been written successfully.")
else:
    print("Output file was not created or is empty.")