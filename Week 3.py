# Auther:Nyah
# Date:Nov 22, 2024
# Depscription: Manipulating strings

#Strings = '""
#intergers = 1
#Flot = 1.23
#boolen = True our False
#sanck case: Underscore

repeated_text = "Repeat  me!" * 3
print(repeated_text)

text = "Nyah"
length = len(text)
print(length)





print(text[-3])
print(text[-1])


text = "Hello, World!"

print(text[0.5]) # Hello
print(text[7.0]) # World!
print(text[-3:]) #d!

print(text.strip())
print(text.upper())
print(text.lower())

text.replace("world" ,"Nyah")
text.find(",")

text = "Hi my name is Nyah!What is your name?"
index = text.find("Nyah")
print(index) # Ptints out the index or position of Nyah

#print out Nyah
substring = text[index:index+4]
print(substring)

(string1) = input("Enter your frist string:")
(string2) = input("Enter your second string:")

if len(string1) > len(string2):
    print("string one is bigger")
elif len(string1) == len(string2):
    print("same size")
else:
    print("String two is bigger")































































"Week 4 is week 5 because on week 4 we were finishing week 3"