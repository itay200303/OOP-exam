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
