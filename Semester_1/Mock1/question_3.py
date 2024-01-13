def getPasserRating(filename):
    with open(filename, "r")as data_file:
        data = data_file.read().splitlines()
        data = [d.split(",") for d in data if d[0] != "#"]

    processed = []
    ret = {}

    for player in data:
        name, att, comp, yds, td, ints = player
        comp, att, yds, td, ints = float(comp), float(
            att), float(yds), float(td), float(ints)
        if name in processed:
            raise KeyError
        if len(player) != 6:
            raise ValueError

        processed.append(name)
        a = min(2.375, ((comp/att) - 0.3) * 5)
        b = min(2.375, ((yds/att)-3)*0.25)
        c = min(2.375, (td/att)*20)
        d = min(2.375, 2.375 - ((ints/att)*25))

        a = max(0, a)
        b = max(0, b)
        c = max(0, c)
        d = max(0, d)
        rating = ((a+b+c+d)/6)*100
        ret[name] = round(rating, 1)

    return ret


if __name__ == "__main__":
    print(getPasserRating("data/nfl2022.csv"))
