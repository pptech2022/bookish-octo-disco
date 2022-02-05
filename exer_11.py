import requests, json
import math

randomness = []
latest_round = -1
reqs = 19

def get_latest_req():
    req = requests.get('https://drand.cloudflare.com/public/latest')
    req = json.loads(req.content)
    global latest_round
    latest_round = req["round"]
    randomness.append(req["randomness"])

def get_the_rest_of_the_req():
    for r in range(0, reqs):
        round = latest_round - reqs + r
        req = requests.get('https://drand.cloudflare.com/public/'+str(round))
        req = json.loads(req.content)
        randomness.append(req["randomness"])

def get_entropy(string):
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])
    return entropy

def get_the_results():
    print("-> Retrieving the "+ str(reqs+1) +" latest requests...")
    get_latest_req()
    get_the_rest_of_the_req()
    data = ''.join(randomness)
    print("-> Generated string")
    print(data)
    print("-> Entropy :", get_entropy(data))

get_the_results()