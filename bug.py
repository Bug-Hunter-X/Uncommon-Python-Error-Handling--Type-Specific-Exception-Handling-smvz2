def function_with_uncommon_bug(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            print("Error: Type mismatch")
            return None
        else:
            print("Error: Unsupported operand type(s) for /'")
            return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result

#Example with uncommon error
print(function_with_uncommon_bug(5,0))#ZeroDivisionError
print(function_with_uncommon_bug("hello",5))#TypeError
print(function_with_uncommon_bug(5,"world"))#TypeError
print(function_with_uncommon_bug(5,2))#10
print(function_with_uncommon_bug([1,2],2)) #TypeError