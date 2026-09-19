from authlib.jose import JoseError, jwt
import time

JWT_SECRET='zJ3pIzorHY0GMIxPncUcs76xJq8BnGFI+md5HDY7Bps='

def encode(data):
    payload = {
        "data": data,
        "exp": int(time.time()) + 3600,
    }
    token = jwt.encode(payload=payload, header={"alg": "HS256"}, key=JWT_SECRET)
    return token.decode("utf-8")

def decode(token):
    try:
        return jwt.decode(token, JWT_SECRET) 
    except JoseError:
        return None

