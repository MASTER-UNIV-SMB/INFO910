# INFO910
### TP DevOps

Haris Coliche et Clément de Louvencourt

L'objectif du TP est de containeuriser une application avec Docker et Kubernetes.

Dans le cadre de mon TP, j'ai réalisé une application Flask, utilisant Nginx en serveur web. L'application a pour but de renvoyer une image de chat pour chaque code HTTP possible. Pour cela elle fait des appels à l'API https://http.cat/ .

## Exercice 1 : Docker

Dans le dossier Docker, l'application se divise en deux dossiers, pour les deux images à faire tourner.

Enfin, à la racine du dossier Docker, on trouve un fichier docker-compose.yaml pour coordonner le lancement.

### Comment lancer l'application ?

L'application se lance via la commande :
`docker-compose up`.

L'application est ensuite accessible à l'adresse : http://localhost:80


## Exercice 2 : Kubernetes

Le dossier Kubernetes contient un service et un deployment pour chacune des deux images. Les deployments permettent de spécifier une image à récupérer pour le deployment, la stratégie de redémarrage, les ressources mémoire et processeurs allouées, les ports à exposer, les variables d'environnement auxquelles doit avoir accès le conteneur, ...
Les services permettent d'exposer les deployements ayant les mêmes labels qu'eux en tant que services : le service flask est exposé "en interne" pour être accessible par nginx, le service nginx est exposé de façon à être accessible à l'extérieur, en l'occurence sur le port 3000.

### Pour lancer l'application (avec Minikube):

L'application se lance via la commande :
`minkube start`

A la racine du dossier Kubernetes, et on applique les 4 fichiers :
`kubectl apply -f flask-dep.yaml,flask-svc.yaml,nginx-dep.yaml,nginx-svc.yaml`

L'application est ensuite accessible à l'adresse : http://ADRESSE_KUBERNETTE:3000

Pour trouver facilement l'URL : `minikube service list`, et en cherchant l'URL liée à "nginx".