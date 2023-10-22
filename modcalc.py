def divide(a,n):
    equation = a / n
    print("Quotient is")
    print(equation)

def mod(a,n):
    equation = a % n
    print("Remainder is")
    print(equation)


if __name__ == '__main__':
    print("Enter value for a")
    a = int(input())
    print("Enter value for n")
    n = int(input())
    divide(a,n)
    mod(a,n)