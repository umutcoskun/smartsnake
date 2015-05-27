class SnakeException(Exception):
    def __init__(self, message=''):
        super(SnakeException, self).__init__(message)