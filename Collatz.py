def collatz():
    print("Enter the number")
    x= int(input())
    while True:
        if x%2==0:
            x=x//2
            print(x)
        else:
            x%2==1
            x=3*x+1
            print(x)
            

        
collatz()
    
