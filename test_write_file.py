from functions.write_file import write_file

def testing(working_directory, file_path, content):
    print(f"{write_file(working_directory, file_path, content)}")
    print("")

def test():
    testing("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    testing("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    testing("calculator", "/tmp/temp.txt", "this should not be allowed")

if __name__ == "__main__":
    test()