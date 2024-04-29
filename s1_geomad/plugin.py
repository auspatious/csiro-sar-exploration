"""
Sentinel-1 mosaic
"""

from typing import Tuple

import xarray as xr
from odc.algo import geomedian_with_mads
from odc.stats.plugins._registry import StatsPluginInterface, register

MEASUREMENTS = [
    "mean_vv",
    "mean_vh",
    "vv",
    "vh",
    "emad",
    "smad",
    "bcmad",
    "count",
]


class S1Mosaic(StatsPluginInterface):
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
        """ """
        # Make nodata nan
        return xx.where(xx != xx.vv.nodata)

    def reduce(self, xx: xr.Dataset) -> xr.Dataset:
        """ """
        gm = geomedian_with_mads(xx, work_chunks=self.chunks, num_threads=32)
        for band in ["vv", "vh"]:
            gm[f"median_{band}"] = xx[band].mean("time")

        return gm


register("s1-mosaic", S1Mosaic)
