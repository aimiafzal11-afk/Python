#loop on string
count = 0
for char in "cucumber":
    if char == 'c':
        count += 1
print(count)

rev = ""
for char in "YOUTH":
    rev = char + rev
print(rev)

#loop on dictionary
student = {"Name":"Ali", "Grade":"A", "Age":24}
for key in student:
    print(key)

for key in student:
    print(student[key])

for key in student:
    print(key, ":", student[key])

student_list = [
    {"Name":"Ali", "Grade":"A", "Age":24},
    {"Name":"Sana", "Grade":"B", "Age":22}
]
for student in student_list:
    print(f"Name: {student.get('Name')} | Age: {student.get('Age')}")