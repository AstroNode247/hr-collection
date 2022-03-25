ATTRITION_TARGET = "attrition"

ATTRITION_FEATURES = ['age', 'distanceEntreMaison', 'nivEtudeSup', 'nombreEmploye',
                      'nivTravail', 'revenuMensuel', 'nbrAncienEntreprise',
                      'pourcAugmentationDeSalaire', 'heureStandard', 'nivCompensation',
                      'anneeExperience', 'nbrFormationAnneeDerniere', 'anneeAncienete',
                      'anneeDernierPromotion', 'anneeAvecManager',
                      'voyageDeTravail', 'departement', 'filiereEtude', 'sexe', 'roleTravail',
                      'etatMatrimonial', 'plusDe18']

ATTRITION_NUM_FEATURES = ['age', 'distanceEntreMaison', 'nivEtudeSup', 'nombreEmploye', 'nivTravail',
                          'revenuMensuel', 'nbrAncienEntreprise', 'pourcAugmentationDeSalaire', 'heureStandard',
                          'nivCompensation', 'anneeExperience', 'nbrFormationAnneeDerniere', 'anneeAncienete',
                          'anneeDernierPromotion', 'anneeAvecManager']

ATTRITION_CAT_FEATURES = ['departement', 'filiereEtude', 'sexe', 'roleTravail',
                          'etatMatrimonial', 'plusDe18']

ATTRITION_LABELED_FEATURES = ['voyageDeTravail']
ATTRITION_SKEWED_FEATURES = ["revenuMensuel"]

PROMOTION_TARGET = "estPromu"

PROMOTION_FEATURES = ["departement", "region", "nivDiplome", "sexe", "chaineRecrutement",
                      "nbrFormation", "age", "noteAnneDerniere", "anneeExperience", "avoirPrix",
                      "noteMoyFormation"]

PROMOTION_CAT_FEATURES = ["departement", "region", "nivDiplome", "sexe", "chaineRecrutement"]
PROMOTION_NUM_FEATURES = ["nbrFormation", "age", "noteAnneDerniere", "anneeExperience",
                          "avoirPrix", "noteMoyFormation"]

PROMOTION_CAT_MISSING = ["nivDiplome"]
PROMOTION_NUM_MISSING = ["noteAnneDerniere"]

PROMOTION_FEATURES_SELECTED = ['nbrFormation', 'age', 'noteAnneDerniere', 'anneeExperience',
                             'avoirPrix', 'noteMoyFormation', 'departement_Analytiques',
                             'departement_Approvisionnement', 'departement_Finance',
                             'departement_Juridique', 'departement_Recherche et Developpement',
                             'departement_Ressources Humaines', 'departement_Ventes',
                             'region_region_1', 'region_region_10', 'region_region_11',
                             'region_region_14', 'region_region_15', 'region_region_2',
                             'region_region_20', 'region_region_22', 'region_region_23',
                             'region_region_24', 'region_region_26', 'region_region_29',
                             'region_region_3', 'region_region_33', 'region_region_4',
                             'region_region_6', 'region_region_7', 'region_region_8',
                             'region_region_9', 'nivDiplome_License', 'nivDiplome_Master ou plus',
                             'nivDiplome_Missing', 'nivDiplome_Secondaire ou moin', 'sexe_f',
                             'sexe_m', 'chaineRecrutement_autre', 'chaineRecrutement_recommendé']
