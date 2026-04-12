from functions.get_files_info import get_files_info

def testing(working_directory, directory):
    if directory == ".":
        print("Result for current directory:")
    else:
        print(f"Result for '{directory}' directory:")

    print(f"  {get_files_info(working_directory, directory)}")
    print("")

def test():
    testing("calculator", ".")
    testing("calculator", "pkg")
    testing("calculator", "/bin")
    testing("calculator", "../")

if __name__ == "__main__":
    test()