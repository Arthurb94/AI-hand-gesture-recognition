# Projet de reconnaissance des mouvements de la main

## Description
Ce projet a été réalisé en tant que projet de fin de 1e année du cycle ingénieur a l'ESIEE Paris. Il a pour but d'interpréter les mouvements de la main pour différentes applications (domotique, langue des signes ...). Dans le cadre de notre projet, nous étions contraints de nous limiter à des applications liées à la domotique (lancer une musique sur commande, allumer la lumière etc.). 

## Fonctionnement des différents programmes
Notre projet comporte quatre programmes python :
- "**CreateDataBase.py**" est un programme qui sert à générer une base de données. Pour cela, il faut lancer le programme, celui-ci va ouvrir la capture caméra. Il faut ensuite que vous réalisiez le mouvement que vous voulez ajouter dans la base de données en face de la caméra en maintenant la touche **"s"** enfoncée. Tant que la touche est maintenue, le programme enregistre les coordonnées de différents points virtuels sur votre main et les stocks dans un fichier csv du nom choisit en fin de programme. Une fois la quantité de coordonnées nécessaire collectées, le programme se ferme. Il faut lancer le programme autant de fois que vous voulez de mouvement. Libre à vous de faire plusieurs passages sur le même mouvement afin d'améliorer la précision de la détection. Le programme peut être interrompu à tout moment en pressant "**q**".
- "**Fusion_csv_normal.py**" fusionne toutes les bases de données csv générées par **CreateDataBase** et stockées dans le dossier bdd.
- "**CreateModel.py**" est le programme qui va générer le modèle d'apprentissage à partir de la base de données préalablement créée. 
- "**ImageV6.py**" est le programme principal du projet. Au lancement, il charge le modèle d'apprentissage et allume la caméra afin de capturer le flux vidéo en live. Ensuite, il lance l'interprétation des mouvements détectés en comparant les entrées de la caméra aux valeurs enregistrées dans le modèle. Certains mouvements sont associés à des petites actions comme lancer une musique, afficher une image ou encore ouvrir une page internet. Pour lancer ces actions, il suffit d'appuyer sur la touche "**a**" lorsque le mouvement en question est détecté. La liste des mouvements associés aux actions sont disponibles et modifiables dans la fonction action de ce programme. Le programme peut être interrompu à tout moment en pressant "**q**".

## 

## Modules nécessaires : 
Toutes les commandes pour télécharger les modules sont disponibles dans le fichier "requirements.txt"

|Nom |Installation|
| ------ | ------ |
|Os |pip install os|
|Csv |pip install csv|
|Numpy |pip install numpy|
|Mediapipe |pip install mediapipe|
|Pandas |pip install pandas|
|Open cv |pip install cv2|
|Subprocess |pip install subprocess|
|Webbrowser |pip install webbrowser|
|Keras |pip install keras|
|Tensorflow |pip install tensorflow|
|Matplotlib |pip install matplotlib |

