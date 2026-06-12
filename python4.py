# Ques 1
#book = {
 #   "title": "Python Programming",
  #  "author": "John Smith",
   # "year": 2024,
    #"price": 499
#}

#print(book["title"])
#print(book["price"])

# Ques 2
#car = {"brand": "Toyota", "model": "Corolla"}

#car["year"] = 2022

#car["model"] = "Camry"

#print(car)

# Ques 3
#user = {
 #   "name": "Vartika",
  #  "email": "Vartika@gmail.com"
#}

#if "email" in user:
 #   print(user["email"])
    
# Ques 4
   
#prices = {"apple": 1.2, "banana": 0.5}

#removed = prices.pop("banana")

#print("Removed:", removed)
#print(prices)

# Ques 5
#data = {"a": 1, "b": 2}

#data.update({"b": 9, "c": 3})

#print(data)

# Ques 6
#data = {}

#data.setdefault("count", 0)

#print(data)

# Ques 7
#d = {"a": 1, "b": 2}

#for x in d:
 #   print(x)

# Ques 8
#scores = {
 #   "Math": 90,
  #  "Science": 85,
   # "English": 78
#}

#for subject, mark in scores.items():
 #   print(f"{subject}: {mark}")
 
 # Ques 9
#scores = {
 #   "Math": 90,
  #  "Science": 85,
   # "English": 78
#}

#average = sum(scores.values()) / len(scores)

#print("Average =", average)

# Ques 10
#cubes = {x: x**3 for x in range(1, 6)}

#print(cubes)

# Ques 11

#scores = {
 #   "Math": 90,
  #  "Science": 85,
   # "English": 78
#}

#high_scores = {
 #   subject: mark
  #  for subject, mark in scores.items()
   # if mark >= 80
#}

#print(high_scores)

# Ques 12
#employees = {
 #   "E001": {"name": "Alice", "salary": 75000},
  #  "E002": {"name": "Bob", "salary": 62000}
#}

#print(employees["E002"]["salary"])

#Ques 12
#employees = {
 #   "E001": {"name": "Alice", "salary": 75000},
  #  "E002": {"name": "Bob", "salary": 62000},
   # "E003": {"name": "Carol", "salary": 80000}
#}

#highest = max(
 #   employees.values(),
  #  key=lambda emp: emp["salary"]
#)

#print("Highest Salary Employee:", highest["name"])

#Ques 13
#employees = {
 #   "E001": {"name": "Alice", "salary": 75000},
  #  "E002": {"name": "Bob", "salary": 62000}
#}

#employees["E001"]["salary"] += 5000


#employees["E003"] = {
 #   "name": "Carol",
  #  "salary": 80000
#}

#print(employees)

