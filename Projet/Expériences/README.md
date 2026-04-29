# Description
Ce dossier contient les configurations des modèles, les échantillonages de ces modèles et des graphiques de leur distribution.
# Utilisation
Il suffit de suivre les instructions de [gflownet](https://github.com/alexhernandezgarcia/gflownet) pour l'installation et l'utilisation. Il est pratique de garder ses fichiers de configurations d'expérience dans le [dossier](https://github.com/alexhernandezgarcia/gflownet/tree/main/config/experiments/crystals)

À la racine de `glownet` on utilise cette commande pour entraîner le modèle avec un fichier de configuration `config.yaml`
```sh
python train.py +experiments=/crystals/config.yaml
``` 
