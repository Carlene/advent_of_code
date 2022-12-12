'''
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

What would your total score be if everything goes exactly according to your strategy guide?
'''

with open("2022/inputs/day_2.txt", "r") as f:
    rps_inputs = f.readlines()
    f.close()

def clean_rps_inputs(rps_inputs):
    '''
    Takes in a list of RPS moves and removes the newlines from each round. 
    Returns a cleaned list of RPS moves.
    '''
    cleaned_rps_inputs = []
    for round in rps_inputs:
        cleaned_rps_inputs.append(round.replace("\n", ""))
    return cleaned_rps_inputs

def find_which_play_won(opponent_encrypted_play_for_round, opponent_guide, your_encrypted_play_for_round, your_guide):
    '''
    Takes in plays made by you and your opponent. 
    Returns the play that won and the score each player gets for winning or losing.
    '''
    # default rules to keep track of
    winning_points = 6
    draw_points = 3
    losing_points = 0
    # score holders
    your_score = 0
    opponent_score = 0

    opponent_play_for_round = opponent_guide[opponent_encrypted_play_for_round]["play"]
    your_play_for_round = your_guide[your_encrypted_play_for_round]["play"]

    # deal with ties first
    if your_play_for_round == opponent_play_for_round:
        your_score = draw_points + your_guide[your_encrypted_play_for_round]["points"]
        opponent_score = draw_points + opponent_guide[opponent_encrypted_play_for_round]["points"]
    # rock beats scissors and loses to paper
    elif your_play_for_round == "rock":
        if opponent_play_for_round == "scissors":
            your_score = winning_points + your_guide[your_encrypted_play_for_round]["points"]
            opponent_score = losing_points + opponent_guide[opponent_encrypted_play_for_round]["points"]
        elif opponent_play_for_round == "paper":
            your_score = losing_points + your_guide[your_encrypted_play_for_round]["points"]
            opponent_score = winning_points + opponent_guide[opponent_encrypted_play_for_round]["points"]
    # scissors beats to paper and loses with rock
    elif your_play_for_round == "scissors":
        if opponent_play_for_round == "paper":
            your_score = winning_points + your_guide[your_encrypted_play_for_round]["points"]
            opponent_score = losing_points + opponent_guide[opponent_encrypted_play_for_round]["points"]
        elif opponent_play_for_round == "rock":
            your_score = losing_points + your_guide[your_encrypted_play_for_round]["points"]
            opponent_score = winning_points + opponent_guide[opponent_encrypted_play_for_round]["points"]
    # paper loses to scissors and beats rock
    elif your_play_for_round == "paper":
        if opponent_play_for_round == "rock":
            your_score = winning_points + your_guide[your_encrypted_play_for_round]["points"]
            opponent_score = losing_points + opponent_guide[opponent_encrypted_play_for_round]["points"]
        elif opponent_play_for_round == "scissors":
            your_score = losing_points + your_guide[your_encrypted_play_for_round]["points"]
            opponent_score = winning_points + opponent_guide[opponent_encrypted_play_for_round]["points"]

    return your_score, opponent_score


def strategy_guide(round):
    '''
    Takes in a single round of RPS and calculates the score for each player based on current rules.
    Returns the scores of both players for the round.
    '''
    opponent_guide = {
        "A": {"play": "rock", "points": 1}, 
        "B": {"play": "paper", "points": 2}, 
        "C": {"play": "scissors", "points": 3}
        }

    your_guide = {
        "X": {"play": "rock", "points": 1}, 
        "Y": {"play": "paper", "points": 2}, 
        "Z": {"play": "scissors", "points": 3}
        }

    # opponent input is the first position, your input is the third
    opponent_encrypted_play_for_round = round[0]
    your_encrypted_play_for_round = round[2]

    if your_encrypted_play_for_round in your_guide and opponent_encrypted_play_for_round in opponent_guide:
        your_score, opponent_score = find_which_play_won(
            opponent_encrypted_play_for_round, 
            opponent_guide, 
            your_encrypted_play_for_round, 
            your_guide
        )
    return your_score, opponent_score


def find_rps_scores(rps_inputs):
    '''
    Takes in a list of RPS moves, cleans the list, and finds scores for both players according to the strategy guide.
    Returns the total scores of both players.
    '''
    # first remove new lines from rps data
    cleaned_rps_inputs = clean_rps_inputs(rps_inputs)
    # total score holders
    your_total_score = 0
    opponent_total_score = 0 

    for round in cleaned_rps_inputs:
        your_score, opponent_score = strategy_guide(round)
        your_total_score += your_score
        opponent_total_score += opponent_score
    
    return {"your_score": your_total_score, "opponent_score": opponent_total_score}

print(find_rps_scores(rps_inputs))