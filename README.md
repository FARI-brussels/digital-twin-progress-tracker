# Fari digital twin progress tracker

## Data Sources










| Name                                      | Description                                                                                                                                                                                                                                                                                     | Provider          | Type        | Implemented   | Url                                                                                                              | Format           | Update frequency   | Harvester                            | Collector                          |   Priority |
|:------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------|:-----------------|:-------------------|:-------------------------------------|:-----------------------------------|-----------:|
| Vehicle Position                          | Real-time train positions                                                                                                                                                                                                                                                                       | SNCB              | Telemetry   | ✅ Yes         | nan                                                                                                              | GeoJSON          | 30 seconds         | SNCBVehiclePositionGeometryHarvester | nan                                |          0 |
| Line sections INFRABEL                    | Segmentation of the rail network based on infrastructure characteristics                                                                                                                                                                                                                        | Infrabel          | Vector Data | ✅ Yes         | nan                                                                                                              | GeoJSON          | Everyday at 02:20  | nan                                  | InfrabelLineSectionCollector       |          0 |
| Operational Points (Stops) INFRABEL       | The operational points of the railway network in Belgium                                                                                                                                                                                                                                        | Infrabel          | Vector Data | ✅ Yes         | nan                                                                                                              | GeoJSON          | Everyday at 01:15  | nan                                  | InfrabelOperationalPointsCollector |          0 |
| Vehicle Position                          | Real-time metro/bus/tram positions                                                                                                                                                                                                                                                              | STIB              | Telemetry   | ✅ Yes         | nan                                                                                                              | GeoJSON          | 20 seconds         | STIBVehiclePositionGeometryHarvester | nan                                |          0 |
| Segments Infrabel                         | The segments of the SNCB network in Belgium                                                                                                                                                                                                                                                     | Infrabel          | Vector Data | ✅ Yes         | nan                                                                                                              | GeoJSON          | Everyday at 01:45  | nan                                  | InfrabelSegmentsCollector          |          0 |
| Segments                                  | The segments of the STIB/MIVB network                                                                                                                                                                                                                                                           | STIB              | Vector Data | ✅ Yes         | nan                                                                                                              | GeoJSON          | unknown            | STIBSegmentsHarvester                | nan                                |          0 |
| Vehicle Aggregated Speed                  | The average speed of STIB/MIVB vehicles in 10-minute intervals                                                                                                                                                                                                                                  | STIB              | Telemetry   | ✅ Yes         | nan                                                                                                              | JSON             | 10 minutes         | StibSegmentsAggregatedSpeedHarvester | nan                                |          0 |
| Vehicle Speed                             | The average speed of STIB/MIVB vehicles in 20-second intervals                                                                                                                                                                                                                                  | STIB              | Telemetry   | ✅ Yes         | nan                                                                                                              | JSON             | 20 seconds         | StibSegmentsSpeedHarvester           | nan                                |          0 |
| Vehicle Distance                          | The distance of each STIB vehicle since the last stop                                                                                                                                                                                                                                           | STIB              | Telemetry   | ✅ Yes         | nan                                                                                                              | JSON             | 20 seconds         | nan                                  | STIBVehiclePositionsCollector      |          0 |
| Shapefile                                 | The shapefile of STIB/MIVB                                                                                                                                                                                                                                                                      | STIB              | Vector Data | ✅ Yes         | nan                                                                                                              | GeoJSON          | Everyday at 03:20  | nan                                  | STIBShapeFilesCollector            |          0 |
| Vehicle Position Lime                     | The positions of Lime vehicles in Brussels                                                                                                                                                                                                                                                      | Lime              | Telemetry   | ✅ Yes         | nan                                                                                                              | GeoJSON          | 5 minutes          | nan                                  | LimeVehiclePositionCollector       |          0 |
| Stops                                     | The stops of STIB/MIVB                                                                                                                                                                                                                                                                          | STIB              | Vector Data | ✅ Yes         | nan                                                                                                              | GeoJSON          | Everyday at 00:20  | nan                                  | STIBStopsCollector                 |          0 |
| Vehicle Position Pony                     | The positions of Pony vehicles in Brussels                                                                                                                                                                                                                                                      | Pony              | Telemetry   | ✅ Yes         | nan                                                                                                              | GeoJSON          | 5 minutes          | nan                                  | PonyVehiclePositionCollector       |          0 |
| Weather                                   | Weather and air quality data for Brussels (from OpenWeather & Irceline)                                                                                                                                                                                                                         | OpenWeather       | Telemetry   | ✅ Yes         | nan                                                                                                              | GeoJSON          | 5 minutes          | nan                                  | OpenWeatherCollector               |          0 |
| Vehicle Position Bolt                     | The positions of Bolt vehicles in Brussels                                                                                                                                                                                                                                                      | Bolt              | Telemetry   | ✅ Yes         | nan                                                                                                              | GeoJSON          | 5 minutes          | nan                                  | BoltVehiclePositionCollector       |          0 |
| Vehicle Position Dott                     | The positions of Dott vehicles in Brussels                                                                                                                                                                                                                                                      | Dott              | Telemetry   | ✅ Yes         | nan                                                                                                              | GeoJSON          | 5 minutes          | nan                                  | DottVehiclePositionCollector       |          0 |
| Wheater and air quality irceline          | Sensor Observation Service for irceline see https://github.com/irceline/open_data?tab=readme-ov-file for more information                                                                                                                                                                       | Irceline          | Telemetry   | ✅ Yes         | https://geo.irceline.be/sos/api/v1/                                                                              | GeoJSON          | 5 minutes          | nan                                  | IrcelineSOSCollector               |          0 |
| Wheater and air quality sensors.community | realtime sensor observation api from sensors.community see https://sensor.community/ for more information                                                                                                                                                                                       | sensors.community | Telemetry   | ❌ No          | https://maps.sensor.community/data/v2/data.dust.min.json                                                         | GeoJSON          | 5 minutes          | nan                                  | nan                                |          1 |
| 3D Constructions                          | LoD 2.2 3D construction                                                                                                                                                                                                                                                                         | Paradigm          | Mesh        | ❌ No          | https://datastore.brussels/web/data/dataset/e9ec2aa4-cffd-11ee-bccc-00090ffe0001#access                          | SHP/DWG/GPKG/SKP | 1 month            | nan                                  | nan                                |          1 |
| lidar brussels                            | LiDAR aérien – 2021                                                                                                                                                                                                                                                                             | Paradigm          | Point Cloud | ❌ No          | https://datastore.brussels/web/data/dataset/ff1124e1-424e-11ee-b156-00090ffe0001#access                          | las              | unknown            | nan                                  | nan                                |          3 |
| google maps traffic layer                 | Raster of the real-time traffic congestion                                                                                                                                                                                                                                                      | Google            | Raster      | ❌ No          | https://developers.google.com/maps/documentation/javascript/examples/layer-traffic#maps_layer_traffic-javascript | webp             | 1 minute           | nan                                  | nan                                |          3 |
| Incidents Fixmystreet                     | The data represents a list of incidents reported to FixMyStreet Brussels with details about each incident such as its unique ID/ status/ and geographical coordinates. The incidents are in various states: "CLOSED"/"CREATED" and "PROCESSING" indicating their current progress or resolution | Fixmystreet       | Vector data | ❌ No          | https://fixmystreet.brussels/api/incidents/map?startDate=YYYY-MM-DD&endDate=YYYY-MM-DD                           | JSON             | nan                | nan                                  | nan                                |          3 |
| One particular incident fixmystreet       | These data represent an incident reported to FixMyStreet Brussels.                                                                                                                                                                                                                              | Fixmystreet       | Vector data | ❌ No          | https://fixmystreet.brussels/api/incidents/#id                                                                   | JSON             | nan                | nan                                  | nan                                |          3 |

