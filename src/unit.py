import pygame
import random

# Constantes
GRID_SIZE = 16
CELL_SIZE = 50
WIDTH = (GRID_SIZE * CELL_SIZE)
HEIGHT = GRID_SIZE * CELL_SIZE
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


class Unit:
    """
    Classe pour représenter une unité.

    ...
    Attributs
    ---------
    x : int
        La position x de l'unité sur la grille.
    y : int
        La position y de l'unité sur la grille.
    health : int
        La santé de l'unité.
    attack_power : int
        La puissance d'attaque de l'unité.
    team : str
        L'équipe de l'unité ('player' ou 'enemy').
    deplacement :
        Moyen de déplacement de l'unité ('soldat' ou 'helico' ou 'char').
    is_selected : bool
        Si l'unité est sélectionnée ou non.

    Méthodes
    --------
    move(dx, dy)
        Déplace l'unité de dx, dy.
    attack(target)
        Attaque une unité cible.
    draw(screen)
        Dessine l'unité sur la grille.
    """

    def __init__(self, x, y, health, attack_power, team, deplacement):
        """
        Construit une unité avec une position, une santé, une puissance d'attaque et une équipe.

        Paramètres
        ----------
        x : int
            La position x de l'unité sur la grille.
        y : int
            La position y de l'unité sur la grille.
        health : int
            La santé de l'unité.
        attack_power : int
            La puissance d'attaque de l'unité.
        team : str
            L'équipe de l'unité ('player' ou 'enemy').
        deplacement : str
            Moyen de déplacement de l'unité ('soldat' ou 'helico' ou 'char').
        """
        self.x = x
        self.y = y
        self.health = health
        self.attack_power = attack_power
        self.team = team  # 'player' ou 'enemy'
        self.deplacement = deplacement  # 'soldat' ou 'helico' ou 'char'
        self.is_selected = False

    def move(self, dx, dy):
        """Déplace l'unité de dx, dy."""
        if 0 <= self.x + dx < GRID_SIZE and 0 <= self.y + dy < GRID_SIZE:
            self.x += dx
            self.y += dy

    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power

    def draw(self, screen):
        """Affiche l'unité sur l'écran."""

        # Afficher les soldats
        if self.deplacement == 'soldat':
            soldat = pygame.image.load("images/soldat.png")
            soldat = pygame.transform.scale(soldat,  (2*CELL_SIZE, 2*CELL_SIZE))  
            screen.blit(soldat, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher les helico
        elif self.deplacement == 'helico':
            helico = pygame.image.load("images/helico.png")
            helico = pygame.transform.scale(helico,  (3*CELL_SIZE, 3*CELL_SIZE)) 
            screen.blit(helico, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher les tank
        elif self.deplacement == 'char':
            char = pygame.image.load("images/char.png")
            char = pygame.transform.scale(char,  (3*CELL_SIZE, 3*CELL_SIZE)) 
            screen.blit(char,(self.x * CELL_SIZE,
                             self.y * CELL_SIZE))
            pygame.display.flip()