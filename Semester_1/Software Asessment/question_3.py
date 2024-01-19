def trick_score(trick, trump_suit):
    TRUMP_RANK = {"Jack": 20, "9": 14, "Ace": 11,
                  "10": 10, "King": 4, "Queen": 3, "8": 0, "7": 0}
    NON_TRUMP_RANK = {"Jack": 2, "9": 0, "Ace": 11,
                      "10": 10, "King": 4, "Queen": 3, "8": 0, "7": 0}
    SUITS = ["Spades", "Diamonds", "Hearts", "Clubs"]
    CARDS = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    if trump_suit not in SUITS:
        raise TypeError("Trump Suit must be a vaild suit")
    if len(trick) != 4:
        raise ValueError("Trick of cards must be 4 cards exactly!")

    score = 0
    for card, suit in trick:
        if suit not in SUITS or card not in CARDS:
            raise ValueError("Invalid trick configuration")
        if suit == trump_suit:
            score += TRUMP_RANK[card]
        else:
            score += NON_TRUMP_RANK[card]

    return score


if __name__ == "__main__":
    trick = {("9", "Clubs"), ("7", "Hearts"),
             ("Queen", "Hearts"), ("Jack", "Hearts")}
    print(trick_score(trick, "Clubs"))
