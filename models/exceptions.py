class InvalidCard(Exception):
    """Thrown on invalid card."""
    def __init__(self, message, card):
        self.message = message
        self.card = card
    
    def __str__(self):
        return self.message
