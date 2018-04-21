import math

class triangle_area():
    def __init__(self):
        print("Choose the proper method for your given knowns. Enter 'object.help_' for options")
        
    def help_(self):
        print("object.method")
        print("object.SSA_scalene - two sides and one angle opposite a given side are given")
        print("object.SSS_scalene - three sides are given")
        print("object.help - lists methods")
    
    def right_triangle(self, a, b):
        ans = (0.5)*(a*b)
        print("Area: %s units^2" %(ans))
        
    def SSA_scalene(self, a, b, c_angle):
        ans = (0.5)*(a*b*(math.sin(c_angle)))
        print("Area: %s units^2" %(ans))
        
    def SSS_scalene(self, a, b, c):
        s = (0.5)*(a + b + c)
        try:
            ans = math.sqrt(s*(s - a)*(s - b)*(s - c))
            print("Area: %s units^2" %(ans))
        except:
            print("Encountered Error: No Triangle")       
