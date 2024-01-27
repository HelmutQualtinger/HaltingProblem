#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
"""
    This hypothetical function takes a program and an input and returns whether
    the program stops on that input. It is not possible to write this function. 
    There are problems which will be forever unanswered. This is one of them. Such 
    questions are called undecidable. And can be formulated in nor more than a few lines of code.

    Args:
        program ( str): source code of a program
        input ( str): input to the program
    Returns:
        bool: True if program stops on input, False otherwise
        
        
"""


def program_stops_on_input(program: str, input_data: str) -> bool:
    # ... Really smart stuff here ...
    return True  # or False, but give a correct answer in all cases in finite time


def main():
    # open its own source code
    file_name = sys.argv[1]
    with open(file_name, 'r', encoding="utf-8") as file:
        program = file.read()

    print("Checking if this program stops on itself\n", program)

    if program_stops_on_input(program, program):
        print('Program stops on itself, but:')
        while True:
            print('Program happily loops forever, while it should stop on itself')
    else:
        print('Program will not stop on itself, it should loop forever')
        print("I stop anyways")
        print(
            'This is alsoa contradiction, so the function program_stops_on_input does not exist')


main()
