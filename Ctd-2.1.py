def raise_1(ex):
    raise ex

class user_entered_Q(Exception):
    pass

list =[]

while True:
  try:

    check = lambda x : raise_1(user_entered_Q()) if x=='q' else list.append(int(x))
    check(input("pls enter a number: "))

  except user_entered_Q:
    break
  except ValueError:
    print("invaild data entry try again")
largest = max(list)
smallest =min(list)
print("largest number is ",largest)
print("smallest number is ",smallest)
