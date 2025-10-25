from dice import d100, _3d6


def generate_number_of_stars(primary_mass: float) -> int:
    """Determine the number of stars in the system based on the mass of the primary star and two rolls."""

    first_roll_for_number_of_stars = _3d6()
    if first_roll_for_number_of_stars < 9:
        return 1
    
    second_roll_for_number_of_stars = d100()
    multiple_stars = 2
    if 76 <= second_roll_for_number_of_stars <= 95:
        multiple_stars = 3
    elif 96 <= second_roll_for_number_of_stars <= 100:
        multiple_stars = 4

    if primary_mass < 0.08:
        return 1 if first_roll_for_number_of_stars <= 13 else multiple_stars
    elif primary_mass < 0.70:
        return 1 if first_roll_for_number_of_stars <= 12 else multiple_stars
    elif primary_mass < 1.00:
        return 1 if first_roll_for_number_of_stars <= 11 else multiple_stars
    elif primary_mass < 1.30:
        return 1 if first_roll_for_number_of_stars <= 10 else multiple_stars
    else: 
        return 1 if first_roll_for_number_of_stars <= 9 else multiple_stars
