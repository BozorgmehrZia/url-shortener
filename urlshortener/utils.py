import random
import string

N = 6

def get_random_string():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))