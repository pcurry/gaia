
from dataclasses import dataclass
from enum import StrEnum


class StarCategory(StrEnum):
    BROWN_DWARF = "Brown Dwarf"
    LOW_MASS_STAR = "Low Mass Star"
    INTERMEDIATE_MASS_STAR = "Intermediate Mass Star"
    HIGH_MASS_STAR = "High Mass Star"


class StellarArrangement(StrEnum):
    SINGLE = "A"
    BINARY = "AB"
    TRINARY_DISTANT_PAIR = "A-BC"
    TRINARY_CLOSE_PAIR = "AB-C"
    QUATERNARY = "AB-CD"


class StellarEvolutionStage(StrEnum):
    MAIN_SEQUENCE = "Main Sequence"
    SUBGIANT = "Subgiant"
    RED_GIANT_BRANCH = "Red Giant Branch"
    HORIZONTAL_BRANCH = "Horizontal Branch"
    WHITE_DWARF = "White Dwarf"


class StellarPopulation(StrEnum):
    YOUNG_POPULATION_I = "Young Population I"
    INTERMEDIATE_POPULATION = "Intermediate Population"
    OLD_POPULATION_I = "Old Population I"
    DISK_POPULATION_II = "Disk Population II"
    HALO_POPULATION_II = "Halo Population II"


@dataclass
class Star:
    mass: float  # in solar masses
    category: StarCategory
    name: str
    effective_temperature: float | None = None # in Kelvin
    initial_effective_temperature: float | None = None # in Kelvin
    final_effective_temperature: float | None = None # in Kelvin
    initial_luminosity: float | None = None # in solar luminosities
    final_luminosity: float | None = None # in solar luminosities
    luminosity_growth_rate: float | None = None
    luminosity: float | None = None # in solar luminosities
    radius: float | None = None # in AU
    main_sequence_lifespan: float | None = None  # in billion years
    evolutionary_stage: StellarEvolutionStage | None = None
    age: float | None = None  # in billion years
    

@dataclass
class StarSystem:
    stars: list[Star]
    stellar_arrangement: StellarArrangement  # e.g., 'Primary', 'Secondary', 'Tertiary', etc.
    system_age: float | None = None # in billion years
    metallicity: float | None = None  # [Fe/H]
    population: StellarPopulation | None = None
    habitable_zone_inner: float | None = None  # in AU
    habitable_zone_outer: float | None = None  # in AU
    has_habitable_zone: bool | None = None
    