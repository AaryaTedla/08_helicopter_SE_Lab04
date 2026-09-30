# Helicopter Lab

This project is a single-topic side-scrolling Helicopter game using
**Pygame**. It introduces students to velocity-based movement,
boundary handling, obstacle collision, distance scoring, and a
temporary shield mechanic, using a small, readable object-oriented
codebase.

---

## What's Provided

A working Helicopter game with:

- A helicopter that moves up and down and speeds up the longer a
  direction key is held
- Obstacles (wall pairs with a gap) that scroll in from the right at a
  steady pace and spawn at random heights
- A basic play loop, though the helicopter currently flies straight
  through obstacles with no consequence

It has **one deliberate bug** (with two distinct symptoms) and
**three features** left for you to build. You are expected to
**analyze**, **interact with an AI assistant**, and **complete/fix**
the game to make it fully functional and more interesting.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**

---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the game:

```bash
python main.py
```

**Controls:** Up/Down arrows to move.

---

## Tasks to Complete

Each task must be completed using an iterative process involving LLM
suggestions and your critical code review.

### Task 1: Fix the movement and boundary bug

> **What you'll see, problem 1:** hold Up for a second or two, then
> immediately switch to holding Down. Instead of the helicopter
> reversing right away, it keeps drifting upward for a noticeable
> moment before it finally starts descending - the controls feel
> laggy and unresponsive exactly when you're trying to change
> direction quickly.
>
> **Why:** in `Helicopter.handle_input` (in `game/helicopter.py`),
> holding a direction key keeps adding to the helicopter's vertical
> speed (`vy`) with no upper limit and nothing slowing it back down.
> The longer you hold a key, the faster it's moving in that direction
> - and the more time the *opposite* key then needs just to cancel
> that speed out before the helicopter can actually start moving the
> other way.
>
> **What you'll see, problem 2:** hold Down for a few seconds and the
> helicopter flies straight off the bottom of the screen and keeps
> going, completely out of view.
>
> **Why:** `Helicopter.update` only checks the top boundary (`if self.y
> < 0`) - there's no matching check for the bottom edge at all.
>
> **Fix both:** cap the helicopter's speed so it can't build up
> forever, and add the missing boundary check so it can never leave
> the screen at the top or the bottom.

### Task 2: Implement obstacle collision and game over

> Add collision detection between the helicopter and the obstacles.
> Touching either the top or bottom wall of an obstacle should end the
> game and display a clear game-over message. Flying safely through
> the gap should never end the game.

### Task 3: Add distance-based scoring

> Track how far the helicopter has traveled and show it as a score
> that increases automatically while the game is running. Display the
> final distance when the game ends, and make sure starting a new game
> resets it back to zero.

### Task 4: Add a shield mechanic

> Add a shield the player can activate that protects the helicopter
> from one obstacle collision. Show a clear indication while it's
> active, and have it disappear the moment it absorbs a hit - after
> that, the helicopter should be vulnerable again until the shield is
> used once more.

---

## Expected Behavior

- Switching between Up and Down should feel immediate - the
  helicopter shouldn't keep drifting in the old direction for a
  noticeable stretch of time after you've pressed the opposite key.
- The helicopter should never be able to fly off the screen, at
  either the top or the bottom, no matter how long a key is held.
- Touching either wall of an obstacle should end the game; flying
  safely through the gap should never end it, no matter where in the
  gap the helicopter is.
- Distance should climb steadily while playing, be shown clearly when
  the game ends, and reset to zero on a new game.
- Activating the shield should be clearly visible, protect against
  exactly one collision, and turn back off right after.

---

## Folder Structure

```
helicopter/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   ├── helicopter.py
│   ├── obstacle.py
│   └── renderer.py
└── README.md
```

---

## Submission Checklist

Submission is only the following three things:

- [ ] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [ ] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [ ] The Chat/LLM used page link, with the complete chat history
