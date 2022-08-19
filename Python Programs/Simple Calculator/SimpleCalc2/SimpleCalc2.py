class simple_calc():
    
    def init(self):
        pass
    
    def addition(x,y):
        add=x+y
        return add
    
    def subtraction(x,y):
        sub=x-y
        return sub
    
    def multiplication(x,y):
        mul=x*y
        return mul
    
    def division(x,y):
        div=x/y
        return div
    
    def calc(self):
        
        print("\nInput:-")
        num1=int(input("\nEnter the First Number: "))
        operation=str(input("\nEnter the Operator (+, -, *, /) :  "))
        num2=int(input("\nEnter the Second Number: "))
        print("\nOutput:-")
       
        if operation=='+':
            result=simple_calc.addition(num1,num2)                                
            print("\nThe Addition of",'(',num1, "+", num2,')', "=", result)
        elif operation=='-':
            result=simple_calc.subtraction(num1,num2)                 
            print("\nThe Subtraction of",'(',num1, "-", num2,')', "=", result)
        elif operation=='*':
            result=simple_calc.multiplication(num1,num2)
            print("\nThe Multiplication of",'(',num1, "*", num2,')', "=", result)
        elif operation=='/':
            result=simple_calc.division(num1,num2)
            print("\nThe Division of",'(',num1, "/", num2,')', "=", result)
        else:
            print("\nPlease Enter Right Operator!")
        return result   