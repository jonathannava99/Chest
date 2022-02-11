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
alt="" width="1100" height="650">

<h2> Chest tournament fonctionnement</h2>
<p>Pour faire fonctionner le programme et comprendre comment il fonctionne suivez les instructions suivantes: </p>
<ul>
    <li>Pour démarrer le programme tapez la commande suivante: "python main.py"</li>
    <li>Une fois le programme démarré vous allez voir un menu s'afficher </li><br>
  <img src="https://github.com/jonathannava99/Chest/blob/main/chest_test_images/beginning.png" 
alt="" width="1000" height="200">
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>