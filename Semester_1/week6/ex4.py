"""Write a script that reads the content of a text file and prints it in upper case."""
clean_data = []
with open("changelog.txt", "r", encoding="utf-8")as in_file:
    data = " "
    while data:
        data = in_file.readline().strip()
        clean_data.append(data.upper())

print(" ".join(clean_data))
