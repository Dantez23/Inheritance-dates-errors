# cylinder
class cylinder:
    def __init__(self,radius,height,color):
        self.radius=radius
        self.height=height
        self.color=color

    def calculate_area(self, is_closed = True):
        if is_closed == True:
            area = 2 * 22/7 * self.radius ** 2 + 22/7 * self.radius * self.height
            print(f"area of closed cylinder is: {area}")
        else:
            area = 2 * 22 / 7 * self.radius ** 2 + 22 / 7 * self.radius * self.height
            print(f"area of closed cylinder is: {area}")

    def calc_volume(self):
        v = 22/7 * self.radius ** 2 * self.height
        print(f"volume of cylinder is: {v}")

c1 = cylinder(radius=10, height=11, color='blue')
c2= cylinder(radius=8.5, height=22.35, color='red')
c1.calc_volume()
c1.calc.area(is_closed=False)
