#Question : 1
#def write_handling(filename,lines):
# with open(filename,"w") as file:
#    for lines in lines:
#     file.write(f"{lines}/n")
#     names = ["vartika","ram","sita"]
#     write_lines("names.text",names)
     
     
# Question : 2

#def count_line(filename):
#        try:
#                with open(filename , "r")as file:
#                lines = file.readlines
#                print(len(lines))
#        except FileNotFoundError: 
#                print(0)
#print(count_line("string_line.text"))

#Question 3
#def copy_file(first_file, second_file):
#        with open(first_file,"r")as f1:
#         lines = f1.readline()
         
#         with open(second_file,"w")as f2:
#                 for line in lines:
#                     f2.write(line)
#copy_file("calculater.txt","test.txt")

#Question 4
#import os
#from datetime import datetime
#filename = "calculater.txt" 
#if os.path.exists(filename):
#        with open(filename,"r")as f:
#         print(f.read())
#else:
#        print(f"'{filename}'does not exist - skipping.")

# Question 5
#import os
#students_data = [
#    ["Name",  "Age", "Score"],
#    ["Alice",  21,    92],
#    ["Bob",    22,    85],
#    ["Carol",  20,    78],
#    ["Diana",  23,    95],
#]
#with open("student.csv","r") as cvsfile:
#        reader = csv.reader(csvfile)
#        header = next(reader)
#        print(f"/n{'| . join(header)'}")
#        print("-"*25)
#        for row in reader:
#                print(f"  {row[0]:<8} | {row[1]:>3} | {row[2]:>5}")

#Question 6
#import os
#students_data = [
#    ["Name",  "Age", "Score"],
#    ["Alice",  21,    92],
#    ["Bob",    22,    85],
#    ["Carol",  20,    78],
#    ["Diana",  23,    95],
#]
#with open("students.csv", "r") as csvfile:
#    reader = csvfile.DictReader(csvfile)
#    scores = [int(row["Score"]) for row in reader]

#print(f"\nAverage score: {sum(scores)/len(scores):.1f}")
#print(f"Highest score: {max(scores)}")

# Question 7
#def log_event(message , logfile="app.log"):
#        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
##                file.write (f"'[{timestamp}]'{message/n}")
#log_event("Application started")
#log_event("user Alice login")
#log_event("File uploaded successfully")
#print("Log entries appended.")

#Question 8 (13)

#def word_count(filename):
#    counts = {}

#    with open(filename, "r") as file:
#        for line in file:
#            words = line.lower().split()

#            for word in words:
#                if word not in counts:
#                    counts[word] = 0

#                counts[word] += 1

    
#print(word_count("sample.txt"))

# Question 9 (10)
import os

def safe_read(filename):
    if os.path.exists(filename):
        file = open(filename, "r")
        content = file.read()
        file.close()
        return content
    return "FILE NOT FOUND"
