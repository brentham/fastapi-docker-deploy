from fastapi import HTTPException, status

class CustomHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)
        
def not_found_exception(detail: str):
    return CustomHTTPException(status.HTTP_404_NOT_FOUND, detail=detail)