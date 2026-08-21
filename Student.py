class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(self.name, "your average score is: ", sum / 3)

s1 = Student("Alia", [54, 87, 67])
s1.get_average()