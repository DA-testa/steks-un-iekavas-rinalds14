# python3

from collections import namedtuple
import os

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))


        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
            
    if opening_brackets_stack:
        return opening_brackets_stack[0].position

    return "Success"

def main():
    choice = input("F for files I for input:")
    file_path = os.path.join("steks-un-iekavas-rinalds14", 'test')
    if choice == "F":
        for i in range(6):
            with open(os.path.join(file_path, str(i)), 'r') as f:
                text = f.read()
                mismatch = find_mismatch(text)
                print(mismatch)
    elif choice == "I":
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
    else:
        print("There is no other choice :P")

if __name__ == "__main__":
    main()
