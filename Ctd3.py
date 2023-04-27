import random
def raise_1(ex):
    raise ex
def coin_toss():
    list_1=["heads","tail"] 
    print(random.sample(list_1,k=1))
def Rand_Num():
    d=input("enter the range of numbers: ")   
    list_2=d.split()
    if int(list_2[0]) > int(list_2[-1]):
        print("The random number : ",random.randrange(int(list_2[-1]),int(list_2[0]))) 
    elif int(list_2[0]) < int(list_2[-1]):
        print("The random number : ",random.randrange(int(list_2[0]),int(list_2[-1]))) 
    else:
        print("invalid range try again, Game Over!")

def Random_choice():
    i=input("enter your choices: ")
    list_3=i.split()
    print("the random choice is : ",random.sample(list_3,k=1))

class user_entered_exit(Exception):
    pass
class out_of_range(Exception):
    pass

#while True:
 # try:

  #  check = lambda x : raise_1(user_entered_exit()) if x=="exit"  else int(x)
   # z=check(input("pls choose game from 1-3 : "))
    #if z < 0 or z > 3 :
     # raise_1(out_of_range)
    #print(z)
    #if z==1:
     #   coin_toss()
    #elif z==2:
     #   Rand_Num()
    #elif z==3:
     #   Random_choice()        
  #except user_entered_exit:
   # break
  #except ValueError:
   # print("invaild data entry try again")
  #except out_of_range:
   # print("out of range pls choose from 1-3!")
