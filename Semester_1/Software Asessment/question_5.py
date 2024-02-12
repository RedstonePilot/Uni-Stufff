from copy import deepcopy


class GameObject:
    """Class to represent the wooden object
    """

    def __init__(self, shape, colour):
        """Initialise the class

        Args:
            shape (str): The shape of the wooden object
            colour (str): The colour of said object
        """
        self._shape = shape
        self._colour = colour

    @property
    def shape(self):
        """Keeps the shape propety protected"""
        return deepcopy(self._shape)

    @property
    def colour(self):
        """Keeps the colour property protected"""
        return deepcopy(self._colour)

    def __eq__(self, other):
        """Returns True if the colour and shape are the same"""
        if not isinstance(other, GameObject):
            return False
        shape = self._shape == other._shape
        colour = self._colour == other._colour
        return shape and colour

    def __hash__(self):
        """returns a hash of the object"""
        return hash((self.shape, self.colour))


class GameCard:
    """A class to represent the card in the game"""

    def __init__(self, object1, object2):
        """Initialises the class so the card has 2 objects

        Args:
            object1 (GameObject): The first game object
            object2 (GameObject): The second game object on the card
        """
        self._content = [deepcopy(object1), deepcopy(object2)]

    @property
    def content(self):
        """Keeps the content property protected"""
        return deepcopy(self._content)

    def __eq__(self, other):
        """Overloads the equals operator so that 2 cards are the same if 
           their two objects are the same shape and colour"""
        if not isinstance(other, GameCard):
            return False
        return set(self.content) == set(other.content)


class CardDeck:
    """Class representing the Deck in the game"""

    def __init__(self, pcs):
        """Initialises the class with a given set of wooden items to play with

        Args:
            pcs (list): List of gameObjects that are available to play with

        Raises:
            ValueError: If there are not 3,4 or 5 pieces or
                        if 2 pieces share the same shape and colour
        """
        shape = set()
        colour = set()
        if len(pcs) > 5 or len(pcs) < 3:
            raise ValueError("There must be 3,4 or 5 pieces")
        for pc in pcs:
            if pc.shape in shape or pc.colour in colour:

                raise ValueError(
                    "No piece may share the same shape or colour!")
            shape.add(pc.shape)
            shape.add(pc.colour)

        self.pieces = pcs

    def generate_deck(self):
        """Generates the usable deck of cards given the pieces available

        Returns:
            list: List of cards that are valid
        """
        deck = []
        colours = [pc.colour for pc in self.pieces]
        shapes = [pc.shape for pc in self.pieces]
        for pc in self.pieces:
            t_col = deepcopy(colours)
            t_col.remove(pc.colour)
            t_shp = deepcopy(shapes)
            t_shp.remove(pc.shape)

            combo = (t_col[0], t_shp[1]), (t_col[1], t_shp[0])

            deck.append(GameCard(pc, GameObject(combo[0][0], combo[0][1])))
            deck.append(GameCard(pc, GameObject(combo[1][0], combo[1][1])))
            deck.append(GameCard(GameObject(
                combo[0][0], combo[0][1]), GameObject(combo[1][0], combo[1][1])))

        return deck


if __name__ == "__main__":

    game = CardDeck([GameObject("Green", "Bottle"), GameObject(
        "Red", "Chair"), GameObject("Blue", "Book")])

    (game.generate_deck())
