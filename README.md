# 2023-BigDataVisualization

## Table of Contents
1. [Software requirements](#software-requirements)
2. [Goal of Work](#Goal-of-Work)
3. [Content of this repository](#Content-of-this-repository)
      1. [Notebooks](#Notebooks)
      2. [CSV & GeoJSON data](#CSV_&-GeoJSON-data)
4. [Comments](#comments)

## Software requirements 

Election_results_county_map.ipynb
Election_results_municipality_map.ipynb
Election_results_province_map.ipynb
Elections_result_Barcelona_MAP.ipynb
ForeignersByProvince.ipynb
Participation_results_county_map.ipynb
Participation_results_municipality_map.ipynb
Participation_results_province_map.ipynb
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

This work is aimed to show how different factors are correlated with elections results. We show these results on scale of district, municipality, county and province. We consider factors such as income, language use and employment.

## Content of this repository
### Notebooks
Our repository contains the following notebooks:

* Election_results_county_map.ipynb
* Election_results_municipality_map.ipynb
* Election_results_province_map.ipynb
* Elections_result_Barcelona_MAP.ipynb
* ForeignersByProvince.ipynb: This creates a map of Barcelona's districts that shows which the concentration of foreigners residency across the districts
* Participation_results_county_map.ipynb
* Participation_results_municipality_map.ipynb
* Participation_results_province_map.ipynb

### CSV & GeoJSON data
Our repository contains the following data:
* G20192-Columnes-ME.csv : raw election data results with the number of votes each party receives is in columns
* G20192-Columnes-ME-EN.csv : column heads translated in english for transparency
* G20192-Participació-ME.csv : raw election data results with participation numbers
* G20192-Vots-ME.csv : raw election data with number of votes
* districts_BCN.geojson : map of Barcelona's districts
* municipality_map.geojson : map of Catalonia's municipalities
* county_map.geojson : map of Catalonia's counties (comarcas)
* province_map.geojson : map of Catalonia's provinces

This is a work by Abdelrhman Abdelmooty, Giada Damiani, João Catraio, Karlos Martínez and Jose Trespalle. This work is licensed under CC-BY-4.0 license.
