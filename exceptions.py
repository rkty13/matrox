class DimensionError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class DoesNotExistError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)