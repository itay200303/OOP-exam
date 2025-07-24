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