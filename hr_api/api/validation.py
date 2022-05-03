from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """Invalid model input."""


SYNTAX_ERROR_FIELD_MAP = {
    '1stFlrSF': 'FirstFlrSF',
    '2ndFlrSF': 'SecondFlrSF',
    '3SsnPorch': 'ThreeSsnPortch'
}


class AttritionDataRequestSchema(Schema):
    age = fields.Integer(allow_none=True)
    voyageDeTravail = fields.Str(allow_none=True)
    departement = fields.Str(allow_none=True)
    distanceEntreMaison = fields.Integer(allow_none=True)
    nivEtudeSup = fields.Integer(allow_none=True)
    filiereEtude = fields.Str(allow_none=True)
    nombreEmploye = fields.Integer(allow_none=True)
    IdEmploye = fields.Integer(allow_none=True)
    sexe = fields.Str(allow_none=True)
    nivTravail = fields.Integer(allow_none=True) 
    roleTravail = fields.Str(allow_none=True)
    etatMatrimonial = fields.Str(allow_none=True)
    revenuMensuel = fields.Integer(allow_none=True) 
    nbrAncienEntreprise = fields.Float(allow_none=True)
    plusDe18 = fields.Str(allow_none=True)
    pourcAugmentationDeSalaire = fields.Integer(allow_none=True) 
    heureStandard = fields.Integer(allow_none=True)                  
    nivCompensation = fields.Integer(allow_none=True) 
    anneeExperience = fields.Float(allow_none=True)
    nbrFormationAnneeDerniere = fields.Integer(allow_none=True) 
    anneeAncienete = fields.Integer(allow_none=True) 
    anneeDernierPromotion = fields.Integer(allow_none=True) 
    anneeAvecManager = fields.Integer(allow_none=True) 
    attrition = fields.Str(allow_none=True)

class PromotionDataRequestSchema(Schema):
    IdEmploye = fields.Integer()
    departement = fields.Str()
    region = fields.Str()
    nivDiplome = fields.Str(allow_none=True)
    sexe = fields.Str()
    chaineRecrutement = fields.Str()
    nbrFormation = fields.Integer()
    age = fields.Integer()
    noteAnneDerniere = fields.Float(allow_none=True)
    anneeExperience = fields.Integer()
    avoirPrix = fields.Integer()
    noteMoyFormation = fields.Integer()
    estPromu = fields.Integer(allow_none=True)


def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data, data_request):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    if data_request == 'promotion':
        schema = PromotionDataRequestSchema(many=True)
    elif data_request == 'attrition':
        schema = AttritionDataRequestSchema(many=True)
    else:
        raise ValueError('Data request not specify or null') 

    errors = {}
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
