from functions.get_file_content import get_file_content
from config import MAX_CHARS

def testing(working_directory, file):
    content = get_file_content(working_directory, file)
    len_content = len(content)
    '''    
    if  content[0:6] != "Error:":
        print(f"File length: {len_content}")
        print(content)
        if len_content > MAX_CHARS:
            print(content[MAX_CHARS:])
    else:
        '''
    print(content)
    print("")

def test():
    #testing("calculator", "lorem.txt")
    testing("calculator", "main.py")
    testing("calculator", "pkg/calculator.py")
    testing("calculator", "/bin/cat")
    testing("calculator", "pkg/does_not_exist.py")

if __name__ == "__main__":
    test()