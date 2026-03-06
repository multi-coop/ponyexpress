from copy import deepcopy
from enum import Enum

from pony_express.service.grist import not_in_grist, GristService
from pony_express.service.pdf import generate_pdf
from pony_express.service.utils import get_date_from_timestamp, TEMPLATES_FOLDER_PATH, concat_values
from slugify import slugify


# Main Function
def generate_contrats_pedagogiques():
    grist_service = GristService(GRIST_DOC_ID, GRIST_SERVER, GRIST_ORG)
    people = grist_service.get_grist_data(GRIST_TABLE, STUDENT_DATA, should_be_exported)
    data_to_upload = []
    for person in people:
        person = apply_data_transformation(person)
        pdf_path = generate_pdf(person,
                                TEMPLATES_FOLDER_PATH + "contrat_pedagogique",
                                "contrat_pedagogique_template",
                                "contrat_pedagogique",
                                slugify(person[STUDENT_DATA.name.name] + "_pedagogique")
                                )
        pdf_id = grist_service.upload_attachments(pdf_path)
        data_to_upload.append({'id': person['id'], 'contrat_pedagogique_pdf_non_signe': ["L", pdf_id]})
    if data_to_upload:
        grist_service.update_grist_data(GRIST_TABLE, data_to_upload)


# Access informations to the Grist Data
GRIST_SERVER = "https://grist.numerique.gouv.fr"
GRIST_ORG = "pony-express"
GRIST_DOC_ID = "3a8bd9w2WHfb6HrcRg8kms"
GRIST_TABLE = "Demarche_128447_annotations"

"""
Definition of all the information required by the PDF
the name of the enum must be the name of the Typst parameter (ex: start_date)
the value of the enum must be the name of the column in Grist (ex: ref_champs_date_debut_activite_hors_jours_de_voyage)
"""


class STUDENT_DATA(Enum):
    name = "nom_participant"
    firstname = "prenom_s_participant"
    address = "adresse_participant"
    email = "mail_participant"
    phone = "telephone_participant"
    start_date = "ref_champs_date_debut_activite_hors_jours_de_voyage"
    end_date = "ref_champs_date_fin_activite_hors_jours_de_voyage"
    country_town = "ref_champs_pays_d_accueil"
    town = not_in_grist("town") ## MISSING
    name_guardian_1 = "nom_parent_tuteur_legal_1"
    firstname_guardian_1 = not_in_grist("firstname_guardian_1") ## MISSING
    email_guardian_1 = "mail_parent_tuteur_legal_1"
    phone_guardian_1 = "telephone_parent_tuteur_legal_1"
    name_guardian_2 = "nom_parent_tuteur_legal_2"
    firstname_guardian_2 = not_in_grist("firstname_guardian_2") ## MISSING
    email_guardian_2 = "mail_parent_tuteur_legal_2"
    phone_guardian_2 = "telephone_parent_tuteur_legal_2"
    guardians = not_in_grist("guardians") #Computed
    activity_type = "ref_champs_indiquer_le_type_de_mobilite"
    acquis_1 = "Acquis_1"
    acquis_2 = "Acquis_2"
    acquis_3 = "Acquis_3"
    acquis_list = not_in_grist("acquis_list") #Computed
    activite_1 = "Activite_1"
    activite_2 = "Activite_2"
    activite_3 = "Activite_3"
    activities = not_in_grist("activities") #Computed
    tutoring_1 = "Ref_table_tutorat_et_suivi_de_cette_activite_1"
    tutoring_2 = "Ref_table_tutorat_et_suivi_de_cette_activite_2"
    tutoring_3 = "Ref_table_tutorat_et_suivi_de_cette_activite_3"
    tutorings = not_in_grist("tutorings") #Computed
    project_code = not_in_grist("project_code") ## MISSING
    sending_organisation_name = not_in_grist("sending_organisation_name") ## MISSING
    sending_organisation_address = not_in_grist("sending_organisation_address") ## MISSING
    sending_organisation_email = not_in_grist("sending_organisation_email") ## MISSING
    sending_organisation_phone = not_in_grist("sending_organisation_phone") ## MISSING
    hosting_organisation_name = not_in_grist("hosting_organisation_name") ## MISSING
    hosting_organisation_address = not_in_grist("hosting_organisation_address") ## MISSING
    hosting_organisation_email = not_in_grist("hosting_organisation_email") ## MISSING
    hosting_organisation_phone = not_in_grist("hosting_organisation_phone") ## MISSING
    qualification = not_in_grist("qualification") ## MISSING
    school_year = not_in_grist("school_year") ## MISSING
    european_qualification_framework = not_in_grist("european_qualification_framework") ## MISSING
    staff_qualification = not_in_grist("staff_qualification") ## MISSING
    staff_school_year = not_in_grist("staff_school_year") ## MISSING
    staff_european_qualification_framework = not_in_grist("staff_european_qualification_framework") ## MISSING
    hosting_responsables = not_in_grist("hosting_responsables") #Computed
    sending_responsables = not_in_grist("sending_responsables") #Computed
    companions = not_in_grist("companions") #Computed

