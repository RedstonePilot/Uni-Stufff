"""Write a function save_list2file(sentences, filename) that takes twoparameters, 
where sentences is a list of string, and filename is a string representing thename of the file where the 
content of sentences must be saved. Each element of the listsentences should be written on its own line 
in the file filename"""


def save_list2file(sent, name):
    with open(f"{name}.txt", "w", encoding="utf-8")as out_file:
        for s in sent:
            out_file.write(s)
            out_file.write("\n")


save_list2file(["line1", "line2", "line3"], "exo2")
