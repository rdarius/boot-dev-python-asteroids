import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    drawable.add(player)
    updatable.add(player)

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60)/1000

        for entity in updatable:
            entity.update(dt)

        for entity in asteroids:
            if player.is_collission(entity):
                print("Game Over!")
                sys.exit(0)

            for bullet in shots:
                if bullet.is_collission(entity):
                    entity.split()
                    bullet.kill()
                    continue

        screen.fill(pygame.Color(0, 0, 0), pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
