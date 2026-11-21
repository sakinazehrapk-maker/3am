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

def hints():
    if ghost in HOUSE[player]:
        slow(random.choice([
            "you hear scratching from the next room...",
            "a cold breeze creeps under the door. something is CLOSE.",
            "someone whispers your name. from the room next to you.",
        ]))
    elif random.random() < 0.3:
        slow(random.choice([
            "somewhere in the house, a floorboard creaks.",
            "you hear humming. its a lullaby. nobody lives here who hums.",
            "Your phone buzzes. Unknown number. It just says: 'behind you'.",
        ]))
def ghost_encounter():
    """returns True if you survive"""
    global battery, ghost
    print()
    slow("!!! THE GHOST IS IN THE ROOM !!!", 0.05)
    if has_flashlight and battery > 0:
        slow("Type 'light' to blast it with your flashlight!")
        start = time.time()
        answer = input("> ").strip().lower()
        if answer == "light" and time.time() - start < 5:
            battery -= 1
            ghost = "basement"
            slow("The beam hits it. It SCREAMS and melts into the walls.")
            slow(f"(flashlight battery: {battery} left)")
            return True
    else:
        slow("You reach for a flashlight... but you don't have one (or it's dead).")
    return False
def game_over():
    pause()
    slow("Everything goes cold. The lights go out.")
    pause()
    slow("The last thing you see is your phone: 3:" + f"{minutes:02d}" + " AM.")
    pause()
    slow("YOU DIED. Better luck next night.", 0.06)
    sys.exit()
def win(text):
    pause()
    slow(text)
    pause()
    slow("YOU SURVIVED THE 3 AM. Go to sleep. (Lol, good luck.)", 0.05)
    sys.exit()
def show_help():
    print("""
Commands:
  go <room>     move (ex: go hallway)
  take          pick up an item in the room
  open door     try to escape (hallway only)
  look          look around again
  help          show this
  quit          give up
""")
def intro():
    print("=" * 46)
    slow("          3 : 0 0   A . M .", 0.08)
    print("=" * 46)
    slow("You wake up for no reason. The whole house is silent.")
    slow("Too silent. Then... a slow scratching from downstairs.")
    slow("You can either find the KEY and escape through the front door,")
    slow("or survive until 4:00 AM when the ghost goes away.")
    slow("Each move costs time. The ghost is hunting you.")
    show_help()