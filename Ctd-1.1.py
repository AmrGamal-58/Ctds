while True:
    try: 
        num=int(input("enter a number from 0-942: "))
        if num>= 0 and num <= 942  :   
           break
        else:
           print("invalid data entered pls try again")
    except :
        print("invalid data entered pls try again")
def ones(no):

    if no==100:
        return 21
    elif no > 100 and no <200:
        return 21+1*(no-100)
    elif no > 100 and no < 940 :
        return 120 +((no/100)-1)*20
    elif no==10:
        return 2
    elif no>10 and no< 100:
        return 10+(no/10)
    elif no<10 and no!=0:
        return 1
    else:
        return 0
no_of_ones=int(0)
firstdigit=num
secondigit=0
thirdigit=0
if firstdigit<200 and firstdigit>100:
    thirdigit=int(firstdigit%10)
    secondigit=(firstdigit/10)%10
    
    no_of_ones=ones(firstdigit)+ones(secondigit*10)+ones(thirdigit)
elif firstdigit/10 >=10:
    thirdigit=firstdigit%10
    firstdigit=firstdigit/10
    secondigit=int(firstdigit%10)
    firstdigit=int(firstdigit/10)
    no_of_ones=ones(firstdigit*100)+ones(secondigit*10)+ones(thirdigit)



elif firstdigit/10 < 10 and firstdigit!=0:
    secondigit=firstdigit
    thirdigit=secondigit%10
    secondigit=int(secondigit/10)
    no_of_ones=int(ones(secondigit*10))+int(ones(thirdigit))




else:
    thirdigit=firstdigit
    no_of_ones=int(ones(thirdigit))


print("number of ones in ",num," is ",no_of_ones)
