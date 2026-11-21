# 3 A.M.

a spooky text game that runs in your terminal. i made this in python and honestly it kinda scared me while testing it at night. (it was not even 3am, it was like 9pm, but still.)

## what is this??

you wake up at **3:00 AM** for no reason. the house is super quiet. then you hear scratching from downstairs. yeah. not good.

there's a ghost walking around your house and it is hunting you. you have to get out alive.

## how to win

there are two ways:

1. **escape** - find the rusty key in the kitchen, go to the hallway, and type `open door`
2. **survive** - stay alive until **4:00 AM** when the ghost goes away

## how to lose

the ghost finds you and you don't have a working flashlight. yeah. that's it. you die.

## how to run it

you need python 3 installed (if you have it you're good, no extra stuff to download).

open your terminal and type:

```
python3 main.py
```

on windows you might have to type `python main.py` instead.

## commands

| command | what it does |
|---------|--------------|
| `go <room>` | move to another room (like `go hallway`) |
| `take` | pick up the item in the room |
| `look` | look around the room again |
| `open door` | try to escape (only works in the hallway) |
| `help` | shows the commands |
| `quit` | gives up (coward) |

## the map


          [bathroom]
              |
[bedroom] - [hallway] - [basement]
              |
        [living room] - [kitchen]


(the ghost starts in the basement. good luck.)

## tips (please read these)

- grab the **flashlight** in your bedroom FIRST. trust me.
- when the ghost shows up, type `light` fast!! you only have like 5 seconds
- the flashlight battery only works **2 times** so don't waste it
- every move costs time, so don't just wander around
- if you hear scratching, the ghost is in the room NEXT to you

## how the ghost works (for nerds)

half the time the ghost walks around randomly, and the other half it chases you using something called BFS (breadth-first search). i learned it online and it took me forever to understand but it works!! so the ghost always knows the shortest path to you. kinda unfair tbh.

## things i want to add later

- more rooms (attic??)
- a sanity meter so you start seeing fake stuff
- a second ghost
- maybe sound effects

## credits

made by me!! (and a lot of googling)

if you find a bug, don't tell me, just pretend it's part of the haunting 