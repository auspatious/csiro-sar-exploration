up:
	docker-compose up

init:
	datacube system init --no-init-users

product:
	datacube product add https://data.dea.ga.gov.au/odc-conf/sentinel_examples/s1a_gamma0_scene.yaml

index:
	AWS_DEFAULT_REGION=ap-southeast-2 \
		s3-to-dc \
			's3://dea-public-data/odc-conf/sentinel_examples/Sentinel-1/**/*.yaml' \
			--no-sign-request

save_tasks:
	odc-stats save-tasks \
		--temporal-range="2017--P1Y" \
		--frequency="annual" \
		--grid="au-30" \
		--input-products="s1_gamma0_geotif_scene" \
		test.db

# Sample tile x40y07
run_task_old:
	odc-stats run \
		--config="config_old.yaml" \
		--threads="16" \
		--memory-limit="10GB" \
		--location="file:///Users/alex/git/auspatious/csiro-sar-exploration/mosaic_stats/output" \
		test.db \
		"2017--P1Y,40,6"

# Sample tile x40y07
run_task:
	odc-stats run \
		--config="config.yaml" \
		--threads="16" \
		--memory-limit="10GB" \
		--location="file:///Users/alex/git/auspatious/csiro-sar-exploration/mosaic_stats/output" \
		job.db \
		"2023--P1Y,40,6"

# Alex suspects that this doesn't work because the input
# datasets are eo and not eo3!
run_task_eo3:
	odc-stats run \
		--apply_eodatasets3 \
		--config="config.yaml" \
		--resolution="30" \
		--threads="16" \
		--memory-limit="10GB" \
		--location="file:///Users/alex/git/auspatious/csiro-sar-exploration/mosaic_stats/output_eod" \
		test.db \
		"2017--P1Y,+040,+006"
