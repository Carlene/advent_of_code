'''
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
'''

with open("2022/inputs/day_3.txt", "r") as f:
    rucksacks = f.read().splitlines() 
    f.close()

def find_item_priority(rucksack):
    '''
    With rucksacks, convert each item into it's priority level
    Returns rucksacks item priority, split by compartment
    '''
    rucksack_priority = []

    for item in rucksack:
        if item == item.lower():
            # dividing by 32 bits gives you the item's actual letter position
            item_priority = ord(item)%32
        else:
            # ordinal isn't case sensitive, so add 26 for capital letters
            item_priority = (ord(item)%32) + 26
        rucksack_priority.append(item_priority)

    return rucksack_priority

def split_rucksacks_into_compartments(rucksacks):
    '''
    Takes a list of a bunch of rucksacks and splits each one into two compartments
    Returns the split up rucksacks.
    '''

    rucksack_priority_by_compartment = {"first_compartment": {}, "second_compartment": {}}
    rucksack_count = 1

    for rucksack in rucksacks:
        inside_first_compartment = rucksack_priority_by_compartment["first_compartment"]
        inside_second_compartment = rucksack_priority_by_compartment["second_compartment"]
        # find the halfway mark in the rucksack to find the end of the first compartment
        end_of_first_compartment = int(len(rucksack)/2)
        # convert rucksack items into their item priority
        rucksack_priority = find_item_priority(rucksack)
        # put the first half of the rucksack in the first compartment
        inside_first_compartment[rucksack_count] = rucksack_priority[0:end_of_first_compartment]
        inside_first_compartment[rucksack_count] = set(inside_first_compartment[rucksack_count])
        # and the second half in the second compartment
        inside_second_compartment[rucksack_count] = rucksack_priority[end_of_first_compartment:]
        inside_second_compartment[rucksack_count] = set(inside_second_compartment[rucksack_count])
        rucksack_count += 1
    return rucksack_priority_by_compartment

def split_rucksacks_into_groups(rucksacks):
    '''
    Takes a list of a bunch of rucksacks and splits every three rucksacks into one group.
    Returns the split up rucksacks.
    '''
    rucksack_priorities_by_group = {}
    rucksack_count = 0
    group_number = 1

    for rucksack in rucksacks:
        rucksack_priority = find_item_priority(rucksack)
        # if we're on the third rucksack for the current group, move to the next group unless it's the zeroth or first rucksack
        if rucksack_count % 3 == 0 and rucksack_count != 0 and rucksack_count != 1:
            group_number += 1
        if group_number in rucksack_priorities_by_group:
            rucksack_priorities_by_group[group_number].append(set(rucksack_priority))
        else:
            rucksack_priorities_by_group[group_number] = []
            rucksack_priorities_by_group[group_number].append(set(rucksack_priority))
        rucksack_count += 1

    return rucksack_priorities_by_group


def find_duped_item_priority_across_compartments(rucksacks):
    '''
    Find the duplicate item in each rucksack across both compartments.
    Returns the summed up item priorities of all duplicate items.
    '''
    rucksack_priority_by_compartment = split_rucksacks_into_compartments(rucksacks)
    total_duped_priorities_across_compartments = 0

    for i in range(len(rucksack_priority_by_compartment["first_compartment"])):
        # find the duped item across both sets of compartments
        duped_priority_lst = list(rucksack_priority_by_compartment["first_compartment"][i + 1].intersection(rucksack_priority_by_compartment["second_compartment"][i + 1]))
        # there should only be one duped item, but checking in case
        if len(duped_priority_lst) == 1:
            duped_priority = duped_priority_lst[0]
        total_duped_priorities_across_compartments += duped_priority

    return total_duped_priorities_across_compartments


def find_duped_item_priority_across_groups(rucksacks):
    '''
    Find the duplicate item in each rucksack across groups.
    Returns the summed up item priorities of all duplicate items.
    '''
    rucksack_priorities_by_group = split_rucksacks_into_groups(rucksacks)
    total_duped_priorities_across_groups = 0

    for group_number, item_priorities in rucksack_priorities_by_group.items():
        if len(item_priorities) == 3:
            # check to see which item the three rucksacks have in common
            tripled_priority_list = list(item_priorities[0].intersection(item_priorities[1]).intersection(item_priorities[2]))
            # there should only be one duped item, but checking in case
            if len(tripled_priority_list) == 1:
                tripled_item_priority = tripled_priority_list[0]
                total_duped_priorities_across_groups += tripled_item_priority

    return total_duped_priorities_across_groups

# print(find_duped_item_priority_across_compartments(rucksacks))
print(find_duped_item_priority_across_groups(rucksacks))