class Shape:
    count=0
    def __init__(self,name,color,d1,d2 :None):
        self.name=name
        self.dim1=d1
        self.dim2=d2
        self.color=color
        Shape.count+=1

    def __str__(self) -> str:
        return ("name: ",self.name)
    
    def area(self):
        if(self.name == 'circle'):
            print("area is : ",3.14*self.dim1**2)
        elif(self.name=='triangle'):
            print("area is : ",0.5*self.dim1*self.dim2)
        elif(self.name=='rectangle'):
            print("rectangle area is : ",self.dim1*self.dim2)
        elif(self.name=='square'):
            print("area is : ",self.dim1**2)
        else:
            print("Type Error ")
    
class Circle(Shape):
    
    count = 0

    def __init__(self,color,rad):
        Circle.count+=1
        super().__init__("circle", color, rad, rad)
        self.radi=rad
    
    def area(self):
        print("Circle area is : ",3.14*self.radi**2)
    


print("Shape counter is :",Shape.count)
obj1=Shape("rectangle","red",12,10)
obj1.area()
print("Shape counter is :",Shape.count)
obj2=Circle("gray",1)
print("Circle counter is :",Circle.count)
obj2.area()
print("Shape counter is :",Shape.count)


            

