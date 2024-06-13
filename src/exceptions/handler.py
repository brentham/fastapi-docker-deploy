from fastapi import HTTPException, status

def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }

def http_exception():
    return HTTPException(status_code=404, detail="Route not found")


def get_user_exception():
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    return credentials_exception

def token_exception():
    token_exception_response = HTTPException(status.HTTP_401_UNAUTHORIZED, detail="incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    return token_exception