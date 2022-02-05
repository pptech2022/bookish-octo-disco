import requests, json, re

randomness = []
latest_round = -1
reqs = 99

def get_latest_req():
    req = requests.get('https://drand.cloudflare.com/public/latest')
    req = json.loads(req.content)
    global latest_round
    latest_round = req["round"]
    randomness.append(''.join(format(ord(x), 'b') for x in req["randomness"]))

def get_the_rest_of_the_req():
    for r in range(0, reqs):
        round = latest_round - reqs + r
        req = requests.get('https://drand.cloudflare.com/public/'+str(round))
        req = json.loads(req.content)
        randomness.append(''.join(format(ord(x), 'b') for x in req["randomness"]))

def get_the_results():
    print("-> Retrieving the "+ str(reqs+1) +" latest requests...")
    get_latest_req()
    get_the_rest_of_the_req()
    data = ''.join(randomness)
    print("-> Generated binary")
    print(data)
    print()
    print("-> Biggest sequence of zeros")
    print(max(re.compile("(0+0)*").findall(data)))
    print()
    print("-> Biggest sequence of ones")
    print(max(re.compile("(1+1)*").findall(data)))

get_the_results()