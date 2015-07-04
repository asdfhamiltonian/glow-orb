# glow-orb
python programs for calculating sunset/sunrise times, moon position, etc.

sun2.py:

Uses longitude and latitude to calculate sunset time, sunrise time, solar noon,
and sunlight duration for the present day.

It also contains code for calculating the present time on a Wadokei, a
type of mechanical solar clock that was used in Edo era Japan. This method
of timekeeping divides day and night into six hours each, so the clock hand
needs to move at a different speed depending on if it is night or day.

More information on wadokei is available on wikipedia:
http://en.wikipedia.org/wiki/Japanese_clock

wadokeinew.py:
This code includes a menu for selecting one of multiple cities, or alternatively the user can input custom coordinates. The code will then render a continuously updating wadokei for that location.

luna.py:
Contains a python object for calculting the moon's relative position for a given location on earth. Should be accurate to within about 4 arc minutes.

planets.py:
Contains a python object for calculating the apparent position of any planet for a given location on earth.
