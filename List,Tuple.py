#LIST
numbers = [1, 2, 2, 4, 5]
print(numbers)

numbers.append(6)        #add item
print(numbers)
numbers.insert(1, 11)    #insert at index
print(numbers)
numbers.remove(2)        #remove first occurence of 2
print(numbers)
numbers.pop()            #remove from last
print(numbers)
numbers.sort()           #sort list
print(numbers)
numbers.reverse()        #reverse list
print(numbers)

for num in numbers:      #loop on list
    print(num)

#TUPLE
cities = ("lahore", "karachi", "multan", "lahore")
print(cities[1])                    #access from index
print(cities.count("lahore"))       #count
print(cities.index("karachi"))      #print index value

