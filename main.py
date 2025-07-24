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