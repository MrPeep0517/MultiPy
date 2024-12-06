print("Welcome to the Python Multitool. :)")

try:
    import datetime
    from unittest import case
    from rich import print
    from math import factorial
    import os
except ImportError as e:
    print(f"Sorry couldn't import {e}")
    quit()

num2_run = True

def calc(num1, num2, operation):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "f":
            return factorial(num1)
        case "^":
            return num1 ** num2

def main():
    while True:
        cmd = input("$> ")
        match cmd:
            case 'exit':
                break
            case "quit":
                break
            case "now":
                print(datetime.datetime.now())
            case "calc":
                num2_run = True
                try:
                    num1 = int(input("\t$> "))
                except:
                    print("[red]Error:\n\tnum1 = int(input(\"\\t$> \"))\n\t^^^^ ^ ^^^^^^^^^^^^^^^ ^^^\nValueError: Value must be an integer.[red]")
                    continue
                try:
                    operation = input("\t$> ")
                except:
                    print("[red]Error:\n\toperation = input(\"\\t$> \")\n\t^^^^^^^^^ ^ ^^^^^^^^^^^^^^^ ^^\nValueError: Value must be an operation.[red]")
                    continue
                if operation == "f":
                    num2_run = False
                if num2_run:
                    try:
                        num2 = int(input("\t$> "))
                    except:
                        print("[red]Error:\n\tnum2 = int(input(\"\\t$> \"))\n\t^^^^ ^ ^^^^^^^^^^^^^^^ ^^^\nValueError: Value must be an integer.[red]")
                        continue
                try:
                    print(f"{num1} {operation} {num2} = {calc(num1, num2, operation)}")
                except:
                    print(f"factorial({num1}) = {calc(num1, 0, operation)}")
            case "clr":
                os.system('clear')
main()