try:
    print("reading file content:")
    file=open("sample.txt","r")
    read_file=file.read()
    print(read_file)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not found.")
