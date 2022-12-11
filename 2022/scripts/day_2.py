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
    if round[0] in opponent_guide and round[2] in your_guide:
        opponent_play_for_round = opponent_guide[round[0]]["play"]
        your_play_for_round = your_guide[round[2]]["play"]
        # if opponent_play_for_round == "rock":

def find_which_play_won(opponent_play_for_round, your_play_for_round):
    '''
    Takes in plays made by you and your opponent. 
    Returns the play that won and the score each player gets for winning or losing.
    '''
    pass
    # score_per_player = {}

    # if your_play_for_round == "Rock":
    #     if opponent_play_for_round == "Scissors":
    #         return 

    # else:
    #     print(f"{round[0]} and/or {round[2]} input is not in the strategy guide, please check RPS inputs.")
    #     return False, 0




def find_rps_scores(rps_inputs):
    '''
    Takes in a list of RPS moves, cleans the list, and finds scores for both players according to the strategy guide.
    Returns the total scores of both players.
    '''
    # first remove new lines from rps data
    cleaned_rps_inputs = clean_rps_inputs(rps_inputs)

    for round in cleaned_rps_inputs:
        pass