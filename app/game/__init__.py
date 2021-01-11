import pygame as pg

from app import config
from app.game.walkers import Player, Bullet
from app.utils.vector import Vector
from app.utils.maps import import_map


class Game(object):
    def __init__(self):
        """
        Initialize Game object
        """
        pg.init()

        self.surface = pg.display.set_mode(config.GAME_SIZE)

        pg.display.set_caption(config.TITLE)

        self.bg = pg.Surface(self.surface.get_size())
        self.bg.fill(config.BG_COLOR)
        self.bg = self.bg.convert()

        self.surface.blit(self.bg, (0, 0))

        self.walkers = pg.sprite.Group()
        self.players = pg.sprite.Group()

        self.platforms = pg.sprite.Group(
            *import_map()
        )

        self.player1 = Player(config.PLAYER_START[0],
                              '#FF0000',
                              self.platforms,
                              {
                                  'RIGHT': pg.K_RIGHT,
                                  'LEFT': pg.K_LEFT,
                                  'UP': pg.K_UP,
                                  'SHOOT': pg.K_DOWN,
        },
            self.walkers, self.players)

        self.player2 = Player(config.PLAYER_START[1],
                              '#0000FF',
                              self.platforms,
                              {
                                  'RIGHT': pg.K_d,
                                  'LEFT': pg.K_a,
                                  'UP': pg.K_w,
                                  'SHOOT': pg.K_s,
        },
            self.walkers, self.players)

    def run(self) -> int:
        """
        Run game loop
        """
        clock = pg.time.Clock()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return 0

            self.surface.blit(self.bg, (0, 0))

            self.update()

            pg.display.flip()
            clock.tick(config.FPS)
        return 1

    def update(self):
        """
        Update and draw all game objects
        """
        self.walkers.update()
        self.walkers.draw(self.surface)

        self.platforms.draw(self.surface)