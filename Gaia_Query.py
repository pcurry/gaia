#this script pulls Gaia data based on distance from the solar system and converts to sol-centric (x,y,z) coordinates
import numpy as np
from astroquery.gaia import Gaia
from astroquery.simbad import Simbad
from astropy.table import Table
import pandas as pd
#query Gaia dataset for galactic longitude, latitude and parallax of nearby stars (within 25 parsecs)
#will need to update to gaia data release 4 (gaiadr4) when it comes out (no earlier than mid-2026) and gaiadr5 (eta 2030)
query = """
SELECT designation, l, b, parallax, phot_g_mean_mag
FROM gaiadr3.gaia_source
WHERE parallax > 40
"""
job = Gaia.launch_job_async(query)
table = job.get_results()
#%%
gaia_DR3_df = table.to_pandas()
#add stars which do not appear in Gaia DR1, DR2 or DR3 (mostly those that are too bright / not detected due to detector saturation)
csv_file_path = 'not_in_any_Gaia_DR.csv'
not_in_any_Gaia_DR_df = pd.read_csv(csv_file_path)
df_combined = pd.concat([gaia_DR3_df, not_in_any_Gaia_DR_df], ignore_index=True)
#create new column and calculate distance to star (in parsecs) based on Gaia parallax
p=df_combined["parallax"]
d=df_combined["distance"]=1/p*1000
#convert galactic coordinates from degrees to radians
l=np.radians(df_combined["l"])
b=np.radians(df_combined["b"])
#create new column with calculated x-coordinates (where positive x is coreward and negative x is rimward)
df_combined["X"]=d*np.cos(b)*np.cos(l)
#create new column with calculated y-coordinates (where positive y is spinward and negative y is trailing in context of the direction of rotaiton of the galactic disk)
df_combined["Y"]=d*np.cos(b)*np.sin(l)
#create new column with calculated z-coordinates (where positive z is "galactic north" and negative z is "galactic south" per arbitrary convention)
df_combined["Z"]=d*np.sin(b)
# %%
#add special case - the Sun
sol = {
    'designation': ["Sol"], 
    'l': [0.0], 
    'b': [0.0],
    'phot_g_mean_mag': [100.0],
    'parallax': [0.0],
    'distance': [0.0],
    'X': [0.0],
    'Y': [0.0],
    'Z': [0.0]}
df_sol = pd.DataFrame(sol)
df_final = pd.concat([df_combined, df_sol], ignore_index=True)
# %%
print(df_final)
df_final.to_csv('gaia_query_result.csv', index=False)
print("Gaia Query Result Exported to 'gaia_query.result.csv'")