import unittest

import pytest

from unittest.mock import patch, MagicMock

from planetary_system_data.stellar_multiplicity import (
    generate_number_of_stars,
)


@patch('planetary_system_data.stellar_multiplicity.d100')
@patch('planetary_system_data.stellar_multiplicity._3d6')    
class TestGenerateNumberOfStars(unittest.TestCase):

    def test_single_mass_irrelevant(self, mock_3d6, mock_d100):
        # First roll < 9 -> single star regardless of mass
        for primary_mass in [0.05, 0.5, 0.9, 1.2, 1.5]:
            mock_3d6.return_value = 8
            num_stars = generate_number_of_stars(primary_mass)
            self.assertEqual(num_stars, 1)

    def test_single_star_low_mass_primary(self, mock_3d6, mock_d100):
        # Primary mass < 0.08
        primary_mass = 0.05
        
        # First roll <= 13 -> single star
        mock_3d6.return_value = 10

        mock_d100.return_value = 20  
        num_stars = generate_number_of_stars(primary_mass)
        self.assertEqual(num_stars, 1)

        # First roll > 13 -> multiple stars
        mock_3d6.return_value = 15
        mock_d100.return_value = 80  # Should yield 3 stars
        num_stars = generate_number_of_stars(primary_mass)
        self.assertEqual(num_stars, 3)

    def test_multiple_star_scenarios(self, mock_3d6, mock_d100):
        test_cases = [
            (0.5, 12, 1),   # Primary mass < 0.70, first roll <= 12 -> single star
            (0.5, 13, 4),   # Primary mass < 0.70, first roll > 12 -> multiple stars (4 stars)
            (0.9, 11, 1),   # Primary mass < 1.00, first roll <= 11 -> single star
            (0.9, 12, 2),   # Primary mass < 1.00, first roll > 11 -> multiple stars (2 stars)
            (1.2, 10, 1),   # Primary mass < 1.30, first roll <= 10 -> single star
            (1.2, 11, 3),   # Primary mass < 1.30, first roll > 10 -> multiple stars (3 stars)
            (1.5, 9, 1),    # Primary mass >= 1.30, first roll <= 9 -> single star
            (1.5, 10, 4),   # Primary mass >= 1.30, first roll > 9 -> multiple stars (4 stars)
        ]