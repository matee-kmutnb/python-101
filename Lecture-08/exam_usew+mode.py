# Example using w+ mode (write and read)
def example_w_plus_mode():
 # Open the file for reading and writing (truncating it)
 with open('example_w+.txt', 'w+') as file:
 # Write some content to the file
    file.write("This is the first line in the file.\n")
    file.write("This is the second line in the file.\n")

 # Move the file pointer back to the beginning
    file.seek(0)

 # Read the content of the file
    content = file.read()
    print("Content of the file:")
    print(content)

example_w_plus_mode()