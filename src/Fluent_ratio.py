import pandas as pd
import numpy as np
import matplotlib as plt
import geopandas as gpd
import plotly.express as px

catalan_spk_data = pd.read_csv('../data/ConeixementCatala.csv', sep=';')

map_catalonia = 'county_map.geojson'
geo_data = gpd.read_file('../data/county_map.geojson')
#print(geo_data)

geo_data.rename(columns={'nomcomar': 'Comarca'}, inplace=True)
geo_data_sorted = geo_data.sort_values(by='Comarca')

#catalan_by_county = catalan_spk_data.iloc[:, 11:21].groupby(by=catalan_spk_data["Comarca"]).sum()
#catalan_by_county.reset_index()
#print(catalan_spk_data)

# Acknowledging that fluency is when someone speaks

catalan_spk_data['Fluent ratio'] = catalan_spk_data['Can speak'] / catalan_spk_data['Population']


# Assuming df is your DataFrame
# Create a new column 'Fluency label' with default value 'Unknown'
catalan_spk_data['Fluency label'] = 'Unknown'

# Define the conditions and assign labels accordingly
conditions = [
    (catalan_spk_data['Fluent ratio'] < 0.70),
    ((catalan_spk_data['Fluent ratio'] >= 0.70) & (catalan_spk_data['Fluent ratio'] < 0.80)),
    ((catalan_spk_data['Fluent ratio'] >= 0.80) & (catalan_spk_data['Fluent ratio'] < 0.85)),
    (catalan_spk_data['Fluent ratio'] >= 0.85)
]

labels = ['Low', 'Medium', 'Medium High', 'High']

# Use np.select to apply the conditions and assign labels
catalan_spk_data['Fluency label'] = np.select(conditions, labels, default='Unknown')

# Display the updated DataFrame

print(catalan_spk_data)

merged_data = geo_data_sorted.merge(catalan_spk_data, on='Comarca')
#print(merged_data)


fig = px.choropleth_mapbox(
    merged_data,
    geojson=merged_data.geometry,
    locations=merged_data.index,
    color='Fluency label',
    color_discrete_map={'Low': 'yellow', 'Medium': 'blue', 'Medium High': 'purple', 'High': 'red'},
    hover_name='Comarca',
    mapbox_style="carto-positron",
    center={"lat": 41.8781, "lon": 1.7834},  # Center of Catalonia
    zoom=7
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(height=600, width=800)
fig.show()


