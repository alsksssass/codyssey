def pow_calculaor (pow :int , value :float):
    result = value
    for _ in range(pow):
        result *= value
    return result


def main ():
    value = float(input("Enter number: "))
    if not isinstance(value, float):
        return "float 값이 아닙니다"
    pow = int(input("Enter exponent: "))
    if not isinstance(pow, int):
        return "int 값이 아닙니다"
    if(pow < 0 or value < 0):
        return "입력값오류"
    result = pow_calculaor(pow, value)
    
    print(f"Result: {result}")
    
if __name__ == "__main__":
    main()