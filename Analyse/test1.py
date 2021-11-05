# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
column_names = []
delhi = pd.read_csv("cities/Delhi.csv")

# %%
delhi.info()
# %%
delhi.iloc[[0, 1, 2, 3, 4, 5, 9], [0, 1, 2, 3]]

# %%
# price vs carpet area scatter plot
y = np.log(delhi["Price"])
plt.scatter(delhi["Area"], y)
plt.title("carpet area vs price")
plt.xlabel("Carpet Area")
plt.ylabel("Price")
# plt.xscale("log")
# plt.yscale("log")
plt.show()
# %%
# price vs no. of bedrooms
plt.scatter(delhi["No. of Bedrooms"], delhi["Price"])
beds = delhi.loc[:, ["No. of Bedrooms"]]
bed_list = beds.drop_duplicates()
bed_list.sort_values()
print(bed_list)
plt.title("bedrooms vs price")
plt.xlabel("No. of bedrooms")
plt.ylabel("Price")
plt.show()
plt.clf()

# %%
# price vs location
plt.scatter(delhi.loc["Location"], delhi["Price"])
plt.title("locations vs price")
plt.xlabel("Locations")
plt.ylabel("Price")
# plt.yscale("log")
plt.show()
# %%
# frequency distribution of locations
places = delhi["Location"][:]
fig = plt.figure(figsize=(350, 200))
n, bins, patches = plt.hist(places[:], bins=339)
plt.xticks(bins, rotation=90)
plt.show()
plt.clf()
places_list = places.drop_duplicates()
print("bins:")
# print(bins)
# print(patches)
# plt.close()
# %%
# plt.close()
h = delhi.hist(column='Location')

# %%
