# glow-orb
python programs for calculating sunset/sunrise times, moon position, etc.

sun2.py:

Uses longitude and latitude to calculate sunset time, sunrise time, solar noon,
and sunlight duration for the present day.

It also contains code for calculating the present time on a Wadokei, a
disused timekeeping method that started use in Edo era Japan. This way
of timekeeping basically divides day and night each into six equal
hours, so the clock hand moves at a different speed during night and
day.

More information on wadokei is available on wikipedia:
http://en.wikipedia.org/wiki/Japanese_clock

wadokeinew.py:
This code is a menu for selecting one of multiple cities, or alternatively the user can input custom coordinates. The code will then render a continuously updating wadokei for that location.

luna.py:

This contains an object for calculting the moon position for a given location. Should be accurate to within about 4 arc minutes.
