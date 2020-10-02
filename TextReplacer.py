import os, sys, fileinput
from time import sleep

def search(newValue, toReplace, fileName):
    try:
        with fileinput.FileInput(fileName, inplace=True, backup=".bak") as file:
            for line in file:
                print(line.replace(toReplace, newValue), end="")
        print("Done!!")
    except:
        print("An error ocurred")
    
def main():
    print("Welcome! remember this will replace ALL matched words in your documment!!!")
    sleep(2)
    oldValue = input("Insert the value you want to replace: ")
    sleep(1)
    value = input("Great! now insert the new value: ")
    sleep(1)
    fileName = input("Awesome, now insert the name of your file or the absolute path, extention included (for example: foo.html): ")

    search(value, oldValue, fileName)
main()