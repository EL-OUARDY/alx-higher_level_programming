#!/usr/bin/python3
if __name__ == "__main__":  # works only on direct execution
    """custom calculator ^_^"""
    from calculator_1 import add, sub, mul, div  # import all functions
    import sys

    if len(sys.argv) != 4:  # wrong argument count
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    #  check operator
    if (operator != "+" and operator != "-" and
            operator != "*" and operator != "/"):
        # unknown operator
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    #  get user arguments and convert them
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    #  process the desired operation
    if operator == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
