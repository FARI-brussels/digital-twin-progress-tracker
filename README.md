# Fari digital twin progress tracker

## Data Sources



| Name             | Description               | Provider   | Type        | Implemented   | Url                                                                                     | Format           | Update frequency   | Harvester                            | Priority   |
|:-----------------|:--------------------------|:-----------|:------------|:--------------|:----------------------------------------------------------------------------------------|:-----------------|:-------------------|:-------------------------------------|:-----------|
| 3D Constructions | LoD 2.2 3D construction   | Paradigm   | Mesh        | ❌ No          | https://datastore.brussels/web/data/dataset/e9ec2aa4-cffd-11ee-bccc-00090ffe0001#access | SHP/DWG/GPKG/SKP | 1 month            | nan                                  | High       |
| lidar brussels   | LiDAR aérien – 2021       | Paradigm   | point cloud | ❌ No          | https://datastore.brussels/web/data/dataset/ff1124e1-424e-11ee-b156-00090ffe0001#access | las              | unknown            | nan                                  | low        |
| Vehicle Position | Real-time train positions | SNCB       | Telemetry   | ✅ Yes         | nan                                                                                     | GeoJSON          | 30 seconds         | SNCBVehiclePositionGeometryHarvester | nan        |

## Implementation Status

![Implementation Status](assets/implementation_chart.svg)

**1 out of 3 resources implemented (33.33%)**

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



