import pygame
import random

# Constantes
GRID_SIZE = 16
CELL_SIZE = 50
WIDTH = (GRID_SIZE * CELL_SIZE)
HEIGHT = GRID_SIZE * CELL_SIZE
FPS = 30

class Case:
    """
    Classe pour représenter une case.

    ...
    Attributs
    ---------
    x : int
        La position x de la case sur la grille.
    y : int
        La position y de la case  sur la grille.
    proprite : str
        Propriete de la case('mur' ou 'herbe' ou 'flag1' ou 'flag2').
    

    Méthodes
    --------
    draw(screen)
        Dessine l'unité sur la grille.
    """
    
    def draw(self, screen):
        """Affiche les case sur l'écran."""
        
        # Afficher du drapeau du joueur 1 
        if self.propriete == 'flag1':
            flag_player1 = pygame.image.load("images/flag1.png")
            flag_player1 = pygame.transform.scale(flag_player1,  (2*CELL_SIZE, 2*CELL_SIZE))  
            screen.blit(flag_player1, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher du drapeau du joueur 2 
        elif self.propriete == 'flag2':
            flag_player2 = pygame.image.load("images/flag2.png")
            flag_player2 = pygame.transform.scale(flag_player2,  (2*CELL_SIZE, 2*CELL_SIZE))  
            screen.blit(flag_player2, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Map foret
        # Afficher les murs
        elif self.propriete == 'mur':
            mur = pygame.image.load("images/mur.webp")
            mur = pygame.transform.scale(mur,  (CELL_SIZE, CELL_SIZE))  
            screen.blit(mur, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher les buisson
        elif self.propriete == 'buisson':
            buisson = pygame.image.load("images/buisson.png")
            buisson = pygame.transform.scale(buisson,  (5*CELL_SIZE, 3*CELL_SIZE))  
            screen.blit(buisson, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher les arbres
        elif self.propriete == 'arbre':
            arbre = pygame.image.load("images/arbre.png")
            arbre = pygame.transform.scale(arbre,  (3*CELL_SIZE, 2*CELL_SIZE))  
            screen.blit(arbre, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher la boue
        elif self.propriete == 'boue':
            boue = pygame.image.load("images/boue.png")
            boue = pygame.transform.scale(boue,  (8*CELL_SIZE, 5*CELL_SIZE))  
            screen.blit(boue, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher la montagne
        elif self.propriete == 'roche':
            roche = pygame.image.load("images/roche.png")
            roche= pygame.transform.scale(roche,  (2*CELL_SIZE, 2*CELL_SIZE))  
            screen.blit(roche, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher le puit
        elif self.propriete == 'puit':
            puit = pygame.image.load("images/puit.png")
            puit= pygame.transform.scale(puit,  (2*CELL_SIZE, CELL_SIZE))  
            screen.blit(puit, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Map desert
        # Afficher les chameaux
        elif self.propriete == 'chameau':
            chameau = pygame.image.load("images/chameau.png")
            chameau = pygame.transform.scale(chameau,  (2*CELL_SIZE, 2*CELL_SIZE))  
            screen.blit(chameau, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher les dunes
        elif self.propriete == 'dune2':
            dune = pygame.image.load("images/dune2.png")
            dune = pygame.transform.scale(dune,  (3*CELL_SIZE, 3*CELL_SIZE))  
            screen.blit(dune, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()

        # Afficher les palmiers
        elif self.propriete == 'oasis':
            palmier = pygame.image.load("images/oasis.webp")
            palmier = pygame.transform.scale(palmier,  (3*CELL_SIZE, 3*CELL_SIZE))  
            screen.blit(palmier, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()
        
        
        # Afficher les montagnes
        elif self.propriete == 'dune':
            dune = pygame.image.load("images/dune.png")
            dune = pygame.transform.scale(dune,  (5*CELL_SIZE, 3*CELL_SIZE))  
            screen.blit(dune, (self.x * CELL_SIZE,
                                self.y * CELL_SIZE))
            pygame.display.flip()
        

    def __init__(self, x, y, propriete):
        self.x = x
        self.y = y
        self.propriete = propriete
        self.traversable = self.est_traversable()
        self.bloque_balles = self.bloque_les_balles()
        self.effet = self.effet_case()

    def est_traversable(self):
        """Détermine si la case est traversable."""
        if self.propriete in ["mur", "arbre", "dune", "dune2"]:
            return False
        return True

    def bloque_les_balles(self):
        """Détermine si la case bloque les projectiles."""
        if self.propriete in ["mur", "arbre", "dune", "dune2", "chameau"]:
            return True
        return False

    def effet_case(self):
        """Applique l'effet spécifique selon le type de case."""
        effets = {
            "buisson": "Invisible et invincible",
            "oasis": "Soigne les unités",
            "chameau": "Augmente la vitesse",
            "flag1": "Point de capture Joueur 1",
            "flag2": "Point de capture Joueur 2"
        }
        return effets.get(self.propriete, None)

    def draw(self, screen):
        """Affiche la case sur l'écran."""
        image_path = {
            "flag1": "images/flag1.png",
            "flag2": "images/flag2.png",
            "mur": "images/mur.webp",
            "buisson": "images/buisson.png",
            "arbre": "images/arbre.png",
            "chameau": "images/chameau.png",
            "dune": "images/dune.png",
            "dune2": "images/dune2.png",
            "palmier": "images/oasis.webp"
        }
        if self.propriete in image_path:
            image = pygame.image.load(image_path[self.propriete])
            size_multiplier = 2 if self.propriete in ["buisson", "chameau", "flag1", "flag2"] else 1
            image = pygame.transform.scale(image, (size_multiplier * CELL_SIZE, size_multiplier * CELL_SIZE))
            screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))

    def __str__(self):
        """Représentation en chaîne de la case."""
        return f"Case({self.x}, {self.y}, {self.propriete}, Traversable: {self.traversable}, Effet: {self.effet})"

# Exemple d'initialisation
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flags of Glory")
clock = pygame.time.Clock()

# Exemple de grille
grid = [
    [Case(x, y, random.choice(["mur", "arbre", "buisson", "flag1", "flag2", "chameau", "dune", "dune2", "palmier"])) for x in range(GRID_SIZE)]
    for y in range(GRID_SIZE)
]

# Boucle principale
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner la grille
    for row in grid:
        for cell in row:
            cell.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
