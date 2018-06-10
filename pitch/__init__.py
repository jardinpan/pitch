"""A digital signal processing experiment on pitch tracking.

Pitch
=====
A digital signal processing experiment on pitch tracking.

Usage
-----
Firstly, import Pitch:
    >>> import pitch
To read and perform pitch:
    >>> audio = pitch.read('sample.mp3')
    >>> track_data = pitch.track(audio)
To visualize the tracking result:
    >>> track_data.visualize()
    >>> track_data.spectrum()

Author
------
Zilong Liang @ June, 2018

"""

from .util import *
from .track import *
