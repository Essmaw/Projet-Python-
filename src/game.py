import pygame
from random import *
from unit import *
from case import *
from interface import *

def handle_player_turn(self):
    """Tour du joueur"""
    for selected_unit in self.player_units:

        # Tant que l'unité n'a pas terminé son tour
        has_acted = False
        selected_unit.is_selected = True
        self.flip_display()
        while not has_acted:

        # Important: cette boucle permet de gérer les événements Pygame
            for event in pygame.event.get():

                # Gestion de la fermeture de la fenêtre
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Gestion des touches du clavier
                if event.type == pygame.KEYDOWN:

                    # Déplacement (touches fléchées)
                    dx, dy = 0, 0
                    if event.key == pygame.K_LEFT:
                        dx = -1
                    elif event.key == pygame.K_RIGHT:
                        dx = 1
                    elif event.key == pygame.K_UP:
                            dy = -1
                    elif event.key == pygame.K_DOWN:
                            dy = 1

                    selected_unit.move(dx, dy)
                    self.flip_display()

                    # Attaque (touche espace) met fin au tour
                    if event.key == pygame.K_SPACE:
                        for enemy in self.enemy_units:
                            if abs(selected_unit.x - enemy.x) <= 1 and abs(selected_unit.y - enemy.y) <= 1:
                                selected_unit.attack(enemy)
                                if enemy.health <= 0:
                                    self.enemy_units.remove(enemy)

                        has_acted = True
                        selected_unit.is_selected = False

def handle_enemy_turn(self):
    """IA très simple pour les ennemis."""
    for enemy in self.enemy_units:

        # Déplacement aléatoire
        target = random.choice(self.player_units)
        dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
        dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
        enemy.move(dx, dy)

        # Attaque si possible
        if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
            enemy.attack(target)
            if target.health <= 0:
                self.player_units.remove(target)

def main():

    # Initialisation de Pygame
    pygame.init()

    # Instanciation de la fenêtre
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mon jeu de stratégie")
    
    # Charger les fresque
    try:
        fresque = pygame.image.load("images/fresque_1.png")
        fresque = pygame.transform.scale(fresque, (WIDTH,HEIGHT))  
    except pygame.error as e:
        print(f"Erreur lors du chargement de l'image : {e}")
        return

    # Afficher la fresque
    screen.blit(fresque, (0, 0))
    pygame.display.flip()

    # Attendre qu'une touche soit pressée
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

   
    # Instanciation du jeu
    game = Game(screen)

   # Boucle principale
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Simulation des tours de jeu (simplifié ici)
        game.flip_display()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
