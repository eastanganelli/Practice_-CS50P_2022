""" Libraries Import """
from library.stack import Stack

def main() -> None:
    """ Main """
    miPilita: Stack = Stack()
    
    for i in range(7):
        miPilita.push(i)
        
    for i in reversed(range(7)):
        print(miPilita.pop()._Value)

def function_custom() -> any:
    """ Custom Function """
    return 1

if __name__ == "__main__":
    main()
