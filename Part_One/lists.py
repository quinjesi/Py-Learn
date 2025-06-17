list_one = ['black' , 'white', 'red', 'blue', 'green']
print(list_one[3])
print(list_one[-2])
print(list_one[1:4])
print(list_one[1:4:2]) #[start:stop:step]

list_one[1] = 'purple' #replacing item at index 1
print(list_one)

list_one.append('yellow') #adding item to the end of the list
print(list_one)

list_one.insert(2, 'orange') #inserting item at index 2
print(list_one)

list_one.remove('red') #removing item by value
print(list_one)

list_one.pop(2) #removing item by index
print(list_one)

list_one.sort() #sorting the list
print(list_one)

list_one.reverse() #reversing the list
print(list_one)

a = len(list_one)
print(a)

list_two = ['apple', 'orange', 'banana', 'mango']

b = list_one + list_two
print(b)

list_three = list_one * 2
print(list_three)



# Dictionary
dict_one = {'name': 'Maria', 'age': 25, 'height':1.53, 'gender': 'female'}
c = dict_one['name']
print(c)

dict_one['age'] = 26 #updating value
print(dict_one)
dict_one['weight'] = 60 #adding new key-value pair
print(dict_one)

for key, value in dict_one.items():
    print(f"{key}: {value}")

for y in dict_one:
    print(dict_one[y])



