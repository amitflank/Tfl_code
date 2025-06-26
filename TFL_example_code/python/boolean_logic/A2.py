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
# - Students who didn't score at least 80 in either subject (NOT with OR)
# - Students who scored exactly 80 in at lest one subject
def high_achievers(scores: dict) -> list:
    pass # replace with your code

def partial_achievers(scores: dict) -> list:
    pass # replace with your code

def underperformers(scores: dict) -> list:
    pass # replace with your 

def got_one_80(scores: dict) -> list:
    pass

# Problem 2: Movie Age Filter
# Return viewers who are allowed to watch a movie if they are 18+ OR have permission.

viewers = {
    "Eli": {"age": 17, "has_permission": True},
    "Fay": {"age": 20, "has_permission": False},
    "Gus": {"age": 15, "has_permission": False},
    "Hal": {"age": 18, "has_permission": True}
}

def allowed_viewers(viewers: dict) -> list:
    pass # replace with your code

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
    pass # replace with your code

def connected_but_broken(devices: dict) -> list:
   pass # replace with your code

def not_connected_or_ipless(devices: dict) -> list:
    pass # replace with your code

