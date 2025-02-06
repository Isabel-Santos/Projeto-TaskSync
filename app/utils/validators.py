def validate_email(email):
    if '@' not in email:
        raise ValueError("Invalid email address")
