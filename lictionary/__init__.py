import collections

class Lictionary(collections.MutableSequence):
    __slots__ = ('_items',)

    def __init__(self, items=None):
        super(Lictionary, self).__init__()
        self._items = items or []

    @property
    def items(self):
        return self._items
    
    def insert(self, index, item):
        self._items.insert(index, item)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._items[key]
        else:
            # TODO(nicholasbishop): simple implementation for now, not
            # efficient for large number of items
            for ele in reversed(self._items):
                if isinstance(ele, tuple) and len(ele) == 2 and ele[0] == key:
                    return ele[1]
            raise KeyError('not found')

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self._items[key] = value
        else:
            raise NotImplementedError()

    def __delitem__(self, key):
        raise NotImplementedError()

    def __len__(self):
        return len(self._items)

    def get(self, key, default=None):
        try:
            return self[key]
        except (IndexError, KeyError):
            return default
