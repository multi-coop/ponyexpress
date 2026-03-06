import pathlib
from datetime import datetime


def get_date_from_timestamp(str_timestamp: str) -> str:
    if isinstance(str_timestamp, list):
        str_timestamp = _parse_grist_date_data(str_timestamp)
    timestamp = int(str_timestamp)
    date = datetime.fromtimestamp(timestamp)
    return date.strftime("%d-%m-%y")

def _parse_grist_date_data(grist_date: list[str]) -> str:
    return grist_date[1]

def concat_values(data: dict, labels: list) -> list:
    data_list = []
    for label in labels:
        if data[label]:
            data_list.append(data[label])
    return data_list

TEMPLATES_FOLDER_PATH = str(pathlib.Path(__file__).parent.parent.parent.parent.resolve()) + "/templates/"
