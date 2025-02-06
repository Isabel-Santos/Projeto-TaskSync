from flask_jwt_extended import jwt_required, get_jwt_identity
import jwt

def encode_token(user_id):
    return jwt.encode({'sub': user_id}, 'jwt_secret', algorithm = 'HS256')

def decode_token(token):
    try:
        return jwt.decode(token, 'jwt_secret', algorithm = ['HS256'])
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expirado!")
    
@jwt_required()
def get_current_user():
    return get_jwt_identity()