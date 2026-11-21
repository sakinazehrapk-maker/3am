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
