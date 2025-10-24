# this sub-program covers step 7 ("Stellar Classification") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

Spectral_Type_of_Star_A = "None"
if Number_of_Stars >= 1:
    if Evolutionary_Stage_of_Star_A == "White Dwarf":
        Spectral_Type_of_Star_A = "D"
    if Evolutionary_Stage_of_Star_A != "White Dwarf":
        if Temperature_Effective_of_Star_A >= 16500:
            Spectral_Type_of_Star_A = "B3"
            #median temperature of 17000 Kelvin
        if 15500 <= Temperature_Effective_of_Star_A < 16500:
            Spectral_Type_of_Star_A = "B4"
            #median temperature of 16000 Kelvin
        if 14500 <= Temperature_Effective_of_Star_A < 15500:
            Spectral_Type_of_Star_A = "B5"
            #median temeperature of 15000 Kelvin
        if 13500 <= Temperature_Effective_of_Star_A < 14500:
            Spectral_Type_of_Star_A = "B6"
            #median temperature of 14000 Kelvin
        if ((11900+13000)/2) <= Temperature_Effective_of_Star_A < ((13000+14000)/2):
            Spectral_Type_of_Star_A = "B7"
            #median temperature of 13000 Kelvin
        if ((10800+11900)/2) <= Temperature_Effective_of_Star_A < ((11900+13000)/2):
            Spectral_Type_of_Star_A = "B8"
            #median temperature of 11900 Kelvin
        if ((9700+10800)/2) <= Temperature_Effective_of_Star_A < ((10800+11900)/2):
            Spectral_Type_of_Star_A = "B9"
            #median temperature of 10800
        if ((9450+9700)/2) <= Temperature_Effective_of_Star_A < ((9700+10800)/2):
            Spectral_Type_of_Star_A = "A0"
            #median temperaure of 9700
        if ((9200+9450)/2) <= Temperature_Effective_of_Star_A < ((9450+9700)/2):
            Spectral_Type_of_Star_A = "A1"
            #mediuam temperature of 9450
        if ((8950+9200)/2) <= Temperature_Effective_of_Star_A < ((9200+9450)/2):
            Spectral_Type_of_Star_A = "A2"
            #median temperature of 9200 Kelvin
        if ((8700+8950)/2) <= Temperature_Effective_of_Star_A < ((8950+9200)/2):
            Spectral_Type_of_Star_A = "A3"
            #median temperature of 8950 Kelvin
        if ((8450+8700)/2) <= Temperature_Effective_of_Star_A < ((8700+8950)/2):
            Spectral_Type_of_Star_A = "A4"
            #median temperature of 8700 Kelvin
        if ((8200+8450)/2) <= Temperature_Effective_of_Star_A < ((8450+8700)/2):
            Spectral_Type_of_Star_A = "A5"
            #median temperature of 8450 Kelvin
        if ((7950+8200)/2) <= Temperature_Effective_of_Star_A < ((8200+8450)/2):
            Spectral_Type_of_Star_A = "A6"
            #median temperature of 8200 Kelvin
        if ((7700+7950)/2) <= Temperature_Effective_of_Star_A < ((7950+8200)/2):
            Spectral_Type_of_Star_A = "A7"
            #median temperature of 7950 Kelvin
        if ((7460+7700)/2) <= Temperature_Effective_of_Star_A < ((7700+7950)/2):
            Spectral_Type_of_Star_A = "A8"
            #median temperature of 7700 Kelvin
        if ((7220+7460)/2) <= Temperature_Effective_of_Star_A < ((7460+7700)/2):
            Spectral_Type_of_Star_A = "A9"
            #median temperature of 7460 Kelvin
        if ((7090+7220)/2) <= Temperature_Effective_of_Star_A < ((7720+7460)/2):
            Spectral_Type_of_Star_A = "F0"
            #median temperature of 7220 Kelvin
        if ((6890+7090)/2) <= Temperature_Effective_of_Star_A < ((7090+7220)/2):
            Spectral_Type_of_Star_A = "F1"
            #median temperature of 7090 Kelvin
        if ((6760+6890)/2) <= Temperature_Effective_of_Star_A < ((6890+7090)/2):
            Spectral_Type_of_Star_A = "F2"
            #median temperature of 6890 Kelvin
        if ((6630+6760)/2) <= Temperature_Effective_of_Star_A < ((6760+6890)/2):
            Spectral_Type_of_Star_A = "F3"
            #median temperature of 6760 Kelvin
        if ((6500+6630)/2) <= Temperature_Effective_of_Star_A < ((6630+6760)/2):
            Spectral_Type_of_Star_A = "F4"
            #median temperature of 6630 Kelvin
        if ((6370+6500)/2) <= Temperature_Effective_of_Star_A < ((6500+6630)/2):
            Spectral_Type_of_Star_A = "F5"
            #median temperature of 6500 Kelvin
        if ((6240+6370)/2) <= Temperature_Effective_of_Star_A < ((6370+6500)/2):
            Spectral_Type_of_Star_A = "F6"
            #median temperature of 6370 Kelvin
        if ((6110+6240)/2) <= Temperature_Effective_of_Star_A < ((6240+6370)/2):
            Spectral_Type_of_Star_A = "F7"
            #median temperature of 6240 Kelvin
        if ((6020+6110)/2) <= Temperature_Effective_of_Star_A < ((6110+6240)/2):
            Spectral_Type_of_Star_A = "F8"
            #median temperature of 6110 Kelvin
        if ((5930+6020)/2) <= Temperature_Effective_of_Star_A < ((6020+6110)/2):
            Spectral_Type_of_Star_A = "F9"
            #median temperature of 6020 Kelvin
        if ((5850+5930)/2) <= Temperature_Effective_of_Star_A < ((5930+6020)/2):
            Spectral_Type_of_Star_A = "G0"
            #median temperature of 5930 Kelvin
        if ((5770+5850)/2) <= Temperature_Effective_of_Star_A < ((5850+5930)/2):
            Spectral_Type_of_Star_A = "G1"
            #median temperature of 5850 Kelvin
        if ((5700+5770)/2) <= Temperature_Effective_of_Star_A < ((5770+5850)/2):
            Spectral_Type_of_Star_A = "G2"
            #median temperature of 5770 Kelvin
        if ((5630+5700)/2) <= Temperature_Effective_of_Star_A < ((5700+5770)/2):
            Spectral_Type_of_Star_A = "G3"
            #median temperature of 5700 Kelvin
        if ((5570+5630)/2) <= Temperature_Effective_of_Star_A < ((5630+5700)/2):
            Spectral_Type_of_Star_A = "G4"
            #median temperature of 5630 Kelvin
        if ((5510+5570)/2) <= Temperature_Effective_of_Star_A < ((5570+5630)/2):
            Spectral_Type_of_Star_A = "G5"
            #median temperature of 5570 Kelvin
        if ((5450+5510)/2) <= Temperature_Effective_of_Star_A < ((5510+5570)/2):
            Spectral_Type_of_Star_A = "G6"
            #median temperature of 5510 Kelvin
        if ((5390+5450)/2) <= Temperature_Effective_of_Star_A < ((5450+5510)/2):
            Spectral_Type_of_Star_A = "G7"
            #median temperature of 5450 Kelvin
        if ((5330+5390)/2) <= Temperature_Effective_of_Star_A < ((5390+5450)/2):
            Spectral_Type_of_Star_A = "G8"
            #median temperature of 5390 Kelvin
        if ((5270+5330)/2) <= Temperature_Effective_of_Star_A < ((5330+5390)/2):
            Spectral_Type_of_Star_A = "G9"
            #median temperature of 5330 Kelvin
        if ((5130+5270)/2) <= Temperature_Effective_of_Star_A < ((5270+5330)/2):
            Spectral_Type_of_Star_A = "K0"
            #median temperature of 5270 Kelvin
        if ((4990+5130)/2) <= Temperature_Effective_of_Star_A < ((5130+5270)/2):
            Spectral_Type_of_Star_A = "K1"
            #median temperature of 5130 Kelvin
        if ((4850+4990)/2) <= Temperature_Effective_of_Star_A < ((4990+5130)/2):
            Spectral_Type_of_Star_A = "K2"
            #median temperature of 4990 Kelvin
        if ((4710+4850)/2) <= Temperature_Effective_of_Star_A < ((4850+4990)/2):
            Spectral_Type_of_Star_A = "K3"
            #median temperature of 4850 Kelvin
        if ((4560+4710)/2) <= Temperature_Effective_of_Star_A < ((4710+4850)/2):
            Spectral_Type_of_Star_A = "K4"
            #median temperature of 4710 Kelvin
        if ((4410+4560)/2) <= Temperature_Effective_of_Star_A < ((4560+4710)/2):
            Spectral_Type_of_Star_A = "K5"
            #median temperature of 4560 Kelvin
        if ((4270+4410)/2) <= Temperature_Effective_of_Star_A < ((4410+4560)/2):
            Spectral_Type_of_Star_A = "K6"
            #median temperature of 4410 Kelvin
        if ((4130+4270)/2) <= Temperature_Effective_of_Star_A < ((4270+4410)/2):
            Spectral_Type_of_Star_A = "K7"
            #median temperature of 4270 Kelvin
        if ((3990+4130)/2) <= Temperature_Effective_of_Star_A < ((4130+4270)/2):
            Spectral_Type_of_Star_A = "K8"
            #median temperature of 4130 Kelvin
        if ((3850+3990)/2) <= Temperature_Effective_of_Star_A < ((3990+4130)/2):
            Spectral_Type_of_Star_A = "K9"
            #median temperature of 3990 Kelvin
        if ((3700+3850)/2) <= Temperature_Effective_of_Star_A < ((3850+3990)/2):
            Spectral_Type_of_Star_A = "M0"
            #median temperature of 3850 Kelvin
        if ((3540+3700)/2) <= Temperature_Effective_of_Star_A < ((3700+3850)/2):
            Spectral_Type_of_Star_A = "M1"
            #median temperature of 3700 Kelvin
        if ((3380+3540)/2) <= Temperature_Effective_of_Star_A < ((3540+3700)/2):
            Spectral_Type_of_Star_A = "M2"
            #median temperature of 3540 Kelvin
        if ((3220+3380)/2) <= Temperature_Effective_of_Star_A < ((3380+3540)/2):
            Spectral_Type_of_Star_A = "M3"
            #median temperature of 3380 Kelvin
        if ((3060+3220)/2) <= Temperature_Effective_of_Star_A < ((3220+3380)/2):
            Spectral_Type_of_Star_A = "M4"
            #median temperature of 3220 Kelvin
        if ((2900+3060)/2) <= Temperature_Effective_of_Star_A < ((3060+3220)/2):
            Spectral_Type_of_Star_A = "M5"
            #median temperature of 3060 Kelvin
        if ((2740+2900)/2) <= Temperature_Effective_of_Star_A < ((2900+3060)/2):
            Spectral_Type_of_Star_A = "M6"
            #median temperature of 2900 Kelvin
        if ((2580+2740)/2) <= Temperature_Effective_of_Star_A < ((2740+2900)/2):
            Spectral_Type_of_Star_A = "M7"
            #median temperature of 2740 Kelvin
        if ((2420+2580)/2) <= Temperature_Effective_of_Star_A < ((2580+2740)/2):
            Spectral_Type_of_Star_A = "M8"
            #median temperature of 2580 Kelvin
        if ((2270+2420)/2) <= Temperature_Effective_of_Star_A < ((2420+2580)/2):
            Spectral_Type_of_Star_A = "M9"
            #median temperature of 2420 Kelvin
        if ((2170+2270)/2) <= Temperature_Effective_of_Star_A < ((2270+2420)/2):
            Spectral_Type_of_Star_A = "L0"
            #median temperature of 2270 Kelvin
        if ((2070+2170)/2) <= Temperature_Effective_of_Star_A < ((2170+2270)/2):
            Spectral_Type_of_Star_A = "L1"
            #median temperature of 2170 Kelvin
        if ((1970+2070)/2) <= Temperature_Effective_of_Star_A < ((2070+2170)/2):
            Spectral_Type_of_Star_A = "L2"
            #median temperature of 2070 Kelvin
        if ((1870+1970)/2) <= Temperature_Effective_of_Star_A < ((1970+2070)/2):
            Spectral_Type_of_Star_A = "L3"
            #median temperature of 1970 Kelvin
        if ((1770+1870)/2) <= Temperature_Effective_of_Star_A < ((1870+1970)/2):
            Spectral_Type_of_Star_A = "L4"
            #median temperature of 1870 Kelvin
        if ((1660+1770)/2) <= Temperature_Effective_of_Star_A < ((1770+1870)/2):
            Spectral_Type_of_Star_A = "L5"
            #median temperature of 1770 Kelvin
        if ((1560+1660)/2) <= Temperature_Effective_of_Star_A < ((1660+1770)/2):
            Spectral_Type_of_Star_A = "L6"
            #median temperature of 1660 Kelvin
        if ((1460+1560)/2) <= Temperature_Effective_of_Star_A < ((1560+1660)/2):
            Spectral_Type_of_Star_A = "L7"
            #median temperature of 1560 Kelvin
        if ((1360+1460)/2) <= Temperature_Effective_of_Star_A < ((1460+1560)/2):
            Spectral_Type_of_Star_A = "L8"
            #median temperature of 1460 Kelvin
        if ((1260+1360)/2) <= Temperature_Effective_of_Star_A < ((1360+1460)/2):
            Spectral_Type_of_Star_A = "L9"
            #median temperature of 1360 Kelvin
        if ((1190+1260)/2) <= Temperature_Effective_of_Star_A < ((1260+1360)/2):
            Spectral_Type_of_Star_A = "T0"
            #median temperature of 1260 Kelvin
        if ((1120+1190)/2) <= Temperature_Effective_of_Star_A < ((1190+1260)/2):
            Spectral_Type_of_Star_A = "T1"
            #median temperature of 1190 Kelvin
        if ((1040+1120)/2) <= Temperature_Effective_of_Star_A < ((1120+1190)/2):
            Spectral_Type_of_Star_A = "T2"
            #median temperature of 1120 Kelvin
        if ((960+1040)/2) <= Temperature_Effective_of_Star_A < ((1040+1120)/2):
            Spectral_Type_of_Star_A = "T3"
            #median temperature of 1040 Kelvin
        if ((880+960)/2) <= Temperature_Effective_of_Star_A < ((960+1040)/2):
            Spectral_Type_of_Star_A = "T4"
            #median temperature of 960 Kelvin
        if ((800+880)/2) <= Temperature_Effective_of_Star_A < ((880+960)/2):
            Spectral_Type_of_Star_A = "T5"
            #median temperature of 880 Kelvin
        if ((720+800)/2) <= Temperature_Effective_of_Star_A < ((800+880)/2):
            Spectral_Type_of_Star_A = "T6"
            #median temperature of 800 Kelvin
        if ((640+720)/2) <= Temperature_Effective_of_Star_A < ((720+800)/2):
            Spectral_Type_of_Star_A = "T7"
            #median temperature of 720 Kelvin
        if ((570+640)/2) <= Temperature_Effective_of_Star_A < ((640+720)/2):
            Spectral_Type_of_Star_A = "T8"
            #median temperature of 640 Kelvin
        if ((500+570)/2) <= Temperature_Effective_of_Star_A < ((570+640)/2):
            Spectral_Type_of_Star_A = "T9"
            #median temperature of 570 Kelvin
        if Temperature_Effective_of_Star_A < ((500+570)/2):
            Spectral_Type_of_Star_A = "Y0"
    print(f"Spectral Type of Star A: {Spectral_Type_of_Star_A}")

