def separate_starting_stacks_from_rearrangement_procedures():
    with open("2022/inputs/day_5.txt", "r") as f:
        file = f.read()
        f.close()

    # find the word "move" to find the first instruction, where the file should be separated
    index_separator = file.find("move") - len("move") + 2
    starting_stacks = file[:index_separator]
    rearrangement_procedures = file[index_separator:]

    # split up the instructions and drop the first two empty strings
    rearrangement_procedures = rearrangement_procedures.split("\n")[2:]
    
    # split up stacks
    starting_stacks = starting_stacks.split("\n")

    return starting_stacks, rearrangement_procedures


def clean_starting_stacks(starting_stacks, spaces = 3, given_amount_of_stacks = 9):
    '''
    every three spaces is a new crate
    first 3 is information, last space is a delimiter
    amount_of_stacks: how many stacks are in the original file
    '''

    stack_by_column = {} # holder for stacks by numbered column

    for row_of_crates in starting_stacks:
        stack_column = 1 # which stack we're currently going through
        starting_crate_placement = 0 # the beginning of the item in the row of stacks
        ending_crate_placement = spaces # the emd of the item in the row of stacks
        amount_of_stacks = given_amount_of_stacks

        # add each crate to it's proper stack in order
        while amount_of_stacks != 0:
            crate = row_of_crates[starting_crate_placement:ending_crate_placement]
            crate = crate.strip().strip("[").strip("]")

            # the crates that denote the stack number are the end of the row, so ignore 
            if crate.isdigit():
                pass
            # skip empty crates
            elif len(crate) == 0:
                pass
            else:
                if stack_column not in stack_by_column:
                    stack_by_column[stack_column] = [crate]
                else:
                    stack_by_column[stack_column].append(crate)
                # four characters separate each crate
                # first 3 is crate information, last character is a delimiter
            stack_column += 1
            amount_of_stacks -= 1
            starting_crate_placement = ending_crate_placement + 1
            ending_crate_placement += 4

    return stack_by_column


def break_up_procedure(procedure):
    '''
    go through one procedure from the rearrangement procedure and break it up into each action part (how many are moving, moving from where, moving to where)
    return the broken up procedure
    '''
    # "move" tells us how many crates are going to move
    move_keyword = "move"
    amount_of_crates_to_move_position = procedure.find(move_keyword) + len(move_keyword) + 1 # plus 1 to account for the extra space
    amount_of_crates_to_move = procedure[amount_of_crates_to_move_position]

    # might move a double digit amount of crates
    if procedure[amount_of_crates_to_move_position + 1].isdigit():
        amount_of_crates_to_move += procedure[amount_of_crates_to_move_position + 1]
    amount_of_crates_to_move = int(amount_of_crates_to_move)

    # "from" shows us where the amount of moved crates will come from
    from_keyword = "from"
    from_stack_column_position = int(procedure.find(from_keyword) + len(from_keyword) + 1) # plus 1 to account for the extra space
    from_stack_column = int(procedure[from_stack_column_position])

    # and "to" tells us where the moved crates are going, starting with the top of the stack
    to_keyword = "to"
    to_stack_column_position = int(procedure.find(to_keyword) + len(to_keyword) + 1) # plus 1 to account for the extra space
    to_stack_column = int(procedure[to_stack_column_position])

    return amount_of_crates_to_move, from_stack_column, to_stack_column


def follow_one_procedure(procedure, stacks, crane = 9000):
    ''' 
    apply the procedure to the current configuration of stacked crates
    return the configuration of crates after the procedure
    crane: int, the model of crane that's moving the crates. the 9001 can grab multiple crates at once, preserving order
    '''
    amount_of_crates_to_move, from_stack_column, to_stack_column = break_up_procedure(procedure)

    # find the stack of crates we need to move
    crates_to_move = stacks[from_stack_column][:amount_of_crates_to_move]
    if crane == 9000:
        # the CrateMover 9000 can only move one crate at a time, so need to reverse the order of the stack
        crates_to_move.reverse() 
    stacks[to_stack_column] = crates_to_move + stacks[to_stack_column]

    # remove the moved crates from the original stack
    for crate in crates_to_move:
        stacks[from_stack_column].remove(crate)

    return stacks


def go_through_rearrangement_procedure(crane = 9000):
    '''
    apply the entire rearrangement procedure instructions to the stacks of crates
    returns the new stacks, along with the crates at the top of each stack
    '''
    starting_stacks, rearrangement_procedures = separate_starting_stacks_from_rearrangement_procedures()
    stacks_by_column = clean_starting_stacks(starting_stacks)
    top_crates = []

    # go through each procedure
    for procedure in rearrangement_procedures:
        stacks_by_column = follow_one_procedure(procedure, stacks_by_column, crane)

    # and find the crate at the top of each stack
    for i in range(len(stacks_by_column)):
        crates = stacks_by_column[i + 1]
        if len(crates) > 0: # ignore empty stacks
            top_crates.append(crates[0])
    
    return stacks_by_column, top_crates

stacks_by_column, top_crates = go_through_rearrangement_procedure(crane = 9001)
print("".join(top_crates))