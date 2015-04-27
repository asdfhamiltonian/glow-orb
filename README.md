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

More information on wadokei are available on wikipedia:
http://en.wikipedia.org/wiki/Japanese_clock

If the entire code is run, it will display a wadokei time for the
location entered on line 175.

wadokeinew.py:

This code basically adds a menu to sun2.py. Multiple cities are available from the menu, or alternatively the user
can input their own coordinates. Still haven't found a gracefull way to exit the tkinter display loop at the end though
so it's a bit of a work in progress

luna.py:

This contains an object for calculting the moon position for a given location. Should be accurate to within about 4 arc minutes.
