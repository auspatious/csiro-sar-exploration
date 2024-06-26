ows_cfg = {
    "global": {
        # Master config for all services and products.
        "response_headers": {
            "Access-Control-Allow-Origin": "*",  # CORS header
        },
        "services": {
            "wms": True,
            "wcs": True,
            "wmts": True,
        },
        "published_CRSs": {
            "EPSG:3857": {  # Web Mercator
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:3577": {  # GDA-94, Australian Albers. Not sure why, but it's required!
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:4326": {"geographic": True, "vertical_coord_first": True},  # WGS-84
        },
        "allowed_urls": [
            "http://localhost:8000",
        ],
        # Metadata to go straight into GetCapabilities documents
        "title": "TESTING",
        "abstract": """TODO...""",
        "info_url": "",
        "keywords": ["TESTING"],
        "contact_info": {
            "person": "TODO",
            "organisation": "TESTING",
            "position": "",
            "address": {
                "type": "postal",
                "address": "TODO",
                "city": "TODO",
                "state": "TODO",
                "postcode": "TODO",
                "country": "New Caledonia",
            },
            "telephone": "TODO",
            "fax": "",
            "email": "TODO",
        },
        "fees": "",
        "access_constraints": "TODO",
    },  # END OF global SECTION
    "wms": {
        # Config for WMS service, for all products/layers
        # "s3_aws_zone": "us-west-2",
        "max_width": 512,
        "max_height": 512,
    },  # END OF wms SECTION
    "wcs": {
        # Config for WCS service, for all products/coverages
        "default_geographic_CRS": "EPSG:4326",
        "formats": {
            "GeoTIFF": {
                # "renderer": "datacube_ows.wcs_utils.get_tiff",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_tiff",
                    "2": "datacube_ows.wcs2_utils.get_tiff",
                },
                "mime": "image/geotiff",
                "extension": "tif",
                "multi-time": False,
            },
            "netCDF": {
                # "renderer": "datacube_ows.wcs_utils.get_netcdf",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_netcdf",
                    "2": "datacube_ows.wcs2_utils.get_netcdf",
                },
                "mime": "application/x-netcdf",
                "extension": "nc",
                "multi-time": True,
            },
        },
        "native_format": "GeoTIFF",
    },  # END OF wcs SECTION
    "layers": [
        {
            "include": "ows_config.sar.mosaic.layer",
            "type": "python",
        },
    ],
}
