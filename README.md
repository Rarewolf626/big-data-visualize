# 2023-BigDataVisualization

## Table of Contents
1. [Software requirements](#software-requirements)
2. [Goal of Work](#Goal-of-Work)
3. [Content of this repository](#Content-of-this-repository)
      1. [Notebooks](#Notebooks)
      2. [CSV & GeoJSON data](#CSV_&-GeoJSON-data)
4. [Comment](#comment)

## Software requirements 
* Python 3.8 or higher
* Essential Python packages in `requirements.txt`
  * [geopandas](https://geopandas.org/)
  * [numpy](https://numpy.org/)
  * [matplotlib](https://matplotlib.org/)
  * [pandas](https://pandas.pydata.org/)
  * [scipy](https://scipy.org/)
* Jupyter Notebooks or Jupyter Lab
  * [Installing Jupyter](https://jupyter.org/install)

## Goal of Work 

This work is aimed to show how different factors are correlated with the Spanish general elections results of November 2019. We show these results on scale of district, municipality, county and province. We consider factors such as income, language use and employment.

## Content of this repository
### Notebooks
Our repository contains the following notebooks:

* Election_results_county_map.ipynb: This creates a map of the Catalan counties showing the election results.
* Election_results_municipality_map.ipynb: This creates a map of the Catalan municipalities showing the election results.
* Election_results_province_map.ipynb: This creates a map of the Catalan provinces showing the election results.
* Elections_result_Barcelona_MAP.ipynb: This creates a map of Barcelona's districts showing the election results.
* Income_map_Barcelona.ipynb: This creates a map of Barcelona's districts showing the average income per household.
* Income_map_Catalonia.ipynb: This creates a map of Catalan municipalities, counties and provinces showing the average net income per person.
* Election_Results_by_Census&Unenployement.ipynb: This creates two scatter plots relating the votes to Catalanist/Non-Catalanist parties respect to the census and then respect to the unenployement rate.
* ForeignersByProvince.ipynb: This creates a map of Barcelona's districts that shows which the concentration of foreigners residency across the districts
* Participation_results_county_map.ipynb: This creates a map of the Catalan counties showing the participation results.
* Participation_results_municipality_map.ipynb: This creates a map of the Catalan municipalities showing the participation results.
* Participation_results_province_map.ipynb: This creates a map of the Catalan provinces showing the participation results.
* catalan_votes_vs_participation.ipynb: This creates a plot of the rate of votes to Catalan parties vs. participation rate.
* Fluent_ratio.py : Creates the plot for the percentage of fluent Catalan speakers in comparison to total population of each county.

### CSV & GeoJSON data
Our repository contains the following data:
* G20192-Columnes-ME-EN.csv : Spanish general election results from November 2019. It contains the number of votes each party received and participation data by district, municipality, county (comarca) and province. Column heads were translated into English for transparency.
* districts_BCN.geojson : map of Barcelona's districts [[Link to Source]](https://w20.bcn.cat/cartobcn/)
* income_data.csv: average net income per person by Barcelona's districts, and Catalan municipalities, counties and provinces. [[Link to Source]](https://www.ine.es/jaxiT3/Tabla.htm?t=30896&L=0)
* municipality_county_province_cat.csv: Administrative division of Catalonia into municipalities, counties and provinces. Used to average data from municipalities to counties and provinces. [[Adapted from here]](https://www.icgc.cat/Descarregues/Cartografia-vectorial/Divisions-administratives)
* municipality_map.geojson : map of Catalonia's municipalities [[Link to Source]](https://analisi.transparenciacatalunya.cat/Urbanisme-infraestructures/L-mits-administratius-municipals-de-Catalunya/97qg-zvqd)
* county_map.geojson : map of Catalonia's counties (comarcas) [[Link to Source]](https://analisi.transparenciacatalunya.cat/Urbanisme-infraestructures/L-mits-administratius-comarcals-de-Catalunya/aasi-gwnd)
* province_map.geojson : map of Catalonia's provinces [[Link to Source]](https://analisi.transparenciacatalunya.cat/Urbanisme-infraestructures/L-mits-administratius-provincials-de-Catalunya/d2un-hz8w)
* Desempleo.csv : Number of unemployed people by municipality.
* Foreign.csv : Number of foreigner residents by districts.
* ConeixementCatala.csv : Numbers of people that speak, understant, read Catalan. The data is exposed by County of Catalunya. The corresponding plotting of this data is Fluent_ratio.py. We considered that people who speak it, are the ones to be considered fluent.
* Knowledge_Catalan_Districts_Barcelona.csv : Table of the data relative to Catala understanding skills (speak, understand, read, write or all of the above (complete fluency)). The Data is organized by districts of Barcelona. 

##Comment
This is a work by Abdelrhman Abdelmooty (gomgoma), Giada Damiani (giadadamiani), João Catraio (JprCat), Karlos Martínez (kostasotaduis) and Jose Arnal Trespallé (trespalle). This work is licensed under CC-BY-4.0 license.
