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