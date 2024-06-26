# From https://raw.githubusercontent.com/digitalearthafrica/config/master/services/ows_refactored/radar_backscatter/ows_sentinel1_cfg.py

dataset_cache_rules = [
    {
        "min_datasets": 5,
        "max_age": 60 * 60 * 24,
    },
    {
        "min_datasets": 9,
        "max_age": 60 * 60 * 24 * 7,
    },
    {
        "min_datasets": 17,
        "max_age": 60 * 60 * 24 * 30,
    },
    {
        "min_datasets": 65,
        "max_age": 60 * 60 * 24 * 120,
    },
]

reslim_continental = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 10.0,
        "dataset_cache_rules": dataset_cache_rules,
    },
    "wcs": {
        "max_datasets": 32,  # Defaults to no dataset limit
    },
}

style_vh_over_vv_mean = {
    "name": "style_vh_over_vv_mean",
    "title": "VV, VH and VH/VV (mean)",
    "abstract": "False colour representation of VV, VH and VH/VV for R, G and B respectively",
    "additional_bands": [],
    "components": {
        "red": {"vv_mean": 1.0, "scale_range": [0.0, 0.28]},
        "green": {"vh_mean": 1.0, "scale_range": [0.0, 0.06]},
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "vh_mean",
                "band2": "vv_mean",
                "scale_from": [0.0, 0.49],
            },
        },
    },
}

style_vh_over_vv_gm = {
    "name": "style_vh_over_vv_gm",
    "title": "VV, VH and VH/VV (geomedian)",
    "abstract": "False colour representation of VV, VH and VH/VV for R, G and B respectively",
    "additional_bands": [],
    "components": {
        "red": {"vv_gm": 1.0, "scale_range": [0.0, 0.28]},
        "green": {"vh_gm": 1.0, "scale_range": [0.0, 0.06]},
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {
                "band1": "vh_gm",
                "band2": "vv_gm",
                "scale_from": [0.0, 0.49],
            },
        },
    },
}

styles = {
    f"style{name}": {
        "name": name,
        "title": name.upper(),
        "abstract": f"{name} band",
        "additional_bands": [],
        "components": {
            "red": {name: 1.0, "scale_range": [0.0, 0.28]},
            "green": {name: 1.0, "scale_range": [0.0, 0.28]},
            "blue": {name: 1.0, "scale_range": [0.0, 0.28]},
        },
    }
    for name in ["vv_mean", "vh_mean", "vv_std", "vh_std", "vv_gm", "vh_gm"]
}


style_count = {
    "name": "count",
    "title": "Observation count",
    "abstract": "Count of observations included in median calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count",
        },
    },
    "needed_bands": ["count"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#FFFFFF",
            "alpha": 1,
        },
        {"value": 10, "color": "#f3fabf"},
        {"value": 15, "color": "#e1f3b2"},
        {"value": 20, "color": "#c6e9b4"},
        {"value": 25, "color": "#97d6b9"},
        {"value": 30, "color": "#6bc6be"},
        {"value": 35, "color": "#42b6c4"},
        {"value": 40, "color": "#299dc1"},
        {"value": 45, "color": "#1f80b8"},
        {"value": 50, "color": "#225da8"},
        {"value": 60, "color": "#24419a"},
        {"value": 70, "color": "#1b2c80"},
        {"value": 80, "color": "#081d58"},
    ],
    "legend": {
        "begin": "0",
        "end": "80",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "80": {"suffix": "<"},
        },
    },
}

# styles tmad
sdev_scaling = [0.020, 0.18]
edev_scaling = [6.2, 7.3]
bcdev_scaling = [0.025, 0.13]

style_tmad_sdev_std = {
    "name": "arcsec_sdev",
    "title": "Spectral MAD (SMAD)",
    "abstract": "",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_arcsec",
        "mapped_bands": True,
        "kwargs": {"band": "smad", "scale_from": sdev_scaling, "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["smad"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nSMAD"},
            "4.0": {"label": "High\nSMAD"},
        },
    },
}

style_tmad_edev_std = {
    "name": "log_edev",
    "title": "Euclidean MAD (EMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {"band": "emad", "scale_from": edev_scaling, "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["emad"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nEMAD"},
            "4.0": {"label": "High\nEMAD"},
        },
    },
}


style_tmad_bcdev_std = {
    "name": "log_bcdev",
    "title": "Bray-Curtis MAD (BCMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {
            "band": "bcmad",
            "scale_from": bcdev_scaling,
            "scale_to": [0.0, 4.0],
        },
    },
    "needed_bands": ["bcmad"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nBCMAD"},
            "4.0": {"label": "High\nBCMAD"},
        },
    },
}

style_tmad_rgb_std = {
    "name": "tmad_rgb_std",
    "title": "MADs - SMAD, EMAD, BCMAD",
    "abstract": "Good for cropland and forest",
    "components": {
        "red": {
            "function": "datacube_ows.band_utils.single_band_arcsec",
            "mapped_bands": True,
            "kwargs": {
                "band": "smad",
                "scale_from": sdev_scaling,
            },
        },
        "green": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {
                "band": "emad",
                "scale_from": edev_scaling,
            },
        },
        "blue": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {
                "band": "bcmad",
                "scale_from": bcdev_scaling,
            },
        },
    },
    "additional_bands": ["smad", "bcmad", "emad"],
}


layer = {
    "title": "Sentinel 1 GRD Gamma0 Annual Mosaic 20 m",
    "name": "csiro_s1_mosaic_20m",
    "abstract": "",
    "product_name": "csiro_s1_mosaic_annual_20m",
    "bands": {
        "vv_mean": [],
        "vh_mean": [],
        "vv_std": [],
        "vh_std": [],
        "vv_gm": [],
        "vh_gm": [],
        "emad": [],
        "smad": [],
        "bcmad": [],
        "count": [],
    },
    "dynamic": False,
    "resource_limits": reslim_continental,
    "time_resolution": "summary",
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
        "apply_solar_corrections": False,
    },
    "native_crs": "EPSG:3577",
    "native_resolution": [20, -20],
    "styling": {
        "default_style": "style_vh_over_vv_mean",
        "styles": [
            style_vh_over_vv_mean,
            style_vh_over_vv_gm,
            *styles.values(),
            style_count,
            style_tmad_rgb_std,
            style_tmad_sdev_std,
            style_tmad_edev_std,
            style_tmad_bcdev_std,
        ],
    },
}
