import jwt
from datetime import datetime, timedelta

def generate_jwt_token(user_id, user_name):
    secret_key="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    payload = {
        "user_id": user_id,
        "user_name": user_name,
        "exp": datetime.utcnow() + timedelta(days=1)  # Tempo de expiração do token
    }
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token
