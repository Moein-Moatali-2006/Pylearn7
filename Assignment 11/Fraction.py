#Moein Moatali


#make class for Fraction
class Fraction:
    
    def __init__(self,s,m):
        self.s=s
        self.m=m
    
    def sum(self,other):
        result_s=(self.s * other.m) + (other.s * other.m)
        result_m=self.m * other.m
        result=Fraction(result_s , result_m)
        return result
    
    def show(self):
        print(self.s ,"/", self.m)

    def sub(self,other):
        result_s=(self.s * other.m) - (self.m * other.s)
        result_m=self.m * other.m
        result=Fraction(result_s , result_m)
        return result
    
    def mul(self,other):
        result_s=self.s*other.s
        result_m=self.m * other.m
        result = Fraction(result_s,result_m)
        return result
    
    def div(self,other):
        result_s=self.s * other.m
        result_m=self.m * other.s
        result =Fraction(result_s,result_m)
        return result
    
    def convert_fraction_to_number(self):
        return self.s / self.m
    
    def simple(self):
        unit=self.s // self.m
        result_s=self.s % self.m
        result_m=self.m
        return f"{unit} unit and  {result_s} / {result_m}"


#make fraction
fraction_1=Fraction(17,4)
fraction_2=Fraction(3,4)
#sum
fraction_3=fraction_1.sum(fraction_2)
fraction_3.show()
#sub
fraction_4=fraction_1.sub(fraction_2)
fraction_4.show()
#mul
fraction_5=fraction_1.mul(fraction_2)
fraction_5.show()
#div
fraction_6=fraction_1.div(fraction_2)
fraction_6.show()
# convert_fraction_to_number
print(fraction_1.convert_fraction_to_number())
#simple
fraction_7=fraction_1.simple()
print(fraction_7)


