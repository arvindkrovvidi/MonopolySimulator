class PlayerBrokeError(Exception):
    def __init__(self, player):
        self.player = player
        self.exc_message = str(self.player) + " is broke!"

class PropertyNotFreeError(Exception):
    def __init__(self, asset):
        self.asset = asset
        self.exc_message = str(self.asset) + " is already owned by" + str(self.asset.owner)

class InvalidPropertyTypeError(Exception):
    def __init__(self, function, asset):
        self.function = function
        self.asset = asset
        self.exc_message = "Cannot perform " + self.function.__name__ + " on type " + type(asset)

class InsufficientFundsError(Exception):

    def __init__(self, player):
        self.player = player
        self.exc_message = str(player) + " does not have sufficient funds for this transaction!"