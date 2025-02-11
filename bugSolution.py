def improved_function_with_uncommon_bug(a, b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise TypeError("Operands must be numbers")
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

#Example
print(improved_function_with_uncommon_bug(5,0))#ZeroDivisionError
print(improved_function_with_uncommon_bug("hello",5))#TypeError
print(improved_function_with_uncommon_bug(5,"world"))#TypeError
print(improved_function_with_uncommon_bug(5,2))#2.5
print(improved_function_with_uncommon_bug([1,2],2)) #TypeError