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
        azdif = abs(degrees(self.location.calclist(2015,8,10,9,0,0)[5]) - 57.7800)
        altdif = abs(degrees(self.location.calclist(2015,8,10,9,0,0)[6]) - -5.7166)
        self.assertLess(azdif, 0.03)
        self.assertLess(altdif, 0.03)

        #25 years later, year 2040:
        
        azdif = abs(degrees(self.location.calclist(2040,8,10,9,0,0)[5]) - 341.3909)
        altdif = abs(degrees(self.location.calclist(2040,8,10,9,0,0)[6]) - -33.0098)
        self.assertLess(azdif, 0.03)
        self.assertLess(altdif, 0.03)

    def test_azalt_JA(self):
        """
        Compares azimuth and altitude values to Nasa's
        HORIZONs ephemeris for Japan Location
        """
        azdif = abs(degrees(self.location2.calclist(2015,8,10,9,0,0)[5]) - 322.4536)
        altdif = abs(degrees(self.location2.calclist(2015,8,10,9,0,0)[6]) - -27.5202)
        self.assertLess(azdif, 0.03)
        self.assertLess(altdif, 0.03)

        #25 years later, year 2040:
        
        azdif = abs(degrees(self.location2.calclist(2040,8,10,9,0,0)[5]) - 264.9162)
        altdif = abs(degrees(self.location2.calclist(2040,8,10,9,0,0)[6]) - 24.3637)
        self.assertLess(azdif, 0.03)
        self.assertLess(altdif, 0.03)
        
if __name__ == '__main__':
    unittest.main()
