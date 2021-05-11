## Informations générales communes aux deux architectures :

* 1 861 lignes
* Learning rate dynamique (start : 0.001 puis application d'un facteur 0.75 toutes les 10 époques)
* Images en entrée : hauteur 64 = hauteur de référence de transkribus, largeur variable
* Batch de 1
* Nombre époques : 30, avec early stopping (5 époques sans progression)
* Données entraînement : 10 XML (total : 1692 lignes, train : 1524 lignes, val : 168)
* Données test : 1 XML (168 lignes) : p48.xml
* Pas de normalisation unicode réalisée
* Pas de data augmentation

! Différence !
Pour Kraken j'utilise des images BW car meilleurs scores
Pour Calfa j'utilise des images couleur (idem)


## Expériences
### Modèle abrégé (= sans abréviations) avec espaces :
* Nombre classes : 60
* accuracy kraken : 95.11% ====> voir kraken-abrege_avec-espace_p48.txt
* accuracy calfa-marg : 95.29%

### Modèle abrégé sans espaces :
* Nombre classes : 59
* accuracy kraken : 95.45% ====> voir kraken-abrege_sans-espace_p48.txt
* accuracy calfa-marg : 95.45%

*Remarques* : Bon impact du learning rate dynamique pour Kraken.

### Modèle développé (= avec abréviations) avec espaces :
* Nombre classes : 34
* accuracy kraken : 89.41%
* accuracy calfa-marg : 96.24% ====> voir calfa-developpe_avec-espace_p48.txt

*Remarques* : Croissance rapide de kraken (époque 3 = 80% accuracy) puis stagne presque à partir de époque 10 malgré nouveau learning rate. Fin à l'époque 20 (90.48 en train).

### Modèle développé sans espaces :
* Nombre classes : 33
* accuracy kraken : 90.31%
* accuracy calfa-marg : 97.04% ====> voir calfa-developpe_sans-espace_p48.txt

*Remarques* : Croissance rapide de kraken (époque 4 = 83.28%) puis pertinence du Learning rate dynamique. Progression régulière. Fin à l'époque 27 (92.27). Mais résultat final à peine meilleur. Semble toutefois être capable de lire plusieurs abréviations.