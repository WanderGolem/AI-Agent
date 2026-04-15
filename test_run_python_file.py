from functions.run_python_file import run_python_file

def testing(working_directory, file_path, arg=None):
    print(f"{run_python_file(working_directory, file_path, arg)}")
    print("")

def test():
    testing("calculator", "main.py")
    testing("calculator", "main.py", ["3 + 5"])
    testing("calculator", "tests.py")
    testing("calculator", "../main.py")
    testing("calculator", "nonexistent.py")
    testing("calculator", "lorem.txt")

if __name__ == "__main__":
    test()