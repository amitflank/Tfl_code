# --- Applied Boolean Logic Problems ---

scores = {
    "Alice": {"math": 85, "english": 78},
    "Bob": {"math": 90, "english": 82},
    "Charlie": {"math": 70, "english": 88},
    "Dana": {"math": 95, "english": 91},
    "Eve": {"math": 60, "english": 80},
    "Frank": {"math": 80, "english": 85}
}


# Problem 1: High Achievers
# Given a dictionary of student scores, return:
# - Students who scored at least 80 in both subjects (AND)
# - Students who scored at least 80 in either subject (OR)
# - Students who didn't score 80 in either subject (NOT with OR)
def high_achievers1(scores: dict) -> list:
    high_achievers = [] 
    for name, s in scores.items():
        if s["math"] >= 80 and s["english"] >= 80:
            high_achievers.append(name)
    return high_achievers

def high_achievers2(scores: dict) -> list:
    return [name for name, s in scores.items() if s["math"] >= 80 and s["english"] >= 80] #example of ternary operation in python

def partial_achievers1(scores: dict) -> list:
    partial_achievers = []
    for name, s in scores.items():  
        if s["math"] >= 80 or s["english"] >= 80:
            partial_achievers.append(name)
    return partial_achievers

def partial_achievers2(scores: dict) -> list:
    return [name for name, s in scores.items() if s["math"] >= 80 or s["english"] >= 80]

def underperformers(scores: dict) -> list:
    underperformers = []
    for name, s in scores.items():
        if s["math"] < 80 and s["english"] < 80:
            underperformers.append(name)
    return underperformers

def got_one_80(scores: dict) -> list:
    one_80 = []
    for name, s in scores.items():
        if s["math"] == 80 or s["english"] == 80:
            one_80.append(name)
    return one_80


# Problem 2: Movie Age Filter
# Return viewers who are allowed to watch a movie if they are 18+ OR have permission.

viewers = {
    "Eli": {"age": 17, "has_permission": True},
    "Fay": {"age": 20, "has_permission": False},
    "Gus": {"age": 15, "has_permission": False},
    "Hal": {"age": 18, "has_permission": True}
}

def allowed_viewers(viewers: dict) -> list:
    allowed = []
    for name, info in viewers.items():
        if info["age"] >= 18 or info["has_permission"]:
            allowed.append(name)
    return allowed


# Problem 3: Wi-Fi Diagnostics
# Return lists of devices based on connection and IP status.
# - Fully operational: connected AND has IP
# - Connected but broken: connected AND no IP
# - Either not connected OR no IP

devices = {
    "laptop": {"connected": True, "has_ip": True},
    "printer": {"connected": True, "has_ip": False},
    "phone": {"connected": False, "has_ip": False},
    "tablet": {"connected": True, "has_ip": True}
}


def fully_operational(devices: dict) -> list:
    fully_operational = []
    for name, d in devices.items():
        if d["connected"] and d["has_ip"]:
            fully_operational.append(name)
    return fully_operational


def connected_but_broken(devices: dict) -> list:
    not_broken = []
    for name, d in devices.items():
        if d["connected"] and not d["has_ip"]:
            not_broken.append(name)
    return not_broken


def not_connected_or_ipless(devices: dict) -> list:
    not_conected = []
    for name, d in devices.items():
        if not d["connected"] or not d["has_ip"]:
            not_conected.append(name)
    return not_conected

