# Datacube Configuration

This folder has configuration for the Open Data Cube and Datacube OWS.

There's a docker-compose file for testing, and a set of commands in
the [Makefile](Makefile) that can be used to start and configure the
environment. The [product definition](./csiro_s1_geomad.product-definition.yaml)
will work as is for the beta product, but should be modified for
the final 10 and 20 m products. The only change required is the name
and default resolution.

OWS styles are in the `ows_config` folder and should be fairly
self-explanatory. These styles can be used on the granule-based product
without much work.
