import unittest

from luna import *


class RiseSetTests(unittest.TestCase):
    def setUp(self):
        self.location = Luna(45.394531, -122.694264)
        self.location2 = Luna(35.659725, 139.700157)

    def test_riseset(self):
        """
        makes sure that the riseset doesn't get stuck
        on any day in the next 2 years
        """
        riseSetList = []
        for i in range(0, 365*2):
            riseSetList.append(self.location.risesetlist(i, -7))
        self.assertEqual(len(riseSetList), 365*2)

    def test_riseset_japan(self):
        """
        makes sure that the riseset doesn't get stuck
        on any day in the next 2 years for a location in Japan
        """
        riseSetList = []
        for i in range(0, 365*2):
            riseSetList.append(self.location2.risesetlist(i, -7))
        self.assertEqual(len(riseSetList), 365*2)

class AzAltTests(unittest.TestCase):
    def setUp(self):
        self.location = Luna(45.394531, -122.694264)
        self.location2 = Luna(35.659725, 139.700157)
        
    def test_azalt_US(self):
        """
        Compares azimuth and altitude values to Nasa's
        HORIZONs ephemeris for US location
        """
        azdif = abs(self.location.calculate(2015,8,10,9,0,0)[0] - 57.7800)
        altdif = abs(self.location.calculate(2015,8,10,9,0,0)[1] - -5.7166)
        self.assertLess(azdif, 0.03)
        self.assertLess(altdif, 0.03)

        #25 years later, year 2040:
        
        azdif = abs(self.location.calculate(2040,8,10,9,0,0)[0] - 341.3909)
        altdif = abs(self.location.calculate(2040,8,10,9,0,0)[1] - -33.0098)
        self.assertLess(azdif, 0.03)
        self.assertLess(altdif, 0.03)

    def test_azalt_JA(self):
        """
        Compares azimuth and altitude values to Nasa's
        HORIZONs ephemeris for Japan Location
        """
        azdif = abs(self.location2.calculate(2015,8,10,9,0,0)[0] - 322.4536)
        altdif = abs(self.location2.calculate(2015,8,10,9,0,0)[1] - -27.5202)
        self.assertLess(azdif, 0.03)
        self.assertLess(altdif, 0.03)

        #25 years later, year 2040:
        
        azdif = abs(self.location2.calculate(2040,8,10,9,0,0)[0] - 264.9162)
        altdif = abs(self.location2.calculate(2040,8,10,9,0,0)[1] - 24.3637)
        self.assertLess(azdif, 0.03)
        self.assertLess(altdif, 0.03)
        
if __name__ == '__main__':
    unittest.main()
