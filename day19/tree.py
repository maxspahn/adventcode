
class Tree(object):
    _children = {}
    _parent = {}
    _values = {}

    def __init__(self, parents={}, children={}, values={}):
        self._children = children
        self._parents = parents
        self._values = values

    def addSubtree(parent, subtree):
        assert isinstance(subtree, Tree)
        self._parents[subtree.getRoot()] = parent
        self._children[parent] = subtree

    def addChild(self, parent, child):
        if parent in self._children.keys():
            self._children[parent].append(child[0])
        else:
            print("append")
            self._children[parent] = [child[0]]
        self._parents[child[0]] = parent
        self._values[child[0]] = child[1]

    def getRoot(self):
        return self._root

    def __str__(self):
        return self._children.__str__() + self._parents.__str__() + self._values.__str__()

class OptionString(object):
    _options = []
    _index = 0

    def __init__(self, index, options=[]):
        self._options = options
        self._index = index

    def appendOption(self, options):
        self._options.append(options)

    def setOptions(self, i, options):
        assert (i < len(self._options))
        self._options[i] = options

    def addOption(self, i, option):
        if i < len(self._options):
            self._options[i].append(option)
        elif i == len(self._options):
            self._options.append([option])

    def clean(self):
        self._index = 0
        self._options.clear()

    def getOptions(self, i):
        return self._options[i]

    def len(self):
        return len(self._options)


    def __str__(self):
        return str(self._index) + ":" + self._options.__str__()

