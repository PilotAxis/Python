myfile = open(r"C:\Users\moham\OneDrive\My Document\File Handling\poem.txt", 'r')
str = myfile.read(30)
print(str)
str2 = myfile.read(50)
print(str2)
myfile.close()