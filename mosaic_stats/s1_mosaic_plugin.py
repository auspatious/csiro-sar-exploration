"""
Sentinel-1 mosaic
"""

from typing import Tuple

import xarray as xr

from odc.stats.plugins._registry import StatsPluginInterface, register

MEASUREMENTS = ["mean_vv", "mean_vh", "median_vv", "median_vh", "std_vv", "std_vh", "count"]


class S1Mosaic(StatsPluginInterface):
    NAME = "s1_mosaic"
    SHORT_NAME = NAME
    VERSION = "0.0.0"
    PRODUCT_FAMILY = "general"

    def __init__(
        self,
        **kwargs
    ):
        super().__init__(input_bands=["vv", "vh"], **kwargs)

    @property
    def measurements(self) -> Tuple[str, ...]:
        measurements = ["mean_vv", "mean_vh"]

        return tuple(measurements)

    def fuser(self, xx: xr.Dataset) -> xr.Dataset:
        """
        """
        # Nothing to do here...

        return xx

    def native_transform(self, xx: xr.Dataset) -> xr.Dataset:
        """
        """
        # Nothing to do here either
        return xx

    def reduce(self, xx: xr.Dataset) -> xr.Dataset:
        """
        """

        arrays = []
        for band in ["vv", "vh"]:
            arrays.append(xx[band].median("time").rename(f"median_{band}"))
            arrays.append(xx[band].mean("time").rename(f"mean_{band}"))
            arrays.append(xx[band].std("time").rename(f"std_{band}"))

        # Add count
        arrays.append(xx["vv"].count("time").rename("count").astype("int16"))

        # Merge the arrays together into a Dataset with the names we want
        mosaic = xr.merge(arrays, compat="override")

        return mosaic


register("s1-mosaic", S1Mosaic)
