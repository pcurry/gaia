# this sub-program covers step 9 ("Protoplanetary Disk") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

    # calculate disk density
    if Number_of_Stars >= 1:
        # calculate disk density of Star A
        roll_for_Disk_Density_of_Star_A = _3d6()
        if roll_for_Disk_Density_of_Star_A == 3:
            Disk_Mass_Factor_Star_A = 0.25
            Disk_Mass_Modifier_Star_A = -6
        if roll_for_Disk_Density_of_Star_A == 4:
            Disk_Mass_Factor_Star_A = 0.32
            Disk_Mass_Modifier_Star_A = -5
        if roll_for_Disk_Density_of_Star_A == 5:
            Disk_Mass_Factor_Star_A = 0.4
            Disk_Mass_Modifier_Star_A = -4
        if roll_for_Disk_Density_of_Star_A == 6:
            Disk_Mass_Factor_Star_A = 0.5
            Disk_Mass_Modifier_Star_A = -3
        if roll_for_Disk_Density_of_Star_A == 7:
            Disk_Mass_Factor_Star_A = 0.6
            Disk_Mass_Modifier_Star_A = -2
        if roll_for_Disk_Density_of_Star_A == 8:
            Disk_Mass_Factor_Star_A = 0.7
            Disk_Mass_Modifier_Star_A = -1
        if roll_for_Disk_Density_of_Star_A == 9:
            Disk_Mass_Factor_Star_A = 0.8
            Disk_Mass_Modifier_Star_A = 0
        if roll_for_Disk_Density_of_Star_A == 10:
            Disk_Mass_Factor_Star_A = 1.0
            Disk_Mass_Modifier_Star_A = 0
        if roll_for_Disk_Density_of_Star_A == 11:
            Disk_Mass_Factor_Star_A = 1.0
            Disk_Mass_Modifier_Star_A = 0
        if roll_for_Disk_Density_of_Star_A == 12:
            Disk_Mass_Factor_Star_A = 1.2
            Disk_Mass_Modifier_Star_A = 0
        if roll_for_Disk_Density_of_Star_A == 13:
            Disk_Mass_Factor_Star_A = 1.4
            Disk_Mass_Modifier_Star_A = 1
        if roll_for_Disk_Density_of_Star_A == 14:
            Disk_Mass_Factor_Star_A = 1.7
            Disk_Mass_Modifier_Star_A = 2
        if roll_for_Disk_Density_of_Star_A == 15:
            Disk_Mass_Factor_Star_A = 2.0
            Disk_Mass_Modifier_Star_A = 3
        if roll_for_Disk_Density_of_Star_A == 16:
            Disk_Mass_Factor_Star_A = 2.5
            Disk_Mass_Modifier_Star_A = 4
        if roll_for_Disk_Density_of_Star_A == 17:
            Disk_Mass_Factor_Star_A = 3.2
            Disk_Mass_Modifier_Star_A = 5
        if roll_for_Disk_Density_of_Star_A == 18:
            Disk_Mass_Factor_Star_A = 4.0
            Disk_Mass_Modifier_Star_A = 6
        print(f"Disk Mass Factor for Star A: {Disk_Mass_Factor_Star_A}")
        print(f"Disk Mass Modifier for Star A: {Disk_Mass_Modifier_Star_A}")

    if Number_of_Stars >= 2:
        # calculate disk density of Star B
        roll_for_Disk_Density_of_Star_B = _3d6()
        if roll_for_Disk_Density_of_Star_B == 3:
            Disk_Mass_Factor_Star_B = 0.25
            Disk_Mass_Modifier_Star_B = -6
        if roll_for_Disk_Density_of_Star_B == 4:
            Disk_Mass_Factor_Star_B = 0.32
            Disk_Mass_Modifier_Star_B = -5
        if roll_for_Disk_Density_of_Star_B == 5:
            Disk_Mass_Factor_Star_B = 0.4
            Disk_Mass_Modifier_Star_B = -4
        if roll_for_Disk_Density_of_Star_B == 6:
            Disk_Mass_Factor_Star_B = 0.5
            Disk_Mass_Modifier_Star_B = -3
        if roll_for_Disk_Density_of_Star_B == 7:
            Disk_Mass_Factor_Star_B = 0.6
            Disk_Mass_Modifier_Star_B = -2
        if roll_for_Disk_Density_of_Star_B == 8:
            Disk_Mass_Factor_Star_B = 0.7
            Disk_Mass_Modifier_Star_B = -1
        if roll_for_Disk_Density_of_Star_B == 9:
            Disk_Mass_Factor_Star_B = 0.8
            Disk_Mass_Modifier_Star_B = 0
        if roll_for_Disk_Density_of_Star_B == 10:
            Disk_Mass_Factor_Star_B = 1.0
            Disk_Mass_Modifier_Star_B = 0
        if roll_for_Disk_Density_of_Star_B == 11:
            Disk_Mass_Factor_Star_B = 1.0
            Disk_Mass_Modifier_Star_B = 0
        if roll_for_Disk_Density_of_Star_B == 12:
            Disk_Mass_Factor_Star_B = 1.2
            Disk_Mass_Modifier_Star_B = 0
        if roll_for_Disk_Density_of_Star_B == 13:
            Disk_Mass_Factor_Star_B = 1.4
            Disk_Mass_Modifier_Star_B = 1
        if roll_for_Disk_Density_of_Star_B == 14:
            Disk_Mass_Factor_Star_B = 1.7
            Disk_Mass_Modifier_Star_B = 2
        if roll_for_Disk_Density_of_Star_B == 15:
            Disk_Mass_Factor_Star_B = 2.0
            Disk_Mass_Modifier_Star_B = 3
        if roll_for_Disk_Density_of_Star_B == 16:
            Disk_Mass_Factor_Star_B = 2.5
            Disk_Mass_Modifier_Star_B = 4
        if roll_for_Disk_Density_of_Star_B == 17:
            Disk_Mass_Factor_Star_B = 3.2
            Disk_Mass_Modifier_Star_B = 5
        if roll_for_Disk_Density_of_Star_B == 18:
            Disk_Mass_Factor_Star_B = 4.0
            Disk_Mass_Modifier_Star_B = 6
        print(f"Disk Mass Factor for Star B: {Disk_Mass_Factor_Star_B}")
        print(f"Disk Mass Modifier for Star B: {Disk_Mass_Modifier_Star_B}")

    if Number_of_Stars >= 3:
        # calculate disk density of Star C
        roll_for_Disk_Density_of_Star_C = _3d6()
        if roll_for_Disk_Density_of_Star_C == 3:
            Disk_Mass_Factor_Star_C = 0.25
            Disk_Mass_Modifier_Star_C = -6
        if roll_for_Disk_Density_of_Star_C == 4:
            Disk_Mass_Factor_Star_C = 0.32
            Disk_Mass_Modifier_Star_C = -5
        if roll_for_Disk_Density_of_Star_C == 5:
            Disk_Mass_Factor_Star_C = 0.4
            Disk_Mass_Modifier_Star_C = -4
        if roll_for_Disk_Density_of_Star_C == 6:
            Disk_Mass_Factor_Star_C = 0.5
            Disk_Mass_Modifier_Star_C = -3
        if roll_for_Disk_Density_of_Star_C == 7:
            Disk_Mass_Factor_Star_C = 0.6
            Disk_Mass_Modifier_Star_C = -2
        if roll_for_Disk_Density_of_Star_C == 8:
            Disk_Mass_Factor_Star_C = 0.7
            Disk_Mass_Modifier_Star_C = -1
        if roll_for_Disk_Density_of_Star_C == 9:
            Disk_Mass_Factor_Star_C = 0.8
            Disk_Mass_Modifier_Star_C = 0
        if roll_for_Disk_Density_of_Star_C == 10:
            Disk_Mass_Factor_Star_C = 1.0
            Disk_Mass_Modifier_Star_C = 0
        if roll_for_Disk_Density_of_Star_C == 11:
            Disk_Mass_Factor_Star_C = 1.0
            Disk_Mass_Modifier_Star_C = 0
        if roll_for_Disk_Density_of_Star_C == 12:
            Disk_Mass_Factor_Star_C = 1.2
            Disk_Mass_Modifier_Star_C = 0
        if roll_for_Disk_Density_of_Star_C == 13:
            Disk_Mass_Factor_Star_C = 1.4
            Disk_Mass_Modifier_Star_C = 1
        if roll_for_Disk_Density_of_Star_C == 14:
            Disk_Mass_Factor_Star_C = 1.7
            Disk_Mass_Modifier_Star_C = 2
        if roll_for_Disk_Density_of_Star_C == 15:
            Disk_Mass_Factor_Star_C = 2.0
            Disk_Mass_Modifier_Star_C = 3
        if roll_for_Disk_Density_of_Star_C == 16:
            Disk_Mass_Factor_Star_C = 2.5
            Disk_Mass_Modifier_Star_C = 4
        if roll_for_Disk_Density_of_Star_C == 17:
            Disk_Mass_Factor_Star_C = 3.2
            Disk_Mass_Modifier_Star_C = 5
        if roll_for_Disk_Density_of_Star_C == 18:
            Disk_Mass_Factor_Star_C = 4.0
            Disk_Mass_Modifier_Star_C = 6
        print(f"Disk Mass Factor for Star C: {Disk_Mass_Factor_Star_C}")
        print(f"Disk Mass Modifier for Star C: {Disk_Mass_Modifier_Star_C}")

    if Number_of_Stars == 4:
        roll_for_Disk_Density_of_Star_D = _3d6()
        if roll_for_Disk_Density_of_Star_D == 3:
            Disk_Mass_Factor_Star_D = 0.25
            Disk_Mass_Modifier_Star_D = -6
        if roll_for_Disk_Density_of_Star_D == 4:
            Disk_Mass_Factor_Star_D = 0.32
            Disk_Mass_Modifier_Star_D = -5
        if roll_for_Disk_Density_of_Star_D == 5:
            Disk_Mass_Factor_Star_D = 0.4
            Disk_Mass_Modifier_Star_D = -4
        if roll_for_Disk_Density_of_Star_D == 6:
            Disk_Mass_Factor_Star_D = 0.5
            Disk_Mass_Modifier_Star_D = -3
        if roll_for_Disk_Density_of_Star_D == 7:
            Disk_Mass_Factor_Star_D = 0.6
            Disk_Mass_Modifier_Star_D = -2
        if roll_for_Disk_Density_of_Star_D == 8:
            Disk_Mass_Factor_Star_D = 0.7
            Disk_Mass_Modifier_Star_D = -1
        if roll_for_Disk_Density_of_Star_D == 9:
            Disk_Mass_Factor_Star_D = 0.8
            Disk_Mass_Modifier_Star_D = 0
        if roll_for_Disk_Density_of_Star_D == 10:
            Disk_Mass_Factor_Star_D = 1.0
            Disk_Mass_Modifier_Star_D = 0
        if roll_for_Disk_Density_of_Star_D == 11:
            Disk_Mass_Factor_Star_D = 1.0
            Disk_Mass_Modifier_Star_D = 0
        if roll_for_Disk_Density_of_Star_D == 12:
            Disk_Mass_Factor_Star_D = 1.2
            Disk_Mass_Modifier_Star_D = 0
        if roll_for_Disk_Density_of_Star_D == 13:
            Disk_Mass_Factor_Star_D = 1.4
            Disk_Mass_Modifier_Star_D = 1
        if roll_for_Disk_Density_of_Star_D == 14:
            Disk_Mass_Factor_Star_D = 1.7
            Disk_Mass_Modifier_Star_D = 2
        if roll_for_Disk_Density_of_Star_D == 15:
            Disk_Mass_Factor_Star_D = 2.0
            Disk_Mass_Modifier_Star_D = 3
        if roll_for_Disk_Density_of_Star_D == 16:
            Disk_Mass_Factor_Star_D = 2.5
            Disk_Mass_Modifier_Star_D = 4
        if roll_for_Disk_Density_of_Star_D == 17:
            Disk_Mass_Factor_Star_D = 3.2
            Disk_Mass_Modifier_Star_D = 5
        if roll_for_Disk_Density_of_Star_D == 18:
            Disk_Mass_Factor_Star_D = 4.0
            Disk_Mass_Modifier_Star_D = 6
        print(f"Disk Mass Factor for Star D: {Disk_Mass_Factor_Star_D}")
        print(f"Disk Mass Modifier for Star D: {Disk_Mass_Modifier_Star_D}")

    # calculate planetismal masses
    if Number_of_Stars >= 1:
        Planetismal_Mass_for_Star_A = Disk_Mass_Factor_Star_A * Mass_A * Metallicity
        print(f"Planentismal Mass for Star A: {Planetismal_Mass_for_Star_A}")
    if Number_of_Stars >= 2:
        Planetismal_Mass_for_Star_B = Disk_Mass_Factor_Star_B * Mass_B * Metallicity
        print(f"Planentismal Mass for Star B: {Planetismal_Mass_for_Star_B}")
    if Number_of_Stars >= 3:
        Planetismal_Mass_for_Star_C = Disk_Mass_Factor_Star_C * Mass_C * Metallicity
        print(f"Planentismal Mass for Star C: {Planetismal_Mass_for_Star_C}")
    if Number_of_Stars == 4:
        Planetismal_Mass_for_Star_D = Disk_Mass_Factor_Star_D * Mass_D * Metallicity
        print(f"Planentismal Mass for Star D: {Planetismal_Mass_for_Star_D}")

    # calculate disk inner edges
    if Number_of_Stars >= 1:
        Disk_Inner_Edge_for_Star_A = (_2d6) * 0.005 * (Mass_A ** (1/3))
        Disk_Inner_Edge_for_Star_A = round(Disk_Inner_Edge_for_Star_A,3)
        print(f"Disk Inner Edge for Star A: {Disk_Inner_Edge_for_Star_A} AU")
    if Number_of_Stars >= 2:
        Disk_Inner_Edge_for_Star_B = (_2d6) * 0.005 * (Mass_B ** (1/3))
        Disk_Inner_Edge_for_Star_B = round(Disk_Inner_Edge_for_Star_B,3)
        print(f"Disk Inner Edge for Star B: {Disk_Inner_Edge_for_Star_B} AU")
    if Number_of_Stars >= 3:
        Disk_Inner_Edge_for_Star_C = (_2d6) * 0.005 * (Mass_C ** (1/3))
        Disk_Inner_Edge_for_Star_C = round(Disk_Inner_Edge_for_Star_C,3)
        print(f"Disk Inner Edge for Star C: {Disk_Inner_Edge_for_Star_C} AU")
    if Number_of_Stars == 4:
        Disk_Inner_Edge_for_Star_D = (_2d6) * 0.005 * (Mass_D ** (1/3))
        Disk_Inner_Edge_for_Star_D = round(Disk_Inner_Edge_for_Star_D,3)
        print(f"Disk Inner Edge for Star D: {Disk_Inner_Edge_for_Star_D} AU")

    # calculate ice lines
    if Number_of_Stars >= 1:
        Radius_of_Ice_Line_for_Star_A = 4 * math.sqrt(Initial_Luminosity_of_Star_A)
        Radius_of_Ice_Line_for_Star_A = round(Radius_of_Ice_Line_for_Star_A,3)
        print(f"Ice Line for Star A: {Radius_of_Ice_Line_for_Star_A} AU")
    if Number_of_Stars >= 2:
        Radius_of_Ice_Line_for_Star_B = 4 * math.sqrt(Initial_Luminosity_of_Star_B)
        Radius_of_Ice_Line_for_Star_B = round(Radius_of_Ice_Line_for_Star_B,3)
        print(f"Ice Line for Star B: {Radius_of_Ice_Line_for_Star_B} AU")
    if Number_of_Stars >= 3:
        Radius_of_Ice_Line_for_Star_C = 4 * math.sqrt(Initial_Luminosity_of_Star_C)
        Radius_of_Ice_Line_for_Star_C = round(Radius_of_Ice_Line_for_Star_C,3)
        print(f"Ice Line for Star C: {Radius_of_Ice_Line_for_Star_C} AU")
    if Number_of_Stars == 4:
        Radius_of_Ice_Line_for_Star_D = 4 * math.sqrt(Initial_Luminosity_of_Star_D)
        Radius_of_Ice_Line_for_Star_D = round(Radius_of_Ice_Line_for_Star_D,3)
        print(f"Ice Line for Star D: {Radius_of_Ice_Line_for_Star_D} AU")

    # calculate slow accretion lines
    if Number_of_Stars >= 1:
        Radius_of_Slow_Accretion_Line_for_Star_A = 20 * (Mass_A ** (1/3))
        Radius_of_Slow_Accretion_Line_for_Star_A = round(Radius_of_Slow_Accretion_Line_for_Star_A,3)
        print(f"Slow Accretion Line for Star A: {Radius_of_Slow_Accretion_Line_for_Star_A} AU")
    if Number_of_Stars >= 2:
        Radius_of_Slow_Accretion_Line_for_Star_B = 20 * (Mass_B ** (1/3))
        Radius_of_Slow_Accretion_Line_for_Star_B = round(Radius_of_Slow_Accretion_Line_for_Star_B,3)
        print(f"Slow Accretion Line for Star B: {Radius_of_Slow_Accretion_Line_for_Star_B} AU")
    if Number_of_Stars >= 3:
        Radius_of_Slow_Accretion_Line_for_Star_C = 20 * (Mass_C ** (1/3))
        Radius_of_Slow_Accretion_Line_for_Star_C = round(Radius_of_Slow_Accretion_Line_for_Star_C,3)
        print(f"Slow Accretion Line for Star C: {Radius_of_Slow_Accretion_Line_for_Star_C} AU")
    if Number_of_Stars == 4:
        Radius_of_Slow_Accretion_Line_for_Star_D = 20 * (Mass_D ** (1/3))
        Radius_of_Slow_Accretion_Line_for_Star_D = round(Radius_of_Slow_Accretion_Line_for_Star_D,3)
        print(f"Slow Accretion Line for Star D: {Radius_of_Slow_Accretion_Line_for_Star_D} AU")

    # calculate forbidden zones
    if Number_of_Stars == 1:
        print("Single Star System - No Forbidden Zone for Planet Formation")
    if Number_of_Stars == 2:
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A = (1/3) * binary_minimum_distance
        print(f"Forbidden Zone for Star A begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A} AU")
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B = (1/3) * binary_minimum_distance
        print(f"Forbidden Zone for Star B begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B} AU")
    if Number_of_Stars == 3:
        if Stellar_Arrangement == "A-BC":
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A = (1/3) * A_BC_minimum_distance
            print(f"Forbidden Zone for Star A begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A} AU")
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B = (1/3) * BC_minimum_distance
            print(f"Forbidden Zone for Star B begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B} AU")
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C = (1/3) * BC_minimum_distance
            print(f"Forbidden Zone for Star C begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C} AU")
        if Stellar_Arrangement == "AB-C":
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A = (1/3) * AB_minimum_distance
            print(f"Forbidden Zone for Star A begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A} AU")
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B = (1/3) * AB_minimum_distance
            print(f"Forbidden Zone for Star B begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B} AU")
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C = (1/3) * AB_C_minimum_distance
            print(f"Forbidden Zone for Star c begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C} AU")
    if Number_of_Stars == 4:
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A = (1/3) * AB_minimum_distance
        print(f"Forbidden Zone for Star A begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A} AU")
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B = (1/3) * AB_minimum_distance
        print(f"Forbidden Zone for Star B begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B} AU")
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C = (1/3) * CD_minimum_distance
        print(f"Forbidden Zone for Star C begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C} AU")
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D = (1/3) * CD_minimum_distance
        print(f"Forbidden Zone for Star D begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D} AU")

    # arrange planetary formation orbits
    if Number_of_Stars >= 1:

        Star_A_Protoplanet_1_Flag = "Yes"
        Star_A_Protoplanet_1_Speed_Flag = "Fast"
        Star_A_Protoplanet_2_Flag = "Yes"
        Star_A_Protoplanet_2_Speed_Flag = "Fast"
        Star_A_Protoplanet_3_Flag = "Yes"
        Star_A_Protoplanet_3_Speed_Flag = "Fast"
        Star_A_Protoplanet_4_Flag = "Yes"
        Star_A_Protoplanet_4_Speed_Flag = "Fast"
        Star_A_Protoplanet_5_Flag = "Yes"
        Star_A_Protoplanet_5_Speed_Flag = "Fast"
        Star_A_Protoplanet_6_Flag = "Yes"
        Star_A_Protoplanet_6_Speed_Flag = "Fast"
        Star_A_Protoplanet_7_Flag = "Yes"
        Star_A_Protoplanet_7_Speed_Flag = "Fast"
        Star_A_Protoplanet_8_Flag = "Yes"
        Star_A_Protoplanet_8_Speed_Flag = "Fast"
        Star_A_Protoplanet_9_Flag = "Yes"
        Star_A_Protoplanet_9_Speed_Flag = "Fast"
        Star_A_Protoplanet_10_Flag = "Yes"
        Star_A_Protoplanet_10_Speed_Flag = "Fast"
        Star_A_Protoplanet_11_Flag = "Yes"
        Star_A_Protoplanet_11_Speed_Flag = "Fast"
        Star_A_Protoplanet_12_Flag = "Yes"
        Star_A_Protoplanet_12_Speed_Flag = "Fast"
        Star_A_Protoplanet_13_Flag = "Yes"
        Star_A_Protoplanet_13_Speed_Flag = "Fast"
        Star_A_Protoplanet_14_Flag = "Yes"
        Star_A_Protoplanet_14_Speed_Flag = "Fast"
        Star_A_Protoplanet_15_Flag = "Yes"
        Star_A_Protoplanet_15_Speed_Flag = "Fast"
        Star_A_Protoplanet_16_Flag = "Yes"
        Star_A_Protoplanet_16_Speed_Flag = "Fast"

        formation_orbit_0_for_Star_A = Disk_Inner_Edge_for_Star_A

        formation_orbit_1_for_Star_A = 0.6 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 1 for Star A is at {formation_orbit_1_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_1_for_Star_A:
            print("Formation Orbit 1 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 1 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 1 is outisde the slow accretion line")
            Star_A_Protoplanet_1_Speed_Flag = "Slow"

        formation_orbit_2_for_Star_A = 0.8 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 2 for Star A is at {formation_orbit_2_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_2_for_Star_A:
            print("Formation Orbit 2 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 2 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 2 is outisde the slow accretion line")
            Star_A_Protoplanet_2_Speed_Flag = "Slow"

        formation_orbit_3_for_Star_A = 1.2 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 3 for Star A is at {formation_orbit_3_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_3_for_Star_A:
            print("Formation Orbit 3 is within the inner edge - no protoplanet formed") 
            Star_A_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 3 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 3 is outisde the slow accretion line")
            Star_A_Protoplanet_3_Speed_Flag = "Slow"

        formation_orbit_4_for_Star_A = 1.8 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 4 for Star A is at {formation_orbit_4_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_4_for_Star_A:
            print("Formation Orbit 4 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 4 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 4 is outisde the slow accretion line")
            Star_A_Protoplanet_4_Speed_Flag = "Slow"

        formation_orbit_5_for_Star_A = 2.7 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 5 for Star A is at {formation_orbit_5_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_5_for_Star_A:
            print("Formation Orbit 5 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 5 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 5 is outisde the slow accretion line")
            Star_A_Protoplanet_5_Speed_Flag = "Slow"

        formation_orbit_6_for_Star_A = 4.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 6 for Star A is at {formation_orbit_6_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_6_for_Star_A:
            print("Formation Orbit 6 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 6 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 6 is outisde the slow accretion line")
            Star_A_Protoplanet_6_Speed_Flag = "Slow"

        formation_orbit_7_for_Star_A = 6.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 7 for Star A is at {formation_orbit_7_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_7_for_Star_A:
            print("Formation Orbit 7 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 7 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 7 is outisde the slow accretion line")
            Star_A_Protoplanet_7_Speed_Flag = "Slow"

        formation_orbit_8_for_Star_A = 9.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 8 for Star A is at {formation_orbit_8_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_8_for_Star_A:
            print("Formation Orbit 8 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 8 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 8 is outisde the slow accretion line")
            Star_A_Protoplanet_8_Speed_Flag = "Slow"

        formation_orbit_9_for_Star_A = 13.5 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 9 for Star A is at {formation_orbit_9_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_9_for_Star_A:
            print("Formation Orbit 9 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 9 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 9 is outisde the slow accretion line")
            Star_A_Protoplanet_9_Speed_Flag = "Slow"

        formation_orbit_10_for_Star_A = 20.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 10 for Star A is at {formation_orbit_10_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_10_for_Star_A:
            print("Formation Orbit 10 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 10 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 10 is outisde the slow accretion line")
            Star_A_Protoplanet_10_Speed_Flag = "Slow"

        formation_orbit_11_for_Star_A = 30.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 11 for Star A is at {formation_orbit_11_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_10_for_Star_A:
            print("Formation Orbit 11 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 11 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 11 is outisde the slow accretion line")
            Star_A_Protoplanet_11_Speed_Flag = "Slow"

        formation_orbit_12_for_Star_A = 45.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 12 for Star A is at {formation_orbit_12_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_12_for_Star_A:
            print("Formation Orbit 12 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 12 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 12 is outisde the slow accretion line")
            Star_A_Protoplanet_12_Speed_Flag = "Slow"

        formation_orbit_13_for_Star_A = 68.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 13 for Star A is at {formation_orbit_13_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_13_for_Star_A:
            print("Formation Orbit 13 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 13 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 13 is outisde the slow accretion line")
            Star_A_Protoplanet_13_Speed_Flag = "Slow"

        formation_orbit_14_for_Star_A = 100.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 14 for Star A is at {formation_orbit_14_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_14_for_Star_A:
            print("Formation Orbit 14 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 14 is outisde the slow accretion line")
            Star_A_Protoplanet_14_Speed_Flag = "Slow"

        formation_orbit_15_for_Star_A = 150.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 15 for Star A is at {formation_orbit_15_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_15_for_Star_A:
            print("Formation Orbit 15 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 15 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 15 is outisde the slow accretion line")
            Star_A_Protoplanet_15_Speed_Flag = "Slow"

        formation_orbit_16_for_Star_A = 222.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 16 for Star A is at {formation_orbit_16_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_16_for_Star_A:
            print("Formation Orbit 16 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 16 is outisde the slow accretion line")
            Star_A_Protoplanet_16_Speed_Flag = "Slow"

    if Number_of_Stars >= 2:
        Star_B_Protoplanet_1_Flag = "Yes"
        Star_B_Protoplanet_1_Speed_Flag = "Fast"
        Star_B_Protoplanet_2_Flag = "Yes"
        Star_B_Protoplanet_2_Speed_Flag = "Fast"
        Star_B_Protoplanet_3_Flag = "Yes"
        Star_B_Protoplanet_3_Speed_Flag = "Fast"
        Star_B_Protoplanet_4_Flag = "Yes"
        Star_B_Protoplanet_4_Speed_Flag = "Fast"
        Star_B_Protoplanet_5_Flag = "Yes"
        Star_B_Protoplanet_5_Speed_Flag = "Fast"
        Star_B_Protoplanet_6_Flag = "Yes"
        Star_B_Protoplanet_6_Speed_Flag = "Fast"
        Star_B_Protoplanet_7_Flag = "Yes"
        Star_B_Protoplanet_7_Speed_Flag = "Fast"
        Star_B_Protoplanet_8_Flag = "Yes"
        Star_B_Protoplanet_8_Speed_Flag = "Fast"
        Star_B_Protoplanet_9_Flag = "Yes"
        Star_B_Protoplanet_9_Speed_Flag = "Fast"
        Star_B_Protoplanet_10_Flag = "Yes"
        Star_B_Protoplanet_10_Speed_Flag = "Fast"
        Star_B_Protoplanet_11_Flag = "Yes"
        Star_B_Protoplanet_11_Speed_Flag = "Fast"
        Star_B_Protoplanet_12_Flag = "Yes"
        Star_B_Protoplanet_12_Speed_Flag = "Fast"
        Star_B_Protoplanet_13_Flag = "Yes"
        Star_B_Protoplanet_13_Speed_Flag = "Fast"
        Star_B_Protoplanet_14_Flag = "Yes"
        Star_B_Protoplanet_14_Speed_Flag = "Fast"
        Star_B_Protoplanet_15_Flag = "Yes"
        Star_B_Protoplanet_15_Speed_Flag = "Fast"
        Star_B_Protoplanet_16_Flag = "Yes"
        Star_B_Protoplanet_16_Speed_Flag = "Fast"

        formation_orbit_0_for_Star_B = Disk_Inner_Edge_for_Star_B

        formation_orbit_1_for_Star_B = 0.6 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 1 for Star A is at {formation_orbit_1_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_1_for_Star_B:
            print("Formation Orbit 1 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 1 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 1 is outisde the slow accretion line")
            Star_B_Protoplanet_1_Speed_Flag = "Slow"

        formation_orbit_2_for_Star_B = 0.8 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 2 for Star A is at {formation_orbit_2_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_2_for_Star_B:
            print("Formation Orbit 2 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 2 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 2 is outisde the slow accretion line")
            Star_B_Protoplanet_2_Speed_Flag = "Slow"

        formation_orbit_3_for_Star_B = 1.2 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 3 for Star A is at {formation_orbit_3_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_3_for_Star_B:
            print("Formation Orbit 3 is within the inner edge - no protoplanet formed") 
            Star_B_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 3 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 3 is outisde the slow accretion line")
            Star_B_Protoplanet_3_Speed_Flag = "Slow"

        formation_orbit_4_for_Star_B = 1.8 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 4 for Star A is at {formation_orbit_4_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_4_for_Star_B:
            print("Formation Orbit 4 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 4 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 4 is outisde the slow accretion line")
            Star_B_Protoplanet_4_Speed_Flag = "Slow"

        formation_orbit_5_for_Star_B = 2.7 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 5 for Star A is at {formation_orbit_5_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_5_for_Star_B:
            print("Formation Orbit 5 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 5 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 5 is outisde the slow accretion line")
            Star_B_Protoplanet_5_Speed_Flag = "Slow"

        formation_orbit_6_for_Star_B = 4.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 6 for Star A is at {formation_orbit_6_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_6_for_Star_B:
            print("Formation Orbit 6 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 6 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 6 is outisde the slow accretion line")
            Star_B_Protoplanet_6_Speed_Flag = "Slow"

        formation_orbit_7_for_Star_B = 6.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 7 for Star A is at {formation_orbit_7_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_7_for_Star_B:
            print("Formation Orbit 7 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 7 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 7 is outisde the slow accretion line")
            Star_B_Protoplanet_7_Speed_Flag = "Slow"

        formation_orbit_8_for_Star_B = 9.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 8 for Star A is at {formation_orbit_8_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_8_for_Star_B:
            print("Formation Orbit 8 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 8 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 8 is outisde the slow accretion line")
            Star_B_Protoplanet_8_Speed_Flag = "Slow"

        formation_orbit_9_for_Star_B = 13.5 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 9 for Star A is at {formation_orbit_9_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_9_for_Star_B:
            print("Formation Orbit 9 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 9 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 9 is outisde the slow accretion line")
            Star_B_Protoplanet_9_Speed_Flag = "Slow"

        formation_orbit_10_for_Star_B = 20.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 10 for Star A is at {formation_orbit_10_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_10_for_Star_B:
            print("Formation Orbit 10 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 10 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 10 is outisde the slow accretion line")
            Star_B_Protoplanet_10_Speed_Flag = "Slow"

        formation_orbit_11_for_Star_B = 30.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 11 for Star A is at {formation_orbit_11_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_10_for_Star_B:
            print("Formation Orbit 11 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 11 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 11 is outisde the slow accretion line")
            Star_B_Protoplanet_11_Speed_Flag = "Slow"

        formation_orbit_12_for_Star_B = 45.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 12 for Star A is at {formation_orbit_12_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_12_for_Star_B:
            print("Formation Orbit 12 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 12 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 12 is outisde the slow accretion line")
            Star_B_Protoplanet_12_Speed_Flag = "Slow"

        formation_orbit_13_for_Star_B = 68.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 13 for Star A is at {formation_orbit_13_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_13_for_Star_B:
            print("Formation Orbit 13 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 13 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 13 is outisde the slow accretion line")
            Star_B_Protoplanet_13_Speed_Flag = "Slow"

        formation_orbit_14_for_Star_B = 100.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 14 for Star A is at {formation_orbit_14_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_14_for_Star_B:
            print("Formation Orbit 14 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 14 is outisde the slow accretion line")
            Star_B_Protoplanet_14_Speed_Flag = "Slow"

        formation_orbit_15_for_Star_B = 150.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 15 for Star A is at {formation_orbit_15_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_15_for_Star_B:
            print("Formation Orbit 15 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 15 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 15 is outisde the slow accretion line")
            Star_B_Protoplanet_15_Speed_Flag = "Slow"

        formation_orbit_16_for_Star_B = 222.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 16 for Star A is at {formation_orbit_16_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_16_for_Star_B:
            print("Formation Orbit 16 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 16 is outisde the slow accretion line")
            Star_B_Protoplanet_16_Speed_Flag = "Slow"

    if Number_of_Stars >= 3:
        Star_C_Protoplanet_1_Flag = "Yes"
        Star_C_Protoplanet_1_Speed_Flag = "Fast"
        Star_C_Protoplanet_2_Flag = "Yes"
        Star_C_Protoplanet_2_Speed_Flag = "Fast"
        Star_C_Protoplanet_3_Flag = "Yes"
        Star_C_Protoplanet_3_Speed_Flag = "Fast"
        Star_C_Protoplanet_4_Flag = "Yes"
        Star_C_Protoplanet_4_Speed_Flag = "Fast"
        Star_C_Protoplanet_5_Flag = "Yes"
        Star_C_Protoplanet_5_Speed_Flag = "Fast"
        Star_C_Protoplanet_6_Flag = "Yes"
        Star_C_Protoplanet_6_Speed_Flag = "Fast"
        Star_C_Protoplanet_7_Flag = "Yes"
        Star_C_Protoplanet_7_Speed_Flag = "Fast"
        Star_C_Protoplanet_8_Flag = "Yes"
        Star_C_Protoplanet_8_Speed_Flag = "Fast"
        Star_C_Protoplanet_9_Flag = "Yes"
        Star_C_Protoplanet_9_Speed_Flag = "Fast"
        Star_C_Protoplanet_10_Flag = "Yes"
        Star_C_Protoplanet_10_Speed_Flag = "Fast"
        Star_C_Protoplanet_11_Flag = "Yes"
        Star_C_Protoplanet_11_Speed_Flag = "Fast"
        Star_C_Protoplanet_12_Flag = "Yes"
        Star_C_Protoplanet_12_Speed_Flag = "Fast"
        Star_C_Protoplanet_13_Flag = "Yes"
        Star_C_Protoplanet_13_Speed_Flag = "Fast"
        Star_C_Protoplanet_14_Flag = "Yes"
        Star_C_Protoplanet_14_Speed_Flag = "Fast"
        Star_C_Protoplanet_15_Flag = "Yes"
        Star_C_Protoplanet_15_Speed_Flag = "Fast"
        Star_C_Protoplanet_16_Flag = "Yes"
        Star_C_Protoplanet_16_Speed_Flag = "Fast"

        formation_orbit_0_for_Star_C = Disk_Inner_Edge_for_Star_C

        formation_orbit_1_for_Star_C = 0.6 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 1 for Star A is at {formation_orbit_1_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_1_for_Star_C:
            print("Formation Orbit 1 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 1 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 1 is outisde the slow accretion line")
            Star_C_Protoplanet_1_Speed_Flag = "Slow"

        formation_orbit_2_for_Star_C = 0.8 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 2 for Star A is at {formation_orbit_2_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_2_for_Star_C:
            print("Formation Orbit 2 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 2 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 2 is outisde the slow accretion line")
            Star_C_Protoplanet_2_Speed_Flag = "Slow"

        formation_orbit_3_for_Star_C = 1.2 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 3 for Star A is at {formation_orbit_3_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_3_for_Star_C:
            print("Formation Orbit 3 is within the inner edge - no protoplanet formed") 
            Star_C_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 3 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 3 is outisde the slow accretion line")
            Star_C_Protoplanet_3_Speed_Flag = "Slow"

        formation_orbit_4_for_Star_C = 1.8 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 4 for Star A is at {formation_orbit_4_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_4_for_Star_C:
            print("Formation Orbit 4 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 4 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 4 is outisde the slow accretion line")
            Star_C_Protoplanet_4_Speed_Flag = "Slow"

        formation_orbit_5_for_Star_C = 2.7 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 5 for Star A is at {formation_orbit_5_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_5_for_Star_C:
            print("Formation Orbit 5 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 5 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 5 is outisde the slow accretion line")
            Star_C_Protoplanet_5_Speed_Flag = "Slow"

        formation_orbit_6_for_Star_C = 4.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 6 for Star A is at {formation_orbit_6_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_6_for_Star_C:
            print("Formation Orbit 6 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 6 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 6 is outisde the slow accretion line")
            Star_C_Protoplanet_6_Speed_Flag = "Slow"

        formation_orbit_7_for_Star_C = 6.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 7 for Star A is at {formation_orbit_7_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_7_for_Star_C:
            print("Formation Orbit 7 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 7 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 7 is outisde the slow accretion line")
            Star_C_Protoplanet_7_Speed_Flag = "Slow"

        formation_orbit_8_for_Star_C = 9.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 8 for Star A is at {formation_orbit_8_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_8_for_Star_C:
            print("Formation Orbit 8 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 8 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 8 is outisde the slow accretion line")
            Star_C_Protoplanet_8_Speed_Flag = "Slow"

        formation_orbit_9_for_Star_C = 13.5 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 9 for Star A is at {formation_orbit_9_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_9_for_Star_C:
            print("Formation Orbit 9 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 9 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 9 is outisde the slow accretion line")
            Star_C_Protoplanet_9_Speed_Flag = "Slow"

        formation_orbit_10_for_Star_C = 20.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 10 for Star A is at {formation_orbit_10_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_10_for_Star_C:
            print("Formation Orbit 10 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 10 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 10 is outisde the slow accretion line")
            Star_C_Protoplanet_10_Speed_Flag = "Slow"

        formation_orbit_11_for_Star_C = 30.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 11 for Star A is at {formation_orbit_11_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_10_for_Star_C:
            print("Formation Orbit 11 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 11 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 11 is outisde the slow accretion line")
            Star_C_Protoplanet_11_Speed_Flag = "Slow"

        formation_orbit_12_for_Star_C = 45.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 12 for Star A is at {formation_orbit_12_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_12_for_Star_C:
            print("Formation Orbit 12 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 12 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 12 is outisde the slow accretion line")
            Star_C_Protoplanet_12_Speed_Flag = "Slow"

        formation_orbit_13_for_Star_C = 68.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 13 for Star A is at {formation_orbit_13_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_13_for_Star_C:
            print("Formation Orbit 13 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 13 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 13 is outisde the slow accretion line")
            Star_C_Protoplanet_13_Speed_Flag = "Slow"

        formation_orbit_14_for_Star_C = 100.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 14 for Star A is at {formation_orbit_14_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_14_for_Star_C:
            print("Formation Orbit 14 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 14 is outisde the slow accretion line")
            Star_C_Protoplanet_14_Speed_Flag = "Slow"

        formation_orbit_15_for_Star_C = 150.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 15 for Star A is at {formation_orbit_15_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_15_for_Star_C:
            print("Formation Orbit 15 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 15 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 15 is outisde the slow accretion line")
            Star_C_Protoplanet_15_Speed_Flag = "Slow"

        formation_orbit_16_for_Star_C = 222.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 16 for Star A is at {formation_orbit_16_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_16_for_Star_C:
            print("Formation Orbit 16 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 16 is outisde the slow accretion line")
            Star_C_Protoplanet_16_Speed_Flag = "Slow"

    if Number_of_Stars == 4:
        Star_D_Protoplanet_1_Flag = "Yes"
        Star_D_Protoplanet_1_Speed_Flag = "Fast"
        Star_D_Protoplanet_2_Flag = "Yes"
        Star_D_Protoplanet_2_Speed_Flag = "Fast"
        Star_D_Protoplanet_3_Flag = "Yes"
        Star_D_Protoplanet_3_Speed_Flag = "Fast"
        Star_D_Protoplanet_4_Flag = "Yes"
        Star_D_Protoplanet_4_Speed_Flag = "Fast"
        Star_D_Protoplanet_5_Flag = "Yes"
        Star_D_Protoplanet_5_Speed_Flag = "Fast"
        Star_D_Protoplanet_6_Flag = "Yes"
        Star_D_Protoplanet_6_Speed_Flag = "Fast"
        Star_D_Protoplanet_7_Flag = "Yes"
        Star_D_Protoplanet_7_Speed_Flag = "Fast"
        Star_D_Protoplanet_8_Flag = "Yes"
        Star_D_Protoplanet_8_Speed_Flag = "Fast"
        Star_D_Protoplanet_9_Flag = "Yes"
        Star_D_Protoplanet_9_Speed_Flag = "Fast"
        Star_D_Protoplanet_10_Flag = "Yes"
        Star_D_Protoplanet_10_Speed_Flag = "Fast"
        Star_D_Protoplanet_11_Flag = "Yes"
        Star_D_Protoplanet_11_Speed_Flag = "Fast"
        Star_D_Protoplanet_12_Flag = "Yes"
        Star_D_Protoplanet_12_Speed_Flag = "Fast"
        Star_D_Protoplanet_13_Flag = "Yes"
        Star_D_Protoplanet_13_Speed_Flag = "Fast"
        Star_D_Protoplanet_14_Flag = "Yes"
        Star_D_Protoplanet_14_Speed_Flag = "Fast"
        Star_D_Protoplanet_15_Flag = "Yes"
        Star_D_Protoplanet_15_Speed_Flag = "Fast"
        Star_D_Protoplanet_16_Flag = "Yes"
        Star_D_Protoplanet_16_Speed_Flag = "Fast"

        formation_orbit_0_for_Star_D = Disk_Inner_Edge_for_Star_D

        formation_orbit_1_for_Star_D = 0.6 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 1 for Star A is at {formation_orbit_1_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_1_for_Star_D:
            print("Formation Orbit 1 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 1 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 1 is outisde the slow accretion line")
            Star_D_Protoplanet_1_Speed_Flag = "Slow"

        formation_orbit_2_for_Star_D = 0.8 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 2 for Star A is at {formation_orbit_2_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_2_for_Star_D:
            print("Formation Orbit 2 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 2 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 2 is outisde the slow accretion line")
            Star_D_Protoplanet_2_Speed_Flag = "Slow"

        formation_orbit_3_for_Star_D = 1.2 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 3 for Star A is at {formation_orbit_3_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_3_for_Star_D:
            print("Formation Orbit 3 is within the inner edge - no protoplanet formed") 
            Star_D_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 3 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 3 is outisde the slow accretion line")
            Star_D_Protoplanet_3_Speed_Flag = "Slow"

        formation_orbit_4_for_Star_D = 1.8 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 4 for Star A is at {formation_orbit_4_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_4_for_Star_D:
            print("Formation Orbit 4 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 4 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 4 is outisde the slow accretion line")
            Star_D_Protoplanet_4_Speed_Flag = "Slow"

        formation_orbit_5_for_Star_D = 2.7 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 5 for Star A is at {formation_orbit_5_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_5_for_Star_D:
            print("Formation Orbit 5 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 5 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 5 is outisde the slow accretion line")
            Star_D_Protoplanet_5_Speed_Flag = "Slow"

        formation_orbit_6_for_Star_D = 4.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 6 for Star A is at {formation_orbit_6_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_6_for_Star_D:
            print("Formation Orbit 6 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 6 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 6 is outisde the slow accretion line")
            Star_D_Protoplanet_6_Speed_Flag = "Slow"

        formation_orbit_7_for_Star_D = 6.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 7 for Star A is at {formation_orbit_7_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_7_for_Star_D:
            print("Formation Orbit 7 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 7 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 7 is outisde the slow accretion line")
            Star_D_Protoplanet_7_Speed_Flag = "Slow"

        formation_orbit_8_for_Star_D = 9.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 8 for Star A is at {formation_orbit_8_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_8_for_Star_D:
            print("Formation Orbit 8 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 8 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 8 is outisde the slow accretion line")
            Star_D_Protoplanet_8_Speed_Flag = "Slow"

        formation_orbit_9_for_Star_D = 13.5 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 9 for Star A is at {formation_orbit_9_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_9_for_Star_D:
            print("Formation Orbit 9 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 9 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 9 is outisde the slow accretion line")
            Star_D_Protoplanet_9_Speed_Flag = "Slow"

        formation_orbit_10_for_Star_D = 20.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 10 for Star A is at {formation_orbit_10_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_10_for_Star_D:
            print("Formation Orbit 10 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 10 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 10 is outisde the slow accretion line")
            Star_D_Protoplanet_10_Speed_Flag = "Slow"

        formation_orbit_11_for_Star_D = 30.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 11 for Star A is at {formation_orbit_11_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_10_for_Star_D:
            print("Formation Orbit 11 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 11 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 11 is outisde the slow accretion line")
            Star_D_Protoplanet_11_Speed_Flag = "Slow"

        formation_orbit_12_for_Star_D = 45.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 12 for Star A is at {formation_orbit_12_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_12_for_Star_D:
            print("Formation Orbit 12 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 12 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 12 is outisde the slow accretion line")
            Star_D_Protoplanet_12_Speed_Flag = "Slow"

        formation_orbit_13_for_Star_D = 68.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 13 for Star A is at {formation_orbit_13_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_13_for_Star_D:
            print("Formation Orbit 13 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 13 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 13 is outisde the slow accretion line")
            Star_D_Protoplanet_13_Speed_Flag = "Slow"

        formation_orbit_14_for_Star_D = 100.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 14 for Star A is at {formation_orbit_14_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_14_for_Star_D:
            print("Formation Orbit 14 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 14 is outisde the slow accretion line")
            Star_D_Protoplanet_14_Speed_Flag = "Slow"

        formation_orbit_15_for_Star_D = 150.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 15 for Star A is at {formation_orbit_15_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_15_for_Star_D:
            print("Formation Orbit 15 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 15 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 15 is outisde the slow accretion line")
            Star_D_Protoplanet_15_Speed_Flag = "Slow"

        formation_orbit_16_for_Star_D = 222.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 16 for Star A is at {formation_orbit_16_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_16_for_Star_D:
            print("Formation Orbit 16 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 16 is outisde the slow accretion line")
            Star_D_Protoplanet_16_Speed_Flag = "Slow"
