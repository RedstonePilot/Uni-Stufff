"""We want to create a function sum_from_file(filename) that calculate the sum of all
int contained in the text file filename."""


def sum_from_file(name):
    cleaned_data = []
    data = " "
    with open(f"{name}.txt", "r", encoding="utf-8")as in_file:
        while data:
            data = in_file.readline().strip()
            data = list(data.split())
            cleaned_data += data

            total = sum(int(i) for i in cleaned_data if i.isdigit())

    print(total)


sum_from_file("exo6")
