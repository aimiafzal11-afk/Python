# Create a new file "practice.txt" using python. Add the following data in it:
with open("practice.txt", "w") as f:
    f.write("Hi everyone \nwe are learning FileI/O"
            "\nusing Java. \nI like programming in Java.")

# WAF that replace all occurrences of "java" with "python" in above file.
def replace():
    with open("practice.txt", "r") as f:
        data = f.read()
        new_data = data.replace("Java", "Python")
        print(new_data)

    with open("practice.txt", "w") as f:
        f.write(new_data)

replace()

# Search if the word "learning" exists in the file or not
search = "learning"
with open("practice.txt", "r") as f:
    d = f.read()
    if search in d:
        print("Found!")
    else:
        print("Not Found!")

# WAF to find in which line of the file does the word "learning"occur first.
# Print -1 if word not found.
def find_word(word):
    with open("practice.txt", "r") as f:
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if word in data:
                return line_no
            line_no += 1

    return -1

print(find_word("learning"))

# From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count +=1

print(count)