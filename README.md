# Battle Simulator (Python)

## Overview

Battle-Simulator is a begineer project whose main intention was for me to have a deeper understanding of building projects. The game itself creates randomised gameplay scenarios based the on the players, attacks and their roles assigned and find the last standing person.
No two running of the project would be the same and so different attacks, different roles, different scenarios

---

## Features

  * Each player is assigned a role
  * Each role has a unique set of attacks with different effects
  * Players take turns automatically
  * Targets are selected dynamically from alive players only
  * Damage-based attacks (negative values)
  * Healing abilities (positive values)
  * Neutral actions (e.g., dodge)
  * Death is handled dynamically and removes players from the game
  * Add attacks or players or moves or even roles in the array and it wouldn't distrupt the logic of the code
  * All actions are recorded in a `.log` file
  * Timestamped entries for traceability and debugging

---


## How It Works

1. Players are initialized with:
   * Name
   * Role
   * Attack set

2. Game loop begins:
   * Each player takes turns attacking
   * Targets are randomly selected (excluding self)

3. Damage/Healing is applied:
   * HP is updated
   * Death is checked

4. Loop continues until:
   * Only one player remains, which would be the winner


## Running the Project

You can download or copy the code and run in your desired IDE. Make sure the IDE supports Python and you can find the output in terminal

## Lesson learnt
This project was made after my intermediate course to get a deeper understanding of the process of building projects. While I did struggle at the start, I decided to take a new approach of planning the working (pseudocode) and then make it and I build 95% of the code in just a single day and the rest of the other days I spent fixing issues. I used AI to find bugs as the output was long enough for me to analyze and find the bugs. This game was optimised fully I believe and also it is just a mini project

[![Watch the preview here](https://github.com/user-attachments/assets/650c16c9-39dc-40e8-8b31-03a7268384e3)](https://github.com/user-attachments/assets/ef25964a-a897-47da-8767-67a2fb55d967)


