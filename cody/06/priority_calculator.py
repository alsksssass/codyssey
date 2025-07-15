import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devide(a, b):
    return a / b

ops = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}

def evaluate(tokens):
    stack = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ("*", "/"):
            if not stack:
                raise ValueError("Invalid input.")
            prev = float(stack.pop())
            i += 1
            try:
                next_val = float(tokens[i])
            except:
                raise ValueError("Invalid input.")
            result = ops[token](prev, next_val)
            stack.append(str(result))
        else:
            stack.append(token)
        i += 1

    result = float(stack[0])
    i = 1
    while i < len(stack):
        op = stack[i]
        val = float(stack[i+1])
        result = ops[op](result, val)
        i += 2
    return result

def main():
    while True:
        try:
            expr = input("수식을 입력하세요 (예: 4 + 5 * 3 - 2), 종료(exit): ")
            if expr.lower() == "exit":
                print("프로그램 종료")
                sys.exit(0)
            tokens = expr.strip().split()
            if not tokens:
                continue
            result = evaluate(tokens)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print("Invalid input.")

if __name__ == "__main__":
    main()
