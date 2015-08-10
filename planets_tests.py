import unittest

from planets import *


class AzaltTests(unittest.TestCase):
    def setUp(self):
        self.location = Planets(45.394531, -122.694264)
        self.mercury = self.location.calcMercuryDate(2015, 8, 10, 9, 0, 0)
        self.venus = self.location.calcVenusDate(2015, 8, 10, 9, 0, 0)
        self.mars = self.location.calcMarsDate(2015, 8, 10, 9, 0, 0)
        self.jupiter = self.location.calcJupiterDate(2015, 8, 10, 9, 0, 0)
        self.saturn = self.location.calcSaturnDate(2015, 8, 10, 9, 0, 0)
        self.uranus = self.location.calcUranusDate(2015, 8, 10, 9, 0, 0)
        self.neptune = self.location.calcNeptuneDate(2015, 8, 10, 9, 0, 0)
        self.pluto = self.location.calcPlutoDate(2015, 8, 10, 9, 0, 0)
        
    def test_mercury(self):
        """comparing calculated valuse to expected values
        from NASA's HORIZONS ephemeris for a given location
        in Lake Oswego"""
        azdif = abs(self.mercury[0] - 353.0472)
        altdif = abs(self.mercury[1] - -33.4527)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_venus(self):
        azdif = abs(self.venus[0] - 6.4373)
        altdif = abs(self.venus[1] - -38.2337)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_mars(self):
        azdif = abs(self.mars[0] - 27.1314)
        altdif = abs(self.mars[1] - -19.1048)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_jupiter(self):
        azdif = abs(self.jupiter[0] - 358.4542)
        altdif = abs(self.jupiter[1] - -32.2345)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_saturn(self):
        azdif = abs(self.saturn[0] - 260.1354)
        altdif = abs(self.saturn[1] - -15.5868)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_uranus(self):
        azdif = abs(self.uranus[0] - 117.1776)
        altdif = abs(self.uranus[1] - 33.6988)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_neptune(self):
        azdif = abs(self.neptune[0] - 167.8573)
        altdif = abs(self.neptune[1] - 34.9076)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_pluto(self):
        azdif = abs(self.pluto[0] - 223.6936)
        altdif = abs(self.pluto[1] - 11.4794)
        self.assertLess(azdif, 0.2)
        self.assertLess(altdif, 0.2)
    
if __name__ == '__main__':
    unittest.main()