Spectral_Type_of_Star_B = "None"
if Number_of_Stars >= 2:
    Spectral_Type_of_Star_B = "None"
    if Evolutionary_Stage_of_Star_B == "White Dwarf":
        Spectral_Type_of_Star_B = "D"
    if Evolutionary_Stage_of_Star_B != "White Dwarf":
        if Temperature_Effective_of_Star_B >= 16500:
            Spectral_Type_of_Star_B = "B3"
            #median temperature of 17000 Kelvin
        if 15500 <= Temperature_Effective_of_Star_B < 16500:
            Spectral_Type_of_Star_B = "B4"
            #median temperature of 16000 Kelvin
        if 14500 <= Temperature_Effective_of_Star_B < 15500:
            Spectral_Type_of_Star_B = "B5"
            #median temeperature of 15000 Kelvin
        if 13500 <= Temperature_Effective_of_Star_B < 14500:
            Spectral_Type_of_Star_B = "B6"
            #median temperature of 14000 Kelvin
        if ((11900+13000)/2) <= Temperature_Effective_of_Star_B < ((13000+14000)/2):
            Spectral_Type_of_Star_B = "B7"
            #median temperature of 13000 Kelvin
        if ((10800+11900)/2) <= Temperature_Effective_of_Star_B < ((11900+13000)/2):
            Spectral_Type_of_Star_B = "B8"
            #median temperature of 11900 Kelvin
        if ((9700+10800)/2) <= Temperature_Effective_of_Star_B < ((10800+11900)/2):
            Spectral_Type_of_Star_B = "B9"
            #median temperature of 10800
        if ((9450+9700)/2) <= Temperature_Effective_of_Star_B < ((9700+10800)/2):
            Spectral_Type_of_Star_B = "A0"
            #median temperaure of 9700
        if ((9200+9450)/2) <= Temperature_Effective_of_Star_B < ((9450+9700)/2):
            Spectral_Type_of_Star_B = "A1"
            #mediuam temperature of 9450
        if ((8950+9200)/2) <= Temperature_Effective_of_Star_B < ((9200+9450)/2):
            Spectral_Type_of_Star_B = "A2"
            #median temperature of 9200 Kelvin
        if ((8700+8950)/2) <= Temperature_Effective_of_Star_B < ((8950+9200)/2):
            Spectral_Type_of_Star_B = "A3"
            #median temperature of 8950 Kelvin
        if ((8450+8700)/2) <= Temperature_Effective_of_Star_B < ((8700+8950)/2):
            Spectral_Type_of_Star_B = "A4"
            #median temperature of 8700 Kelvin
        if ((8200+8450)/2) <= Temperature_Effective_of_Star_B < ((8450+8700)/2):
            Spectral_Type_of_Star_B = "A5"
            #median temperature of 8450 Kelvin
        if ((7950+8200)/2) <= Temperature_Effective_of_Star_B < ((8200+8450)/2):
            Spectral_Type_of_Star_B = "A6"
            #median temperature of 8200 Kelvin
        if ((7700+7950)/2) <= Temperature_Effective_of_Star_B < ((7950+8200)/2):
            Spectral_Type_of_Star_B = "A7"
            #median temperature of 7950 Kelvin
        if ((7460+7700)/2) <= Temperature_Effective_of_Star_B < ((7700+7950)/2):
            Spectral_Type_of_Star_B = "A8"
            #median temperature of 7700 Kelvin
        if ((7220+7460)/2) <= Temperature_Effective_of_Star_B < ((7460+7700)/2):
            Spectral_Type_of_Star_B = "A9"
            #median temperature of 7460 Kelvin
        if ((7090+7220)/2) <= Temperature_Effective_of_Star_B < ((7720+7460)/2):
            Spectral_Type_of_Star_B = "F0"
            #median temperature of 7220 Kelvin
        if ((6890+7090)/2) <= Temperature_Effective_of_Star_B < ((7090+7220)/2):
            Spectral_Type_of_Star_B = "F1"
            #median temperature of 7090 Kelvin
        if ((6760+6890)/2) <= Temperature_Effective_of_Star_B < ((6890+7090)/2):
            Spectral_Type_of_Star_B = "F2"
            #median temperature of 6890 Kelvin
        if ((6630+6760)/2) <= Temperature_Effective_of_Star_B < ((6760+6890)/2):
            Spectral_Type_of_Star_B = "F3"
            #median temperature of 6760 Kelvin
        if ((6500+6630)/2) <= Temperature_Effective_of_Star_B < ((6630+6760)/2):
            Spectral_Type_of_Star_B = "F4"
            #median temperature of 6630 Kelvin
        if ((6370+6500)/2) <= Temperature_Effective_of_Star_B < ((6500+6630)/2):
            Spectral_Type_of_Star_B = "F5"
            #median temperature of 6500 Kelvin
        if ((6240+6370)/2) <= Temperature_Effective_of_Star_B < ((6370+6500)/2):
            Spectral_Type_of_Star_B = "F6"
            #median temperature of 6370 Kelvin
        if ((6110+6240)/2) <= Temperature_Effective_of_Star_B < ((6240+6370)/2):
            Spectral_Type_of_Star_B = "F7"
            #median temperature of 6240 Kelvin
        if ((6020+6110)/2) <= Temperature_Effective_of_Star_B < ((6110+6240)/2):
            Spectral_Type_of_Star_B = "F8"
            #median temperature of 6110 Kelvin
        if ((5930+6020)/2) <= Temperature_Effective_of_Star_B < ((6020+6110)/2):
            Spectral_Type_of_Star_B = "F9"
            #median temperature of 6020 Kelvin
        if ((5850+5930)/2) <= Temperature_Effective_of_Star_B < ((5930+6020)/2):
            Spectral_Type_of_Star_B = "G0"
            #median temperature of 5930 Kelvin
        if ((5770+5850)/2) <= Temperature_Effective_of_Star_B < ((5850+5930)/2):
            Spectral_Type_of_Star_B = "G1"
            #median temperature of 5850 Kelvin
        if ((5700+5770)/2) <= Temperature_Effective_of_Star_B < ((5770+5850)/2):
            Spectral_Type_of_Star_B = "G2"
            #median temperature of 5770 Kelvin
        if ((5630+5700)/2) <= Temperature_Effective_of_Star_B < ((5700+5770)/2):
            Spectral_Type_of_Star_B = "G3"
            #median temperature of 5700 Kelvin
        if ((5570+5630)/2) <= Temperature_Effective_of_Star_B < ((5630+5700)/2):
            Spectral_Type_of_Star_B = "G4"
            #median temperature of 5630 Kelvin
        if ((5510+5570)/2) <= Temperature_Effective_of_Star_B < ((5570+5630)/2):
            Spectral_Type_of_Star_B = "G5"
            #median temperature of 5570 Kelvin
        if ((5450+5510)/2) <= Temperature_Effective_of_Star_B < ((5510+5570)/2):
            Spectral_Type_of_Star_B = "G6"
            #median temperature of 5510 Kelvin
        if ((5390+5450)/2) <= Temperature_Effective_of_Star_B < ((5450+5510)/2):
            Spectral_Type_of_Star_B = "G7"
            #median temperature of 5450 Kelvin
        if ((5330+5390)/2) <= Temperature_Effective_of_Star_B < ((5390+5450)/2):
            Spectral_Type_of_Star_B = "G8"
            #median temperature of 5390 Kelvin
        if ((5270+5330)/2) <= Temperature_Effective_of_Star_B < ((5330+5390)/2):
            Spectral_Type_of_Star_B = "G9"
            #median temperature of 5330 Kelvin
        if ((5130+5270)/2) <= Temperature_Effective_of_Star_B < ((5270+5330)/2):
            Spectral_Type_of_Star_B = "K0"
            #median temperature of 5270 Kelvin
        if ((4990+5130)/2) <= Temperature_Effective_of_Star_B < ((5130+5270)/2):
            Spectral_Type_of_Star_B = "K1"
            #median temperature of 5130 Kelvin
        if ((4850+4990)/2) <= Temperature_Effective_of_Star_B < ((4990+5130)/2):
            Spectral_Type_of_Star_B = "K2"
            #median temperature of 4990 Kelvin
        if ((4710+4850)/2) <= Temperature_Effective_of_Star_B < ((4850+4990)/2):
            Spectral_Type_of_Star_B = "K3"
            #median temperature of 4850 Kelvin
        if ((4560+4710)/2) <= Temperature_Effective_of_Star_B < ((4710+4850)/2):
            Spectral_Type_of_Star_B = "K4"
            #median temperature of 4710 Kelvin
        if ((4410+4560)/2) <= Temperature_Effective_of_Star_B < ((4560+4710)/2):
            Spectral_Type_of_Star_B = "K5"
            #median temperature of 4560 Kelvin
        if ((4270+4410)/2) <= Temperature_Effective_of_Star_B < ((4410+4560)/2):
            Spectral_Type_of_Star_B = "K6"
            #median temperature of 4410 Kelvin
        if ((4130+4270)/2) <= Temperature_Effective_of_Star_B < ((4270+4410)/2):
            Spectral_Type_of_Star_B = "K7"
            #median temperature of 4270 Kelvin
        if ((3990+4130)/2) <= Temperature_Effective_of_Star_B < ((4130+4270)/2):
            Spectral_Type_of_Star_B = "K8"
            #median temperature of 4130 Kelvin
        if ((3850+3990)/2) <= Temperature_Effective_of_Star_B < ((3990+4130)/2):
            Spectral_Type_of_Star_B = "K9"
            #median temperature of 3990 Kelvin
        if ((3700+3850)/2) <= Temperature_Effective_of_Star_B < ((3850+3990)/2):
            Spectral_Type_of_Star_B = "M0"
            #median temperature of 3850 Kelvin
        if ((3540+3700)/2) <= Temperature_Effective_of_Star_B < ((3700+3850)/2):
            Spectral_Type_of_Star_B = "M1"
            #median temperature of 3700 Kelvin
        if ((3380+3540)/2) <= Temperature_Effective_of_Star_B < ((3540+3700)/2):
            Spectral_Type_of_Star_B = "M2"
            #median temperature of 3540 Kelvin
        if ((3220+3380)/2) <= Temperature_Effective_of_Star_B < ((3380+3540)/2):
            Spectral_Type_of_Star_B = "M3"
            #median temperature of 3380 Kelvin
        if ((3060+3220)/2) <= Temperature_Effective_of_Star_B < ((3220+3380)/2):
            Spectral_Type_of_Star_B = "M4"
            #median temperature of 3220 Kelvin
        if ((2900+3060)/2) <= Temperature_Effective_of_Star_B < ((3060+3220)/2):
            Spectral_Type_of_Star_B = "M5"
            #median temperature of 3060 Kelvin
        if ((2740+2900)/2) <= Temperature_Effective_of_Star_B < ((2900+3060)/2):
            Spectral_Type_of_Star_B = "M6"
            #median temperature of 2900 Kelvin
        if ((2580+2740)/2) <= Temperature_Effective_of_Star_B < ((2740+2900)/2):
            Spectral_Type_of_Star_B = "M7"
            #median temperature of 2740 Kelvin
        if ((2420+2580)/2) <= Temperature_Effective_of_Star_B < ((2580+2740)/2):
            Spectral_Type_of_Star_B = "M8"
            #median temperature of 2580 Kelvin
        if ((2270+2420)/2) <= Temperature_Effective_of_Star_B < ((2420+2580)/2):
            Spectral_Type_of_Star_B = "M9"
            #median temperature of 2420 Kelvin
        if ((2170+2270)/2) <= Temperature_Effective_of_Star_B < ((2270+2420)/2):
            Spectral_Type_of_Star_B = "L0"
            #median temperature of 2270 Kelvin
        if ((2070+2170)/2) <= Temperature_Effective_of_Star_B < ((2170+2270)/2):
            Spectral_Type_of_Star_B = "L1"
            #median temperature of 2170 Kelvin
        if ((1970+2070)/2) <= Temperature_Effective_of_Star_B < ((2070+2170)/2):
            Spectral_Type_of_Star_B = "L2"
            #median temperature of 2070 Kelvin
        if ((1870+1970)/2) <= Temperature_Effective_of_Star_B < ((1970+2070)/2):
            Spectral_Type_of_Star_B = "L3"
            #median temperature of 1970 Kelvin
        if ((1770+1870)/2) <= Temperature_Effective_of_Star_B < ((1870+1970)/2):
            Spectral_Type_of_Star_B = "L4"
            #median temperature of 1870 Kelvin
        if ((1660+1770)/2) <= Temperature_Effective_of_Star_B < ((1770+1870)/2):
            Spectral_Type_of_Star_B = "L5"
            #median temperature of 1770 Kelvin
        if ((1560+1660)/2) <= Temperature_Effective_of_Star_B < ((1660+1770)/2):
            Spectral_Type_of_Star_B = "L6"
            #median temperature of 1660 Kelvin
        if ((1460+1560)/2) <= Temperature_Effective_of_Star_B < ((1560+1660)/2):
            Spectral_Type_of_Star_B = "L7"
            #median temperature of 1560 Kelvin
        if ((1360+1460)/2) <= Temperature_Effective_of_Star_B < ((1460+1560)/2):
            Spectral_Type_of_Star_B = "L8"
            #median temperature of 1460 Kelvin
        if ((1260+1360)/2) <= Temperature_Effective_of_Star_B < ((1360+1460)/2):
            Spectral_Type_of_Star_B = "L9"
            #median temperature of 1360 Kelvin
        if ((1190+1260)/2) <= Temperature_Effective_of_Star_B < ((1260+1360)/2):
            Spectral_Type_of_Star_B = "T0"
            #median temperature of 1260 Kelvin
        if ((1120+1190)/2) <= Temperature_Effective_of_Star_B < ((1190+1260)/2):
            Spectral_Type_of_Star_B = "T1"
            #median temperature of 1190 Kelvin
        if ((1040+1120)/2) <= Temperature_Effective_of_Star_B < ((1120+1190)/2):
            Spectral_Type_of_Star_B = "T2"
            #median temperature of 1120 Kelvin
        if ((960+1040)/2) <= Temperature_Effective_of_Star_B < ((1040+1120)/2):
            Spectral_Type_of_Star_B = "T3"
            #median temperature of 1040 Kelvin
        if ((880+960)/2) <= Temperature_Effective_of_Star_B < ((960+1040)/2):
            Spectral_Type_of_Star_B = "T4"
            #median temperature of 960 Kelvin
        if ((800+880)/2) <= Temperature_Effective_of_Star_B < ((880+960)/2):
            Spectral_Type_of_Star_B = "T5"
            #median temperature of 880 Kelvin
        if ((720+800)/2) <= Temperature_Effective_of_Star_B < ((800+880)/2):
            Spectral_Type_of_Star_B = "T6"
            #median temperature of 800 Kelvin
        if ((640+720)/2) <= Temperature_Effective_of_Star_B < ((720+800)/2):
            Spectral_Type_of_Star_B = "T7"
            #median temperature of 720 Kelvin
        if ((570+640)/2) <= Temperature_Effective_of_Star_B < ((640+720)/2):
            Spectral_Type_of_Star_B = "T8"
            #median temperature of 640 Kelvin
        if ((500+570)/2) <= Temperature_Effective_of_Star_B < ((570+640)/2):
            Spectral_Type_of_Star_B = "T9"
            #median temperature of 570 Kelvin
        if Temperature_Effective_of_Star_B < ((500+570)/2):
            Spectral_Type_of_Star_B = "Y0"
    print(f"Spectral Type of Star B: {Spectral_Type_of_Star_B}")

