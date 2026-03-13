import os
import pathlib
import subprocess

generated_file_path = str(pathlib.Path(__file__).parent.parent.parent.parent.resolve()) + "/generated/"
fonts_path = str(pathlib.Path(__file__).parent.parent.parent.parent.resolve()) + "/templates/"

def generate_pdf(data: dict, template_folder: str, template_file_name: str, template_name: str,
                 generated_file_name: str):
    generated_file = generated_file_path + generated_file_name
    typ_file = generated_file + ".typ"
    pdf_file = generated_file + ".pdf"
    call_to_template = create_call_to_template_string(template_name, data)
    with open(typ_file, "w") as file:
        file.writelines([
            f"#import \"{template_folder}/{template_file_name}.typ\": *\n",
            call_to_template
        ])
        file.close()
        subprocess.run(["typst", "compile", "--root", "/", typ_file, '--font-path', fonts_path])
        os.remove(typ_file)
    return pdf_file


def create_call_to_template_string(template_name, data):
    call_to_template = f"#{template_name}("
    for key, value in data.items():
        param = f"{key}:{to_typst_string(value)},"
        call_to_template += param
    call_to_template += ")"
    return call_to_template

def to_typst_string(param: any) -> str :
    if isinstance(param, list):
      return list_to_string(param)
    elif isinstance(param, dict):
      return dict_to_string(param)
    elif isinstance(param, tuple):
      return list_to_string(param)
    else :
      return '"'+str(param)+'"'

def list_to_string(py_list: list | tuple) -> str:
    typst_list = "("
    for item in py_list:
        typst_list += to_typst_string(item)
        typst_list += ","
    typst_list += ")"
    return typst_list

def dict_to_string(py_dict: dict) -> str:
    typst_dict = "("
    for key, value in py_dict.items():
        typst_dict += key + ":" + to_typst_string(value)
        typst_dict += ","
    typst_dict += ")"
    return typst_dict

