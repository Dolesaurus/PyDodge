# PyDodge
numpy/PyQt4 based game

The objective of this game is to survive as long as possible, evaiding every bullets flying around.

The original work of this game is "special training 99" which can be found on http://bee.in.coocan.jp/tk/ , though the detail algorithm and scoring might be different. 
I implemented this game on Python to apply RL and let an AI learn to play this game. I will work on building AI by myself, but if anyone wants to tryout this game with your own algorithm, it will be welcome!

pydodge.py::The main file
play_dodge.py::PyQt4 based gui running the game, press any key to startover, WASD/ arrows to control

TODO lists:
 - Make spawning rate and maximum velocity vary over time.
 - Release some hard-coded variables
 - It is bugged when I press 2 keys concurrently and release one of them.
