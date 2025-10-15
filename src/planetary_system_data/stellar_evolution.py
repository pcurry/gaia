import math


def temperature_of_low_mass_star(mass: float, age: float) -> float:
    return 18600 * ((mass ** 0.8) / (age ** 0.3))


def evolve_star(mass: float, system_age: float, star_name: str) -> tuple[float, float, float, float]:
    mass_to_the_4th = mass ** 4
    mass_to_the_3rd = mass ** 3
    mass_to_the_2nd = mass ** 2

    def fourth_power_equation_in_mass(a: float, b: float, c: float, d: float, e: float) -> float:
        return a * mass_to_the_4th + b * mass_to_the_3rd + c * mass_to_the_2nd + d * mass + e
    
    Temperature_Effective_of_Star_A = None
    Luminosity_of_Star_A = None
    Main_Sequence_Lifespan_of_Star_A = None

    if mass < 0.08:
        Temperature_Effective_of_Star_A = temperature_of_low_mass_star(mass, system_age)
        Luminosity_of_Star_A = (Temperature_Effective_of_Star_A ** 4) / (1.1e+17)
        Main_Sequence_Lifespan_of_Star_A = (1 / (mass ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice brown dwarf lifespans are longer than the current age of the universe

    elif 0.08 <= mass <= 0.5:
        Temperature_Effective_of_Star_A = fourth_power_equation_in_mass(-78806, 125050, -74194, 20692, 1272.2)
        Luminosity_of_Star_A = fourth_power_equation_in_mass(2.1901, -2.2436, 0.919, -0.1023, 0.0039)
        Main_Sequence_Lifespan_of_Star_A = (1 / (mass ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice red dwarf lifespans are longer than the current age of the universe
        
    else:  # mass > 0.5
        Initial_Effective_Temperature_of_Star_A = None
        Final_Effective_Temperature_of_Star_A = None
        Initial_Luminosity_of_Star_A = None
        Luminosity_Growth_Rate_of_Star_A = None

        Initial_Effective_Temperature_of_Star_A = fourth_power_equation_in_mass(15.992, -198.64, 578.86, 3020.1, 2060)
        Final_Effective_Temperature_of_Star_A = fourth_power_equation_in_mass(15.893, 154.37, 384.94, 2105.7, 3631.6)
        Initial_Luminosity_of_Star_A = fourth_power_equation_in_mass(-0.2707, 10.15, 28.137, 31.268, 11.559)
        if mass <= 4:
            Luminosity_Growth_Rate_of_Star_A = 0.8295 * (mass ** 6) - 9.2448 * (mass ** 5) + fourth_power_equation_in_mass(40.931, -90.562, 104.59, -59.148, 13.745)
        else:  # mass > 4
            Luminosity_Growth_Rate_of_Star_A = (0.000005 ** (3.9985 * mass)) 
        
        Main_Sequence_Lifespan_of_Star_A = 11.452 * (mass ** -3.157)

        Temperature_Effective_of_Star_A = Initial_Effective_Temperature_of_Star_A + (system_age / Main_Sequence_Lifespan_of_Star_A) * (Final_Effective_Temperature_of_Star_A - Initial_Effective_Temperature_of_Star_A)

        if system_age <= (0.8 * Main_Sequence_Lifespan_of_Star_A):
            growth_rate_power = system_age
        else:  # system_age > (0.8 * Main_Sequence_Lifespan_of_Star_A)
            growth_rate_power = 3 * system_age - 1.6 * Main_Sequence_Lifespan_of_Star_A
            
        Luminosity_of_Star_A = Initial_Luminosity_of_Star_A * (Luminosity_Growth_Rate_of_Star_A ** growth_rate_power)
        
    Radius_of_Star_A = (
        155000 * ((math.sqrt(Luminosity_of_Star_A)) /(Temperature_Effective_of_Star_A * Temperature_Effective_of_Star_A)) 
        if 0.08 <= mass
        else 0.00047 
    )
    Temperature_Effective_of_Star_A = round(Temperature_Effective_of_Star_A, 1)
    Luminosity_of_Star_A = round(Luminosity_of_Star_A, 5)
    Radius_of_Star_A = round(Radius_of_Star_A, 5)
    print(f"Effective Temperature of {star_name} {Temperature_Effective_of_Star_A} Kelvin")
    print(f"Luminosity of {star_name}: {Luminosity_of_Star_A} solar luminosities")
    print(f"Radius of {star_name}: {Radius_of_Star_A} AU")
    return Temperature_Effective_of_Star_A, Luminosity_of_Star_A, Main_Sequence_Lifespan_of_Star_A, Main_Sequence_Lifespan_of_Star_A
