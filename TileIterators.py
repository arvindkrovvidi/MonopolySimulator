class TileList:
    """
        A list of Properties. Data is a list.
    """
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0:
                raise IndexError("Tile number does not exist")
            for asset in self.data:
                if asset.tile_no == key:
                    return asset
        else:
            raise TypeError("Invalid key")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def append(self, asset):
        self.data.append(asset)

    def __contains__(self, item):
        for asset in self.data:
            if asset.tile_no == item.tile_no:
                return item

    def __add__(self, other):
        for each in other:
            self.append(each)
        return self

class TileDict:
    """
    A dictionary of properties and their owners. Data is a dictionary. assets are list of properties. Values are list of players.
    """
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __getitem__(self, asset):
        if asset in self.data:
            return self.data.get(asset)
        else:
            raise KeyError(f"{asset} does not exist in the dictionary")

    def __next__(self):
        if self.index < len(list(self.data.keys())):
            result = self[list(self.data.keys())[self.index]]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __contains__(self, asset):
        for each in list(self.data.keys()):
            if each.tile_no == asset.tile_no:
                return each

    def update_dict(self, dictionary):
        self.data.update(dictionary)
        list(self.data.keys()).append(list(dictionary.keys())[0])
