# #!/usr/bin/python3


print ("Lätt\n\n")

file = ""
file = open("text.txt")

print (file.read().upper())

file.close()


print ("Medel\n\n")

file1 = [""]
file1 = open("text.txt")

file2 = file1.read()

list_file = file2.split()
list_words = file2.split().replace('.',' ')

print (file2)
print (list_file)
print (list_words)
