# this sub-program covers step 2 ("Stellar Multiplcity") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

Number_of_Stars = 0
first_roll_for_number_of_stars = _3d6()
second_roll_for_number_of_stars = d100()

if Mass_A < 0.08:
    if 1 <= first_roll_for_number_of_stars <= 13:
        Number_of_Stars = 1
    elif 14 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4
elif 0.08 <= Mass_A < 0.70:
    if 1 <= first_roll_for_number_of_stars <= 12:
        Number_of_Stars = 1
    elif 13 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4
elif 0.7 <= Mass_A < 1.00:
    if 1 <= first_roll_for_number_of_stars <= 11:
        Number_of_Stars = 1
    elif 12 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4
elif 1.00 <= Mass_A < 1.30:
    if 1 <= first_roll_for_number_of_stars <= 10:
        Number_of_Stars = 1
    elif 11 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4
elif 1.30 <= Mass_A: 
    if 1 <= first_roll_for_number_of_stars <= 9:
        Number_of_Stars = 1
    elif 10 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4

print(f"Number of Stars in System: {Number_of_Stars}")
