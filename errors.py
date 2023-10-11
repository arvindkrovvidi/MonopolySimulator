class PlayerBrokeError(Exception):
    exc_message = "Player is broke!"

class PropertyNotFreeError(Exception):
    exc_message = "Property is not free to buy"