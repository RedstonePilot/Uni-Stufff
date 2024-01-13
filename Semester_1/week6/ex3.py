"""Write a function save_to_log(entry, logfile) that takes two parameters,
 a stringentry to be written at the end of the text file named logfile (also a string). 
 The previouscontent of the logfile MUST NOT be erased."""


def save_to_log(entry, logfile):
    with open(f"{logfile}.txt", "a", encoding="utf-8")as out_file:
        out_file.write(entry)


save_to_log("This is the end of the file\n", "exo3")
