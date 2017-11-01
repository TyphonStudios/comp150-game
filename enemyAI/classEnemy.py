"""

"""

import pygame
import random
import math

# spawn
#   - no overlap
#   - off screen
#   - x spawn points of screen
#       - if spawn point 1 contins enemy{
#           - Generate list without spawn point 1
#           - Spawn enemy in random spawn point}
# moving
#   - move towards player
#   - cone of influence for steering behaviour
#       - look at direction that the collision is moving and make use of the vectors to rotate to avoid colision while
#           remaining on the same path
#           - line interception?
#               - polygon testing?
# attacking/defending
#   -D&D
# death

