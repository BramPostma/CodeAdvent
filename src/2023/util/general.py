""" General Util funcs """


def read_text(file_path: str) -> list[str]:
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Remove newline characters from each line
            lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    
def is_numeric(char: str):
    """ Checks if char is numeric """
    return char.isdigit()

def len_of_int(integer: int) -> int:
    """ Returns the length of a int """
    return len(str(integer))
