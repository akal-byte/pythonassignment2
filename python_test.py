x = [100,110,120,130,140,150]
y=[num*5 for   num in x]
print(y)

def divisible_by_three(n):
    numbers_range=range(1,n)
    for number in numbers_range:
        if number%3==0:
            print(number)
divisible_by_three(20)

x = [[1,2],[3,4],[5,6]]
def flatten_list(x):
    y=[]
    for a in x:
        for d in a:
            y.append(d)
    return y      
print(flatten_list(x = [[1,2],[3,4],[5,6]]))

def smallest(list):
    return min(list)
smallest(list=[12,678,89,345,789,234,678])

def remove_duplicate(x):
    y=set(x)
    list2=list(y)
    print(list2)
remove_duplicate(x = ['a','b','a','e','d','b','c','e','f','g','h'])

def divisible_by_seven():
    num_list=[]
    for number in range(100,200):
        if number%7==0:
            num_list.append(number)
    return num_list
        
print(divisible_by_seven())

def greet_student():
    students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}],
    for student in students:
       print(students)
        
greet_student()    


class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        area=self.length*self.width
        print(area) 
    def perimeter(self):
        perimeter=2*(self.width+self.length)
        print(perimeter) 
rectangle=Rectangle(24,56)
rectangle.area()
rectangle.perimeter()

       
        



