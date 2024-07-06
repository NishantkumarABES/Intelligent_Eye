file = open("objects_info.txt", "r")
text = file.read().split("\n")
object_info = {}

for statement in text:
    index = statement.find(":")
    object_info[statement[:index]] = statement[index+2:]

print(object_info)
