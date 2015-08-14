import unittest

from planets import *


class AzaltTests(unittest.TestCase):
    def setUp(self):
        #set up first location
        self.location = Planets(45.394531, -122.694264)
        self.mercury = self.location.calcMercuryDate(2015, 8, 10, 9, 0, 0)
        self.venus = self.location.calcVenusDate(2015, 8, 10, 9, 0, 0)
        self.mars = self.location.calcMarsDate(2015, 8, 10, 9, 0, 0)
        self.jupiter = self.location.calcJupiterDate(2015, 8, 10, 9, 0, 0)
        self.saturn = self.location.calcSaturnDate(2015, 8, 10, 9, 0, 0)
        self.uranus = self.location.calcUranusDate(2015, 8, 10, 9, 0, 0)
        self.neptune = self.location.calcNeptuneDate(2015, 8, 10, 9, 0, 0)
        self.pluto = self.location.calcPlutoDate(2015, 8, 10, 9, 0, 0)

        self.location2 = Planets(35.659725, 139.700157)
        self.mercury2 = self.location2.calcMercuryDate(2015, 8, 10, 9, 0, 0)
        self.venus2 = self.location2.calcVenusDate(2015, 8, 10, 9, 0, 0)
        self.mars2 = self.location2.calcMarsDate(2015, 8, 10, 9, 0, 0)
        self.jupiter2 = self.location2.calcJupiterDate(2015, 8, 10, 9, 0, 0)
        self.saturn2 = self.location2.calcSaturnDate(2015, 8, 10, 9, 0, 0)
        self.uranus2 = self.location2.calcUranusDate(2015, 8, 10, 9, 0, 0)
        self.neptune2 = self.location2.calcNeptuneDate(2015, 8, 10, 9, 0, 0)
        self.pluto2 = self.location2.calcPlutoDate(2015, 8, 10, 9, 0, 0)

        
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

    def test_mercury2(self):
        """comparing calculated valuse to expected values
        from NASA's HORIZONS ephemeris for a given location
        in Japan"""
        azdif = abs(self.mercury2[0] - 271.1972)
        altdif = abs(self.mercury2[1] - 17.2541)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_venus2(self):
        azdif = abs(self.venus2[0] - 273.5674)
        altdif = abs(self.venus2[1] - 5.6328)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_mars2(self):
        azdif = abs(self.mars2[0] - 298.4337)
        altdif = abs(self.mars2[1] - -2.8391)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_jupiter2(self):
        azdif = abs(self.jupiter2[0] - 275.0555)
        altdif = abs(self.jupiter2[1] - 14.3686)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_saturn2(self):
        azdif = abs(self.saturn2[0] - 176.0815)
        altdif = abs(self.saturn2[1] - 36.3586)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_uranus2(self):
        azdif = abs(self.uranus2[0] - 43.6752)
        altdif = abs(self.uranus2[1] - -36.3215)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_neptune2(self):
        azdif = abs(self.neptune2[0] - 87.0609)
        altdif = abs(self.neptune2[1] - -19.5243)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_pluto2(self):
        azdif = abs(self.pluto2[0] - 130.8946)
        altdif = abs(self.pluto2[1] - 15.5723)
        self.assertLess(azdif, 0.2)
        self.assertLess(altdif, 0.2)

class FutureTests(unittest.TestCase):
    def setUp(self):
        """Testing to see if still accurate
        25 years in the future. Again by comparing to expected
        values from NASA's HORIZONs ephemeris"""
        self.location = Planets(45.394531, -122.694264)
        self.mercury = self.location.calcMercuryDate(2040, 8, 10, 9, 0, 0)
        self.venus = self.location.calcVenusDate(2040, 8, 10, 9, 0, 0)
        self.mars = self.location.calcMarsDate(2040, 8, 10, 9, 0, 0)
        self.jupiter = self.location.calcJupiterDate(2040, 8, 10, 9, 0, 0)
        self.saturn = self.location.calcSaturnDate(2040, 8, 10, 9, 0, 0)
        self.uranus = self.location.calcUranusDate(2040, 8, 10, 9, 0, 0)
        self.neptune = self.location.calcNeptuneDate(2040, 8, 10, 9, 0, 0)
        self.pluto = self.location.calcPlutoDate(2040, 8, 10, 9, 0, 0)

    def test_mercury(self):
        """comparing calculated valuse to expected values
        from NASA's HORIZONS ephemeris for a given location
        in Lake Oswego"""
        azdif = abs(self.mercury[0] - 14.3278)
        altdif = abs(self.mercury[1] - -25.5597)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_venus(self):
        azdif = abs(self.venus[0] - 350.1652)
        altdif = abs(self.venus[1] - -34.1148)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_mars(self):
        azdif = abs(self.mars[0] - 326.2909)
        altdif = abs(self.mars[1] - -37.6001)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_jupiter(self):
        azdif = abs(self.jupiter[0] - 321.9995)
        altdif = abs(self.jupiter[1] - -37.0401)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_saturn(self):
        azdif = abs(self.saturn[0] - 312.6558)
        altdif = abs(self.saturn[1] - -35.2244)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_uranus(self):
        azdif = abs(self.uranus[0] - 24.9104)
        altdif = abs(self.uranus[1] - -21.2100)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_neptune(self):
        azdif = abs(self.neptune[0] - 101.6701)
        altdif = abs(self.neptune[1] - 27.6615)
        self.assertLess(azdif, 0.05)
        self.assertLess(altdif, 0.05)

    def test_pluto(self):
        azdif = abs(self.pluto[0] - 179.6168)
        altdif = abs(self.pluto[1] - 22.1272)
        self.assertLess(azdif, 0.2)
        self.assertLess(altdif, 0.2)

if __name__ == '__main__':
    unittest.main()
