<h1>Chest tournament</h1>
<h2>Prérequis</h2>
<p>Installer les paquetes du fichier requirements.txt</p>
<h2>Flake Report</h2>
<p>Pour génerer un repéertoire flake report contenant le fichier html qui repertorie 
toutes les violations faites aux règles de la PEP 8 suivez les instructions suivantes.
</p>
<ul>
    <li>Si vous avez oublié installez le paquet flake8 avec la commande suivante: 
"python -m pip install flake8".</li><br>
    <li>Installez aussi le paquet flake8-html pour non seulement épelucher les fichiers et
marquer les violations en console mais aussi pour génere le fichier html. La commande 
pour l'installer est "pip install flake8-html"</li><br>
    <li>Une fois ces deux là installez pour répertorier toutes les violations dans un 
fichier html sans prendre en compte les fichier de l'environnement python et avec 
une violation de ligne de  119 tapez la commande suivante:

"flake8 --format=html --htmldir=flake-report --extend-exclude envs --max-line-length 119".
</li>
</ul>
<img src="https://github.com/jonathannava99/Chest/blob/main/flake-report/flake-violations.png" 
alt="" >

<h2> Chest tournament fonctionnement</h2>
<p>Pour faire fonctionner le programme et comprendre comment il fonctionne suivez les instructions suivantes: </p>
<ul>
    <li>Pour démarrer le programme tapez la commande suivante: "python main.py"</li><br>
    <li>Une fois le programme démarré vous allez voir un menu s'afficher.</li><br>
  <img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/beginning.png" 
alt="" style="margin-bottom: 15px">
    <li>Pour créer un tournoi il suffit de selectionner "Créer un tournoi" tapez sur la touche entrée.
Une fois cela fait des informations vous seront demandées.</li><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/create_tournament.png" alt="">
    <li>Il est pas possible d'effacer en ligne de commande avec le paquet inquirer donc faites très attention à pas
faire de fautes. Pour le nombre de tours il faut absolument un numero et pour la date 
il faut que ça soit absolument dans le format "yyy-mm-dd".</li><br>
    <li>Ensuite le programme va vous demander de renseigner les joueurs. Sur l'image ils sont au 
nombre de 4 pour l'exemple mais normalement c'est 8.</li><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/create_players.png" alt=""><br>
    <li>Les même regles s'applique ici sur la date. Et pour le classement il faut absolument un numero</li><br>
    <li>Une fois que vous créez le tournoi vous revenez à l'écran d'accueil</li><br>
    <li>Vous pouvez sélectionner le tournoi que vous venez de créer dans la liste de tournois en cours ou 
tout simplement dans la liste de tournois. Une fois selectionné vous aurez accès au menu du tournoi</li><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/tournament_menu.png" alt="">
    <li>Vous pouvez consulter les menu joueurs pour voir toutes les données concernant les joueurs. Mais nous allons 
d'abord commencer le tournoi en sélectionnant "commencer le tournoi".</li><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/turn1.png" alt="">
    <li>Les matchs à jouer du tour 1 vont s'afficher, sélectionner l'un des matchs et marquez les scores. Pour une victoire marquer
1 et 0 pour l'autre et pour l'égalité marquez 0.5 pour les deux.</li><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/comback-to-tournament-menu.png" alt="">
    <li>Un fois les scores renseigner ça vous renvoi vers le menu tournoi à nouveau mais ce n'est plus "commencer le tournoi" 
qui s'affiche mais "continuer le tournoi. A chaque fois que rentrez un score il vous renvoie vers le menu tournoi.
Quand vous avez fait tous les matchs du tournoi vous pouvez sélectionner l'option "valider le tour 1". 
Si vous sélectionnez cette option avant d'avoir fait tous les matchs un message s'affiche en 
vous expliquant que vous n'avez pas fait tous les matchs du tour. Pareille si vous avez déjà joué un match et que 
vous essayez de mettre à nouveau les scores, il vous dit que le match a déjà été joué.</li><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/turn_incompleted.png" alt=""><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/game_already_played.png" alt=""><br>
    <li>Si vous avez bien fait les étapes, il va vous afficher le tour numéro 2. Puis si vous répetez les étapes
vous allez arriver au dernier tour du tournoi quand vous le complétez le tournoi passe en tournoi terminé et le menu tournoi affiche "Tournoi terminé".
</li><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/comback-to-tournament-menu.png" alt=""><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/go-to-tournament-menu.png" alt=""><br>
<img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/tournaments_ended.png" alt=""><br>
</ul>