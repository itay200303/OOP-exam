from enum import Enum, auto
from abc import ABC, abstractmethod
from functools import wraps
import random


# ==== ENUMS ====
class CardSuit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4


class CardRank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


# ==== EXCEPTIONS ====
class DeckCheatingError(Exception):
    pass


# ==== INTERFACES ====
class AbstractCard(ABC):
    @property
    @abstractmethod
    def suit(self):
        pass

    @property
    @abstractmethod
    def rank(self):
        pass

    @abstractmethod
    def get_display_name(self):
        pass


class AbstractDeck(ABC):
    @property
    @abstractmethod
    def cards(self):
        pass

    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def add_card(self, card):
        pass


# ==== DECORATOR ====
def fair_deck(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, Deck):
            seen = set()
            for card in result.cards:
                if card in seen:
                    raise DeckCheatingError("Duplicate card detected in deck!")
                seen.add(card)
        elif isinstance(result, Card):
            pass  # Can add validations here too
        return result

    return wrapper


# ==== CARD IMPLEMENTATION ====
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
        return f"Card(suit={self.suit}, rank={self.rank})"


# ==== DECK IMPLEMENTATION ====
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


# ==== UTILITY FUNCTIONS ====
def max_card(*cards):
    if not cards:
        return None
    return max(cards)


def cards_stats(*cards, **kwargs):
    results = []
    if not cards:
        return results

    cards = list(cards)

    if kwargs.get('max'):
        results.extend(sorted(cards, reverse=True)[:kwargs['max']])
    if kwargs.get('min'):
        results.extend(sorted(cards)[:kwargs['min']])
    if kwargs.get('len'):
        results.append(len(cards))
    return results

# ==== EXAMPLE USAGE ====
if __name__ == "__main__":
    deck = Deck()

    print("Accessing cards directly by index:")
    for i in range(5):
        print(f"Card at index {i}: {deck[i]}")

    print("\nIterating through all cards in the deck:")
    for card in deck:
        print(card)

    print("\nDrawing a card:")
    card1 = deck.draw()
    print("Drew card:", card1)

    print("\nMax and min in deck:")
    print("Max card:", deck.max())
    print("Min card:", deck.min())

    print("\nCustom max_card function:")
    card2 = deck.draw()
    card3 = deck.draw()
    print("Highest:", max_card(card1, card2, card3))

    print("\nCustom cards_stats function:")
    stats = cards_stats(card1, card2, card3, max=2, min=1, len=1)
    print("Stats:", stats)


