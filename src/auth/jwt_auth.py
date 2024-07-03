import jwt


def create_jwt_token(payload):
    secret_key = 'gmvb$MasterKey'
    algorithm = 'HS256'
    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token