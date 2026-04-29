Tout ce qui est utile à l'analyse

# Scripts
- `données.py` créer le jeu de données d'entraînement. Il combine [gull.csv](https://github.com/alexhernandezgarcia/gflownet/blob/main/data/crystals/gull.csv) de `gflownet` et `eform_train.csv` de Alex
- `analyse_projet.py` prend un fichier `.csv` de cristaux généré par `gflownet` puis renvoit un graphique avec 3 sous-graphiques et calcul la densité moyenne et son écart-type
- `training_composition_visualisation.py` calcule les atomes les plus fréquents dans les molécules du jeu d'entraînement
- `data_visualisation_composition.py` crée le graphique `Distribution_of_molecule_composition_based_on_density_trained.png`
# Données générées
- `Alétoire.csv` est les données générées par un modèle gflownet non entraîné avec nos configurations
- `density_Pd.csv` est l'échantillonage turaco density rbf avec `beta` : -0.3516, `center` : 12
- `density_Pt_1.csv` est l'échantillonage turaco density rbf avec `beta` : -0.3516, `center`: 21.45
- `density_Pt_2.csv` est l'échantillonage turaco density rbf avec `beta` : -1e-3, `center` : 21.45
- Les autres échantillonages sont dans [Expériences](https://github.com/Matiou123/IFT-3710/tree/main/Projet/Exp%C3%A9riences)
# Graphiques
- `Distribution_of_molecule_composition_based_on_density_trained.png` est la distribution des cristaux générés par nos modèles avec la comparaison d'une distribution uniforme.
- `Alétoire.pdf` est le graphique du modèle gflownet non entraîné
- `densités_turacos_density.pdf` est le graphique des distributions obtenues en changeant le proxy pour une rbf centrée selon différent centre dans le fichier de configuration [turaco_density.yaml](https://github.com/alexhernandezgarcia/gflownet/blob/main/config/experiments/crystals/turaco_density.yaml).
# Utiles
- `Periodic Table of Elements.csv` est le tableau périodique utilisé dans `training_composition_visualisation.py`
- `train.csv` est le jeu de données retenu par `glownet` dans les expériences.
- `statistiques_density.txt` contient la moyenne et l'écart-type du jeu de données
