import jwt
import datetime
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

# Define a secret key (should be kept safe!)
SECRET_KEY = "my_super_secret_key"

# Create a payload (data inside the token)
payload = {
    "user_id": 123,
    "username": "bhargav_rathod",
    "role": "admin",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60),  # token expires in 60 seconds
    "iat": datetime.datetime.utcnow(),  # issued at
    "nbf": datetime.datetime.utcnow()   # not before
}

# Encode the payload into a JWT token
def create_jwt_token():
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    print("JWT Token:\n", token)
    return token

# Decode the JWT token
def decode_jwt_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print("\n Decoded Payload:")
        for k, v in decoded.items():
            print(f"{k}: {v}")
        return decoded
    except ExpiredSignatureError:
        print("\n Token has expired!")
    except InvalidTokenError as e:
        print("\n Invalid Token:", e)

# Main demo
if __name__ == "__main__":
    print("Creating JWT Token...")
    token = create_jwt_token()

    print("\n Verifying token immediately:")
    decode_jwt_token(token)

    print("\n Waiting for token to expire (simulate by editing 'exp' time or using time.sleep())")
    # import time; time.sleep(61)  # uncomment to simulate expiration
    # decode_jwt_token(token)
