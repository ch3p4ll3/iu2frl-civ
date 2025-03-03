class CivCommandException(BaseException):
    """
    This exception is generated when the CI-V response is NG 
    """
    message: str
    error_code: bytes

    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
    def __str__(self):
        return f"{self.message} (0x{self.error_code:02X})"


class CivTimeoutException(BaseException):
    """
    This exception is generated when the CI-V read gets over the timeout
    """
    pass
