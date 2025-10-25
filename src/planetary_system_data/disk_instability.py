# this sub-program covers step 10 ("Disk Instability") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

    # "Very early in the process of planetary formation, the first gas giant planets may form due to disk instability in the protoplanetary disk
    # Here, the outer protoplanetary disk is perturbed by the gravitation of nearby stars, or due to the formation of large clumps of material by random chance.
    # The disk then forms spiral-arm structures, which can quickly give rise to unusually massive gas giant planets. Disk instability is more likely to occur if the protoplanetary disk is denser
    # (that is, if its disk mass factor, determined in Step Nine, is high)."

    # "To determine at random whether disk instability took place, roll 3d6 and add the disk mass modifier determined in Step Nine. If the result is 12 or higher, one or more planets may form
    # due to disk instability. Otherwise, skip forward to Step Eleven."

    Disk_Stability_for_Star_A = "TBD"
    if Number_of_Stars >= 1:
        Disk_Stability_for_Star_A = "Stable"
        roll_for_Disk_Stability_Star_A = _3d6()        
        if (roll_for_Disk_Density_of_Star_A + Disk_Mass_Modifier_Star_A) >= 12:
            Disk_Stability_for_Star_A = "Unstable"
            print("Protoplanetary Disk around Star A is unstable - potential for planet formation")

    if Number_of_Stars >= 2:
        Disk_Stability_for_Star_B = "Stable"
        roll_for_Disk_Stability_Star_B = _3d6()
        if (roll_for_Disk_Density_of_Star_B + Disk_Mass_Modifier_Star_B) >= 12:
            Disk_Stability_for_Star_B = "Unstable"
            print("Protoplanetary Disk around Star B is unstable - potential for planet formation")
    if Number_of_Stars < 2:
        Disk_Stability_for_Star_B = "Not Applicable"   

    if Number_of_Stars >= 3:
        Disk_Stability_for_Star_C = "Stable"
        roll_for_Disk_Stability_Star_C = _3d6()        
        if (roll_for_Disk_Density_of_Star_C + Disk_Mass_Modifier_Star_C) >= 12:
            Disk_Stability_for_Star_C = "Unstable"
            print("Protoplanetary Disk around Star C is unstable - potential for planet formation")
    if Number_of_Stars < 3:
        Disk_Stability_for_Star_C = "Not Applicable"   

    if Number_of_Stars == 4:
        Disk_Stability_for_Star_D = "Stable"
        roll_for_Disk_Stability_Star_D = _3d6()        
        if (roll_for_Disk_Density_of_Star_D + Disk_Mass_Modifier_Star_D) >= 12:
            Disk_Stability_for_Star_D = "Unstable"
            print("Protoplanetary Disk around Star D is unstable - potential for planet formation")
    if Number_of_Stars < 4:
        Disk_Stability_for_Star_D = "Not Applicable"   

    if Disk_Stability_for_Star_A == "Unstable":
        # "If disk instability has taken place, roll 3d6 twice on the Disk Instability Placement Table, adding the disk mass modifier each time. The first roll will indicate in which formation orbit
        # the first planet may be placed. The second roll will indicate how many planets may be formed during this step." - pg 61

        # "Check the worksheet to see whether the designated first formation orbit falls within a forbidden zone. If it does, then no planets will form in this step despite the possibility of disk
        # instability; skip forward to Step Eleven" - pg 61

        roll_for_first_formation_orbit_star_A = ( _3d6() + Disk_Mass_Modifier_Star_A )
        if roll_for_first_formation_orbit_star_A <= 5:    
            first_formation_orbit_star_A = 13
            if formation_orbit_13_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_A = "Disk Instability Aborted"
        if 6 <= roll_for_first_formation_orbit_star_A <= 7:
            first_formation_orbit_star_A = 12
            if formation_orbit_12_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_A = "Disk Instability Aborted"
        if 8 <= roll_for_first_formation_orbit_star_A <= 9:
            first_formation_orbit_star_A = 11
            if formation_orbit_11_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_A = "Disk Instability Aborted"
        if 10 <= roll_for_first_formation_orbit_star_A <= 11:
            first_formation_orbit_star_A = 10
            if formation_orbit_10_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_A = "Disk Instability Aborted"
        if 12 <= roll_for_first_formation_orbit_star_A <= 13:
            first_formation_orbit_star_A = 9
            if formation_orbit_9_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_A = "Disk Instability Aborted"
        if 14 <= roll_for_first_formation_orbit_star_A <= 15:
            first_formation_orbit_star_A = 8
            if formation_orbit_8_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_A = "Disk Instability Aborted"
        if roll_for_first_formation_orbit_star_A >= 16:
            first_formation_orbit_star_A = 7
            if formation_orbit_7_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_A = "Disk Instability Aborted"
        
        if Disk_Stability_for_Star_A == "Unstable":
            roll_for_number_of_planets_formed_by_disk_instability_star_A = ( _3d6() + Disk_Mass_Modifier_Star_A )
            if roll_for_number_of_planets_formed_by_disk_instability_star_A <= 11:
                number_of_planets_formed_by_disk_instability_star_A = 1
            if 12 <= roll_for_number_of_planets_formed_by_disk_instability_star_A <= 13:
                number_of_planets_formed_by_disk_instability_star_A = 2
            if 14 <= roll_for_number_of_planets_formed_by_disk_instability_star_A <= 15:
                number_of_planets_formed_by_disk_instability_star_A = 3
            if roll_for_number_of_planets_formed_by_disk_instability_star_A >= 16:
                number_of_planets_formed_by_disk_instability_star_A = 4

        # "Otherwise, start with that formation orbit and place a planet on the worksheet in each formation orbit outward, until either: All the required planets have been placed, or
        # the next formation orbit falls into a forbidden zone" - pg. 61

            if number_of_planets_formed_by_disk_instability_star_A >= 1:
                if first_formation_orbit_star_A == 7:
                    Star_A_Protoplanet_7_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 8:
                    Star_A_Protoplanet_8_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 9:
                    Star_A_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 10:
                    Star_A_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 11:
                    Star_A_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 12:
                    Star_A_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 13:
                    Star_A_Protoplanet_13_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_star_A >= 2:
                if first_formation_orbit_star_A == 7:
                    if formation_orbit_8_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_8_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 8:
                    if formation_orbit_9_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 9:
                    if formation_orbit_10_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 10:
                    if formation_orbit_11_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 11:
                    if formation_orbit_12_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 12:
                    if formation_orbit_13_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 13:
                    if formation_orbit_14_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_14_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_star_A >= 3:
                if first_formation_orbit_star_A == 7:
                    if formation_orbit_9_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 8:
                    if formation_orbit_10_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 9:
                    if formation_orbit_11_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 10:
                    if formation_orbit_12_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 11:
                    if formation_orbit_13_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 12:
                    if formation_orbit_14_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_14_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 13:
                    if formation_orbit_15_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_15_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_star_A == 4:
                if first_formation_orbit_star_A == 7:
                    if formation_orbit_10_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 8:
                    if formation_orbit_11_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 9:
                    if formation_orbit_12_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 10:
                    if formation_orbit_13_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 11:
                    if formation_orbit_14_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_14_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 12:
                    if formation_orbit_15_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_15_Flag = "Disk Instability Planet"
                if first_formation_orbit_star_A == 13:
                    if formation_orbit_16_for_Star_A <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
                        Star_A_Protoplanet_16_Flag = "Disk Instability Planet"

    if Disk_Stability_for_Star_B == "Unstable":
        # "If disk instability has taken place, roll 3d6 twice on the Disk Instability Placement Table, adding the disk mass modifier each time. The first roll will indicate in which formation orbit
        # the first planet may be placed. The second roll will indicate how many planets may be formed during this step." - pg 61

        # "Check the worksheet to see whether the designated first formation orbit falls within a forbidden zone. If it does, then no planets will form in this step despite the possibility of disk
        # instability; skip forward to Step Eleven" - pg 61

        roll_for_first_formation_orbit_Star_B = ( _3d6() + Disk_Mass_Modifier_Star_B )
        if roll_for_first_formation_orbit_Star_B <= 5:    
            first_formation_orbit_Star_B = 13
            if formation_orbit_13_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_B = "Disk Instability Aborted"
        if 6 <= roll_for_first_formation_orbit_Star_B <= 7:
            first_formation_orbit_Star_B = 12
            if formation_orbit_12_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_B = "Disk Instability Aborted"
        if 8 <= roll_for_first_formation_orbit_Star_B <= 9:
            first_formation_orbit_Star_B = 11
            if formation_orbit_11_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_B = "Disk Instability Aborted"
        if 10 <= roll_for_first_formation_orbit_Star_B <= 11:
            first_formation_orbit_Star_B = 10
            if formation_orbit_10_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_B = "Disk Instability Aborted"
        if 12 <= roll_for_first_formation_orbit_Star_B <= 13:
            first_formation_orbit_Star_B = 9
            if formation_orbit_9_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_B = "Disk Instability Aborted"
        if 14 <= roll_for_first_formation_orbit_Star_B <= 15:
            first_formation_orbit_Star_B = 8
            if formation_orbit_8_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_B = "Disk Instability Aborted"
        if roll_for_first_formation_orbit_Star_B >= 16:
            first_formation_orbit_Star_B = 7
            if formation_orbit_7_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_B = "Disk Instability Aborted"
        
        if Disk_Stability_for_Star_B == "Unstable":
            roll_for_number_of_planets_formed_by_disk_instability_Star_B = ( _3d6() + Disk_Mass_Modifier_Star_B )
            if roll_for_number_of_planets_formed_by_disk_instability_Star_B <= 11:
                number_of_planets_formed_by_disk_instability_Star_B = 1
            if 12 <= roll_for_number_of_planets_formed_by_disk_instability_Star_B <= 13:
                number_of_planets_formed_by_disk_instability_Star_B = 2
            if 14 <= roll_for_number_of_planets_formed_by_disk_instability_Star_B <= 15:
                number_of_planets_formed_by_disk_instability_Star_B = 3
            if roll_for_number_of_planets_formed_by_disk_instability_Star_B >= 16:
                number_of_planets_formed_by_disk_instability_Star_B = 4

        # "Otherwise, start with that formation orbit and place a planet on the worksheet in each formation orbit outward, until either: All the required planets have been placed, or
        # the next formation orbit falls into a forbidden zone" - pg. 61

            if number_of_planets_formed_by_disk_instability_Star_B >= 1:
                if first_formation_orbit_Star_B == 7:
                    Star_B_Protoplanet_7_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 8:
                    Star_B_Protoplanet_8_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 9:
                    Star_B_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 10:
                    Star_B_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 11:
                    Star_B_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 12:
                    Star_B_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 13:
                    Star_B_Protoplanet_13_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_Star_B >= 2:
                if first_formation_orbit_Star_B == 7:
                    if formation_orbit_8_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_8_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 8:
                    if formation_orbit_9_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 9:
                    if formation_orbit_10_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 10:
                    if formation_orbit_11_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 11:
                    if formation_orbit_12_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 12:
                    if formation_orbit_13_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 13:
                    if formation_orbit_14_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_14_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_Star_B >= 3:
                if first_formation_orbit_Star_B == 7:
                    if formation_orbit_9_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 8:
                    if formation_orbit_10_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 9:
                    if formation_orbit_11_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 10:
                    if formation_orbit_12_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 11:
                    if formation_orbit_13_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 12:
                    if formation_orbit_14_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_14_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 13:
                    if formation_orbit_15_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_15_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_Star_B == 4:
                if first_formation_orbit_Star_B == 7:
                    if formation_orbit_10_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 8:
                    if formation_orbit_11_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 9:
                    if formation_orbit_12_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 10:
                    if formation_orbit_13_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 11:
                    if formation_orbit_14_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_14_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 12:
                    if formation_orbit_15_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_15_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_B == 13:
                    if formation_orbit_16_for_Star_B <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
                        Star_B_Protoplanet_16_Flag = "Disk Instability Planet"

    if Disk_Stability_for_Star_C == "Unstable":
        # "If disk instability has taken place, roll 3d6 twice on the Disk Instability Placement Table, adding the disk mass modifier each time. The first roll will indicate in which formation orbit
        # the first planet may be placed. The second roll will indicate how many planets may be formed during this step." - pg 61

        # "Check the worksheet to see whether the designated first formation orbit falls within a forbidden zone. If it does, then no planets will form in this step despite the possibility of disk
        # instability; skip forward to Step Eleven" - pg 61

        roll_for_first_formation_orbit_Star_C = ( _3d6() + Disk_Mass_Modifier_Star_C )
        if roll_for_first_formation_orbit_Star_C <= 5:    
            first_formation_orbit_Star_C = 13
            if formation_orbit_13_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_C = "Disk Instability Aborted"
        if 6 <= roll_for_first_formation_orbit_Star_C <= 7:
            first_formation_orbit_Star_C = 12
            if formation_orbit_12_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_C = "Disk Instability Aborted"
        if 8 <= roll_for_first_formation_orbit_Star_C <= 9:
            first_formation_orbit_Star_C = 11
            if formation_orbit_11_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_C = "Disk Instability Aborted"
        if 10 <= roll_for_first_formation_orbit_Star_C <= 11:
            first_formation_orbit_Star_C = 10
            if formation_orbit_10_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_C = "Disk Instability Aborted"
        if 12 <= roll_for_first_formation_orbit_Star_C <= 13:
            first_formation_orbit_Star_C = 9
            if formation_orbit_9_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_C = "Disk Instability Aborted"
        if 14 <= roll_for_first_formation_orbit_Star_C <= 15:
            first_formation_orbit_Star_C = 8
            if formation_orbit_8_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_C = "Disk Instability Aborted"
        if roll_for_first_formation_orbit_Star_C >= 16:
            first_formation_orbit_Star_C = 7
            if formation_orbit_7_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_C = "Disk Instability Aborted"
        
        if Disk_Stability_for_Star_C == "Unstable":
            roll_for_number_of_planets_formed_by_disk_instability_Star_C = ( _3d6() + Disk_Mass_Modifier_Star_C )
            if roll_for_number_of_planets_formed_by_disk_instability_Star_C <= 11:
                number_of_planets_formed_by_disk_instability_Star_C = 1
            if 12 <= roll_for_number_of_planets_formed_by_disk_instability_Star_C <= 13:
                number_of_planets_formed_by_disk_instability_Star_C = 2
            if 14 <= roll_for_number_of_planets_formed_by_disk_instability_Star_C <= 15:
                number_of_planets_formed_by_disk_instability_Star_C = 3
            if roll_for_number_of_planets_formed_by_disk_instability_Star_C >= 16:
                number_of_planets_formed_by_disk_instability_Star_C = 4

        # "Otherwise, start with that formation orbit and place a planet on the worksheet in each formation orbit outward, until either: All the required planets have been placed, or
        # the next formation orbit falls into a forbidden zone" - pg. 61

            if number_of_planets_formed_by_disk_instability_Star_C >= 1:
                if first_formation_orbit_Star_C == 7:
                    Star_C_Protoplanet_7_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 8:
                    Star_C_Protoplanet_8_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 9:
                    Star_C_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 10:
                    Star_C_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 11:
                    Star_C_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 12:
                    Star_C_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 13:
                    Star_C_Protoplanet_13_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_Star_C >= 2:
                if first_formation_orbit_Star_C == 7:
                    if formation_orbit_8_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_8_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 8:
                    if formation_orbit_9_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 9:
                    if formation_orbit_10_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 10:
                    if formation_orbit_11_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 11:
                    if formation_orbit_12_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 12:
                    if formation_orbit_13_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 13:
                    if formation_orbit_14_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_14_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_Star_C >= 3:
                if first_formation_orbit_Star_C == 7:
                    if formation_orbit_9_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 8:
                    if formation_orbit_10_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 9:
                    if formation_orbit_11_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 10:
                    if formation_orbit_12_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 11:
                    if formation_orbit_13_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 12:
                    if formation_orbit_14_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_14_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 13:
                    if formation_orbit_15_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_15_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_Star_C == 4:
                if first_formation_orbit_Star_C == 7:
                    if formation_orbit_10_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 8:
                    if formation_orbit_11_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 9:
                    if formation_orbit_12_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 10:
                    if formation_orbit_13_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 11:
                    if formation_orbit_14_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_14_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 12:
                    if formation_orbit_15_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_15_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_C == 13:
                    if formation_orbit_16_for_Star_C <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
                        Star_C_Protoplanet_16_Flag = "Disk Instability Planet"

    if Disk_Stability_for_Star_D == "Unstable":
        # "If disk instability has taken place, roll 3d6 twice on the Disk Instability Placement Table, adding the disk mass modifier each time. The first roll will indicate in which formation orbit
        # the first planet may be placed. The second roll will indicate how many planets may be formed during this step." - pg 61

        # "Check the worksheet to see whether the designated first formation orbit falls within a forbidden zone. If it does, then no planets will form in this step despite the possibility of disk
        # instability; skip forward to Step Eleven" - pg 61

        roll_for_first_formation_orbit_Star_D = ( _3d6() + Disk_Mass_Modifier_Star_D )
        if roll_for_first_formation_orbit_Star_D <= 5:    
            first_formation_orbit_Star_D = 13
            if formation_orbit_13_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_D = "Disk Instability Aborted"
        if 6 <= roll_for_first_formation_orbit_Star_D <= 7:
            first_formation_orbit_Star_D = 12
            if formation_orbit_12_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_D = "Disk Instability Aborted"
        if 8 <= roll_for_first_formation_orbit_Star_D <= 9:
            first_formation_orbit_Star_D = 11
            if formation_orbit_11_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_D = "Disk Instability Aborted"
        if 10 <= roll_for_first_formation_orbit_Star_D <= 11:
            first_formation_orbit_Star_D = 10
            if formation_orbit_10_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_D = "Disk Instability Aborted"
        if 12 <= roll_for_first_formation_orbit_Star_D <= 13:
            first_formation_orbit_Star_D = 9
            if formation_orbit_9_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_D = "Disk Instability Aborted"
        if 14 <= roll_for_first_formation_orbit_Star_D <= 15:
            first_formation_orbit_Star_D = 8
            if formation_orbit_8_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_D = "Disk Instability Aborted"
        if roll_for_first_formation_orbit_Star_D >= 16:
            first_formation_orbit_Star_D = 7
            if formation_orbit_7_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                print("no planets form around Star A due to disk instability - potential planet formation was in the forbidden zone")
                Disk_Stability_for_Star_D = "Disk Instability Aborted"
        
        if Disk_Stability_for_Star_D == "Unstable":
            roll_for_number_of_planets_formed_by_disk_instability_Star_D = ( _3d6() + Disk_Mass_Modifier_Star_D )
            if roll_for_number_of_planets_formed_by_disk_instability_Star_D <= 11:
                number_of_planets_formed_by_disk_instability_Star_D = 1
            if 12 <= roll_for_number_of_planets_formed_by_disk_instability_Star_D <= 13:
                number_of_planets_formed_by_disk_instability_Star_D = 2
            if 14 <= roll_for_number_of_planets_formed_by_disk_instability_Star_D <= 15:
                number_of_planets_formed_by_disk_instability_Star_D = 3
            if roll_for_number_of_planets_formed_by_disk_instability_Star_D >= 16:
                number_of_planets_formed_by_disk_instability_Star_D = 4

        # "Otherwise, start with that formation orbit and place a planet on the worksheet in each formation orbit outward, until either: All the required planets have been placed, or
        # the next formation orbit falls into a forbidden zone" - pg. 61

            if number_of_planets_formed_by_disk_instability_Star_D >= 1:
                if first_formation_orbit_Star_D == 7:
                    Star_D_Protoplanet_7_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 8:
                    Star_D_Protoplanet_8_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 9:
                    Star_D_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 10:
                    Star_D_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 11:
                    Star_D_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 12:
                    Star_D_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 13:
                    Star_D_Protoplanet_13_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_Star_D >= 2:
                if first_formation_orbit_Star_D == 7:
                    if formation_orbit_8_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_8_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 8:
                    if formation_orbit_9_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 9:
                    if formation_orbit_10_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 10:
                    if formation_orbit_11_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 11:
                    if formation_orbit_12_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 12:
                    if formation_orbit_13_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 13:
                    if formation_orbit_14_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_14_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_Star_D >= 3:
                if first_formation_orbit_Star_D == 7:
                    if formation_orbit_9_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_9_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 8:
                    if formation_orbit_10_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 9:
                    if formation_orbit_11_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 10:
                    if formation_orbit_12_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 11:
                    if formation_orbit_13_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 12:
                    if formation_orbit_14_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_14_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 13:
                    if formation_orbit_15_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_15_Flag = "Disk Instability Planet"

            if number_of_planets_formed_by_disk_instability_Star_D == 4:
                if first_formation_orbit_Star_D == 7:
                    if formation_orbit_10_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_10_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 8:
                    if formation_orbit_11_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_11_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 9:
                    if formation_orbit_12_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_12_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 10:
                    if formation_orbit_13_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_13_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 11:
                    if formation_orbit_14_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_14_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 12:
                    if formation_orbit_15_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_15_Flag = "Disk Instability Planet"
                if first_formation_orbit_Star_D == 13:
                    if formation_orbit_16_for_Star_D <= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
                        Star_D_Protoplanet_16_Flag = "Disk Instability Planet"
