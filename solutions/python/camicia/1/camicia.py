def play_next_card(player, central_pile):
    next_card = player.pop(0)
    central_pile.append(next_card)

def check_payment_card(central_pile):
    if central_pile[-1] == 'J' or central_pile[-1] == 'Q' or central_pile[-1] == 'K' or central_pile[-1] == 'A':
        return True
    return False

def penalty(current_player, opponent, central_pile, no_of_cards, cards_played, no_of_tricks, finished, player_a, player_b, game_states, penalty_previously, turn, loop_detected):
    payment_cards = ['J', 'Q', 'K', 'A']
    current_payment_card = central_pile[-1]
    interrupted = False
    penalty_previously += 1

    for i in range(payment_cards.index(current_payment_card) + 1):
        if len(opponent) == 0: break
        next_card = opponent.pop(0)
        central_pile.append(next_card)
        cards_played += 1
        if check_payment_card(central_pile) == True:
            interrupted = True
            central_pile, no_of_cards, cards_played, no_of_tricks, finished, loop_detected, penalty_previously = (
                penalty(opponent, current_player, central_pile, no_of_cards, cards_played, no_of_tricks, finished, player_a, player_b, game_states, penalty_previously, turn, loop_detected)
            )
            break


    if interrupted == False:
        current_player.extend(central_pile)
        game_state = (['N' if c not in 'JQKA' else c for c in player_a],
                ['N' if c not in 'JQKA' else c for c in player_b],
                turn)
        if game_state in game_states:
            loop_detected = True
            finished = True
        game_states.append(game_state)
        no_of_tricks += 1
        central_pile.clear()
        
        if len(current_player) == no_of_cards:
            finished = True

    return central_pile, no_of_cards, cards_played, no_of_tricks, finished, loop_detected, penalty_previously

def simulate_game(player_a, player_b):
    central_pile = []
    no_of_cards = len(player_a) + len(player_b)
    cards_played = 0
    no_of_tricks = 0
    finished = False
    game_states = []
    penalty_previously = 0
    loop_detected = False

    game_state = (['N' if c not in 'JQKA' else c for c in player_a],
                ['N' if c not in 'JQKA' else c for c in player_b],
                0)
    game_states.append(game_state)

    # Safety limit — prevent infinite loop in case of bug
    MAX_ITERATIONS = 10000
    iteration = 0
    k = 0

    # for k in range(no_of_cards * 69):
    while not finished and not loop_detected and iteration < MAX_ITERATIONS:
        iteration += 1
        
        turn = (k + penalty_previously) % 2
        current_player = player_a if turn == 0 else player_b
        opponent = player_b if turn == 0 else player_a

        if len(current_player) != 0:
            play_next_card(current_player, central_pile)
            cards_played += 1
        else:
            opponent += central_pile
            no_of_tricks += 1

            if len(opponent) == no_of_cards:
                finished = True
                break
            continue

            
        if check_payment_card(central_pile) == True:
            central_pile, no_of_cards, cards_played, no_of_tricks, finished, loop_detected, penalty_previously = (
                penalty(current_player, opponent, central_pile, no_of_cards, cards_played, no_of_tricks, finished, player_a, player_b, game_states, penalty_previously, turn, loop_detected)
            )
            if finished == True:
                break

        k += 1
    
    if loop_detected == True:
        return {'status': 'loop', 'cards': cards_played, 'tricks': no_of_tricks}
    else:
        return {'status': 'finished', 'cards': cards_played, 'tricks': no_of_tricks}