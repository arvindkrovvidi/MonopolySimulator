class TileList(list):
    """
        A list of Properties. Data is a list.
    """
    def __init__(self, data):
        self.data = data
        # self.index = 0

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"TileList({repr(self.data)})"

    def __getitem__(self, key: int):
        """
        Get a tile from the list
        :param key: The tile number
        :return: Requested tile
        """
        if isinstance(key, int):
            if key < 0:
                raise IndexError(f"Tile number cannot be less than 0: {key}")
            for asset in self.data:
                if asset.tile_no == key:
                    return asset
            raise KeyError(f'Tile number {key} does not exist')
        else:
            raise KeyError(f"Tile number {key} does not exist")

    def __iter__(self):
        return iter(self.data)

    # def __next__(self):
    #     """
    #     Get the next tile in the list
    #     :return: next tile in the list
    #     """
    #     if self.index < len(self.data):
    #         result = self.data[self.index]
    #         self.index += 1
    #         return result
    #     else:
    #         self.index = 0
    #         raise StopIteration
    #
    def append(self, asset):
        """
        Add a tile to the list
        :param asset: The tile to be added to the list
        """
        if asset not in self.data:
            self.data.append(asset)
    #
    def __contains__(self, item):
        """
        Check if a tile exists in the list
        :param item:
        :return:
        """
        for asset in self.data:
            if asset.tile_no == item.tile_no:
                return True
        return False

    def __add__(self, other):
        """
        Overload the '+' operator to concatenate two tile lists
        :param other: The tile list to be concatenated to the first tile list
        :return: The concatenated tile list
        """
        for each in other:
            self.append(each)
        return self

    def __len__(self):
        return len(self.data)

    def remove(self, asset):
        self.data.remove(asset)

class TileDict:
    """
    A dictionary of properties and their owners. Data is a dictionary. Assets are list of properties. Values are list of players.
    """
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __getitem__(self, asset):
        """
        Get the owner of the tile
        :param asset: The tile
        :return: The owner of the tile
        """
        if asset in self.data:
            return self.data.get(asset)
        else:
            raise KeyError(f"{asset} does not exist in the dictionary")

    def __next__(self):
        """
        Get the next tile-person pair in the dictionary
        :return: Next tile-person pair
        """
        if self.index < len(list(self.data.keys())):
            result = self[list(self.data.keys())[self.index]]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __contains__(self, asset):
        """
        Check if tile exists in the dictionary
        :param asset: Tile
        :return:
        """
        for each in list(self.data.keys()):
            if each.tile_no == asset.tile_no:
                return each

    def update_dict(self, dictionary):
        """
        Add a Tile-Person pair to the dictionary
        :param dictionary:
        """
        self.data.update(dictionary)
        list(self.data.keys()).append(list(dictionary.keys())[0])

    def keys(self):
        """
        Return the list of tiles in the dictionary
        :return: List of tiles
        """
        return self.data.keys()
