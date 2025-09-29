import math

# Custom exception for invalid triangles
class InvalidTriangleError(Exception):
    """Exception raised for invalid triangle geometries"""
    pass

# Base class for all geometric figures
class GeometricFigure:
    def __init__(self, name):
        self.name = name  # Name of the figure

    def calculateArea(self):
        # Method to be implemented by subclasses
        raise NotImplementedError("Method overridden by subclass")
    
    def calculatePerimeter(self):
        # Method to be implemented by subclasses
        raise NotImplementedError("Method overridden by subclass")

# Circle class
class Circle(GeometricFigure):
    def __init__(self, radius):
        super().__init__("Circle")  # Call parent constructor
        self.radius = radius
    
    def calculateArea(self):
        # Area = π * r²
        return math.pi * (self.radius ** 2)
    
    def calculatePerimeter(self):
        # Perimeter = 2 * π * r
        return 2 * math.pi * self.radius

# Rectangle class
class Rectangle(GeometricFigure):
    def __init__(self, base, height):
        super().__init__("Rectangle")  # Call parent constructor
        self.base = base
        self.height = height
    
    def calculateArea(self):
        # Area = base * height
        return self.base * self.height
    
    def calculatePerimeter(self):
        # Perimeter = 2*(base + height)
        return 2 * (self.base + self.height)

# Triangle class
class Triangle(GeometricFigure):
    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")  # Call parent constructor
        
        # Validate if sides can form a triangle
        if not self.is_valid_triangle(side1, side2, side3):
            raise InvalidTriangleError("These sides cannot form a valid triangle")
            
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def is_valid_triangle(self, a, b, c):
        # Check triangle inequality theorem
        return (a + b > c) and (a + c > b) and (b + c > a)
    
    def calculateArea(self):
        # Using Heron's formula: Area = √[s(s-a)(s-b)(s-c)]
        s = self.calculatePerimeter() / 2  # Semi-perimeter
        
        # Check for division by zero (shouldn't happen with validation)
        if s == 0:
            raise ZeroDivisionError("Cannot calculate area with zero perimeter")
            
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area
    
    def calculatePerimeter(self):
        # Perimeter = sum of all sides
        return self.side1 + self.side2 + self.side3

# Test the implementation
print("Geometric Figures Table")
print("-----------------------")

try:
    # Create valid figures
    circle = Circle(6)
    rectangle = Rectangle(2, 8)
    triangle = Triangle(3, 4, 5)  # Valid triangle
    
    figures = [circle, rectangle, triangle]
    
    # Display results
    for figure in figures:
        area = figure.calculateArea()
        perimeter = figure.calculatePerimeter()
        print(f"{figure.name} | Area = {area:.2f} | Perimeter = {perimeter:.2f}")
    
    # Test invalid triangle
    print("\nTesting invalid triangle:")
    invalid_triangle = Triangle(1, 2, 5)  # This will raise an exception
        
except InvalidTriangleError as e:
    print(f"Error creating triangle: {e}")
except ZeroDivisionError as e:
    print(f"Math error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")