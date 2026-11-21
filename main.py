import sys
import time
import random
def slow (text, delay=0.025):
    """prints text like its being typed, very dramatic"""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def pause(s=1.0):
    time.sleep(s)
HOUSE={
    "bedroom":["hallway"],
    "hallway":["bedroom", "bathroom", "living room", "basement"],
    "bathroom":["hallway"],
    "living room":["hallway", "kitchen"],
    "kitchen":["living room"],
    "basement":["hallway"],
}
DESCRIPTIONS={
    "bedroom":"your bedroom. the blanket is warm and its way too late",
    "hallway":"the hallway. the floorboards creek even when you stay still, weird",
    "bathroom":"the bathroom. the mirror is fogged up...and someone drew a lil smiley on it",
    "living room":"the living room. the tv shows static but you KNOW you turned it off",
    "kitchen":"the kitchen. the fridge hums and one cbinet door slowly swings open by itself",
    "basement":"the basement. cold. dark. someting is breathing down there (not you)",
}
player = "bedroom"
ghost="basement"
has_flashlight=False
has_key=False
battery=2
minutes=0
items ={"bedroom":"falshlight","kitchen":"key"}

def clock():
    return f"3:{minutes:02d} AM"

def next_step_toward(start, goal):
    """BFS so the ghost can chase you (yes i googled this)"""
    if start == goal:
        return start
    queue =[(start, [start])]
    seen={start}
    while queue:
        room, path = queue.pop(0)
        for n in HOUSE[room]:
            if n == goal:
                return (path + [n])[1]
            if n not in seen:
                seen.add(n)
                queue.append((n, path + [n]))
    return start
def move_ghost():
    global ghost
    if random.random() < 0.55:
        ghost = next_step_toward(ghost, player)
    else:
        ghost = random.choice(HOUSE[ghost])