## Implementation Status

![Implementation Status](assets/implementation_chart.svg)

**17 out of 23 resources implemented (73.91%)**

## Description

### Type of data 

#### Vector data
Geometric objects with coordinates and attributes:
- Lines (roads, pipes, cables)
- Polygons (buildings, zones, parcels)

#### Point cloud data
Dense collections of 3D points:
- LiDAR scans
- Photogrammetry outputs
- 3D scanning results
- Gaussian splattings

#### Raster data
Pixel-based imagery and elevation data:
- Satellite imagery
- Aerial photos
- Digital elevation models

#### 3D models
Structured representations with geometry and textures:
- BIM (Building Information Models)
- CAD models
- Textured meshes

#### 3D city semantic format
- CityJSON

#### Telemetry data
Time-series information:
- Sensor readings over time
- Movement trajectories/positions
- Historical states


### Harvesters
#### Tiler



## To-Do

- [ ] Test IFC tiler https://github.com/VCityTeam/py3dtilers?tab=readme-ov-file
- [ ] Test pointcloud tiler https://gitlab.com/py3dtiles/py3dtiles
- [ ] Contact paradigm for 3d construction converstion to cityjson
- [ ] Test cityjson tiler https://github.com/3DGI/tyler



## Ressource
- https://projet.liris.cnrs.fr/vcity/
- https://www.geoscity.uliege.be/cms/c_12409035/en/geoscity

## Other DT examples

- https://www.digitalurbantwins.com/
- https://transfer.hft-stuttgart.de/pages/ensysle/application/Dithmarschen/index.html
- https://bremen.virtualcitymap.de/#/
- https://soest.virtualcitymap.de/#/3drouteMenue
- https://www.virtualcitymap.de/ (flooding simulation)
- https://kartta.hel.fi/3d/#/



## Tools
### Generate cityjson from lidar and cadastrial information
https://github.com/Yarroudh/Optim3D

