# Define a class for complex numbers
class Complex:
# Define a constructor to initialize the real and imaginary parts
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

# Define a method to display the complex number
    def display(self):
        if self.imag >= 0:
            print(f"{self.real}+{self.imag}i")
        else:
            print(f"{self.real}{self.imag}i")

# Define a method to add two complex numbers
    def add(self, other):
# Create a new complex number to store the result
        result = Complex(0, 0)
        # Add the real and imaginary parts
        result.real = self.real + other.real
        result.imag = self.imag + other.imag
        # Return the result
        return result

# Define a method to subtract two complex numbers
    def subtract(self, other):
        # Create a new complex number to store the result
        result = Complex(0, 0)
        # Subtract the real and imaginary parts
        result.real = self.real - other.real
        result.imag = self.imag - other.imag
        # Return the result
        return result

# Define a method to multiply two complex numbers
    def multiply(self, other):
        # Create a new complex number to store the result
        result = Complex(0, 0)
        # Use the formula (a+bi)(c+di) = (ac-bd)+(ad+bc)i
        result.real = self.real * other.real - self.imag * other.imag
        result.imag = self.real * other.imag + self.imag * other.real
        # Return the result
        return result

# Create two complex numbers
x = Complex(3, 4)
y = Complex(5, -2)

# Display the complex numbers
print("The first complex number is:")
x.display()
print("The second complex number is:")
y.display()

# Perform the calculations
sum = x.add(y)
difference = x.subtract(y)
product = x.multiply(y)

# Display the results
print("The sum of the complex numbers is:")
sum.display()
print("The difference of the complex numbers is:")
difference.display()
print("The product of the complex numbers is:")
product.display()
