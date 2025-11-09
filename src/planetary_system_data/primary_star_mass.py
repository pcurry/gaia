
from planetary_system_data.dice import d100
from planetary_system_data.dataclasses_and_enumerations import StarCategory, Star


def generate_star_category() -> StarCategory:
    roll_for_star_type = d100()
    if 1 <= roll_for_star_type <= 3: 
        return StarCategory.BROWN_DWARF
    elif 4 <= roll_for_star_type <= 77:
        return StarCategory.LOW_MASS_STAR
    elif 78 <= roll_for_star_type <=90:
        return StarCategory.INTERMEDIATE_MASS_STAR
    else:  # 91-100
        return StarCategory.HIGH_MASS_STAR


def generate_primary_star_mass(category: StarCategory) -> float:
    """Generate the mass of the primary star based on its category.
    Returns the mass in solar masses."""
    roll_for_mass = d100()
    match category:
        case StarCategory.BROWN_DWARF:
            if roll_for_mass <= 10: 
                return 0.015
            elif roll_for_mass <= 29:
                return 0.02
            elif roll_for_mass <= 45:
                return 0.03
            elif roll_for_mass <= 60:
                return 0.04
            elif roll_for_mass <= 74:
                return 0.05
            elif roll_for_mass <= 87:
                return 0.06
            else:  # 88-100
                return 0.07
        case StarCategory.LOW_MASS_STAR:            
            if roll_for_mass <= 13:
                return 0.08
            elif roll_for_mass <= 23:
                return 0.10
            elif roll_for_mass <= 34:
                return 0.12
            elif roll_for_mass <= 43:
                return 0.15
            elif roll_for_mass <= 52:
                return 0.18
            elif roll_for_mass <= 59:
                return 0.22
            elif roll_for_mass <= 65:
                return 0.26
            elif roll_for_mass <= 70:
                return 0.30
            elif roll_for_mass <= 74:
                return 0.34
            elif roll_for_mass <= 77:
                return 0.38
            elif roll_for_mass <= 80:
                return 0.42
            elif roll_for_mass <= 83:
                return 0.46
            elif roll_for_mass <= 86:
                return 0.50
            elif roll_for_mass <= 89:
                return 0.53
            elif roll_for_mass <= 92:
                return 0.56
            elif roll_for_mass <= 95:
                return 0.59
            elif roll_for_mass <= 97:
                return 0.62
            elif roll_for_mass <= 99:
                return 0.65
            else:  # 100
                return 0.68
        case StarCategory.INTERMEDIATE_MASS_STAR:
            if roll_for_mass <= 7:
                return 0.70
            elif roll_for_mass <= 13:
                return 0.72
            elif roll_for_mass <= 19:
                return 0.74
            elif roll_for_mass <= 24:
                return 0.76
            elif roll_for_mass <= 29:
                return 0.78
            elif roll_for_mass <= 34:
                return 0.80
            elif roll_for_mass <= 39:
                return 0.82
            elif roll_for_mass <= 43:
                return 0.84
            elif roll_for_mass <= 47:
                return 0.86
            elif roll_for_mass <= 51:
                return 0.88
            elif roll_for_mass <= 55:
                return 0.90
            elif roll_for_mass <= 59:
                return 0.92
            elif roll_for_mass <= 62:
                return 0.94
            elif roll_for_mass <= 65:
                return 0.96
            elif roll_for_mass <= 68:
                return 0.98
            elif roll_for_mass <= 71:
                return 1.00
            elif roll_for_mass <= 74:
                return 1.02
            elif roll_for_mass <= 78:
                return 1.04
            elif roll_for_mass <= 82:
                return 1.07
            elif roll_for_mass <= 85:
                return 1.10
            elif roll_for_mass <= 89:
                return 1.13
            elif roll_for_mass <= 92:
                return 1.16
            elif roll_for_mass <= 95:
                return 1.19
            elif roll_for_mass <= 97:
                return 1.22
            else:  # 98-100
                return 1.25
        case StarCategory.HIGH_MASS_STAR:
            if roll_for_mass <= 3:
                return 1.28
            elif roll_for_mass <= 6:
                return 1.31
            elif roll_for_mass <= 9:
                return 1.34
            elif roll_for_mass <= 12:
                return 1.37
            elif roll_for_mass <= 16:
                return 1.40
            elif roll_for_mass <= 19:
                return 1.44
            elif roll_for_mass <= 23:
                return 1.48
            elif roll_for_mass <= 27:
                return 1.53
            elif roll_for_mass <= 31:
                return 1.58
            elif roll_for_mass <= 35:
                return 1.64
            elif roll_for_mass <= 38:
                return 1.70
            elif roll_for_mass <= 41:
                return 1.76
            elif roll_for_mass <= 45:
                return 1.82
            elif roll_for_mass <= 49:
                return 1.90
            elif roll_for_mass <= 53:
                return 2.00
            elif roll_for_mass <= 56:
                return 2.10
            elif roll_for_mass <= 59:
                return 2.20
            elif roll_for_mass <= 62:
                return 2.30
            elif roll_for_mass <= 67:
                return 2.40
            elif roll_for_mass <= 71:
                return 2.60
            elif roll_for_mass <= 75:
                return 2.80
            elif roll_for_mass <= 78:
                return 3.00
            elif roll_for_mass <= 82:
                return 3.20
            elif roll_for_mass <= 87:
                return 3.50
            elif roll_for_mass <= 91:
                return 4.00
            elif roll_for_mass <= 94:
                return 4.50
            elif roll_for_mass <= 96:
                return 5.00
            elif roll_for_mass <= 98:
                return 5.50
            else:   # 99-100
                return 6.00


def generate_primary_star() -> Star:
    category = generate_star_category()
    mass = generate_primary_star_mass(category)
    return Star(mass=mass, category=category, name="Star A")

