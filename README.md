# Fari digital twin progress tracker

## Data Sources





| Name                      | Description                                                                                                                                                                                                               | Provider   | Type        | Implemented   | Url                                                                                                              | Format           | Update frequency   | Harvester                            |   Priority |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------|:-----------------|:-------------------|:-------------------------------------|-----------:|
| Vehicle Position          | Real-time train positions                                                                                                                                                                                                 | SNCB       | Telemetry   | ✅ Yes         | nan                                                                                                              | GeoJSON          | 30 second          | SNCBVehiclePositionGeometryHarvester |          0 |
| 3D Constructions          | LoD 2.2 3D construction                                                                                                                                                                                                   | Paradigm   | Mesh        | ❌ No          | https://datastore.brussels/web/data/dataset/e9ec2aa4-cffd-11ee-bccc-00090ffe0001#access                          | SHP/DWG/GPKG/SKP | 1 month            | nan                                  |          1 |
| lidar brussels            | LiDAR aérien – 2021                                                                                                                                                                                                       | Paradigm   | point cloud | ❌ No          | https://datastore.brussels/web/data/dataset/ff1124e1-424e-11ee-b156-00090ffe0001#access                          | las              | unknown            | nan                                  |          3 |
| google maps traffic layer | Raster of the real time traffic congestion (I guess it is related to the average speed of vehicules). It would be nice to write a harvester that get the color of each segment of street in brussels and save that in db) | Google     | raster      | ❌ No          | https://developers.google.com/maps/documentation/javascript/examples/layer-traffic#maps_layer_traffic-javascript | webp             | 1 minute           | nan                                  |          3 |

## Implementation Status

![Implementation Status](assets/implementation-chart.svg)

**1 out of 4 resources implemented (25.0%)**

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





