"""Massive Bodies of the Solar System and Extra Solar Bodies

Contains some predefined massive bodies of the Solar System:

* Sun (☉)
* Moon (☾)
* Mercury (☿)
* Venus (♀)
* Mars (♂)
* Jupiter (♃)
* Saturn (♄)
* Uranus (⛢)
* Neptune (♆)
* Pluto (♇)

Contains some predefined stars defined in :py:class: `~ephem.Star` class.


and a way to define new bodies (:py:class:`~SkyCustom` class).
"""
from ephem import *
from math import radians


class SolarMassive(object):
    """Massive Objects Class.
    """

    def __init__(self, name):
        """Constructor.

        Parameters
        ----------
        name : str
            Name of the body.
        """
        self.body_name = name
        self.body_name = self.body_name.capitalize()
        self.objects = [Saturn(), Mars(), Moon(), Jupiter(), Uranus(), Neptune(), Mercury(), Venus(), Sun(), Pluto()]   # BoilerPlate
        self._indata = False

    def get(self):
        for obj_req in self.objects:
            if obj_req.name == self.body_name:
                self._indata = True
                return obj_req

        if not self._indata:
            raise ValueError('The body queried not present in the inbuilt database, try :py:class:`~SkyCustom` class.')


def _convDegtoDMS(dd):
    mnt, sec = divmod(dd * 3600, 60)
    deg, mnt = divmod(mnt, 60)
    deg_val = str(int(deg)) + ":" + str(int(mnt)) + ":" + str(int(sec)) + ".0"
    return deg_val


class SkyCustom:
    """Class to define your own objects."""

    def __init__(self, name, ra, dec):
        """Constructor.

        Parameters
        ----------
        name : string
            Name of the body.
        ra : string
            Right Ascension of the body
        dec : string
            Declination of the body
        """
        self.name = name
        self.ra = ra
        self.dec = dec
        self.obj = FixedBody()

    @classmethod
    def from_ra_dec_deg(cls, ra, dec, name="Custom Body"):
        """Return sky positions from angles in degrees.

        Parameters
        ----------
        ra : float
            Right Ascension of the body
        dec : float
            Declination of the body
        name : string (optional)
        """
        ra_c = _convDegtoDMS(ra)
        dec_c = _convDegtoDMS(dec)
        return cls(name, ra_c, dec_c)

    @classmethod
    def from_ra_dec_dms(cls, ra, dec, name="Custom Body"):
        """Return sky positions from angles in degrees.

        Parameters
        ----------
        ra : string
            Right Ascension of the body
        dec : string
            Declination of the body
        name : string (optional)
        """
        return cls(name, ra, dec)

    def get(self):
        self.obj.name = self.name
        self.obj._ra = self.ra
        self.obj._dec = self.dec
        return self.obj


class SkyStars:
    """Class SkyStars.
    """

    def __init__(self, name):
        """Constructor.

        Parameters
        ----------
        name : str
            Name of the star.
        """
        self._list = [
            "Polaris", "Vega", "Deneb", "Altair", "Caph", "Schedar", "Scheat",
            "Algenib", "Fomalhaut", "Hamal", "Aldebaran", "Atlas", "Capella",
            "Menkalinan", "Achernar", "Elnath", "Bellatrix", "Rigel", "Mintaka",
            "Alnilam", "Betelgeuse", "Alnitak", "Saiph", "Castor", "Sirius", "Dubhe",
            "Procyon", "Pollux", "Merak", "Canopus", "Megrez", "Phecda", "Alphard",
            "Algieba", "Regulus", "Alioth", "Mizar", "Denebola", "Alcaid", "Sirrah"
        ]
        self.body_name = name
        self._indata = False
        self.body_name = self.body_name.capitalize()

    def get(self):
        for body in self._list:
            if body == self.body_name:
                self._indata = True
                return star(body)
        if not self._indata:
            raise ValueError('The body queried not present in the inbuilt database, try :py:class:`~SkyCustom` class.')
