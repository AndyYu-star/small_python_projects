file = open("scary do not mess with.py","r+")
file.seek(214)
num = int(file.readline().strip(".\")\n"))
num += 1
file.seek(214)
file.write(str(num) + ".\")\n")
file.close()

print("Hello World? I am number 27.")
