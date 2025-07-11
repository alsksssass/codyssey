def pow_calculaor (pow :int , value :float):
    result = 1.0
    for _ in range(pow):
        result *= value
    return result


def main ():
    value = float(input("Enter number: "))
    if not isinstance(value, float):
        return "Invalid exponent input."
    pow = int(input("Enter exponent: "))
    if not isinstance(pow, int):
        return "Invalid number input."
    if(pow < 0 or value < 0):
        return "입력값오류"
    result = pow_calculaor(pow, value)
    
    print(f"Result: {result}")
    
if __name__ == "__main__":
    main()