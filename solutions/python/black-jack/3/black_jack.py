"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ('J','Q','K'): return 10

    if card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        higher_card_local = card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        higher_card_local = card_two
    elif value_of_card(card_one) == value_of_card(card_two):
        higher_card_local = (card_one,card_two)

    return higher_card_local



def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one == 'A': card_one = 11
    if card_two == 'A': card_two = 11

    subtotal = value_of_card(card_one) + value_of_card(card_two)

    if subtotal < 11:
        ace_value = 11
    else:
        ace_value = 1

    return ace_value



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    blackjack = False

    if card_one == 'A':
        if card_two == 'J' or card_two == 'Q' or card_two == 'K' or value_of_card(card_two) == 10:
            blackjack = True

    if card_two == 'A':
        if card_one == 'J' or card_one == 'Q' or card_one == 'K' or value_of_card(card_one) == 10:
            blackjack = True

    return blackjack



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if card_one == card_two:
        return True

    def is_royal(card):
        if card in ('J','Q','K'): return True

    return bool(is_royal(card_one) is True and is_royal(card_two) is True)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    sumtotal = value_of_card(card_one) + value_of_card(card_two)
    return bool(sumtotal in (9, 10, 11))
