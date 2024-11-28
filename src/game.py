import pygame
from random import *
from unit import *
from case import *


class Game:
    """
    Classe pour représenter le jeu.

    ...
    Attributs
    ---------

        La surface de la fenêtre du jeu.
    player_units : list[Unit]
        La liste des unités du joueur.
    enemy_units : list[Unit]
        La liste des unités de l'adversaire.
    """

    def __init__(self, screen):
        """
        Construit le jeu avec la surface de la fenêtre.

        Paramètres
        ----------
        screen : pygame.Surface
            La surface de la fenêtre du jeu.
        """
        self.screen = screen
        self.player_units = [Unit(3, 1, 10, 2, 'player','soldat'),
                             Unit(1, 3, 10, 2, 'player','helico')]

        self.enemy_units = [Unit(11, 10, 8, 1, 'enemy','char'),
                            Unit(10, 13, 8, 1, 'enemy','soldat')]
        
        # Liste des maps avec un terrain spécifique
        self.maps = [
            { # Map 1
                "terrain": "Projet-Python-/images/terrain_herbe.webp",  # Terrain de la map
                "cases": [  # Cases spécifiques de la map
                    Case(5, 5, 'mur'), Case(4, 5, 'mur'),
                    Case(0, 0, 'flag1'), Case(15, 15, 'flag2'),
                    Case(10, 10, 'buisson'), Case(3, 6, 'arbre')
                ]
            },
            { # Map 2
                "terrain": "Projet-Python-/images/terrain_sables.png",
                "cases": [
                    Case(0, 0, 'dune'), Case(3, 0, 'dune'), Case(6, 0, 'dune'), Case(9, 0, 'dune'),Case(12, 0, 'dune'),
                    Case(2, 1, 'flag1'), Case(14, 10, 'flag2'),
                    Case(3, 9, 'dune2'), Case(3, 8, 'dune2'),Case(10, 3, 'dune2'), Case(10, 4, 'dune2'),
                    Case(13, 13, 'palmier'), Case(8, 8, 'palmier')
                ]
            }
            ,
            { # Map 3
                "terrain": "Projet-Python-/images/terrain_neige.png",
                "cases": [
                    Case(6, 6, 'mur'), Case(7, 6, 'mur'),
                    Case(0, 7, 'flag1'), Case(15, 7, 'flag2'),
                    Case(5, 5, 'buisson'), Case(4, 4, 'arbre')
                ]
            }
        ]

        # Sélection d'une map aléatoire
        self.current_map = random.choice(self.maps)

    def draw_map(self):
        """Affiche les cases spécifiques de la map actuelle."""
        for case in self.current_map["cases"]:
            case.draw(self.screen)
            
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

    def flip_display(self):
        """Affiche le jeu."""

        # Charger et afficher le terrain de la map
        try:
            terrain_image = pygame.image.load(self.current_map["terrain"])
            terrain_image = pygame.transform.scale(terrain_image, (CELL_SIZE, CELL_SIZE))  # Adapter la taille à une cellule
        except pygame.error as e:
            print(f"Erreur lors du chargement de l'image du terrain : {e}")
            pygame.quit()
            exit()

        # Dessiner le terrain sur toute la grille
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                self.screen.blit(terrain_image, (x, y))


        # Affiche les cases spécifiques de la map
        self.draw_map()

        # Affiche les unités
        for unit in self.player_units + self.enemy_units:
            unit.draw(self.screen)

        # Rafraîchit l'écran
        pygame.display.flip()
        

def main():

    # Initialisation de Pygame
    pygame.init()

    # Instanciation de la fenêtre
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mon jeu de stratégie")
    
    # Charger les fresque
    try:
        fresque = pygame.image.load("Projet-Python-/images/fresque.png")
        fresque = pygame.transform.scale(fresque, (WIDTH,0.77*HEIGHT))  
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

    # Boucle principale du jeu
    while True:
        game.handle_player_turn()
        game.handle_enemy_turn()


if __name__ == "__main__":
    main()
