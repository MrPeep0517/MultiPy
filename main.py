print("\n\t\t\tWelcome to the Python Multitool. :)\nYou can veiw the docs at: https://github.com/MrPeep0517/PyMulti")

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
num2 = 0
num1 = 0
operation = None


def python():
    print("[green]PYTHON[green]")

    import sys

    indents = ["def", "if", "while", "for"]
    oldCmds = []

    def isindent(text):
        for indent in indents:
            if text.startswith(indent):
                return True
        return False

    def seplist(list: list[str], sep=" ") -> str:
        things = ""
        for item in list:
            if item != list[-1]:
                things += (item + sep)
            else:
                things += item
        return things

    def isvalidindent(text):
        try:
            exec(text + "\n    pass")
        except:
            return False
        else:
            return True

    def pythonterm():
        oldCmds = []
        while True:
            pythonCmd = input(">>> ")
            if pythonCmd == "exit()":
                return 0
            try:
                pythonOut = eval(pythonCmd)
                if pythonOut != None:
                    print(pythonOut)
            except:
                try:
                    if isindent(pythonCmd):
                        if not isvalidindent(pythonCmd):
                            print(
                                f"SyntaxError: invalid syntax\n{pythonCmd} is not valid",
                                file=sys.stderr)
                        else:
                            oldCmds.append(pythonCmd)
                            while True:
                                if oldCmds[-1] == "" and pythonCmd == "":
                                    exec(seplist(oldCmds, "\n"))
                                    break
                                print("...", end=" ")
                                pythonCmd = input()
                                oldCmds.append(pythonCmd)
                    else:
                        exec(pythonCmd)
                except Exception as e:
                    print(
                        f"SyntaxError: invalid syntax\n{pythonCmd} is not valid",
                        file=sys.stderr)

    if __name__ == "__main__":
        pythonterm()
        main()


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
        case "!":
            return factorial(num1)
        case "^":
            return num1 ** num2


def main():
    while True:
        cmd = input("$> ").lower()
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
                if operation == "!":
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
                os.system('cls')
            case "py":
                python()
            case _:
                print(f"Error:\n\t{cmd}\n\t{"^" * len(cmd)}\nCommandError: Command not found: \"{cmd}\".")


main()
