import pygame, os
import game_module as gm
import random


os.environ['SDL_VIDEO_CENTERED'] = '1'          # centrowanie okna
pygame.init()


## ustawienia ekranu i gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
pygame.display.set_caption('Prosta gra platformowa...')
clock = pygame.time.Clock()


# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = set()
        self.movement_x = 0
        self.movement_y = 0
        self.count = 0
        self.lifes = 3
        self.level = None
        self.direction_of_movement = 'right'
        self.set_of_items = pygame.sprite.Group()
        self.set_of_bullets = pygame.sprite.Group()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_left(self):
        self.direction_of_movement='left'
        self.movement_x=-6

    def turn_right(self):
        self.direction_of_movement = 'right'
        self.movement_x = 6

    def _gravity(self):
        if self.movement_y == 0:
            self.movement_y = 1
        else:
            self.movement_y += 0.35
        if self.movement_y > 14:
            self.movement_y = 14

    def jump(self):
        if self.movement_y == 0:
            self.movement_y = -7

    def stop(self):
        self.movement_x = 0

    def _move(self, image_list):
        if self.count <4:
            self.image=image_list[0]
        if self.count>=4 and self.count<8:
            self.image=image_list[1]

        if self.count>8:
            self.count=0
        else:
            self.count += 1

    def update(self):
        #Ruch w poziomie
        self.rect[0]+=self.movement_x
        collisions = pygame.sprite.spritecollide(self, self.level.set_of_platforms, False)
        for o in collisions:
            if self.movement_x > 0:
                self.rect.left = o.rect.right
            if self.movement_x < 0:
                self.rect.right = o.rect.left
        #print(self.movement_y)
        #print("-------------")

        #animacja (co 4)
        if self.movement_x  > 0:
            self._move(gm.IMAGES_R)
        if self.movement_x  < 0:
            self._move(gm.IMAGES_L)
        self._gravity()
        self.rect[1] += self.movement_y

        collisions = pygame.sprite.spritecollide(self,self.level.set_of_platforms,False)
        for o in collisions:
            if self.movement_y < 0:
                self.rect.top = o.rect.bottom
            if self.movement_y > 0:
                self.rect.bottom = o.rect.top
            self.movement_y = 0

        if self.direction_of_movement == "right":
            if self.movement_y > 0:
                self.image = gm.FALL_R
            if self.movement_y < 0:
                self.image = gm.JUMP_R

        if self.direction_of_movement == "left":
            if self.movement_y > 0:
                self.image = gm.FALL_L
            if self.movement_y < 0:
                self.image = gm.JUMP_L
        if self.movement_y == 0 and self.movement_x ==0:
            if self.direction_of_movement == "left":
                self.image = gm.STAND_L
            else:
                self.image = gm.STAND_R
        self.lift_up()

    def lift_up(self):
        for i in self.set_of_items:
            if i.rect.colliderect(self.rect):
                self.items.add(i.name)
                self.set_of_items.remove(i)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                self.turn_left()
            if event.key==pygame.K_RIGHT:
                self.turn_right()
            if event.key == pygame.K_UP:
                self.jump()
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT and self.movement_x < 0:
                self.stop()
                self.image=gm.STAND_L
            if event.key == pygame.K_RIGHT and self.movement_x > 0:
                self.stop()
                self.image = gm.STAND_R

    def shoot(self, event):
        #print(event, self.items, self.items.__len__() )
        if self.items.__len__() > 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print(event, self.items, self.items.__len__())
                    if self.direction_of_movement == "right":
                        self.set_of_bullets.add(Bullet(gm.BULLET_R, self.direction_of_movement))
                    if self.direction_of_movement == "left":
                        self.set_of_bullets.add(Bullet(gm.BULLET_R, self.direction_of_movement))


class Platform(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, rect_x, rect_y):
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Level():

    def __init__(self,player:Player):
        self.player = player
        self.set_of_platforms = set()
        self.set_of_enemies = pygame.sprite.Group()

    def update(self):
        for s in self.set_of_platforms:
            s.update()

        for b in player.set_of_bullets:
            b.update()

        for i in player.set_of_items:
            i.update()
        self._delete_bullets()

        for e in self.set_of_enemies:
            e.update()

    def draw(self, surface):
        for s in self.set_of_platforms:
            s.draw(surface)

        for b in player.set_of_bullets:
            b.draw(surface)

        for i in player.set_of_items:
            i.draw(surface)

        for e in self.set_of_enemies:
            e.draw(surface)

    def _delete_bullets(self):
        print(player.set_of_bullets)
        for b in player.set_of_bullets:
            for p in self.set_of_platforms:
                if p.rect.colliderect(b):
                    player.set_of_bullets.remove(b)
            if gm.WIDTH < b.rect.x:
                player.set_of_bullets.remove(b)


