class Car:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def display_color(self):
        print(self.color)
    def display_cost(self):
        print(self.cost)
d=Car()
d.set_color("red")
d.set_cost(200000)
d.display_color()
d.display_cost()