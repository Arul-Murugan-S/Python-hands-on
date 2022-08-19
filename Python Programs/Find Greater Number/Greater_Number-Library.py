class practice1():
    def init(self):
        pass
    def greaterin3(self):
        num1=int(input())  
        num2=int(input())
        num3=int(input())
        if(num1>num2) and (num1>num3):
            res=num1
        elif(num2>num1)and (num2>num3):
            res=num2
        else:
            res=num3
        print(res,"is greater")
    def greaterin2(self):
        num1=int(input("Enter the First Number:"))      # Must define data type while getting I/P from user
        num2=int(input("Enter the Second Number:"))
        if (num1>num2):
            print(num1,"is greater than",num2)
        else:
            print(num1,"is lesser than",num2)