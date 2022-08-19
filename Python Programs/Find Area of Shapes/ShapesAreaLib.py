#!/usr/bin/env python
# coding: utf-8

# In[1]:


class shapesarea():
    
    def init(self):
        pass
    
    def circle(self):
        r=float(input("Enter the Radius of Circle (r): "))
        acir=3.14*r*r
        print('Area of the Circle is:',acir)
        print('~~~-~~~~-~~~~~-~~~~~-~~~~-~~~~-~~~')
        return acir

    def cube(self):
        a=float(input("Enter the Side of Cube (a): "))
        acube=6*a**2
        print("Area of the Cube is = ",acube)
        print('~~~-~~~~-~~~~~-~~~~~-~~~~-~~~~-~~~')
        return acube
    
    def square(self):
        a=float(input("Enter the Side of Square (a): "))
        asqr=a**2
        print('Area of the sqaure is:',asqr)
        print('~~~-~~~~-~~~~~-~~~~~-~~~~-~~~~-~~~')
        return asqr

    def rectangle(self):
        l=float(input("Enter the Length of Rectangle (l): "))
        w=float(input("Enter the Length of Rectangle (w): "))
        arect=l*w
        print('Area of the rectangle is:',arect)
        print('~~~-~~~~-~~~~~-~~~~~-~~~~-~~~~-~~~')
        return arect


# In[ ]:




