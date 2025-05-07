try:
    file = open("exaemple.txt","r")
    data = file.read()

    print("The data is ",data)
except FileNotFoundError:
    print("An error occured.")