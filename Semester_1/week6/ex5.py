"""Write a function to_upper_case(input_file, output_file) that takes two
string parameters containing the name of two text files. The function reads the content of the
input_file and saves it in upper case into the output_file."""


def to_upper_case(input_file, output_file):
    clean_data = []
    with open(f"{input_file}.txt", "r", encoding="utf-8")as in_file:
        data = " "
        while data:
            data = in_file.readline()
            clean_data.append(data.upper())

    with open(f"{output_file}.txt", "w", encoding="utf-8")as out_file:
        for dat in clean_data:
            out_file.write(dat)


to_upper_case("changelog", "upper")
