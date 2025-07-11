def pow_calculaor (pow :int , value :float):
    result = 1.0
    for _ in range(pow):
        result *= value
    return result


def main ():
    try:
        value = float(input("Enter number: "))
    except:
        return print("Invalid number input.")
    try:
        pow = int(input("Enter exponent: "))
    except:
        return print("Invalid exponent input.")
    if(pow < 0 or value < 0):
        return print("입력값오류")
    result = pow_calculaor(pow, value)
    
    print(f"Result: {result}")
    
if __name__ == "__main__":
    main()