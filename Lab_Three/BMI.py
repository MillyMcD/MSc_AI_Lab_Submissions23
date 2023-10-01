class BMI:

    def __init__(self):
        self.weight=0
        self.height=0
        self.bmi=0

    def set_weight(self,weight):
        self.weight = weight

    def set_height(self,height):
        self.height = height
    
    def calc_bmi(self):
        self.bmi=self.weight/(self.height**2)
    
    def get_bmi(self):
        return self.bmi


def main():
    b = BMI()
    #print(b.weight)

    b.set_weight(77)
    b.set_height(1.75)

    #print (b.weight,b.height)

    b.calc_bmi()
    #print(b.get_bmi())
    print(f'For weigth {b.weight}kg and height {b.height}m the BMI is calculated at {b.get_bmi():0.2f}')

main()
