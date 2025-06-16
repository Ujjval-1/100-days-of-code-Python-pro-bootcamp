# with open("/Users/ujjwa/Downloads/my_file") as file:      #Absolute file path
#     contents = file.read()
#     print(contents)

with open("../../../Downloads/my_file") as file:      # Relative file path
    contents = file.read()
    print(contents)

# with open("/Users/ujjwa/Downloads/my_file" ,mode = "w") as file:     # mode = "a" means appending and if mode ="w" and file name doesn't exist, it will create new for you.
#     file.write("new tesisi")

# Relative file path (./Work/file means we are checking for file in work folder or not...      ../Work/file means first it will go to parent folder of work then check whether file is in parent folder or not)



