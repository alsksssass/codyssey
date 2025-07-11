def pow_calculaor (pow :int , value :float):
    result = value
    for _ in range(pow):
        result *= value
    return result


def main ():
    value = float(input("제곱할 값을 입력하세요"))
    pow = int(input("제곱 횟수를 입력하세요"))
    if(pow < 0 or value < 0):
        return "입력값오류"
    result = pow_calculaor(pow, value)
    
    print(f"값은 {result}입니다.")
    
if __name__ == "__main__":
    main()