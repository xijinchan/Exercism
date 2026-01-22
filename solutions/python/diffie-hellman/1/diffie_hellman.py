import secrets

def private_key(p):
    return secrets.randbelow(p-2)+2


def public_key(p, g, private):
    a = private
    return (g ** a) % p


def secret(p, public, private):
    return (public ** private) % p
