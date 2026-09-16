# Example of common exceptions
try:
    x = 10 / 0 # ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")

print("End of program")
#Output : Error: division by zero