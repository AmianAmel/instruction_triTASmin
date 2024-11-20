# instruction_triTASmin
le but est de créer un TAS min à partir d'un tableau donné 

##Rappel Définition 
Un TASmax est un arbre binaire complet dans lequel chaque clé associée à un nœud est 
supérieure aux clés associées à ses fils droit et gauche s’ils existent.
Construction d’un TAS
Pour construire un TAS, il faut soit insérer les éléments un par un et permuter entre les clés du 
nœud père avec ses fils selon les conditions définis. Ou bien créer un tableau quelconque et le 
transformer en TAS en parcourant les éléments de celui-ci de droite à gauche en effectuant des 
permutations selon les mêmes conditions


##Tri par TAS
Une propriété du TASmax est que l’on sait que la valeur maximale se trouve nécessairement 
au niveau de la racine. Pour trier un tas, il suffira alors de sortir la racine à chaque itération.
