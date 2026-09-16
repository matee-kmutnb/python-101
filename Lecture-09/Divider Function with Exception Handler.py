def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    else:
        return result

a, b = map(int, input("Enter two numbers separated by space: ").split())
print(divide(a, b))
print("End of program")