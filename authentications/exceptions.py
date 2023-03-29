class NotFoundError(Exception):
    """
    Exception raised when a ticker is not found.
    """

    def __init__(self, message=""):
        self.message = message
