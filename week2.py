#Author: Nyah 
#Date:Nov.14.24
#Diposcripstion: Lists

# list of strings 
fruits = ["apple" , "banana", "oranges"]

 # List of intergers
numbers = [1,2,3,4]  
# Both strings and integers
list = ["apple",1, "banana",  3]

#Get survival items 
item1 = input("Enter the frist item:")
item2 = input("Enter the second item")
item3 = input ("Enter the third item")

chosen_items = [item1,item2,item3]
print("To  survive the deserted island you chose: ", chosen_items)

#index is the location or position of item 
# startes at 0
# From the right it starts at -1

listA ={"Apple", "Banana", "Oranges"}
listA [1] = "Pear"
print(listA)

listA[-1] = "Greaps"
print(listA)

# Concatenate = to add together 
new_list = chosen_items + listA
print(new_list)

#.apppend(), .insert(), .remove()

new_list.append("car")
new_list.insert(0,"kiwi")
new_list.remove("car")
print(new_list)

# Homework
num_list = [1,1000,2,4,3,24,77,6,7,11,8]




# remove 3 numbers from the list
num_list.remove(1000)
num_list.remove(24)
num_list.remove(11)



# change the number at 3 and 4 
num_list[2] = 3
num_list[3] = 4




# change the number 77 to 5 
num_list[6] = 5


# Append or add the numbers 9 and 10 to the end
num_list.append(9)
num_list.append(10)
 
# index = the pestion/location of  the item
