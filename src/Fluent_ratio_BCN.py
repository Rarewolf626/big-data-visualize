import pandas as pd
import geopandas as gpd
import plotly.express as px

data = pd.read_csv('../data/Knowledge_Catalan_Districts_Barcelona.csv', sep=';', encoding='latin-1')
geo_data = gpd.read_file('../data/districts_BCN.geojson', encoding='latin-1')
data['Fluency Ratio'] = data['Can speak, read and write'] / data['Population of 2 year or more ']
data = data[['Districts', 'Fluency Ratio']]
data['Fluency Ratio'] = data['Fluency Ratio'].astype(float)
data['Districts'] = data['Districts'].astype(str)
data = data.drop(data.index[0]).reset_index(drop=True)
data['Districts'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data['Fluency label'] = ['Low', 'High', 'Low', 'High', 'High', 'Very High', 'Very High', 'Low', 'Medium', 'Medium']
geo_data = geo_data[['NOM', 'geometry']]
geo_data.rename(columns={'NOM': 'Districts'}, inplace=True)
geo_data['Districts'] = geo_data['Districts'].astype(str)

bcn_gpd = gpd.GeoDataFrame(geo_data)
bcn_gpd['Districts'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

merged_data = bcn_gpd.merge(data, on='Districts')
print(merged_data)
fig = px.choropleth_mapbox(
    merged_data,
    geojson=merged_data.geometry,
    locations=merged_data.index,
    color='Fluency label',  # Change to the column you want to visualize
    color_discrete_map={'Low': 'yellow', 'Medium': 'blue', 'High': 'purple', 'Very High': 'red'},
    hover_name='Districts',
    mapbox_style="carto-positron",
    center={"lat": 41.3874, "lon": 2.1686},
    title='Catalan fluency per districts',  # Center of Catalonia
    zoom=10
)

fig.update_layout(height=600, width=800)
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
