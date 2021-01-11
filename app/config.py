from math import pi

from app.utils.vector import Vector

TITLE = "Cuban Jumper"

BG_COLOR = "#555555"

PLAYER_COLOR = "#FF0000"
PLAYER_SIZE = Vector(14, 20)
PLAYER_START = (
    Vector(100, 50),
    Vector(700, 600)
)
PLAYER_SPEED = 300
PLAYER_JUMP = 700

BULLET_SIZE = Vector(5, 5)
BULLET_COLOR = "#FFFF00"
BULLET_SPEED = 1000

SHOOT_COOLDOWN = 0.3
SHOOT_ANGLE = pi / 6

PLATFORM_COLOR = "#00FF00"
PLATFORM_HEIGHT = 15

GRAVITY = 2000

GAME_SIZE = Vector(1500, 800)

UPDATE_TIMEOUT = 50

FPS = 60

MAP_FILE = "./maps/default.map"
MAP_CELL = Vector(150, 80)