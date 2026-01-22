def best_hands(hands):
    royal_cards = ['10','J','Q','K','A']
    cards_ranking = ['2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A']
    straight_cards_A1 = ['2','3','4','5','A']
    hands_ranking = {
        'High Card': 1,
        'Pair': 2,
        'Two Pair': 3,
        'Three of a Kind': 4,
        'Straight': 5,
        'Flush': 6,
        'Full House': 7,
        'Four of a Kind': 8,
        'Straight Flush': 9,
        'Royal Flush': 10
    }

    # returns variable length tuple: (type of hand, type of hand's value, next highest value, next highest value etc) 
    def categorise(hand):
        ranks = sorted([k[:-1] for k in hand.split(' ')], key=cards_ranking.index)
        suits = [k[-1] for k in hand.split(' ')]

        if set(ranks).issubset(royal_cards) is True and suits.count(suits[0]) == 5:
            return ('Royal Flush',)
        if any([''.join(ranks) in ''.join(cards_ranking),''.join(ranks) in ''.join(straight_cards_A1)]) and suits.count(suits[0]) == 5:
            if ''.join(ranks) in ''.join(straight_cards_A1): return ('Straight Flush', ranks[-2])
            return ('Straight Flush', ranks[-1])
        if any([k for k in ranks if ranks.count(k) >= 4]):
            return ('Four of a Kind', next((x for x in ranks if ranks.count(x) >= 4), None), next((x for x in ranks if ranks.count(x) == 1), None))
        if any([k for k in ranks if ranks.count(k) == 3]) and any([k for k in ranks if ranks.count(k) == 2]):
            return ('Full House', next((k for k in ranks if ranks.count(k) == 3), None), next((k for k in ranks if ranks.count(k) == 2)))
        if suits.count(suits[0]) == 5:
            return ('Flush', ranks[-1], ranks[-2], ranks[-3], ranks[-4], ranks[-5])
        if ''.join(ranks) in ''.join(cards_ranking):
            return ('Straight', ranks[-1])
        if ''.join(ranks) in ''.join(straight_cards_A1):
            return ('Straight', '5')
        if any([k for k in ranks if ranks.count(k) == 3]):
            remaining = [x for x in ranks if ranks.count(x) != 3]
            return ('Three of a Kind', next((x for x in ranks if ranks.count(x) == 3), None), remaining[-1], remaining[-2])
        if len([k for k in ranks if ranks.count(k) == 2]) == 4:
            pairs = [x for x in ranks if ranks.count(x) == 2]
            remaining = next((k for k in ranks if ranks.count(k) == 1))
            return ('Two Pair', pairs[2], pairs[0], remaining)
        if any([k for k in ranks if ranks.count(k) == 2]):
            remaining = [x for x in ranks if ranks.count(x) != 2]
            return ('Pair', next((x for x in ranks if ranks.count(x) == 2), None), remaining[-1], remaining[-2], remaining [-3])
        remaining = [x for x in ranks if x != max(ranks)]
        return ('High Card', max(ranks), remaining[-1], remaining[-2], remaining[-3], remaining[-4])

    highest_hand = categorise(hands[0])
    tie = False

    if len(hands) == 1: return hands
    output = hands[0]
    print('output = ',output)
        
    for hand in hands[1:]:
        current_hand = categorise(hand)
        print('current_hand = ',current_hand)
        print('highest_hand = ',highest_hand)
        print('hands_ranking[current_hand[0]] = ',hands_ranking[current_hand[0]])
        print('hands_ranking[highest_hand[0] = ',hands_ranking[highest_hand[0]])
        if hands_ranking[current_hand[0]] > hands_ranking[highest_hand[0]]:
            highest_hand = current_hand
            output = hand
        elif hands_ranking[current_hand[0]] == hands_ranking[highest_hand[0]]:
            if cards_ranking.index(current_hand[1]) > cards_ranking.index(highest_hand[1]):
                highest_hand = current_hand
                output = hand
            elif cards_ranking.index(current_hand[1]) == cards_ranking.index(highest_hand[1]):
                if cards_ranking.index(current_hand[2]) > cards_ranking.index(highest_hand[2]):
                    highest_hand = current_hand
                    output = hand
                elif cards_ranking.index(current_hand[2]) == cards_ranking.index(highest_hand[2]):
                    if cards_ranking.index(current_hand[3]) > cards_ranking.index(highest_hand[3]):
                        highest_hand = current_hand
                        output = hand
                    elif cards_ranking.index(current_hand[3]) == cards_ranking.index(highest_hand[3]):
                        if cards_ranking.index(current_hand[4]) > cards_ranking.index(highest_hand[4]):
                            highest_hand = current_hand
                            output = hand
                        elif cards_ranking.index(current_hand[4]) == cards_ranking.index(highest_hand[4]):
                            if cards_ranking.index(current_hand[5]) > cards_ranking.index(highest_hand[5]):
                                highest_hand = current_hand
                                output = hand
                            elif cards_ranking.index(current_hand[5]) == cards_ranking.index(highest_hand[5]):
                                tie = True
                                output_multiple_hands = [output, hand]

    if tie == True: return output_multiple_hands
    return [output]
