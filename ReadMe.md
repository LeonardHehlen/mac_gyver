Launch run.py with Python3
Recquired : Pygame.

L’algorithme -
Run.py appelle la méthode run() de ma classe Game, qui va lancer la boucle principale du jeu, dans laquelle à chaque tour, le terrain se dessine, en mettant à jour les items et les cases spéciales, ainsi que le personnage, en mettant à jour sa position. La méthode check_events() du Terrain va checker la position du personnage avec les différentes entités et au cas ou le joueur arriverait sur la case de fin, renvoie un booléen a la boucle principale afin de la terminer, et on arrivera sur l’écran de fin qui affichera la victoire ou la défaite, en fonction du nombre d’items collectés sur le Terrain.
