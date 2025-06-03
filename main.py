import pygame
from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    running = True
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game Over!")
                running = False
            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()

        for drawing in drawable:
            drawing.draw(screen)
        
        pygame.display.flip()
 
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
