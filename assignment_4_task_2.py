#write the file
output_text=input("write your text:")
print("Data successfully written to output.txt file")

file1=open("output.txt","w")
text_1=file1.write(output_text+"\n")
file1.close()

#append in the file
append_text=input("write additional text to append:")
print("data successfully append.")

file2=open("output.txt","a")
appended_txt=file2.write(append_text)
file2.close()
file2.close()

#read and display the file
print("final content of output.txt:")

file3=open("output.txt","r")
print(file3.read())
file3.close()