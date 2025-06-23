try:
    with open("data.txt","r")as file:
        content=file.read()
    print(content)
except FileNotFoundError:
    print("this file was not found")
except IOError:
    print("AN error occured for reading a file")
else:
    print("file read succesfully")
finally:
    print("operation is complete")

