def add(a, b):
  """Adds two numbers."""
  return a + b

def subtract(a, b):
  """Subtracts two numbers."""
  return a - b

def multiply(a, b):
  """Multiplies two numbers."""
  return a * b

def divide(a, b):
  """Divides two numbers. Raises ValueError if b is zero."""
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b

if __name__ == "__main__":
    
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"8 / 2 = {divide(8, 2)}")
    try:
      print(f"8 / 0 = {divide(8, 0)}")
    except ValueError as e:
      print(e)