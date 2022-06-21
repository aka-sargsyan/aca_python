class Error_value(Exception):
    def __init__(self, value):
        self.value = value

    def get_error_value(self):
        return f'ther are no {self.value} measurement'