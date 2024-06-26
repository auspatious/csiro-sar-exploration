up:
	docker-compose up

init:
	docker-compose exec ows datacube -v system init
	docker-compose exec ows datacube-ows-update --schema --role odc

product:
	docker-compose exec ows datacube product update --allow-unsafe /env/product_definition.yaml

index:
	s3-to-dc --stac --skip-lineage "s3://files.auspatious.com/sar-capability/**/*.json"

ows-update:
	docker-compose exec ows \
		bash -c " \
		datacube-ows-update --views && \
		datacube-ows-update \
		"
