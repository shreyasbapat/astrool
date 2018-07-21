import pytest

from astrool.radec import SolarMassive, SkyStars, SkyCustom

def test_SolarMassive_pops_Value_Error():
    body = "Random"
    with pytest.raises(ValueError):
        a = SolarMassive(body).get()
