
import this

thisbox=[23,32,63,23,5,6]
def printf():
    print(thisbox)
def removee(item):
        if item==0:
            thisbox.remove()
        else:
            thisbox.remove(item)
def additem(item):
    thisbox.append(item)
while True:
    printf()
    try:
        user_command=input("type enter or remove: ")
        if user_command=="remove":

            user_remove=input("remove any or remove a specific NO.: ")
            if user_remove=="remove any":
                 if thisbox.count==5:
                        print("can't romve anymore")
                 else:
                        removee(0)
            elif user_remove=="specific":
                    item=int(input("enter the number you want to remove"))                 
                    if thisbox.count==5:
                        print("can't romve anymore")
                    else:
                        removee(item)
        elif user_command=="enter":
            item=int(input("enter the number you want to add: "))
            additem(item)
    except:
        print("invalid input try again ")
