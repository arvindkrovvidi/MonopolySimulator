class PlayerBrokeError(Exception):
    def __init__(self, player):
        self.player = player
        self.exc_message = str(self.player) + " is broke!"

class PropertyNotFreeError(Exception):
    def __init__(self, asset):
        self.asset = asset
        self.exc_message = str(self.asset) + " is owned by " + str(self.asset.owner)

class InvalidPropertyTypeError(Exception):
    def __init__(self, function, asset):
        self.function = function
        self.asset = asset
        self.exc_message = "Cannot perform " + self.function + " on type " + str(type(asset))

class InsufficientFundsError(Exception):

    def __init__(self, player):
        self.player = player
        self.exc_message = str(player) + " does not have sufficient funds for this transaction!"

class CannotBuildHouseError(Exception):
    def __init__(self, player, asset):
        self.player = player
        self.asset = asset
        self.exc_message = f'{str(self.player)} cannot build house on {str(asset)}'

class CannotBuildHotelError(Exception):
    def __init__(self, player, asset):
        self.player = player
        self.asset = asset
        self.exc_message = f'{str(self.player)} cannot build hotel on {str(asset)}'

class CannotSellHouseError(Exception):
    def __init__(self, player, asset):
        self.asset = asset
        self.player = player
        self.exc_message = f'{str(self.player)} cannot sell the house on {str(asset)}'

class CannotSellHotelError(Exception):
    def __init__(self, player, asset):
        self.asset = asset
        self.player = player
        self.exc_message = f'{str(self.player)} cannot sell the hotel on {str(asset)}'

class UnownedPropertyError(Exception):
    def __init__(self, asset):
        self.asset = asset
        self.exc_message = f'No one owns {str(self.asset)}'

class SelfOwnedPropertyError(Exception):
    def __init__(self, player, asset):
        self.player = player
        self.asset = asset
        self.exc_message = f'{self.player} already owns {self.asset}'