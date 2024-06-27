# Argo Workflow for S-1 Mosaic

This folder contains Argo Workflow yaml documents that run
the Datacube Statistician-based workflow to produce annual
mosaics of Sentinel-1 data.

There are currently two versions of the workflow:

1. [single](./stats-s1-geomad-single.yaml), which skips the
   cache DB creation, and uses an existing DB.
2. [year](./stats-s1-year.yaml), which is the full workflow,
   just limited to one year.
3. [all](./stats-s1-geomad-all.yaml), which is a full workflow
   that will process all available tiles

The full workflow is divided into three stages:

1. `generate-db`, which generates a cache of dataset documents
   and divides the work into tiles, ready for execution
2. `fanout-db`, which uses the json dump of tiles to "fanout"
   work into n-tasks, where n is the number of tiles.
3. `process-id`, which receives tile IDs from the fanout step
   and uses the cached DB to run the workload against that tile.

## Notes

We use `parallelism` to manage how many pods are started at once.
Change this setting to run more tasks at the same time.

For resource usage, we're using CPU and memory requests. The memory
is the main constraint, as the process must load lots of data
into memory to be able to process the medians and write out
resulting files.

Any variables that should be changed are usually at the top of the
workflows, for example, the input product, or Docker image tag (version).
