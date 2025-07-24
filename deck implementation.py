class Deck(AbstractDeck):
    def __init__(self, shuffle=True):
        self._cards = [Card(suit, rank) for suit in CardSuit for rank in CardRank]
        if shuffle:
            self.shuffle()

    @property
    def cards(self):
        return list(self._cards)  # Return copy

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop(0) if self._cards else None

    @fair_deck
    def add_card(self, card):
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added.")
        if card in self._cards:
            raise DeckCheatingError("Attempt to add duplicate card to deck.")
        self._cards.append(card)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __iter__(self):
        return iter(self._cards)

    def max(self):
        return max(self._cards)

    def min(self):
        return min(self._cards)
