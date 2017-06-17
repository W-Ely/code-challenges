"""Sort a deck of cards

zebulan, Unnamed, acaccia, j_codez, Mr.Child, iamchingel (plus 3 more warriors)

def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)

"""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    >>> sort_cards(
        ['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']
    )
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    """
    ref = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
        'J': 11, 'Q': 12, 'K': 13
    }
    changed = True
    while changed:
        changed = False
        for i in range(len(cards) - 1):
            if ref[cards[i]] > ref[cards[i+1]]:
                cards[i], cards[i+1] = cards[i+1], cards[i]
                changed = True
    return cards
