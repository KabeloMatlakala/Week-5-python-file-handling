# file_handling_assignment.py

# File Creation
def create_file():
    try:
        # Opening file in write mode and writing initial content
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line.\n")
            file.write("This is the second line, containing a number: 123.\n")
            file.write("This is the third line.\n")
        print("File created and initial content written.")
    except Exception as e:
        print(f"An error occurred during file creation: {e}")
    finally:
        print("File creation process completed.\n")

# File Reading and Display
def read_file():
    try:
        # Opening file in read mode and displaying content
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except FileNotFoundError:
        print("File not found. Please create the file first.")
    except Exception as e:
        print(f"An error occurred during file reading: {e}")
    finally:
        print("File reading process completed.\n")

# File Appending
def append_file():
    try:
        # Opening file in append mode and adding new content
        with open("my_file.txt", 'a') as file:
            file.write("This is an appended line.\n")
            file.write("Here’s another line with a number: 456.\n")
            file.write("Final appended line.\n")
        print("New content appended to the file.")
    except Exception as e:
        print(f"An error occurred during file appending: {e}")
    finally:
        print("File appending process completed.\n")

# Main function to run the tasks
if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()  # To verify the appended content
