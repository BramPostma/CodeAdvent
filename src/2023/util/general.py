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