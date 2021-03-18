import jwt
from app import JWT_SECRET_KEY

def decode_token(bearer_token):
    token = bearer_token.split(" ")[1]
    return jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])