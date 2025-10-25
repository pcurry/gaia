# this sub-program covers step 11 ("Core Accretion") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

    # "To begin, check the worksheet to see whether formation orbit 6 falls within a forbidden zone. If it does, then no planets will form in this step; skip forward to Step Twelve" (pg.63)
    if Number_of_Stars >= 1:
        if formation_orbit_6_for_Star_A < Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 6 around Star A does not lie within a forbidden zone")
            if Planetismal_Mass_for_Star_A < 0.11:
                print("Insufficent Planetesimal Mass - no planets formed due to Core Accretion around Star A")
                Number_of_Core_Accretion_Planets_Supported_By_Planetismal_Mass_for_Star_A = 0
            if 0.11 <= Planetismal_Mass_for_Star_A < 0.17:
                print("Sufficient Planentismal Mass for no more than one Core Accretion planet to form around Star A")
                Number_of_Core_Accretion_Planets_Supported_By_Planetismal_Mass_for_Star_A = 1
            if 0.17 <= Planetismal_Mass_for_Star_A < 0.24:
                print("Sufficient Planetismal Mass for no more than two Core Accretion planets to form around Star A")
                Number_of_Core_Accretion_Planets_Supported_By_Planetismal_Mass_for_Star_A = 2
            if 0.24 <= Planetismal_Mass_for_Star_A:
                print("Sufficient Planetismal Mass for any number of Core Accreiton planets to form around Star A")
                Number_of_Core_Accretion_Planets_Supported_By_Planetismal_Mass_for_Star_A = 10

    # "beginning with formation orbit 6, count formation orbits outward until the next formation orbit: is already occupied by a disk-instability planet, is outside the slow-accretion line, 
    # or falls within a forbidden zone." (pg. 63)
 
        Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A = 0
 
        core_accretion_flag_for_Star_A_orbit_6 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_6 = "No"
        if formation_orbit_6_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_6 = "No"
        if formation_orbit_6_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_6 = "No"
        if core_accretion_flag_for_Star_A_orbit_6 == "TBD":
            core_accretion_flag_for_Star_A_orbit_6 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_6 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)

        core_accretion_flag_for_Star_A_orbit_7 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_7 = "No"
        if formation_orbit_7_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_7 = "No"
        if formation_orbit_7_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_7 = "No"
        if core_accretion_flag_for_Star_A_orbit_7 == "TBD":
            core_accretion_flag_for_Star_A_orbit_7 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_7 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)

        core_accretion_flag_for_Star_A_orbit_8 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_8 = "No"
        if formation_orbit_8_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_8 = "No"
        if formation_orbit_8_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_8 = "No"
        if core_accretion_flag_for_Star_A_orbit_8 == "TBD":
            core_accretion_flag_for_Star_A_orbit_8 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_8 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)

        core_accretion_flag_for_Star_A_orbit_9 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_9 = "No"
        if formation_orbit_9_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_9 = "No"
        if formation_orbit_9_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_9 = "No"
        if core_accretion_flag_for_Star_A_orbit_9 == "TBD":
            core_accretion_flag_for_Star_A_orbit_9 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_9 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)

        core_accretion_flag_for_Star_A_orbit_10 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_10 = "No"
        if formation_orbit_10_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_10 = "No"
        if formation_orbit_10_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_10 = "No"
        if core_accretion_flag_for_Star_A_orbit_10 == "TBD":
            core_accretion_flag_for_Star_A_orbit_10 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_10 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)

        core_accretion_flag_for_Star_A_orbit_11 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_11 = "No"
        if formation_orbit_11_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_11 = "No"
        if formation_orbit_11_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_11 = "No"
        if core_accretion_flag_for_Star_A_orbit_11 == "TBD":
            core_accretion_flag_for_Star_A_orbit_11 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_11 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)

        core_accretion_flag_for_Star_A_orbit_12 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_12 = "No"
        if formation_orbit_12_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_12 = "No"
        if formation_orbit_12_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_12 = "No"
        if core_accretion_flag_for_Star_A_orbit_12 == "TBD":
            core_accretion_flag_for_Star_A_orbit_12 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_12 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)

        core_accretion_flag_for_Star_A_orbit_13 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_13 = "No"
        if formation_orbit_13_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_13 = "No"
        if formation_orbit_13_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_13 = "No"
        if core_accretion_flag_for_Star_A_orbit_13 == "TBD":
            core_accretion_flag_for_Star_A_orbit_13 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_13 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)

        core_accretion_flag_for_Star_A_orbit_14 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_14 = "No"
        if formation_orbit_14_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_14 = "No"
        if formation_orbit_14_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_14 = "No"
        if core_accretion_flag_for_Star_A_orbit_14 == "TBD":
            core_accretion_flag_for_Star_A_orbit_14 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_14 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)
     
        core_accretion_flag_for_Star_A_orbit_15 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_15 = "No"
        if formation_orbit_15_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_15 = "No"
        if formation_orbit_15_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_15 = "No"
        if core_accretion_flag_for_Star_A_orbit_15 == "TBD":
            core_accretion_flag_for_Star_A_orbit_15 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_15 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)

        core_accretion_flag_for_Star_A_orbit_16 = "TBD"
        if Star_A_Protoplanet_6_Flag == "Disk Instability Planet":
            core_accretion_flag_for_Star_A_orbit_16 = "No"
        if formation_orbit_16_for_Star_A > Radius_of_Slow_Accretion_Line_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_16 = "No"
        if formation_orbit_16_for_Star_A > Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            core_accretion_flag_for_Star_A_orbit_16 = "No"
        if core_accretion_flag_for_Star_A_orbit_16 == "TBD":
            core_accretion_flag_for_Star_A_orbit_16 = "Yes"
        if core_accretion_flag_for_Star_A_orbit_16 == "Yes":
            Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A  = (Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + 1)
    
    # "make a note of this number" (pg. 63) - condition is satisified by the parameter "Number_of_Core_Accretiom_Planets_Supported_By_Available_Orbits_for_Star_A"

    # "Now roll 3d6 on the Core Accretion Table, and apply the result to the number of formation orbits counted above. The result is the number of planets that may form due to core
    # accretion, assuming there is sufficient planetesimal mass in the disk"

        roll_for_core_accretion_table_Star_A = _3d6()
        if roll_for_core_accretion_table_Star_A <= 5:
            core_accretion_modifier_Star_A = -2
        if 6 <= roll_for_core_accretion_table_Star_A <= 8:
            core_accretion_modifier_Star_A = -1
        if 9 <= roll_for_core_accretion_table_Star_A <= 12:
            core_accretion_modifier_Star_A = 0
        if 13 <= roll_for_core_accretion_table_Star_A <= 15:
            core_accretion_modifier_Star_A = 1
        if 16 <= roll_for_core_accretion_table_Star_A:
            core_accretion_modifier_Star_A = 2

        Modified_Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A = Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A + core_accretion_modifier_Star_A

    # "The number of planets which form due to core accretion is equal to the number supported by the available planetesimal mass, or the result from the Core Accretion Table, whichever is less." (pg. 63)

        Number_of_Core_Accretion_Planets_Star_A = min(Modified_Number_of_Core_Accretion_Planets_Supported_By_Available_Orbits_for_Star_A, Number_of_Core_Accretion_Planets_Supported_By_Planetismal_Mass_for_Star_A)

        # "Any planets that form during core accretion are likely to migrate inward across the protoplanetary disk, due to interactions between the planet and the mass of the disk. 
        # This sub-step determines how far such migration will carry the young planets. We will refer to the innermost core-accretion planet as the migrating planet" (pg. 63)

        # "Roll 3d6 on the Planetary Migration Table, modifying the roll by adding the disk mass modifier determined in Step Nine. The result is the formation orbit where the migrating planet
        # will arrive after all inward migration takes place" (pg. 64)

        roll_for_planetary_migration_table_Star_A = _3d6()
        if roll_for_planetary_migration_table_Star_A <= 8:
            formation_orbit_after_migration_for_Star_A = 6
            planetismal_mass_factor_for_Star_A = 1.0
        if 9 <= roll_for_planetary_migration_table_Star_A <= 11:
            formation_orbit_after_migration_for_Star_A = 5
            planetismal_mass_factor_for_Star_A = 0.75
        if 12 <= roll_for_planetary_migration_table_Star_A <= 13:
            formation_orbit_after_migration_for_Star_A = 4
            planetismal_mass_factor_for_Star_A = 0.5
        if roll_for_planetary_migration_table_Star_A == 14:
            formation_orbit_after_migration_for_Star_A = 3
            planetismal_mass_factor_for_Star_A = 0.25
        if roll_for_planetary_migration_table_Star_A == 15:
            formation_orbit_after_migration_for_Star_A = 2
            planetismal_mass_factor_for_Star_A = 0.25
        if roll_for_planetary_migration_table_Star_A == 16:
            formation_orbit_after_migration_for_Star_A = 1
            planetismal_mass_factor_for_Star_A = 0.25
        if roll_for_planetary_migration_table_Star_A >= 17:
            formation_orbit_after_migration_for_Star_A = 0
            planetismal_mass_factor_for_Star_A = 0.25

        # "If the result indicates a formation orbit which has been removed from the worksheet due to the special case in Step Nine, then the migrating plant will arrive in formation orbit 0 instead" (pg. 64)
        # need to ADD CODE here

        # "Make a note of the formation orbit where the migrating planet arrives after inward migration." (pg. 64)
        # need to ADD CODE here

        # "Also, make a note of every formation orbit between that one and formation orbit 5, inclusive. You may think of this as the migrating planet appearing in formation orbit 6, then crossing several 
        # other formation orbits on its way inward. All of these orbits should be marked as depleted of planetesimals. In a later step, this may affect the formation of terrestrial planets." (pg. 64)
        # need to ADD CODE here

        # "Make a note of the planetesimal mass factor. This represents the proportion of planetesimals in the inner disk that survive gravitational interaction with the migrating planet, and will also be
        # relevant to the formation of terrestrial planets." (pg. 64)
        # this requirement is met by recording the "planetismal_mass_factor_Star_A" parameter above

        # need to ADD CODE to address the grand track (pg. 64)

        # need to ADD CODE to place core-accretion planets (pg. 64)

    if Number_of_Stars >= 2:
        if formation_orbit_6_for_Star_B < Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 6 around Star B does not lie within a forbidden zone")
            # code here

    if Number_of_Stars >= 3:
        if formation_orbit_6_for_Star_C < Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 6 around Star C does not lie within a forbidden zone")
            # code here

    if Number_of_Stars == 4:
        if formation_orbit_6_for_Star_D < Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 6 around Star D does not lie within a forbidden zone")
            # code here