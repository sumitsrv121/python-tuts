file_reader = open("mydata", "r")
# read whole file
# print(file_reader.read())

# read line
# print(file_reader.readline(), end="")
# print(file_reader.readline(), end="")


file_writer = open("abc", "a")
for line in file_reader:
    file_writer.write(line)
