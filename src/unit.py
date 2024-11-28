import pygame

# Constantes
GRID_SIZE = 16
CELL_SIZE = 50
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
    deplacement : str
        Moyen de déplacement de l'unité ('soldat' ou 'helico' ou 'char').
    is_selected : bool
        Si l'unité est sélectionnée ou non.
    distance_remaining : int
        Nombre de cases que l'unité peut encore parcourir ce tour.

    Méthodes
    --------
    reset_distance()
        Réinitialise la distance restante au début d'un tour.
    move(direction)
        Déplace l'unité dans une direction donnée au maximum de son périmètre.
    attack(target)
        Attaque une unité cible.
    draw(screen)
        Dessine l'unité sur la grille.
    """

    def __init__(self, x, y, health, attack_power, team, deplacement):
        """
        Construit une unité avec une position, une santé, une
puissance d'attaque et une équipe.

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
        self.team = team
        self.deplacement = deplacement
        self.is_selected = False

        # Définit le déplacement maximal par type d'unité
        if self.deplacement == 'helico':
            self.max_distance = 3
        elif self.deplacement == 'soldat':
            self.max_distance = 2
        elif self.deplacement == 'char':
            self.max_distance = 1
        else:
            self.max_distance = 1  # Par défaut

        self.distance_remaining = self.max_distance  # Cases restantes pour le tour

    def reset_distance(self):
        """Réinitialise la distance restante au début d'un nouveau tour."""
        self.distance_remaining = self.max_distance

    def move(self, dx, dy ):
        """
        Déplace l'unité dans une direction donnée, dans la limite de
sa distance restante.

        direction : tuple (dx, dy)
            La direction dans laquelle l'unité doit se déplacer.
        """
        
        distance = abs(dx) + abs(dy)

        # Vérifie si le déplacement demandé dépasse la distance restante
        if distance > self.distance_remaining:
            print(f"Déplacement non autorisé : il reste {self.distance_remaining} cases.")
            return

        # Vérifie les limites de la grille
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            self.x = new_x
            self.y = new_y
            self.distance_remaining -= distance  # Réduit la distance restante
        else:
            print("Déplacement hors des limites de la grille.")

    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power

    def draw(self, screen):
        """Affiche l'unité sur l'écran."""

        # Afficher les soldats
        if self.deplacement == 'soldat':
            soldat = pygame.image.load("Projet-Python-/images/soldat.png")
            soldat = pygame.transform.scale(soldat, ( 2*(CELL_SIZE-1), 2*(CELL_SIZE-1)))
            screen.blit(soldat, (self.x * CELL_SIZE, self.y * CELL_SIZE))

        # Afficher les medecin
        if self.deplacement == 'medecin':
            medecin = pygame.image.load("images/medecin.png")
            medecin  = pygame.transform.scale(medecin ,  (4*CELL_SIZE, 2*CELL_SIZE))  
            screen.blit(medecin , (self.x * CELL_SIZE,
                             self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher les helico
        elif self.deplacement == 'helico':
            helico = pygame.image.load("Projet-Python-/images/helico.png")
            helico = pygame.transform.scale(helico, (3*(CELL_SIZE-2),3* (CELL_SIZE-2)))
            screen.blit(helico, (self.x * CELL_SIZE, self.y * CELL_SIZE))

        # Afficher les chars
        elif self.deplacement == 'char':
            char = pygame.image.load("Projet-Python-/images/char.png")
            char = pygame.transform.scale(char, (3 * CELL_SIZE, 3 * CELL_SIZE))
            screen.blit(char, (self.x * CELL_SIZE, self.y * CELL_SIZE))

