'''
The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one food_item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
'''

with open("advent_of_code_2022/day_1/day_1.txt", "r") as f:
    lst_of_elves_inventories= f.readlines()

def separate_elves_inventories(lst_of_elves_inventories):
    '''
    Takes a list written by elves of their meals and separates that list out by food items per elf in the order it came in
    '''
    food_items_per_elf = {}
    elf_count = 1
    for food_item in lst_of_elves_inventories:
        if food_item == "\n": # new lines means this elf's inventory is finished!
            elf_count += 1
        else:
            try:
                food_item = int(food_item.replace("\n", "")) # turn calorie amounts per meal into integers
                if elf_count in food_items_per_elf: # add to dictionary if we haven't seen this elf yet
                    food_items_per_elf[elf_count].append(food_item)
                else: # otherwise add this elf's meals!
                    food_items_per_elf[elf_count] = [food_item]
            except ValueError: # in case we can't convert the food item's calories to an integer
                print(f"{food_item} calories for elf {elf_count} cannot be converted to an integer.")
    return food_items_per_elf

def count_calorie_totals_per_elf(lst_of_elves_inventories):
    '''
    Takes a list written by elves of their meals, and adds together the calories for each meal per elf
    Returns a dictionary of total calories per elf and the highest total amount of calories an elf has 
    '''
    food_items_per_elf = separate_elves_inventories(lst_of_elves_inventories)
    total_calories_per_elf = {}
    highest_calorie_count = 0
    second_highest_calorie_count = 0
    third_highest_calorie_count = 0

    for elf, food_items in food_items_per_elf.items():
        total_calories_per_elf[elf] = sum(food_items)
        # find out who has the most total calories
        if highest_calorie_count < total_calories_per_elf[elf]:
            third_highest_calorie_count = second_highest_calorie_count # 2nd will move to 3rd place
            second_highest_calorie_count = highest_calorie_count # 1st will move to 2nd place
            highest_calorie_count = total_calories_per_elf[elf] # and we have a new first!
        elif second_highest_calorie_count < total_calories_per_elf[elf]:
            third_highest_calorie_count = second_highest_calorie_count # 2nd will move to 3rd place
            second_highest_calorie_count = total_calories_per_elf[elf] # and we have a new second!
        elif third_highest_calorie_count < total_calories_per_elf[elf]:
            third_highest_calorie_count = total_calories_per_elf[elf] # and we have a new third!

    top_three_elves_calorie_count =  highest_calorie_count + second_highest_calorie_count + third_highest_calorie_count

    return total_calories_per_elf, top_three_elves_calorie_count   

total_calories_per_elf, top_three_elves_calorie_count = count_calorie_totals_per_elf(lst_of_elves_inventories)
print(top_three_elves_calorie_count)