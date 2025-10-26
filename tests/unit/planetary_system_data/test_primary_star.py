import unittest

import pytest

from unittest.mock import patch, MagicMock

from planetary_system_data.primary_star_mass import (
    generate_star_category,
    generate_primary_star_mass,
)
from planetary_system_data.dataclasses_and_enumerations import StarCategory, Star


@patch('planetary_system_data.primary_star_mass.d100')
class TestGeneratePrimaryStarMass(unittest.TestCase):

    def test_brown_dwarf_mass_ranges(self, mock_d100):
        category = StarCategory.BROWN_DWARF
        mass_ranges = [
            (1, 10, 0.015),
            (11, 29, 0.02),
            (30, 45, 0.03),
            (46, 60, 0.04),
            (61, 74, 0.05),
            (75, 87, 0.06),
            (88, 100, 0.07),
        ]
        for low, high, expected_mass in mass_ranges:
            for roll in range(low, high + 1):
                mock_d100.return_value = roll
                mass = generate_primary_star_mass(category)
                self.assertEqual(mass, expected_mass)

    def test_low_mass_star_ranges(self, mock_d100):
        category = StarCategory.LOW_MASS_STAR
        mass_ranges = [
            (1, 13, 0.08),
            (14, 23, 0.10),
            (24, 34, 0.12),
            (35, 43, 0.15),
            (44, 52, 0.18),
            (53, 59, 0.22),
            (60, 65, 0.26),
            (66, 70, 0.30),
            (71, 74, 0.34),
            (75, 77, 0.38),
            (78, 80, 0.42),
            (81, 83, 0.46),
            (84, 86, 0.50),
            (87, 89, 0.55),
            (90, 92, 0.60),
            (93, 95, 0.65),
            (96, 98, 0.70),
            (99, 100, 0.75),
        ]
        for low, high, expected_mass in mass_ranges:
            for roll in range(low, high + 1):
                mock_d100.return_value = roll
                mass = generate_primary_star_mass(category)
                self.assertEqual(mass, expected_mass)
        
        