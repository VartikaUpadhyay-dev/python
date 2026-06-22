#students = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("David", 92)]

#students = sorted(students, reverse=True)

#print(students)

#items = [("pen", 5, 100), ("book", 50, 30), ("bag", 200, 10)]

#total_value = 0
#max_price = items[0][1]
#expensive_product = items[0][0]

#for item in items:
#   total_value = total_value + (item[1] * item[2])

#if item[1] > max_price:
#        max_price = item[1]
#        expensive_product = item[0]
#        print(max_price)

#print("Total Inventory Value =", total_value)
#print("Most Expensive Product =", expensive_product)

#students = [
#    {"name": "Alice", "age": 20, "grades": [80, 90, 100]},
#    {"name": "Bob", "age": 19, "grades": [90, 90, 90]},
#    {"name": "Charlie", "age": 21, "grades": [85, 95, 90]}
#]

#best_student = students[0]
#best_avg = sum(students[0]["grades"]) / len(students[0]["grades"])

                # 80+90+100                 "3"

#for s in students[1:]:
    
    # s=student[1],student[2]
    
#    avg = sum(s["grades"]) / len(s["grades"])

#    if avg > best_avg:
#        best_avg = avg
#        best_student = s

#    elif avg == best_avg and s["age"] < best_student["age"]:
#        best_student = s

#print("Highest Average Student =", best_student["name"])

company = {
    "name": "CEO",
   "reports": [
        {            "name": "Manager1",
            "reports": [
                {"name": "Emp1"},
                {"name": "Emp2"}           ]
        },
        {
    "name": "Manager2",
            "reports": [
            ]
        }
    ]
}       

count = 0
def companyList(company):
    global count
    print(company["name"])

    for manager in company["reports"]:
        print(manager["name"])
        count += 1

    for employee in manager["reports"]:
        print(employee["name"])
        count += 1

companyList(company)

print("Total Employees =", count)



#employees = {
 #   1:{"name":"Alice","department":"IT","salary":50000},
  #  2:{"name": "bob","department":"Bank","salary":20000},
   #3:{"name":"David","department":"IT","salary":40000}
#}
#department = {}
#for emp_id,details in employees.items():
 #   dept = details["department"]
    
  #  if dept not in department:
   #      department[dept] = []

#department[dept].append(details)

#highest_paid = {}

#for dept, emp_list in department.items():
  #  highest = emp_list[0]

   # for emp in emp_list:
        

# orders = [
#     {
#         "order_id": 1,
#         "customer": "Aman",
#         "items": [("Laptop", 1, 50000), ("Mouse", 2, 500)],
#         "status": "delivered"
#     },
#     {
#         "order_id": 2,
#         "customer": "Riya",
#         "items": [("Phone", 1, 30000)],
#         "status": "pending"
#     },
#     {
#         "order_id": 3,
#         "customer": "Aman",
#         "items": [("Keyboard", 1, 2000)],
#         "status": "delivered"
#     },
#     {
#         "order_id": 4,
#         "customer": "Rahul",
#         "items": [("Monitor", 2, 10000)],
#         "status": "delivered"
#     }
# ]

# revenue = 0
# spent = {}

# for order in orders:
#     if order["status"] == "delivered":

#         total = sum(qty * price for product, qty, price in order["items"])

#         revenue += total

#         customer = order["customer"]

#         spent[customer] = spent.get(customer, 0) + total

# top_customer = max(spent, key=spent.get)

# print("Revenue =", revenue)
# print("Top Customer =", top_customer)
# print("Spent =", spent[top_customer])