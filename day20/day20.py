import re
import numpy as np
import copy

class Tile(object):
    _index = 0
    _size = 0

    def __init__(self, size, grid=None, borders=None):
        """TODO: to be defined. """
        if not borders:
            self._borders = [[np.zeros(shape = size, dtype='uint'), i] for i in range(4)]
        else:
            self._borders = borders
        if not grid:
            self._grid = np.zeros(shape = (size, size), dtype='uint')
        else:
            self._grid = grid
        self._size = size

        self._pHeader = re.compile('Tile\s(\d+)\:.*')


    def readTile(self, text):
        mHeader = self._pHeader.match(tile)
        self._index = int(mHeader.group(1))
        rows = re.split('\n', tile)
        for i, row in enumerate(rows[1:]):
            for j, char in enumerate(row):
                if char == '.':
                    self._grid[i][j] = 0
                if char == '#':
                    self._grid[i][j] = 1
        for i in range(self._size):
            self._borders[0][0][i] = self._grid[0][i]
            self._borders[1][0][i] = self._grid[i][-1]
            self._borders[2][0][i] = self._grid[-1][i]
            self._borders[3][0][i] = self._grid[i][0]

    def permutate(self, tf):
        return Tile(self._size, grid=self._grid, borders=self._borders)

    def __str__(self):
        res = ""
        res += "index : " + str(self._index) + "\n"
        for i in range(self._size):
            for j in range(self._size):
                res += str(self._grid[i][j])
            res += "\n"
        res += "\n"
        for i in range(4):
            for j in range(self._size):
                res += str(self._borders[i][0][j])
            res += "\n"
        return res



file = open('input.txt', 'r')
file = open('inputTest.txt', 'r')
text = file.read()


tileSplits = re.split('\n\n', text)
tiles = []



for tile in tileSplits:
    tiles.append(Tile(10))
    tiles[-1].readTile(tile)


newTile = tiles[-1].permutate([0, 0])
