def Fibonacci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        a , b = 0 , 1
        for i in range(x):
            a , b = b , a+b
    return a



def PrimeNum(x):
    if x==1:
        return False
    elif x==2:
        return True
    elif x>2:
        import random
        Used_a = []
        for i in range(20):
            while True:
                #making sure that those 20 random numbers will be different from each other.
                a=random.randint(1, 100000)
                acceptable=True
                for j in Used_a:
                    if a==j:
                        acceptable = False
                if acceptable==True:
                    Used_a.append(a)
                    break
            if ((a**x-a)%x!=0):
                return False
        return True



#asking the user for input
Number = int(input("Give the fibonacci number you want: "))



# 0 is neither prime nor composite!
if Number==0:
    print("It is NOT primary number!")
else:
    FibNumber = Fibonacci(Number)
    if PrimeNum(FibNumber)==True:
        print("It is primary number!")
    else:
        print("It is NOT primary number!")
