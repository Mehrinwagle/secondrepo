class Mymath:
    def first_value(self,x):
        self.x=x

    def second_value(self,y):
        self.y=y 

    def add(self,d):
        self.d=d
        self.d=self.x + self.y
    
    def result(self):
        print("The result is : ",self.d)

p=Mymath()
p.first_value(8.3)
p.second_value(9)
p.add(float)
p.result()

