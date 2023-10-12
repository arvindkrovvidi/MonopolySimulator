class PlayerBrokeError(Exception):
    def __init__(self, player):
        self.player = player
        self.exc_message = self.player + " is broke!"

class PropertyNotFreeError(Exception):
    exc_message = "Property is not free to buy"
    def __init__(self, asset):
        self.asset = asset
        self.exc_message = self.asset + " is not free to buy"