#pulls Gaia data based on distance from solar system and converts to sol-centric (x,y,z) coordinates
import numpy as np
from astroquery.gaia import Gaia
import pandas as pd
#query Gaia dataset for galactic longitude, latitude and parallax of the nearest stars
query = """
SELECT source_id, l, b, parallax
FROM gaiadr3.gaia_source
WHERE parallax > 60
"""
job = Gaia.launch_job(query)
table = job.get_results()
df = table.to_pandas()
#create new column and calculate distance to star (in parsecs) based on Gaia parallax
df.insert(4, "Distance", 1/((df.iloc[:,3]) / 1000), allow_duplicates=True)
#create new column with calculated x-coordinates (where positive x is coreward and negative x is rimward)
df.insert(5, "X", (df.iloc[:,4]*np.cos(np.radians(df.iloc[:,2])))*np.cos(np.radians(df.iloc[:,1])), allow_duplicates=True)
#create new column with calculated y-coordinates (where positive y is spinward and negative y is trailing in context of the direction of rotaiton of the galactic disk)
df.insert(6, "Y", (df.iloc[:,4]*np.cos(np.radians(df.iloc[:,2])))*np.sin(np.radians(df.iloc[:,1])), allow_duplicates=True)
#create new column with calculated z-coordinates (where positive z is "galactic north" and negative z is "galactic south" per arbitrary convention)
df.insert(7, "Z", (df.iloc[:,4]*np.sin(np.radians(df.iloc[:,2]))), allow_duplicates=True)
print(df)