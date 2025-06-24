from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]


def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])


def deal(number_of_hands, cards_per_hand):
    if not isinstance(number_of_hands, int) or number_of_hands < 1:
        raise ValueError("number_of_hands must be a positive integer")
    if not isinstance(cards_per_hand, int) or cards_per_hand < 1:
        raise ValueError("cards_per_hand must be a positive integer")
    if number_of_hands * cards_per_hand > 52:
        raise ValueError("Not enough cards in the deck for the requested hands")
    deck = shuffled_deck()
    hands = []
    for i in range(number_of_hands):
        start_index = i * cards_per_hand
        end_index = start_index + cards_per_hand
        hand = set(deck[start_index:end_index])
        if len(hand) != cards_per_hand:
            raise ValueError("Duplicate cards found in the hand")
        hands.append(hand)
    return hands


def poker_classification(hand):
    if not isinstance(hand, set):
        raise TypeError("The hand must be a set of Card objects")
    if len(hand) != 5:
        raise ValueError("The hand must contain exactly 5 cards")
    if not all(isinstance(card, Card) for card in hand):
        raise TypeError("All elements in the hand must be Card objects")

    # Sort the hand by rank, so the set has to be converted to a list
    hand = sorted(hand, key=lambda card: card.rank)

    # Check for flush (all cards of the same suit)
    is_flush = all(card.suit == hand[0].suit for card in hand)

    # Check for straight (consecutive ranks, but handle Ace as both high and low)
    ranks = [card.rank for card in hand]
    is_broadway_straight = (ranks == [1, 10, 11, 12, 13])
    is_lower_straight = all(
        ranks[i] == ranks[i-1]+1 for i in range(1, len(ranks)))
    is_straight = is_broadway_straight or is_lower_straight

    # Count occurrences of each rank in descending order
    rank_counts = {}
    for card in hand:
        rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1
    counts = sorted(rank_counts.values(), reverse=True)

    # Now we are ready
    if is_flush and is_broadway_straight:
        return "Royal Flush"
    if is_flush and is_straight:
        return "Straight Flush"
    if counts == [4, 1]:
        return "Four of a Kind"
    if counts == [3, 2]:
        return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if counts == [3, 1, 1]:
        return "Three of a Kind"
    if counts == [2, 2, 1]:
        return "Two Pair"
    if counts == [2, 1, 1, 1]:
        return "One Pair"
    return "High Card"
