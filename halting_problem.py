#  halting_problem.py
def program_stops_on_input ( program: str, 
                             input: str ) -> bool:
    """
    This hypothetical function takes a program and an input and returns whether
    the program stops on that input. It is not possible to write this function.

    Args:
        program ( str): source code of a program

    Returns:
        bool: True if program stops on input, False otherwise
    """
    
    # ...
    return True or False # but give a correct answer in all cases in finite time

def main():
    # open its own source code
    with open('halting_problem.py') as f:
        program = f.read()
    if program_stops_on_input(program,program):
        while True:
            print('Program happily loops forever, while it should stop on')
        else:
            print('Program stops on itself, while it should loop forever')
            print("I stop anyways")
            print('This is a contradiction, so the function program_stops_on_input does not exist') 
            


