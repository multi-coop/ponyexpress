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
    people = grist_service.get_grist_data(GRIST_TABLE, STUDENT_DATA, should_be_exported)
    for person in people:
        person = apply_data_transformation(person)
        generate_pdf(person,
                     TEMPLATES_FOLDER_PATH + "exemple",
                     "birthday_template",
                     "birthday",
                     slugify(person[PERSON_DATA.name.name])
                     )


# Access informations to the Grist Data
GRIST_SERVER = "https://docs.getgrist.com"
GRIST_DOC_ID = "uJrM5M5P5Z4Qzm927qDK6a"
GRIST_TABLE = "Anniversaires"


# Definition of all the information required by the PDF
# the name of the enum must be the name of the Typst parameter (ex: start_date)
# the value of the enum must be the name of the column in Grist (ex: ref_champs_date_debut_activite_hors_jours_de_voyage)
class PERSON_DATA(Enum):
    name = "Nom"
    firstname = "Prenom"
    birthday = "Date_d_anniversaire"
    age = not_in_grist("age")


# Return true if all lines from the table must be exported and treated
# Add condition if any must be omitted
def should_be_exported(record) -> bool:
    if hasattr(record, PERSON_DATA.birthday.value):
        # ignore the line if the exemple is in the future
        return getattr(record, PERSON_DATA.birthday.value) < time.time()
    else:
        return False


# Can be used to add any treatment of the data exported from grist
# for instance, date format, address validation etc...
def apply_data_transformation(dict) -> dict:
    transformed_dict = deepcopy(dict)
    transformed_dict[PERSON_DATA.birthday.name] = get_date_from_timestamp(dict[PERSON_DATA.birthday.name])
    transformed_dict[PERSON_DATA.age.name] = calculate_age(dict[PERSON_DATA.birthday.name])
    return transformed_dict


def calculate_age(birthday) -> int:
    now = time.time()
    duration_in_seconds = now - birthday
    years = divmod(duration_in_seconds, 31536000)[0]  # Seconds in a year=365*24*60*60 = 31536000.
    return round(years)


if __name__ == '__main__':
    print("GENERATE BIRTHDAY CARD")
    generate_exemple()
