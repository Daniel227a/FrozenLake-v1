# FrozenLake-v1
Frozen lake involves crossing a frozen lake from start to goal without falling into any holes by walking over the frozen lake. The player may not always move in the intended direction due to the slippery nature of the frozen lake.
Description
The game starts with the player at location [0,0] of the frozen lake grid world with the goal located at far extent of the world e.g. [3,3] for the 4x4 environment.

Holes in the ice are distributed in set locations when using a pre-determined map or in random locations when a random map is generated.

The player makes moves until they reach the goal or fall in a hole.

The action shape is (1,) in the range {0, 3} indicating which direction to move the player.

0: Move left

1: Move down

2: Move right

3: Move up

https://gymnasium.farama.org/environments/toy_text/frozen_lake/#frozen-lake


The Bellman equation

V(s) = \max_a \left( \sum_{s',r} p(s',r|s,a) \left[ r + \gamma V(s') \right] \right)


