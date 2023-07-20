from anchor import Anchor
from div import Div
from form import Form
from img import Img
class JednoduchyFormular:
    def zakladni(self, action, type_input, name_input, id_input, class_input, placeholder_input, name_select, class_select, pocet_moznosti_select):
        zakladni_formular = Form(action = action)
        form_otevri_form = zakladni_formular.vypis_form()
        form_pridej_input = zakladni_formular.pridej_input(type_input, name_input, id_input, class_input, placeholder_input)
        form_pridej_select = zakladni_formular.pridej_select(name_select, class_select, pocet_moznosti_select)
        form_uzavri_form = zakladni_formular.uzavri_form()
        zakladni_formular_list = [form_otevri_form, form_pridej_input, form_pridej_select, form_uzavri_form]
        zakladni_formular_text = " ".join(zakladni_formular_list)
        return zakladni_formular_text




        
