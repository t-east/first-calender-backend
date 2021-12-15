from enum import IntEnum


class StatusCode(IntEnum):

    OK: int = 200
    BadRequest: int = 400
    Unauthorized: int = 401
    Forbidden: int = 403
    NotFound: int = 404
    UnprocessableEntity: int = 422
