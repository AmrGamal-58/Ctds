list_1=[]
list_2=[]
while True:
    z=input("enter the names ffs: ")
    if z.isalpha() and z != "q" or z.__contains__(" "):
        list_1.append(z)
    elif z == "q":
        break
    else:
        print("invalid data entry ")
while True:
    z=input("enter the names in list2 ffs: ")
    if z.isalpha() and z != "q" or z.__contains__(" "):
        list_2.append(z)
    elif z == "q":
        break
    else:
        print("invalid data entry ")        
mutual=[x for x in list_1 if x in list_2 ]
print(mutual)