Spectral_Type_of_Star_C = "None"
if Number_of_Stars >= 3:
    if Evolutionary_Stage_of_Star_C == "White Dwarf":
        Spectral_Type_of_Star_C = "D"
    if Evolutionary_Stage_of_Star_C != "White Dwarf":
        if Temperature_Effective_of_Star_C >= 16500:
            Spectral_Type_of_Star_C = "B3"
            #median temperature of 17000 Kelvin
        if 15500 <= Temperature_Effective_of_Star_C < 16500:
            Spectral_Type_of_Star_C = "B4"
            #median temperature of 16000 Kelvin
        if 14500 <= Temperature_Effective_of_Star_C < 15500:
            Spectral_Type_of_Star_C = "B5"
            #median temeperature of 15000 Kelvin
        if 13500 <= Temperature_Effective_of_Star_C < 14500:
            Spectral_Type_of_Star_C = "B6"
            #median temperature of 14000 Kelvin
        if ((11900+13000)/2) <= Temperature_Effective_of_Star_C < ((13000+14000)/2):
            Spectral_Type_of_Star_C = "B7"
            #median temperature of 13000 Kelvin
        if ((10800+11900)/2) <= Temperature_Effective_of_Star_C < ((11900+13000)/2):
            Spectral_Type_of_Star_C = "B8"
            #median temperature of 11900 Kelvin
        if ((9700+10800)/2) <= Temperature_Effective_of_Star_C < ((10800+11900)/2):
            Spectral_Type_of_Star_C = "B9"
            #median temperature of 10800
        if ((9450+9700)/2) <= Temperature_Effective_of_Star_C < ((9700+10800)/2):
            Spectral_Type_of_Star_C = "A0"
            #median temperaure of 9700
        if ((9200+9450)/2) <= Temperature_Effective_of_Star_C < ((9450+9700)/2):
            Spectral_Type_of_Star_C = "A1"
            #mediuam temperature of 9450
        if ((8950+9200)/2) <= Temperature_Effective_of_Star_C < ((9200+9450)/2):
            Spectral_Type_of_Star_C = "A2"
            #median temperature of 9200 Kelvin
        if ((8700+8950)/2) <= Temperature_Effective_of_Star_C < ((8950+9200)/2):
            Spectral_Type_of_Star_C = "A3"
            #median temperature of 8950 Kelvin
        if ((8450+8700)/2) <= Temperature_Effective_of_Star_C < ((8700+8950)/2):
            Spectral_Type_of_Star_C = "A4"
            #median temperature of 8700 Kelvin
        if ((8200+8450)/2) <= Temperature_Effective_of_Star_C < ((8450+8700)/2):
            Spectral_Type_of_Star_C = "A5"
            #median temperature of 8450 Kelvin
        if ((7950+8200)/2) <= Temperature_Effective_of_Star_C < ((8200+8450)/2):
            Spectral_Type_of_Star_C = "A6"
            #median temperature of 8200 Kelvin
        if ((7700+7950)/2) <= Temperature_Effective_of_Star_C < ((7950+8200)/2):
            Spectral_Type_of_Star_C = "A7"
            #median temperature of 7950 Kelvin
        if ((7460+7700)/2) <= Temperature_Effective_of_Star_C < ((7700+7950)/2):
            Spectral_Type_of_Star_C = "A8"
            #median temperature of 7700 Kelvin
        if ((7220+7460)/2) <= Temperature_Effective_of_Star_C < ((7460+7700)/2):
            Spectral_Type_of_Star_C = "A9"
            #median temperature of 7460 Kelvin
        if ((7090+7220)/2) <= Temperature_Effective_of_Star_C < ((7720+7460)/2):
            Spectral_Type_of_Star_C = "F0"
            #median temperature of 7220 Kelvin
        if ((6890+7090)/2) <= Temperature_Effective_of_Star_C < ((7090+7220)/2):
            Spectral_Type_of_Star_C = "F1"
            #median temperature of 7090 Kelvin
        if ((6760+6890)/2) <= Temperature_Effective_of_Star_C < ((6890+7090)/2):
            Spectral_Type_of_Star_C = "F2"
            #median temperature of 6890 Kelvin
        if ((6630+6760)/2) <= Temperature_Effective_of_Star_C < ((6760+6890)/2):
            Spectral_Type_of_Star_C = "F3"
            #median temperature of 6760 Kelvin
        if ((6500+6630)/2) <= Temperature_Effective_of_Star_C < ((6630+6760)/2):
            Spectral_Type_of_Star_C = "F4"
            #median temperature of 6630 Kelvin
        if ((6370+6500)/2) <= Temperature_Effective_of_Star_C < ((6500+6630)/2):
            Spectral_Type_of_Star_C = "F5"
            #median temperature of 6500 Kelvin
        if ((6240+6370)/2) <= Temperature_Effective_of_Star_C < ((6370+6500)/2):
            Spectral_Type_of_Star_C = "F6"
            #median temperature of 6370 Kelvin
        if ((6110+6240)/2) <= Temperature_Effective_of_Star_C < ((6240+6370)/2):
            Spectral_Type_of_Star_C = "F7"
            #median temperature of 6240 Kelvin
        if ((6020+6110)/2) <= Temperature_Effective_of_Star_C < ((6110+6240)/2):
            Spectral_Type_of_Star_C = "F8"
            #median temperature of 6110 Kelvin
        if ((5930+6020)/2) <= Temperature_Effective_of_Star_C < ((6020+6110)/2):
            Spectral_Type_of_Star_C = "F9"
            #median temperature of 6020 Kelvin
        if ((5850+5930)/2) <= Temperature_Effective_of_Star_C < ((5930+6020)/2):
            Spectral_Type_of_Star_C = "G0"
            #median temperature of 5930 Kelvin
        if ((5770+5850)/2) <= Temperature_Effective_of_Star_C < ((5850+5930)/2):
            Spectral_Type_of_Star_C = "G1"
            #median temperature of 5850 Kelvin
        if ((5700+5770)/2) <= Temperature_Effective_of_Star_C < ((5770+5850)/2):
            Spectral_Type_of_Star_C = "G2"
            #median temperature of 5770 Kelvin
        if ((5630+5700)/2) <= Temperature_Effective_of_Star_C < ((5700+5770)/2):
            Spectral_Type_of_Star_C = "G3"
            #median temperature of 5700 Kelvin
        if ((5570+5630)/2) <= Temperature_Effective_of_Star_C < ((5630+5700)/2):
            Spectral_Type_of_Star_C = "G4"
            #median temperature of 5630 Kelvin
        if ((5510+5570)/2) <= Temperature_Effective_of_Star_C < ((5570+5630)/2):
            Spectral_Type_of_Star_C = "G5"
            #median temperature of 5570 Kelvin
        if ((5450+5510)/2) <= Temperature_Effective_of_Star_C < ((5510+5570)/2):
            Spectral_Type_of_Star_C = "G6"
            #median temperature of 5510 Kelvin
        if ((5390+5450)/2) <= Temperature_Effective_of_Star_C < ((5450+5510)/2):
            Spectral_Type_of_Star_C = "G7"
            #median temperature of 5450 Kelvin
        if ((5330+5390)/2) <= Temperature_Effective_of_Star_C < ((5390+5450)/2):
            Spectral_Type_of_Star_C = "G8"
            #median temperature of 5390 Kelvin
        if ((5270+5330)/2) <= Temperature_Effective_of_Star_C < ((5330+5390)/2):
            Spectral_Type_of_Star_C = "G9"
            #median temperature of 5330 Kelvin
        if ((5130+5270)/2) <= Temperature_Effective_of_Star_C < ((5270+5330)/2):
            Spectral_Type_of_Star_C = "K0"
            #median temperature of 5270 Kelvin
        if ((4990+5130)/2) <= Temperature_Effective_of_Star_C < ((5130+5270)/2):
            Spectral_Type_of_Star_C = "K1"
            #median temperature of 5130 Kelvin
        if ((4850+4990)/2) <= Temperature_Effective_of_Star_C < ((4990+5130)/2):
            Spectral_Type_of_Star_C = "K2"
            #median temperature of 4990 Kelvin
        if ((4710+4850)/2) <= Temperature_Effective_of_Star_C < ((4850+4990)/2):
            Spectral_Type_of_Star_C = "K3"
            #median temperature of 4850 Kelvin
        if ((4560+4710)/2) <= Temperature_Effective_of_Star_C < ((4710+4850)/2):
            Spectral_Type_of_Star_C = "K4"
            #median temperature of 4710 Kelvin
        if ((4410+4560)/2) <= Temperature_Effective_of_Star_C < ((4560+4710)/2):
            Spectral_Type_of_Star_C = "K5"
            #median temperature of 4560 Kelvin
        if ((4270+4410)/2) <= Temperature_Effective_of_Star_C < ((4410+4560)/2):
            Spectral_Type_of_Star_C = "K6"
            #median temperature of 4410 Kelvin
        if ((4130+4270)/2) <= Temperature_Effective_of_Star_C < ((4270+4410)/2):
            Spectral_Type_of_Star_C = "K7"
            #median temperature of 4270 Kelvin
        if ((3990+4130)/2) <= Temperature_Effective_of_Star_C < ((4130+4270)/2):
            Spectral_Type_of_Star_C = "K8"
            #median temperature of 4130 Kelvin
        if ((3850+3990)/2) <= Temperature_Effective_of_Star_C < ((3990+4130)/2):
            Spectral_Type_of_Star_C = "K9"
            #median temperature of 3990 Kelvin
        if ((3700+3850)/2) <= Temperature_Effective_of_Star_C < ((3850+3990)/2):
            Spectral_Type_of_Star_C = "M0"
            #median temperature of 3850 Kelvin
        if ((3540+3700)/2) <= Temperature_Effective_of_Star_C < ((3700+3850)/2):
            Spectral_Type_of_Star_C = "M1"
            #median temperature of 3700 Kelvin
        if ((3380+3540)/2) <= Temperature_Effective_of_Star_C < ((3540+3700)/2):
            Spectral_Type_of_Star_C = "M2"
            #median temperature of 3540 Kelvin
        if ((3220+3380)/2) <= Temperature_Effective_of_Star_C < ((3380+3540)/2):
            Spectral_Type_of_Star_C = "M3"
            #median temperature of 3380 Kelvin
        if ((3060+3220)/2) <= Temperature_Effective_of_Star_C < ((3220+3380)/2):
            Spectral_Type_of_Star_C = "M4"
            #median temperature of 3220 Kelvin
        if ((2900+3060)/2) <= Temperature_Effective_of_Star_C < ((3060+3220)/2):
            Spectral_Type_of_Star_C = "M5"
            #median temperature of 3060 Kelvin
        if ((2740+2900)/2) <= Temperature_Effective_of_Star_C < ((2900+3060)/2):
            Spectral_Type_of_Star_C = "M6"
            #median temperature of 2900 Kelvin
        if ((2580+2740)/2) <= Temperature_Effective_of_Star_C < ((2740+2900)/2):
            Spectral_Type_of_Star_C = "M7"
            #median temperature of 2740 Kelvin
        if ((2420+2580)/2) <= Temperature_Effective_of_Star_C < ((2580+2740)/2):
            Spectral_Type_of_Star_C = "M8"
            #median temperature of 2580 Kelvin
        if ((2270+2420)/2) <= Temperature_Effective_of_Star_C < ((2420+2580)/2):
            Spectral_Type_of_Star_C = "M9"
            #median temperature of 2420 Kelvin
        if ((2170+2270)/2) <= Temperature_Effective_of_Star_C < ((2270+2420)/2):
            Spectral_Type_of_Star_C = "L0"
            #median temperature of 2270 Kelvin
        if ((2070+2170)/2) <= Temperature_Effective_of_Star_C < ((2170+2270)/2):
            Spectral_Type_of_Star_C = "L1"
            #median temperature of 2170 Kelvin
        if ((1970+2070)/2) <= Temperature_Effective_of_Star_C < ((2070+2170)/2):
            Spectral_Type_of_Star_C = "L2"
            #median temperature of 2070 Kelvin
        if ((1870+1970)/2) <= Temperature_Effective_of_Star_C < ((1970+2070)/2):
            Spectral_Type_of_Star_C = "L3"
            #median temperature of 1970 Kelvin
        if ((1770+1870)/2) <= Temperature_Effective_of_Star_C < ((1870+1970)/2):
            Spectral_Type_of_Star_C = "L4"
            #median temperature of 1870 Kelvin
        if ((1660+1770)/2) <= Temperature_Effective_of_Star_C < ((1770+1870)/2):
            Spectral_Type_of_Star_C = "L5"
            #median temperature of 1770 Kelvin
        if ((1560+1660)/2) <= Temperature_Effective_of_Star_C < ((1660+1770)/2):
            Spectral_Type_of_Star_C = "L6"
            #median temperature of 1660 Kelvin
        if ((1460+1560)/2) <= Temperature_Effective_of_Star_C < ((1560+1660)/2):
            Spectral_Type_of_Star_C = "L7"
            #median temperature of 1560 Kelvin
        if ((1360+1460)/2) <= Temperature_Effective_of_Star_C < ((1460+1560)/2):
            Spectral_Type_of_Star_C = "L8"
            #median temperature of 1460 Kelvin
        if ((1260+1360)/2) <= Temperature_Effective_of_Star_C < ((1360+1460)/2):
            Spectral_Type_of_Star_C = "L9"
            #median temperature of 1360 Kelvin
        if ((1190+1260)/2) <= Temperature_Effective_of_Star_C < ((1260+1360)/2):
            Spectral_Type_of_Star_C = "T0"
            #median temperature of 1260 Kelvin
        if ((1120+1190)/2) <= Temperature_Effective_of_Star_C < ((1190+1260)/2):
            Spectral_Type_of_Star_C = "T1"
            #median temperature of 1190 Kelvin
        if ((1040+1120)/2) <= Temperature_Effective_of_Star_C < ((1120+1190)/2):
            Spectral_Type_of_Star_C = "T2"
            #median temperature of 1120 Kelvin
        if ((960+1040)/2) <= Temperature_Effective_of_Star_C < ((1040+1120)/2):
            Spectral_Type_of_Star_C = "T3"
            #median temperature of 1040 Kelvin
        if ((880+960)/2) <= Temperature_Effective_of_Star_C < ((960+1040)/2):
            Spectral_Type_of_Star_C = "T4"
            #median temperature of 960 Kelvin
        if ((800+880)/2) <= Temperature_Effective_of_Star_C < ((880+960)/2):
            Spectral_Type_of_Star_C = "T5"
            #median temperature of 880 Kelvin
        if ((720+800)/2) <= Temperature_Effective_of_Star_C < ((800+880)/2):
            Spectral_Type_of_Star_C = "T6"
            #median temperature of 800 Kelvin
        if ((640+720)/2) <= Temperature_Effective_of_Star_C < ((720+800)/2):
            Spectral_Type_of_Star_C = "T7"
            #median temperature of 720 Kelvin
        if ((570+640)/2) <= Temperature_Effective_of_Star_C < ((640+720)/2):
            Spectral_Type_of_Star_C = "T8"
            #median temperature of 640 Kelvin
        if ((500+570)/2) <= Temperature_Effective_of_Star_C < ((570+640)/2):
            Spectral_Type_of_Star_C = "T9"
            #median temperature of 570 Kelvin
        if Temperature_Effective_of_Star_C < ((500+570)/2):
            Spectral_Type_of_Star_C = "Y0"
    print(f"Spectral Type of Star C: {Spectral_Type_of_Star_C}")

