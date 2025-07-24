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
