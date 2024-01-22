def calculator(func):
    def idk(expression):
        try:
            result = func(expression)
            return result
        except Exception:
            print(f"обана награвся: а нізя на нуль ділити")
            return None

    return idk

@calculator
def calculate(expression):
    a = int(input("перше число"))
    b = int(input("друге число"))
    return eval(expression)


result = calculate("a / b")
print(f"от така біда: {result}")
