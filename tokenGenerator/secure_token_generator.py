import secrets

def secure_token_generator():
    return str(secrets.randbelow(900000)+100000)
print(f"Your token: {secure_token_generator()}")
