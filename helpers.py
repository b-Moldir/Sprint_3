import random
import string


def generate_email(domain='example.com'):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f'{username}@{domain}'