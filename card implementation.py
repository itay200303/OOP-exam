class Card(AbstractCard):
    def __init__(self, suit: CardSuit, rank: CardRank):
        if not isinstance(suit, CardSuit) or not isinstance(rank, CardRank):
            raise ValueError("Invalid suit or rank")
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def get_display_name(self):
        return f"{self.rank.name.capitalize()} of {self.suit.name.capitalize()}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank.value == other.rank.value:
            return self.suit.value < other.suit.value
        return self.rank.value < other.rank.value

    def __gt__(self, other):
        if self.rank.value == other.rank.value:
            return self.suit.value > other.suit.value
        return self.rank.value > other.rank.value

    def __hash__(self):
        return hash((self.suit, self.rank))

    def __str__(self):
        return self.get_display_name()

    def __repr__(self):
        return f"Card(suit={self.suit}, rank={self.rank})

