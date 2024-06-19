"""
Sentinel-1 GeoMAD and other Statistics
"""

from functools import partial
from typing import Tuple

import xarray as xr
from datacube_compute import geomedian_with_mads
from numpy import nan as np_nan
from odc.algo._masking import _first_valid_np, _xr_fuse
from odc.stats.plugins._registry import StatsPluginInterface, register


# s1_geomad/plugin.S1GeoMAD
class S1GeoMAD(StatsPluginInterface):
    NAME = "s1_mosaic"
    SHORT_NAME = NAME
    VERSION = "0.0.0"
    PRODUCT_FAMILY = "general"

    def __init__(
        self,
        geomad_work_chunks: Tuple[int, int] = (600, 600),
        geomad_threads: int = 32,
        **kwargs,
    ):
        self.geomad_work_chunks = geomad_work_chunks
        self.geomad_threads = geomad_threads
        super().__init__(input_bands=["vv", "vh"], **kwargs)

    @property
    def measurements(self) -> Tuple[str, ...]:
        return (
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
        )

    def native_transform(self, xx: xr.Dataset) -> xr.Dataset:
        # Make sure nodata is nan
        xx = xx.where(xx != xx.vv.nodata)
        xx.attrs["nodata"] = np_nan
        for dv in xx.data_vars.values():
            dv.attrs.pop("nodata", None)

        return xx

    def fuser(self, xx: xr.Dataset) -> xr.Dataset:
        return _xr_fuse(xx, partial(_first_valid_np, nodata=np_nan), "")

    def reduce(self, xx: xr.Dataset) -> xr.Dataset:
        print("NODATA", xx.attrs.get("nodata", None))
        gm = geomedian_with_mads(
            xx, work_chunks=self.geomad_work_chunks, num_threads=self.geomad_threads
        )
        for band in ["vv", "vh"]:
            gm[f"{band}_mean"] = xx[band].mean("spec")
            gm[f"{band}_std"] = xx[band].std("spec")

            # Rename bands
            gm = gm.rename({band: f"{band}_gm"})

        return gm


register("s1-mosaic", S1GeoMAD)
