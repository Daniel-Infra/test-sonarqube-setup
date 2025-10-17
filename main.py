# main.py - with intentional issues for SonarQube to find

import os  # Unused import - SonarQube will flag this

def calculate_total(items):
    """Calculate sum of items."""
    total = 0
    for i in range(len(items)):  # Should use for item in items
        total += items[i]
    return total

def unused_function():  # This function is never called
    """This function serves no purpose."""
    return "unused"

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def process(self, value):
        # Missing docstring
        if value > 0:
            self.data.append(value)
        else:
            pass  # Empty block - SonarQube will flag this

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = calculate_total(numbers)
    print(f"Total: {result}")
    
    # Variable assigned but never used
    unused_var = 42
