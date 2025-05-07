# File Read & Write Challenge 🖋️: Create a program that 
# reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and
# handle errors if it doesn’t exist or can’t be read.

# Ask for the file to read
file_name = input("What is the file name? ")

# Try reading the file
try:
    with open(file_name, "r") as read_file:
        data = read_file.read()
        print("Original file contents:")
        print(data)
except FileNotFoundError:
    print("File not found.")
else:
    # Write to a new file only if reading succeeded
    with open("modified_" + file_name, "w") as write_file:
        write_file.write("Write function worked!")

    print(f"Modified content written to: modified_{file_name}")
finally:
    print("Thank you for your service.")

