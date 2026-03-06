import time
from copy import deepcopy
from enum import Enum

from pony_express.service.grist import GristService, not_in_grist
from pony_express.service.pdf import generate_pdf
from pony_express.service.utils import get_date_from_timestamp, TEMPLATES_FOLDER_PATH
from slugify import slugify


# Main Function
def generate_exemple():
    grist_service = GristService(GRIST_DOC_ID, GRIST_SERVER, GRIST_ORG)
    people = grist_service.get_grist_data(GRIST_TABLE, PERSON_DATA, should_be_exported)
    data_to_upload = []
    for person in people:
        person = apply_data_transformation(person)
        pdf_path = generate_pdf(person,
                     TEMPLATES_FOLDER_PATH + "contrat_financier",
                     "contrat_financier_template",
                     "contrat_financier",
                     slugify(person[PERSON_DATA.participant_nom.name]+"_financier")
                     )
        pdf_id = grist_service.upload_attachments(pdf_path)
        data_to_upload.append({'id': person['id'], 'contrat_financier_pdf_non_signe':  ["L", pdf_id]})
    if data_to_upload:
        grist_service.update_grist_data(GRIST_TABLE, data_to_upload)


# Access informations to the Grist Data
# https://grist.numerique.gouv.fr/o/pony-express/3a8bd9w2WHfb
GRIST_SERVER = "https://grist.numerique.gouv.fr"
GRIST_ORG = "pony-express"
GRIST_DOC_ID = "3a8bd9w2WHfb6HrcRg8kms"
GRIST_TABLE = "Demarche_128447_annotations"


# Definition of all the information required by the PDF
# the name of the enum must be the name of the Typst parameter (ex: start_date)
# the value of the enum must be the name of the column in Grist (ex: ref_champs_date_debut_activite_hors_jours_de_voyage)
class PERSON_DATA(Enum):
    project_code = not_in_grist("code_projet")
    sector = "L’enseignement et la formation professionnels"
    activity_type=""
    organism=""
    organism_legal_status=""
    organism_address=""
    organism_email=""
    organism_code=""
    organism_person_name=""
    organism_person_title=""
    participant=not_in_grist("participant_fullname")
    participant_prenom="prenom_s_participant"
    participant_nom="nom_participant"
    participant_birthday="date_naissance"
    participant_address="adresse_participant"
    participant_phone="telephone_participant"
    participant_email="mail_participant"
    start_date=""
    end_date=""
    trip_duration="nombre_de_jours_de_voyage"
    duree_jours_bourse=""
    valeur_bourse="montant_bourse"
    frais_sejour=""
    frais_voyage=""
    limite_prolongation=""
    accompte_pourcentage=""
    option_prise_en_charge="Options modalité de prise en charge de la bourse choisie par l'EPL"


# Return true if all lines from the table must be exported and treated
# Add condition if any must be omitted
def should_be_exported(record) -> bool:
    return True


# Can be used to add any treatment of the data exported from grist
# for instance, date format, address validation etc...
def apply_data_transformation(dict) -> dict:
    transformed_dict = deepcopy(dict)
    transformed_dict[PERSON_DATA.participant_birthday.name] = get_date_from_timestamp(dict[PERSON_DATA.participant_birthday.name])
    transformed_dict[PERSON_DATA.participant.name] = dict[PERSON_DATA.participant_prenom.name] + " " + dict[PERSON_DATA.participant_nom.name]
    return transformed_dict

if __name__ == '__main__':
    print("GENERATE CONTRAT FINANCIER")
    generate_exemple()
