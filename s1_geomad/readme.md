# SAR Mosaic Stats Plugin

This folder contains an installable Python module, which is
a [Datacube Statistician](https://github.com/opendatacube/odc-stats)
plugin. What this means is we can write our logic for creating
a mosaic product in this plugin and the Stats tool handles
the boilerplate, like finding, loading, processing, merging,
packaging and so on.

There's a [Makefile](Makefile) in this folder that holds some
commands that can be used to test the processing.

Testing assumes there's a local datacube instance to work against.

## Notes

* Note that the default coordinate reference system is Australian
  Albers (epsg:3577), which is in metres, while the original data
  at the granule level is being produced in degrees. We should
  look into the distortions this might be making in resampling and
  could consider using a lat/lon grid.
