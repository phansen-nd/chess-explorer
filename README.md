# Chess Explorer
A way to consume the chess.com public API. 

## Set-up
Pretty lightweight so far. Just clone the repo on your machine (or fork it), change `chess_explorer.py` to be executable (`chmod +x chess_explorer.py`), and run it.

### Dependencies
Decided to use Python3 because that's what I happened to have on my computer. Could switch to Python2 before it's too late if there's a compelling reason.

Additionally, these packages can be installed with `pip` (`pip3`):
* [requests](https://requests.readthedocs.io/en/latest/)
* [dacite](https://github.com/konradhalas/dacite)

### Testing
You can run it with any valid chess.com username. If you don't have one feel free to try it out with *twopats* (me) or *hikaru*.
