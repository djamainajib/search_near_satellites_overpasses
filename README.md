# search_near_satellites_overpasses

This code search for satellites overpasses acquired during a given temporal gap (delta t) over a given point P. 

The actual version supports Sentinel-2, Landsat-8, Landsat-9 and Harmonised Landsat (HLS) sensors.

User should specify:
- the latitude/longitude of the point of interrest in EPSG:4326
- the period of interrest startDate/endDate
- the couple of satellites to considered 
- the maximum temporal gap between the selected acquisition (delta_t_max)

The code outputs a FataFrame of all the satellites aquisitions (from 2 different sensors) within at short period of time (delta t).

##### Example:

* For the geo-location 37.42189 N, 122.08412 W, we can find 4 Sentinel-2 images acquired whithin 1 day maximum of a Landsat-8 image between March 1st and August 30th, 2020, 

<ins>Details (code output)<ins>

| Collection_1 | lon_1 | lat_1 | id_1 | date_1 | Collection_2 | lon_2 | lat_2 | id_2 | date_2 |
| -------- | ------- |-------- | ------- |-------- | ------- |-------- | ------- |-------- | ------- |
|0|COPERNICUS/S2_SR_HARMONIZED |-122.084191|37.421928|20200504T184921_20200504T185732_T10SEG_0|2020-05-04|LANDSAT/LC08/C02/T1_L2|-122.084191|37.421928|LC08_044034_20200505_0|2020-05-05|
|1| COPERNICUS/S2_SR_HARMONIZED|-122.084191|37.421928|20200623T184921_20200623T185629_T10SEG_0|2020-06-23|LANDSAT/LC08/C02/T1_L2|-122.084191|37.421928|LC08_044034_20200622_0|2020-06-22|
|2|COPERNICUS/S2_SR_HARMONIZED|-122.084191|37.421928|20200708T184919_20200708T185408_T10SEG_0|2020-07-08|LANDSAT/LC08/C02/T1_L2|-122.084191|37.421928|LC08_044034_20200708_0|2020-07-08|
|3|COPERNICUS/S2_SR_HARMONIZED|-122.084191|37.421928|20200723T184921_20200723T185433_T10SEG_0|2020-07-23|LANDSAT/LC08/C02/T1_L2|-122.084191|37.421928|LC08_044034_20200724_0|2020-07-24|

    
    
