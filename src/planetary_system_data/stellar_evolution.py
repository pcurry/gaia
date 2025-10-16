import math

from planetary_system_data.dataclasses_and_enumerations import Star


def temperature_of_low_mass_star(mass: float, age: float) -> float:
    return 18600 * ((mass ** 0.8) / (age ** 0.3))


def steller_conditions(star: Star, system_age: float) -> Star:
    
    mass_to_the_4th = star.mass ** 4
    mass_to_the_3rd = star.mass ** 3
    mass_to_the_2nd = star.mass ** 2

    def fourth_power_equation_in_mass(a: float, b: float, c: float, d: float, e: float) -> float:
        return a * mass_to_the_4th + b * mass_to_the_3rd + c * mass_to_the_2nd + d * mass + e
    
    if star.mass < 0.08:
        star.effective_temperature = temperature_of_low_mass_star(star.mass, system_age)
        star.luminosity = (star.effective_temperature ** 4) / (1.1e+17)
        star.main_sequence_lifespan = (1 / (star.mass ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice brown dwarf lifespans are longer than the current age of the universe

    elif 0.08 <= star.mass <= 0.5:
        star.effective_temperature = fourth_power_equation_in_mass(-78806, 125050, -74194, 20692, 1272.2)
        star.luminosity = fourth_power_equation_in_mass(2.1901, -2.2436, 0.919, -0.1023, 0.0039)
        star.main_sequence_lifespan = (1 / (star.mass ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice red dwarf lifespans are longer than the current age of the universe
        
    else:  # mass > 0.5
        star.initial_effective_temperature = fourth_power_equation_in_mass(15.992, -198.64, 578.86, 3020.1, 2060)
        star.final_effective_temperature = fourth_power_equation_in_mass(15.893, 154.37, 384.94, 2105.7, 3631.6)
        star.initial_luminosity = fourth_power_equation_in_mass(-0.2707, 10.15, 28.137, 31.268, 11.559)
        if star.mass <= 4:
            star.luminosity_growth_rate = (
                0.8295 * (star.mass ** 6) - 9.2448 * (star.mass ** 5) + 
                fourth_power_equation_in_mass(40.931, -90.562, 104.59, -59.148, 13.745)
            )
        else:  # mass > 4
            star.luminosity_growth_rate = (0.000005 ** (3.9985 * star.mass)) 
        
        star.main_sequence_lifespan = 11.452 * (star.mass ** -3.157)
        star.effective_temperature = (
            star.initial_effective_temperature + 
            (system_age / star.main_sequence_lifespan) * 
            (star.final_effective_temperature - star.initial_effective_temperature)
        )

        if system_age <= (0.8 * star.main_sequence_lifespan):
            growth_rate_power = system_age
        else:  # system_age > (0.8 * Main_Sequence_Lifespan_of_Star_A)
            growth_rate_power = (
                3 * system_age - 1.6 * star.main_sequence_lifespan
            )
        star.luminosity = star.initial_luminosity * (star.luminosity_growth_rate ** growth_rate_power)
        
    star.radius = (
        155000 * ((math.sqrt(star.luminosity)) / (star.effective_temperature ** 2))
        if 0.08 <= star.mass
        else 0.00047 
    )
    star.effective_temperature = round(star.effective_temperature, 1)
    star.luminosity = round(star.luminosity, 5)
    star.radius = round(star.radius, 5)
    print(f"Effective Temperature of {star.name} {star.effective_temperature} Kelvin")
    print(f"Luminosity of {star.name}: {star.luminosity} solar luminosities")
    print(f"Radius of {star.name}: {star.radius} AU")
    return star


