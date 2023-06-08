#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    operators = ["+", "-", "*", "/"]
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        result = add(a, b)
    elif sys.argv[2] == "-":
        result = sub(a, b)
    elif sys.argv[2] == "*":
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    sys.exit(0)