"""
Return true if all lines from the table must be exported and treated
Add condition if any must be omitted
"""


def should_be_exported(record: dict) -> bool:
    return True
    if 'status' in record:
        return record['status'] == "instruction"
    else:
        return False


"""
Can be used to add any treatment of the data exported from grist
for instance, date format, address validation etc...
"""


def apply_data_transformation(data: dict) -> dict:
    transformed_dict = deepcopy(data)
    transformed_dict[STUDENT_DATA.start_date.name] = get_date_from_timestamp(data[STUDENT_DATA.start_date.name])
    transformed_dict[STUDENT_DATA.end_date.name] = get_date_from_timestamp(data[STUDENT_DATA.end_date.name])
    transformed_dict[STUDENT_DATA.activities.name] = concat_values(data, [STUDENT_DATA.activite_1.name, STUDENT_DATA.activite_2.name,STUDENT_DATA.activite_3.name])
    transformed_dict[STUDENT_DATA.guardians.name] = get_guardians(data)
    transformed_dict[STUDENT_DATA.acquis_list.name] = concat_values(data, [STUDENT_DATA.acquis_1.name, STUDENT_DATA.acquis_2.name, STUDENT_DATA.acquis_3.name])
    transformed_dict[STUDENT_DATA.tutorings.name] = concat_values(data, [STUDENT_DATA.tutoring_1.name, STUDENT_DATA.tutoring_2.name, STUDENT_DATA.tutoring_3.name])
    transformed_dict[STUDENT_DATA.companions.name] = [{'name': not_in_grist(STUDENT_DATA.companions.name),
        'firstname': "",
        'email': "",
        'phone': "",
        'responsabilities': ""}]
    transformed_dict[STUDENT_DATA.hosting_responsables.name] = [{'name': not_in_grist(STUDENT_DATA.companions.name),
        'firstname': "",
        'email': "",
        'phone': "",
        'responsabilities': ""}]
    transformed_dict[STUDENT_DATA.sending_responsables.name] = [{'name': not_in_grist(STUDENT_DATA.companions.name),
        'firstname': "",
        'email': "",
        'phone': "",
        'responsabilities': ""}]
    return transformed_dict


def get_guardians(data: dict) -> list[dict]:
    guardians = []
    if data[STUDENT_DATA.name_guardian_1.name]:
        guardians.append({
            "name": data[STUDENT_DATA.name_guardian_1.name],
            "firstname": data[STUDENT_DATA.firstname_guardian_1.name],
            "email": data[STUDENT_DATA.email_guardian_1.name],
            "phone": data[STUDENT_DATA.phone_guardian_1.name]
        })
    if data[STUDENT_DATA.name_guardian_2.name]:
        guardians.append({
            "name": data[STUDENT_DATA.name_guardian_2.name],
            "firstname": data[STUDENT_DATA.firstname_guardian_2.name],
            "email": data[STUDENT_DATA.email_guardian_2.name],
            "phone": data[STUDENT_DATA.phone_guardian_2.name]
        })
    return guardians


if __name__ == '__main__':
    print("GENERATE CONTRATS PEDAGOGIQUES")
    generate_contrats_pedagogiques()