class Level_1(Level):
    def __init__(self, player:Player):
        super().__init__(player)

        list_platforms = [[420, 70, 750, 350],
                          [980, 70, 0, gm.HEIGHT-70],
                          [560, 70, 0, 170],
                          [140, 70, 1240, 600]]

        list_of_enemies = [[420, 70, 750, 350],
                           [560, 70, 0, 170]]

        for w in list_platforms:
            self.set_of_platforms.add(Platform(gm.DARKRED, *w))

        self.set_of_enemies.add(Platform_Enemy(self.set_of_platforms[0], gm.ZOMBIE_STAND_R,
                                               gm.ZOMBIE_IMAGES_RIGHT,
                                               gm.ZOMBIE_IMAGES_LEFT,
                                               gm.ZOMBIE_DEAD_R, gm.ZOMBIE_DEAD_L, movement_x=3, movement_y=0))
        shotgun = Item(gm.SHOTGUN, 'shotgun')
        shotgun.rect.x = 600
        shotgun.rect.y = 600
        player.set_of_items.add(shotgun)


class Item(pygame.sprite.Sprite):
    def __init__(self, image, name):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, direction):
        super().__init__()
        self.image = image
        self.direction_of_movement = direction
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center


    def update(self):
        if self.direction_of_movement == "right":
            self.rect.x += 15
        if self.direction_of_movement == "left":
            self.rect.x -= 15

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):

    def __init__(self, image, images_right, images_left, images_dead_right, images_dead_left, movement_x, movement_y):
        self.image = image
        self.images_right = images_right
        self.images_left = images_left
        self.images_dead_right = images_dead_right
        self.images_dead_left = images_dead_left
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.rect = self.image.get_rect()
        self.lifes = 1
        self._count = 0

    def update(self):
        self.rect.x += self.movement_x
        if self.lifes == 0 and self._count > 7:
            self.kill()
        if self.lifes > 0:
            if self.movement_x > 0:
                if self._count < 4:
                    self.image = self.images_right[0]
                if self._count >= 4 and self._count < 8:
                    self.image = self.images_right[1]
                if self._count > 7:
                    self._count = 0
            elif self.movement_x < 0:
                if self._count < 4:
                    self.image = self.images_left[0]
                if self._count >= 4 and self._count < 8:
                    self.image = self.images_left[1]
                if self._count > 7:
                    self._count = 0
            else:
                self.image = gm.ZOMBIE_STAND_R
            self._count += 1
        else:
            if self.movement_x >= 0:
                self.image = self.images_dead_right
            else:
                self.image = self.images_dead_left


class Platform_Enemy(Enemy):

    def __init__(self, platform:Platform, image, images_right, images_left, images_dead_right, images_dead_left, movement_x=0, movement_y=0):
        super().__init__(image, images_right, images_left, images_dead_right, images_dead_left, movement_x, movement_y)
        self.platform = platform
        self.rect.bottom = self.platform.rect.y
        self.rect.center = (self.platform.rect.x + random.randint(0, self.platform.width), self.platform.rect.y)

    def update(self):
        super().update()
        if self.platform.rect.x == self.rect.x:
            self.movement_x *= -1
        elif self.platform.rect.x + self.platform.width == self.rect.x:
            self.movement_x *= -1


# konkretyzacja obiektów
player = Player(gm.STAND_R)
player.rect.center = screen.get_rect().center
current_level = Level_1(player)
player.level = current_level
# enemy = Platform_Enemy(Platform(gm.DARKRED, 210, 70, 520, 200), gm.ZOMBIE_STAND_R, (gm.ZOMBIE_WALK_R1, gm.ZOMBIE_WALK_R2), (gm.ZOMBIE_WALK_L1, gm.ZOMBIE_WALK_L2), gm.ZOMBIE_DEAD_R, gm.ZOMBIE_DEAD_L, movement_x=3)


# głowna pętla gry
window_open = True
while window_open:
    screen.fill(gm.LIGHTBLUE)
    # pętla zdarzeń
    for event in pygame.event.get():
        #print(event)
        player.shoot(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        elif event.type == pygame.QUIT:
            window_open = False
        player.get_event(event)



    # rysowanie i aktualizacja obiektów
    player.draw(screen)
    player.update()
   #enemy.update()
    current_level.update()
    current_level.draw(screen)
    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)

pygame.quit()