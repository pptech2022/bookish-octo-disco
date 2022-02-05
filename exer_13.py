import requests, json, re

randomness = []
latest_round = -1
reqs = 99

def get_latest_req():
    req = requests.get('https://drand.cloudflare.com/public/latest')
    req = json.loads(req.content)
    global latest_round
    latest_round = req["round"]
    tmp_randomness = req["randomness"]
    print("The requestred string")
    print("================================================")
    print(tmp_randomness)
    print()
    for i in range(0, len(tmp_randomness), 2):
        randomness.append(hex(int(tmp_randomness[i:i+2], 16)))

def compare_to_kino_numbers():
    req = requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
    req = json.loads(req.content)
    return req["last"]["winningNumbers"]["list"]

def get_the_results():
    get_latest_req()
    integers = []
    print("The hex numbers")
    print("================================================")
    print(randomness)
    print()
    for r in randomness:
        integers.append(int(r, base=16))
    print("The integers")
    print("================================================")
    print(integers)
    print()
    integers = [j%80 for j in integers]
    print("The modulo integers")
    print("================================================")
    print(integers)
    print()
    integers = sorted(list(dict.fromkeys(integers)))
    print("Delete duplicates integers")
    print("================================================")
    print(integers)
    print()
    print("Integers in Kino")
    print("================================================")
    kino_numbers = compare_to_kino_numbers()
    for i in integers:
        if(i in kino_numbers):
            print(i, end=" ")
    print()

get_the_results()