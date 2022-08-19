class practice1():
    def init(self):
        pass
    def greaterin3(self):
        num1=int(input("I'st Number: "))  
        num2=int(input("II'nd Number: "))
        num3=int(input("III'rd Number: "))
        if(num1>num2) and (num1>num3):
            res=num1
        elif(num2>num1)and (num2>num3):
            res=num2
        else:
            res=num3
        print("\n",res,"is greater\n")
    def greaterin2(self):
        num1=int(input("Enter the First Number: "))      # Must define data type while getting I/P from user
        num2=int(input("Enter the Second Number: "))
        if (num1>num2):
            print("\n",num1,"is Greater than",num2)
        if (num2>num1):     
            print("\n",num2,"is Greater than",num1)