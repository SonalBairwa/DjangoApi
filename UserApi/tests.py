import random
import string

a=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(14))
print(a)