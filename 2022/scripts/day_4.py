with open("2022/inputs/day_4.txt", "r") as f:
    section_assignment_pairs = f.read().splitlines() 
    f.close()

def clean_section_assignment(section_assignment):
    '''
    Takes a section assignment, and splits up the start and ending parts of the section
    '''
    starting_section = int(section_assignment[:section_assignment.find('-')])
    ending_section = int(section_assignment[section_assignment.find('-') + 1:])
    return starting_section, ending_section


def find_overlapping_assignments(section_assignment_pairs):
    '''
    Takes a list of section assignment pairs, and finds if one pair's section completely overlaps the other
    Returns the count of completely overlapped pairs.
    '''
    overlapped_assignments = 0

    for assignment_pair in section_assignment_pairs:
        # split up assignment pairs to easily find the start and end of each pair
        split_assignment_pairs = assignment_pair.split(',')
        first_pair = split_assignment_pairs[0]
        second_pair = split_assignment_pairs[1]
        starting_section_first_pair, ending_section_first_pair = clean_section_assignment(first_pair)
        starting_section_second_pair, ending_section_second_pair = clean_section_assignment(second_pair)

        # if overlapped, the start of one pair will be <= the start of the other pair
        # and the end of one pair will be >= the end of the other pair
        if starting_section_first_pair <= starting_section_second_pair and ending_section_first_pair >= ending_section_second_pair:
            overlapped_assignments += 1
        elif starting_section_second_pair <= starting_section_first_pair and ending_section_second_pair >= ending_section_first_pair:
            overlapped_assignments += 1

    return overlapped_assignments
        
print(find_overlapping_assignments(section_assignment_pairs))