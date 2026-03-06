---
title: Generer votre propre pdf
description: Generer votre propre pdf
---

In ordre to create your own PDF, you will need : 

- to create a Typst template that will create a PDF with the desired layout
- configure a python script that will import the Grist data and export them as PDF

Pony express will
- import your data from grist
- create a typst file that will import and setup your template
- compile this file to a pdf and delete the intermediary file

## Typst 

Typst is an user friendly Latex alternative.
You can find the documentation [here](https://typst.app/docs/) and experiment with it in their [online app](https://typst.app/app/)

Create a folder in `templates` for your own projet.

You can use `./templates/exemple/birthday_template.typ` as reference.

Being a template, it can't be compiled itself. You need another file that will import it and give it its required parameters (those are the files created automatically by pony_express)

You can create your own to test your template independently from pony_express.
_`./template/exemple/test_birthday.typ`_ is an exemple of such a file

To test it : 

- you can compile it ``typst compile templates/exemple/test_birthday.typ ``
- you can import both the test_birthday and the birthday_template in the typst webapp to experiment with it online
- you can use the [tinymist extension](https://marketplace.visualstudio.com/items?itemName=myriad-dreamin.tinymist) for VSCodium to have a direct preview locally
  - troubleshooting : the extension does not give you the error message. is there is no working preview, compile your file manually to display the compilation error messages

### Fonts 

You can add any font in your template folder. It will be scanned and added by pony express when compiling.

## Python 

Once you have a template, you can now duplicate the src/exemple.py file. 
Use the included commentaries to configure the variables and functions according to your needs.

You can now run it by calling 

```sh
poetry run python src/pony_express/exemple.py
```

The generated pdf will appear `generated`
