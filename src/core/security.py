from pwdlib import PasswordHash

PasswordContext = PasswordHash.recommended()


class AuthSecurity:

    @staticmethod
    def hash_password(password : str):
        return PasswordContext.hash(password)
    
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return PasswordContext.verify(plain_password, hashed_password)