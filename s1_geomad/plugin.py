"""
Sentinel-1 mosaic
"""

from typing import Tuple

import xarray as xr
from odc.stats.plugins._registry import StatsPluginInterface, register

MEASUREMENTS = [
    "mean_vv",
    "mean_vh",
    "median_vv",
    "median_vh",
    "std_vv",
    "std_vh",
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

    def native_transform(self, xx: xr.Dataset) -> xr.Dataset:
        """Rename lon,lat to x,y"""
        xx = xx.rename({"longitude": "x", "latitude": "y"})
        return xx

    def fuser(self, xx: xr.Dataset) -> xr.Dataset:
        """ """
        # Make nodata nan
        return xx.where(xx != xx.vv.nodata)

    def reduce(self, xx: xr.Dataset) -> xr.Dataset:
        """ """
        arrays = []
        for band in ["vv", "vh"]:
            arrays.append(xx[band].median(axis=0).rename(f"median_{band}"))
            arrays.append(xx[band].mean(axis=0).rename(f"mean_{band}"))
            arrays.append(xx[band].std(axis=0).rename(f"std_{band}"))

        # Add count
        arrays.append(xx["vv"].count(axis=0).rename("count").astype("int16"))

        # Merge the arrays together into a Dataset with the names we want
        mosaic = xr.merge(arrays, compat="override")

        return mosaic


register("s1-mosaic", S1Mosaic)
