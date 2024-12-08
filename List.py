list=["apples","mangos","bananas","strawberries","grapes"]
print (list)
print (list[3])
print (list[1])
print (list[0:3])
print (list[-3])
if "strawberries" in list:
    print ("Strawberries is present")

if "grapefruit" in list:
    list.append("grapefruit")
    print(list)

list.pop(-3)
print (list)
list.remove("apples")
print (list)

for fruit in list:
    print (fruit)

print (len(list))

for i in range (len(list)):
    print (list[i])

username=["Ishita","Amari","Maya","Tanya"]
user=input()

if user in username:
    print ("User is present.")

else:
    print ("User is not present.")