Spectral_Type_of_Star_D = "None"
if Number_of_Stars == 4:
    if Evolutionary_Stage_of_Star_D == "White Dwarf":
        Spectral_Type_of_Star_D = "D"
    if Evolutionary_Stage_of_Star_D != "White Dwarf":
        if Temperature_Effective_of_Star_D >= 16500:
            Spectral_Type_of_Star_D = "B3"
            #median temperature of 17000 Kelvin
        if 15500 <= Temperature_Effective_of_Star_D < 16500:
            Spectral_Type_of_Star_D = "B4"
            #median temperature of 16000 Kelvin
        if 14500 <= Temperature_Effective_of_Star_D < 15500:
            Spectral_Type_of_Star_D = "B5"
            #median temeperature of 15000 Kelvin
        if 13500 <= Temperature_Effective_of_Star_D < 14500:
            Spectral_Type_of_Star_D = "B6"
            #median temperature of 14000 Kelvin
        if ((11900+13000)/2) <= Temperature_Effective_of_Star_D < ((13000+14000)/2):
            Spectral_Type_of_Star_D = "B7"
            #median temperature of 13000 Kelvin
        if ((10800+11900)/2) <= Temperature_Effective_of_Star_D < ((11900+13000)/2):
            Spectral_Type_of_Star_D = "B8"
            #median temperature of 11900 Kelvin
        if ((9700+10800)/2) <= Temperature_Effective_of_Star_D < ((10800+11900)/2):
            Spectral_Type_of_Star_D = "B9"
            #median temperature of 10800
        if ((9450+9700)/2) <= Temperature_Effective_of_Star_D < ((9700+10800)/2):
            Spectral_Type_of_Star_D = "A0"
            #median temperaure of 9700
        if ((9200+9450)/2) <= Temperature_Effective_of_Star_D < ((9450+9700)/2):
            Spectral_Type_of_Star_D = "A1"
            #mediuam temperature of 9450
        if ((8950+9200)/2) <= Temperature_Effective_of_Star_D < ((9200+9450)/2):
            Spectral_Type_of_Star_D = "A2"
            #median temperature of 9200 Kelvin
        if ((8700+8950)/2) <= Temperature_Effective_of_Star_D < ((8950+9200)/2):
            Spectral_Type_of_Star_D = "A3"
            #median temperature of 8950 Kelvin
        if ((8450+8700)/2) <= Temperature_Effective_of_Star_D < ((8700+8950)/2):
            Spectral_Type_of_Star_D = "A4"
            #median temperature of 8700 Kelvin
        if ((8200+8450)/2) <= Temperature_Effective_of_Star_D < ((8450+8700)/2):
            Spectral_Type_of_Star_D = "A5"
            #median temperature of 8450 Kelvin
        if ((7950+8200)/2) <= Temperature_Effective_of_Star_D < ((8200+8450)/2):
            Spectral_Type_of_Star_D = "A6"
            #median temperature of 8200 Kelvin
        if ((7700+7950)/2) <= Temperature_Effective_of_Star_D < ((7950+8200)/2):
            Spectral_Type_of_Star_D = "A7"
            #median temperature of 7950 Kelvin
        if ((7460+7700)/2) <= Temperature_Effective_of_Star_D < ((7700+7950)/2):
            Spectral_Type_of_Star_D = "A8"
            #median temperature of 7700 Kelvin
        if ((7220+7460)/2) <= Temperature_Effective_of_Star_D < ((7460+7700)/2):
            Spectral_Type_of_Star_D = "A9"
            #median temperature of 7460 Kelvin
        if ((7090+7220)/2) <= Temperature_Effective_of_Star_D < ((7720+7460)/2):
            Spectral_Type_of_Star_D = "F0"
            #median temperature of 7220 Kelvin
        if ((6890+7090)/2) <= Temperature_Effective_of_Star_D < ((7090+7220)/2):
            Spectral_Type_of_Star_D = "F1"
            #median temperature of 7090 Kelvin
        if ((6760+6890)/2) <= Temperature_Effective_of_Star_D < ((6890+7090)/2):
            Spectral_Type_of_Star_D = "F2"
            #median temperature of 6890 Kelvin
        if ((6630+6760)/2) <= Temperature_Effective_of_Star_D < ((6760+6890)/2):
            Spectral_Type_of_Star_D = "F3"
            #median temperature of 6760 Kelvin
        if ((6500+6630)/2) <= Temperature_Effective_of_Star_D < ((6630+6760)/2):
            Spectral_Type_of_Star_D = "F4"
            #median temperature of 6630 Kelvin
        if ((6370+6500)/2) <= Temperature_Effective_of_Star_D < ((6500+6630)/2):
            Spectral_Type_of_Star_D = "F5"
            #median temperature of 6500 Kelvin
        if ((6240+6370)/2) <= Temperature_Effective_of_Star_D < ((6370+6500)/2):
            Spectral_Type_of_Star_D = "F6"
            #median temperature of 6370 Kelvin
        if ((6110+6240)/2) <= Temperature_Effective_of_Star_D < ((6240+6370)/2):
            Spectral_Type_of_Star_D = "F7"
            #median temperature of 6240 Kelvin
        if ((6020+6110)/2) <= Temperature_Effective_of_Star_D < ((6110+6240)/2):
            Spectral_Type_of_Star_D = "F8"
            #median temperature of 6110 Kelvin
        if ((5930+6020)/2) <= Temperature_Effective_of_Star_D < ((6020+6110)/2):
            Spectral_Type_of_Star_D = "F9"
            #median temperature of 6020 Kelvin
        if ((5850+5930)/2) <= Temperature_Effective_of_Star_D < ((5930+6020)/2):
            Spectral_Type_of_Star_D = "G0"
            #median temperature of 5930 Kelvin
        if ((5770+5850)/2) <= Temperature_Effective_of_Star_D < ((5850+5930)/2):
            Spectral_Type_of_Star_D = "G1"
            #median temperature of 5850 Kelvin
        if ((5700+5770)/2) <= Temperature_Effective_of_Star_D < ((5770+5850)/2):
            Spectral_Type_of_Star_D = "G2"
            #median temperature of 5770 Kelvin
        if ((5630+5700)/2) <= Temperature_Effective_of_Star_D < ((5700+5770)/2):
            Spectral_Type_of_Star_D = "G3"
            #median temperature of 5700 Kelvin
        if ((5570+5630)/2) <= Temperature_Effective_of_Star_D < ((5630+5700)/2):
            Spectral_Type_of_Star_D = "G4"
            #median temperature of 5630 Kelvin
        if ((5510+5570)/2) <= Temperature_Effective_of_Star_D < ((5570+5630)/2):
            Spectral_Type_of_Star_D = "G5"
            #median temperature of 5570 Kelvin
        if ((5450+5510)/2) <= Temperature_Effective_of_Star_D < ((5510+5570)/2):
            Spectral_Type_of_Star_D = "G6"
            #median temperature of 5510 Kelvin
        if ((5390+5450)/2) <= Temperature_Effective_of_Star_D < ((5450+5510)/2):
            Spectral_Type_of_Star_D = "G7"
            #median temperature of 5450 Kelvin
        if ((5330+5390)/2) <= Temperature_Effective_of_Star_D < ((5390+5450)/2):
            Spectral_Type_of_Star_D = "G8"
            #median temperature of 5390 Kelvin
        if ((5270+5330)/2) <= Temperature_Effective_of_Star_D < ((5330+5390)/2):
            Spectral_Type_of_Star_D = "G9"
            #median temperature of 5330 Kelvin
        if ((5130+5270)/2) <= Temperature_Effective_of_Star_D < ((5270+5330)/2):
            Spectral_Type_of_Star_D = "K0"
            #median temperature of 5270 Kelvin
        if ((4990+5130)/2) <= Temperature_Effective_of_Star_D < ((5130+5270)/2):
            Spectral_Type_of_Star_D = "K1"
            #median temperature of 5130 Kelvin
        if ((4850+4990)/2) <= Temperature_Effective_of_Star_D < ((4990+5130)/2):
            Spectral_Type_of_Star_D = "K2"
            #median temperature of 4990 Kelvin
        if ((4710+4850)/2) <= Temperature_Effective_of_Star_D < ((4850+4990)/2):
            Spectral_Type_of_Star_D = "K3"
            #median temperature of 4850 Kelvin
        if ((4560+4710)/2) <= Temperature_Effective_of_Star_D < ((4710+4850)/2):
            Spectral_Type_of_Star_D = "K4"
            #median temperature of 4710 Kelvin
        if ((4410+4560)/2) <= Temperature_Effective_of_Star_D < ((4560+4710)/2):
            Spectral_Type_of_Star_D = "K5"
            #median temperature of 4560 Kelvin
        if ((4270+4410)/2) <= Temperature_Effective_of_Star_D < ((4410+4560)/2):
            Spectral_Type_of_Star_D = "K6"
            #median temperature of 4410 Kelvin
        if ((4130+4270)/2) <= Temperature_Effective_of_Star_D < ((4270+4410)/2):
            Spectral_Type_of_Star_D = "K7"
            #median temperature of 4270 Kelvin
        if ((3990+4130)/2) <= Temperature_Effective_of_Star_D < ((4130+4270)/2):
            Spectral_Type_of_Star_D = "K8"
            #median temperature of 4130 Kelvin
        if ((3850+3990)/2) <= Temperature_Effective_of_Star_D < ((3990+4130)/2):
            Spectral_Type_of_Star_D = "K9"
            #median temperature of 3990 Kelvin
        if ((3700+3850)/2) <= Temperature_Effective_of_Star_D < ((3850+3990)/2):
            Spectral_Type_of_Star_D = "M0"
            #median temperature of 3850 Kelvin
        if ((3540+3700)/2) <= Temperature_Effective_of_Star_D < ((3700+3850)/2):
            Spectral_Type_of_Star_D = "M1"
            #median temperature of 3700 Kelvin
        if ((3380+3540)/2) <= Temperature_Effective_of_Star_D < ((3540+3700)/2):
            Spectral_Type_of_Star_D = "M2"
            #median temperature of 3540 Kelvin
        if ((3220+3380)/2) <= Temperature_Effective_of_Star_D < ((3380+3540)/2):
            Spectral_Type_of_Star_D = "M3"
            #median temperature of 3380 Kelvin
        if ((3060+3220)/2) <= Temperature_Effective_of_Star_D < ((3220+3380)/2):
            Spectral_Type_of_Star_D = "M4"
            #median temperature of 3220 Kelvin
        if ((2900+3060)/2) <= Temperature_Effective_of_Star_D < ((3060+3220)/2):
            Spectral_Type_of_Star_D = "M5"
            #median temperature of 3060 Kelvin
        if ((2740+2900)/2) <= Temperature_Effective_of_Star_D < ((2900+3060)/2):
            Spectral_Type_of_Star_D = "M6"
            #median temperature of 2900 Kelvin
        if ((2580+2740)/2) <= Temperature_Effective_of_Star_D < ((2740+2900)/2):
            Spectral_Type_of_Star_D = "M7"
            #median temperature of 2740 Kelvin
        if ((2420+2580)/2) <= Temperature_Effective_of_Star_D < ((2580+2740)/2):
            Spectral_Type_of_Star_D = "M8"
            #median temperature of 2580 Kelvin
        if ((2270+2420)/2) <= Temperature_Effective_of_Star_D < ((2420+2580)/2):
            Spectral_Type_of_Star_D = "M9"
            #median temperature of 2420 Kelvin
        if ((2170+2270)/2) <= Temperature_Effective_of_Star_D < ((2270+2420)/2):
            Spectral_Type_of_Star_D = "L0"
            #median temperature of 2270 Kelvin
        if ((2070+2170)/2) <= Temperature_Effective_of_Star_D < ((2170+2270)/2):
            Spectral_Type_of_Star_D = "L1"
            #median temperature of 2170 Kelvin
        if ((1970+2070)/2) <= Temperature_Effective_of_Star_D < ((2070+2170)/2):
            Spectral_Type_of_Star_D = "L2"
            #median temperature of 2070 Kelvin
        if ((1870+1970)/2) <= Temperature_Effective_of_Star_D < ((1970+2070)/2):
            Spectral_Type_of_Star_D = "L3"
            #median temperature of 1970 Kelvin
        if ((1770+1870)/2) <= Temperature_Effective_of_Star_D < ((1870+1970)/2):
            Spectral_Type_of_Star_D = "L4"
            #median temperature of 1870 Kelvin
        if ((1660+1770)/2) <= Temperature_Effective_of_Star_D < ((1770+1870)/2):
            Spectral_Type_of_Star_D = "L5"
            #median temperature of 1770 Kelvin
        if ((1560+1660)/2) <= Temperature_Effective_of_Star_D < ((1660+1770)/2):
            Spectral_Type_of_Star_D = "L6"
            #median temperature of 1660 Kelvin
        if ((1460+1560)/2) <= Temperature_Effective_of_Star_D < ((1560+1660)/2):
            Spectral_Type_of_Star_D = "L7"
            #median temperature of 1560 Kelvin
        if ((1360+1460)/2) <= Temperature_Effective_of_Star_D < ((1460+1560)/2):
            Spectral_Type_of_Star_D = "L8"
            #median temperature of 1460 Kelvin
        if ((1260+1360)/2) <= Temperature_Effective_of_Star_D < ((1360+1460)/2):
            Spectral_Type_of_Star_D = "L9"
            #median temperature of 1360 Kelvin
        if ((1190+1260)/2) <= Temperature_Effective_of_Star_D < ((1260+1360)/2):
            Spectral_Type_of_Star_D = "T0"
            #median temperature of 1260 Kelvin
        if ((1120+1190)/2) <= Temperature_Effective_of_Star_D < ((1190+1260)/2):
            Spectral_Type_of_Star_D = "T1"
            #median temperature of 1190 Kelvin
        if ((1040+1120)/2) <= Temperature_Effective_of_Star_D < ((1120+1190)/2):
            Spectral_Type_of_Star_D = "T2"
            #median temperature of 1120 Kelvin
        if ((960+1040)/2) <= Temperature_Effective_of_Star_D < ((1040+1120)/2):
            Spectral_Type_of_Star_D = "T3"
            #median temperature of 1040 Kelvin
        if ((880+960)/2) <= Temperature_Effective_of_Star_D < ((960+1040)/2):
            Spectral_Type_of_Star_D
            #median temperatue of 960 Kelvin
        if ((800+880)/2) <= Temperature_Effective_of_Star_D < ((880+960)/2):
            Spectral_Type_of_Star_D = "T5"
            #median temperature of 880 Kelvin
        if ((720+800)/2) <= Temperature_Effective_of_Star_D < ((800+880)/2):
            Spectral_Type_of_Star_D = "T6"
            #median temperature of 800 Kelvin
        if ((640+720)/2) <= Temperature_Effective_of_Star_D < ((720+800)/2):
            Spectral_Type_of_Star_D = "T7"
            #median temperature of 720 Kelvin
        if ((570+640)/2) <= Temperature_Effective_of_Star_D < ((640+720)/2):
            Spectral_Type_of_Star_D = "T8"
            #median temperature of 640 Kelvin
        if ((500+570)/2) <= Temperature_Effective_of_Star_D < ((570+640)/2):
            Spectral_Type_of_Star_D = "T9"
            #median temperature of 570 Kelvin
        if Temperature_Effective_of_Star_D < ((500+570)/2):
            Spectral_Type_of_Star_D = "Y0"
    print(f"Spectral Type of Star D: {Spectral_Type_of_Star_D}")
