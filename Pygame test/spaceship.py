import pygame as pg


class Spaceship(pg.sprite.Sprite):
    """x, y - coordinates Spaceship
    filename - path to the image
    speed - speed coordinates 'x'
    width - width screen"""

    def __init__(self, x, y, filename, speed, width):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.width = width

    def update(self, *args):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x > self.width-self.rect.width:
                self.rect.x = self.width-self.rect.width

    def bullet(self, *args):
        pass
