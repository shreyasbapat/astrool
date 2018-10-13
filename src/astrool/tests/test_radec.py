import ephem
import pytest

from astrool.radec import SolarMassive, SkyStars, SkyCustom


def test_SolarMassive_pops_Value_Error():
    body = "Random"
    with pytest.raises(ValueError):
        SolarMassive(body).get()


def test_SkyStars_creation():
    body = 'Polaris'
    assert isinstance(SkyStars(body).get(), ephem.FixedBody)

    bad_body = 'Random'
    with pytest.raises(ValueError):
        SkyStars(bad_body).get()

    body_badcase = 'pOlArIs'
    assert isinstance(SkyStars(body_badcase).get(), ephem.FixedBody)
