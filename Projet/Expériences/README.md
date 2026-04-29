# Description
Ce dossier contient les configurations des modèles, les échantillonages de ces modèles et des graphiques de leur distribution.
# Utilisation
Le projet dépend de [gflownet](https://github.com/alexhernandezgarcia/gflownet). Il suffit de suivre les instructions de [gflownet](https://github.com/alexhernandezgarcia/gflownet) pour l'installation et l'utilisation. Il est pratique de garder ses fichiers de configurations d'expérience dans le dossier [gflownet/config/experiments/crystals/](https://github.com/alexhernandezgarcia/gflownet/tree/main/config/experiments/crystals)

À la racine de `glownet` on utilise cette commande pour entraîner le modèle avec un fichier de configuration `config.yaml` qui se trouve dans le [gflownet/config/experiments/crystals/](https://github.com/alexhernandezgarcia/gflownet/tree/main/config/experiments/crystals).

```sh
python train.py +experiments=/crystals/config.yaml
``` 
Après l'entraînement, un dossier du modèle devrait être créé et se trouver dans `gflownet/logs/crystalgfn/local/`. Le nom du dossier devrait être un type  *timestamp*, par exemple `/2026-04-07_18-17-05_985445`. Il faut utiliser ce dossier pour l'échantillonage. Il faut passer cette commande à la racine de `gflownet` pour échantilloner
```sh
python eval.py rundir=gflownet/logs/crystalgfn/local/2026-04-07_18-17-05_985445/ n_samples=1000
```
Un fichier `gfn_samples.csv` devrait être alors être créé dans `gflownet/logs/crystalgfn/local/2026-04-07_18-17-05_985445/eval/samples` qui représente l'échantillonage du modèle.

Pour obtenir le graphique et les statistiques (moyenne et écart-type) de l'échantillion, on peut utiliser le script [analyse_projet.py](https://github.com/Matiou123/IFT-3710/blob/main/Projet/analyse_projet.py). Dans ce script, il suffit juste de changer le chemin vers le fichier d'échantillonage et de changer le sur-titre pour qu'il soit approprié, donc ces deux variables
```python
# Chemin csv eval
chemin = "logs/crystalgfn/local/2026-04-13_00-36-55_666578/eval/samples/gfn_samples.csv"
titre = "testing.pdf" # Sur-titre du graphique
```
