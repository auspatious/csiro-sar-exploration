# SAR Exploration

This repository contains a range of content resulting from a short
contract with CSIRO exploring SAR data, specifically around producing
radiometrically terrain corrected Sentinel-1 data and annual
mosaics of this RTC data.

## Contents

1. Initial work consisted on an [audit of data](availability_audit/readme.md)
    availability across various platforms.
2. Some work was undertaken to [explore the use of Sarsen](sarsen/Prepare_and_Run_Sarsen.ipynb)
    to produce RTC data. The tool works quite simply and is Python-based.
3. A [notebook](S1_Mosaic_Notebook.ipynb) was prepared to produce a geomedian,
    median absolute deviations, means and standard deviations of a year of S-1 RTC data.
4. A [Datacube Statistician](https://github.com/opendatacube/odc-stats) plugin
    was developed to produce the annual mosaic product, named [S1GeoMAD](s1_geomad/readme.md)
5. An [Argo workflow](argo/readme.md) was produced to run the mosaic product.
6. Some work was undertaken to set up [Datacube OWS styles](datacube/readme.md) for
    visualising the annual mosaic.
