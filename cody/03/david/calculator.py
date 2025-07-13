import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def devide(a, b):
    return a / b


ops = {"+": add, "-": subtract, "*": multiply, "/": devide}


def get_float(prompt):
    while True:
        raw = input(prompt)
        if raw == "exit":
            print("프로그램 종료")
            sys.exit(0)
        try:
            cleaned = raw.strip().replace("\t", "").replace(" ", "")
            return float(cleaned)
        except ValueError:
            print("입력값이 잘못되었습니다. 실수를 입력해주세요.1")


def defaultApp():
    while True:
        print("계산할 값을 입력해 주세요 종료시(exit)")
        value1 = get_float("실수를 입력하세요: ")
        value2 = get_float("다음 실수를 입력하세요: ")
        operator = input("연산자를 입력하세요 (+, -, *, /): ").strip()

        if operator == "/" and value2 == 0:
            print("Error: Division by zero.")
            continue
        if operator in ops:
            print(f"Result: <{int(ops[operator](value1,value2))}>")
        else:
            print("Invalid operator.")
            continue


if __name__ == "__main__":
    defaultApp()
