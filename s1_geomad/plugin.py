"""
Sentinel-1 GeoMAD and other Statistics
"""

from typing import Tuple

import numpy as np
import xarray as xr
from odc.algo import geomedian_with_mads
from odc.stats.plugins._registry import StatsPluginInterface, register

MEASUREMENTS = [
    "vv_mean",
    "vh_mean",
    "vv_std",
    "vh_std",
    "vv_gm",
    "vh_gm",
    "emad",
    "smad",
    "bcmad",
    "count",
]


class S1GeoMAD(StatsPluginInterface):
    NAME = "s1_mosaic"
    SHORT_NAME = NAME
    VERSION = "0.0.0"
    PRODUCT_FAMILY = "general"

    def __init__(self, **kwargs):
        super().__init__(input_bands=["vv", "vh"], **kwargs)

    @property
    def measurements(self) -> Tuple[str, ...]:
        return tuple(MEASUREMENTS)

    def fuser(self, xx: xr.Dataset) -> xr.Dataset:
        # Make sure nodata is nan
        xx = xx.where(xx != xx.vv.nodata)
        xx.attrs["nodata"] = np.nan
        return

    def reduce(self, xx: xr.Dataset) -> xr.Dataset:
        gm = geomedian_with_mads(xx, work_chunks=self.chunks, num_threads=32)
        for band in ["vv", "vh"]:
            gm[f"{band}_mean"] = xx[band].mean("time")
            gm[f"{band}_std"] = xx[band].std("time")

            # Rename bands
            gm = gm.rename({band: f"{band}_gm"})

        return gm


register("s1-mosaic", S1GeoMAD)
