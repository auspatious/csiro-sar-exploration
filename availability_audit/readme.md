# Availability Audit

These notebooks are intended to produce statistics on Sentinel-1 GRD
data availability over Australia.

Notebooks are available for the following data repositories:

* [Alaska Satellite Facility](./ASF_ViewAustralian_S1GRD.ipynb)
* [Copernicus Dataspace](./COP_ViewAustralian_S1GRD.ipynb)
* [Element-84's Earth Search](./E84_ViewAustralian_S1GRD.ipynb)
* [MSPC STAC API](./MSPC_STAC_ViewAustralian_S1GRD.ipynb) and
   [MSPC Parquet](./MSPC_ViewAustralian_S1GRD.ipynb).

## Summary

Granule counts vary significantly between ASF, Element-84 (which
indexes the Sinergise AWS open data bucket) and the MSPC. The
Sinergise-managed public data bucket has the more consistently
larger numbers, which makes sense, as they work the closest with ESA.
Copernicus (ESA)  has the most granules, and it's a bit
suspicious that ASF is showing more than then sometimes, as ESA
should be the primary custodian.

Counts of just descending and IW instrument mode and a constrained
area of interest are shown below.

| Year | Count COP | Count ASF | Count E-84 | Count MSPC |
| ---- | --------- | --------- | ---------- | ---------- |
| 2014 | 116       | 54        | 121        | 102        |
| 2015 | 1653      | 1592      | 1644       | 1644       |
| 2016 | 3632      | 3017      | 3614       | 3614       |
| 2017 | 8635      | 8911      | 8628       | 8171       |
| 2018 | 8833      | 9069      | 8766       | 8235       |
| 2019 | 8906      | 9214      | 8859       | 8553       |
| 2020 | 8875      | 8958      | 8865       | 8344       |
| 2021 | 8805      | 8676      | 8736       | 8381       |
| 2022 | 5755      | 5560      | 5617       | 5491       |
| 2023 | 5671      | 5612      | 5671       | 5233       |