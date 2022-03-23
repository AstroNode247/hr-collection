import pandas as pd
import sqlite3

from hr_collection.hr_pipeline.pipeline.base_pipeline import BaseData, ITransformer

from hr_collection.config import config


class PromotionData(BaseData, ITransformer):
    def __init__(self):
        super().__init__()
        self.data = pd.read_csv(f"{config.DATASETS_DIR}/{config.PROMOTION_DATA_FILE}")

    def transform(self):
        data_cols = ['idEmploye', 'departement', 'region', 'nivDiplome', 'sexe', 'chaineRecrutement', 'nbrFormation',
                     'age', 'noteAnneDerniere', 'anneeExperience', 'avoirPrix', 'noteMoyFormation',
                     'estPromu']
        self.data.columns = data_cols

        self.data['departement'] = self.data['departement'].replace(
            ['Sales & Marketing', 'Operations', 'Technology', 'Procurement', 'Analytics', 'Finance', 'HR', 'Legal',
             'R&D'],
            ['Ventes', 'Operations', 'Technologie', 'Approvisionnement', 'Analytiques', 'Finance',
             'Ressources Humaines', 'Juridique', 'Recherche et Developpement'],
        )

        self.data['nivDiplome'] = self.data['nivDiplome'].replace(
            ["Bachelor's", "Master's & above", "Below Secondary"],
            ["License", "Master ou plus", "Secondaire ou moin"]
        )

        self.data['chaineRecrutement'] = self.data['chaineRecrutement'].replace(
            ["other", "sourcing", "referred"],
            ["autre", "sourcing", "recommendé"],
        )


class AttritionData(BaseData, ITransformer):
    def __init__(self):
        super().__init__()
        self.data = pd.read_csv(f"{config.DATASETS_DIR}/{config.ATTRITION_DATA_FILE}")

    def transform(self):
        french_cols = ['age', 'attrition', 'voyageDeTravail', 'departement', 'distanceEntreMaison', 'nivEtudeSup',
                       'filiereEtude',
                       'nombreEmploye', 'idEmploye', 'sexe', 'nivTravail', 'roleTravail', 'etatMatrimonial',
                       'revenuMensuel',
                       'nbrAncienEntreprise', 'plusDe18', 'pourcAugmentationDeSalaire', 'heureStandard',
                       'nivCompensation',
                       'anneeExperience', 'nbrFormationAnneeDerniere', 'anneeAncienete', 'anneeDernierPromotion',
                       'anneeAvecManager']
        self.data.columns = french_cols

        self.data['attrition'] = self.data['attrition'] \
            .replace(['No', 'Yes'], ['Non', 'Oui'])

        self.data['voyageDeTravail'] = self.data['voyageDeTravail'] \
            .replace(['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'],
                     ['Voyage rarement', 'Voyage frequemment', 'Aucun voyage'])

        self.data['departement'] = self.data['departement'] \
            .replace(['Research & Development', 'Sales', 'Human Resources'],
                     ['Recherche et Developpement', 'Ventes', 'Ressources Humaines'])

        self.data['filiereEtude'] = self.data['filiereEtude'] \
            .replace(['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other', 'Human Resources'],
                     ['Sciences de la vie', 'Medecine', 'Marketing', 'Diplome Polytechnique', 'Autre',
                      'Ressources Humaine'])

        self.data['sexe'] = self.data['sexe'] \
            .replace(['Male', 'Female'],
                     ['Homme', 'Femme'])

        self.data['roleTravail'] = self.data['roleTravail'] \
            .replace(['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director',
                      'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director',
                      'Human Resources'],
                     ['Directeurs des ventes', 'Chercheurs', 'Technicien de laboratoire', 'Directeur de fabrication',
                      'Médecin interne', 'Manager', 'Commercial', 'Directeur de recherche', 'Ressources humaines'])

        self.data['etatMatrimonial'] = self.data['etatMatrimonial'] \
            .replace(['Married', 'Single', 'Divorced'],
                     ['Marrié', 'Célibataire', 'Divorcé'])

        self.data['plusDe18'] = self.data['plusDe18'].replace('Y', 'O')
