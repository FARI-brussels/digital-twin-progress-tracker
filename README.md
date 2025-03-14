# Fari digital twin progress tracker

## Data Sources


| Name             | Description               | Provider   | Type      | Url                                                                                     | Format           | Update frequency   | Harverster                           | Implemented   | Priority   |
|:-----------------|:--------------------------|:-----------|:----------|:----------------------------------------------------------------------------------------|:-----------------|:-------------------|:-------------------------------------|:--------------|:-----------|
| 3d constructions | Lod 2.2 3d construction   | paradigm   | mesh      | https://datastore.brussels/web/data/dataset/e9ec2aa4-cffd-11ee-bccc-00090ffe0001#access | shp/dwg/gpkg/skp | 1mounth            | nan                                  | ❌ No          | high       |
| Vehicle Position | real time train positions | sncb       | telemetry | nan                                                                                     | geojson          | 30seconds          | SNCBVehiclePositionGeometryHarvester | ✅ Yes         | nan        |

## Implementation Status

![Implementation Status](assets/implementation_chart.svg)

**1 out of 2 resources implemented (50.0%)**

## Description

### Type of data 

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



