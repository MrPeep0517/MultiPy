print("\n\t\t\tWelcome to the Python Multitool. :)\nYou can view the docs at: https://github.com/MrPeep0517/MultiPy")


import datetime
from rich import print
from math import factorial
import os
import sys

RED = "\033[31m"
RESET = "\033[0m"
num2_run = True
num2 = 0
num1 = 0
operation = None


def python(cmd):
    if not cmd:
        print("[green]PYTHON[green]")

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
        if cmd:
            pythonCmd = cmd
        else:
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
                        if not cmd:
                            print(
                                f"SyntaxError: invalid syntax\n{pythonCmd} is not valid",
                                file=sys.stderr)
                        else:
                            raise Exception
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
                if not cmd:
                    print(
                        f"SyntaxError: invalid syntax\n{pythonCmd} is not valid",
                        file=sys.stderr)
                else:
                    raise Exception

    if __name__ == "__main__":
        pythonterm()
        main()


def calc(equation):
    equation1 = list(equation)
    try:
        if equation1[2].isdigit():
            equation1[2] = int(equation1[2])
        if equation1[0].isdigit():
            equation1[0] = int(equation1[0])
        match equation1[1]:
            case "+":
                return equation1[0] + equation1[2]
            case "-":
                return equation1[0] - equation1[2]
            case "*":
                return equation1[0] * equation1[2]
            case "/":
                return equation1[0] / equation1[2]
            case "^":
                return equation1[0] ** equation1[2]
    except IndexError:
        equation1[0] = int(equation1[0])
        return factorial(equation1[0])


def main():
    while True:
        cmd = input("$> ").lower()
        match cmd:
            case 'help':
                print("\tYou can view the docs at: https://github.com/MrPeep0517/MultiPy")
            case 'exit':
                break
            case "quit":
                break
            case "now":
                print(datetime.datetime.now())
            case "calc":
                print("\tPlease just put you equation into the raw input.")
            case "clr":
                os.system('cls')
            case _:
                try:
                    try:
                        cleaned_input = ""
                        for char in cmd:
                            if char != " ":
                                cleaned_input += char
                        answer = calc(cleaned_input)
                        if answer != None:
                            print("\t" + answer)
                        else:
                            raise Exception
                    except:
                        print(python(cmd))
                except:
                    print(RED + f"Error:\n\t{cmd}\n\t{"^" * len(cmd)}\nCommandError: Command not found: \"{cmd}\"." + RESET)


main()
