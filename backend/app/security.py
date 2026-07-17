from jose import jwt


def create_token(user):

    payload={
        "user":user
    }

    return jwt.encode(
        payload,
        "secret",
        algorithm="HS256"
    )