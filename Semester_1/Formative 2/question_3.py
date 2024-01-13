def read_from_file(filename):
    """Parses Data from a file into:
        {Name:{200m:time,800m:time,100m:time},...}
        As long as the file conforms to the format:
        Name,time1,time2,time3
        Any lines with # will be ignored


    Args:
        filename (str): path to file containing the data to be parsed

    Raises:
        ValueError: If the file doesn't conform to the correct format

    Returns:
        dict: A nested dictionary in the format
             {Name:{200m:time,800m:time,100m:time},...}
    """
    fin_dict = {}
    races = ["200m", "110m", "800m"]
    with open(filename, "r", encoding="utf-8")as in_file:
        data = " "
        while data:
            data = in_file.readline().strip()
            if data and data[0] != "#":  # ignore empty/hashed out rows
                data = data.split(",")
                if len(data) != 4:  # wrong format of data
                    raise ValueError

                fin_dict[data[0]] = {race: float(
                    time) for race, time in (zip(races, data[1:]))}
    return fin_dict
