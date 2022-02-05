import random, hashlib

AM = "17216"
tmp = hashlib.sha256(AM.encode()).hexdigest()
seed = int (tmp, 16)
random.seed(seed)
exercises_list = list(range(1, 14))
random.shuffle(exercises_list)
print(exercises_list[:4])