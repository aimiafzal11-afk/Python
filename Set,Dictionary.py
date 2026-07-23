#SET
num = {1,2,3,3}
print(num)                          #no duplicate will display
print(num.add(6))
print(num.remove(2))
print(num.pop())
print(num.clear())

A = {"ali", "amna"}
B = {"amna", "asia"}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))

#DICTIONARY
employee = {
    "id" : 1,
    "name" : "Ali",
    "salary" : 10000,
    "post" : "manager"
}
employee["salary"] = 23000          #update
employee["city"] = "Lahore"         #add
employee.pop("post")                #remove
print(employee)

print(employee.get("name"))
print(employee.keys())
print(employee.values())
print(employee.items())

new_data = {"post" : "freelancer"}
employee.update(new_data)
print(employee)

for key, value in employee.items() :
    print(key, ":", value)