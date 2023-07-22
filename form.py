from select_ import Select
from div import Div
from img import Img
from anchor import Anchor
from input import Input
from markupsafe import Markup

#třída Form
class Form:

#list pro ukládání formuláře a definování počtu elementů ve formuláři
    seznam_formular = []
    seznam_inputu = []
    seznam_selectu = []
    seznam_divu = []
    seznam_img = []
    seznam_anchor = []

#paramentry při inicializaci objektu
    def __init__(self, action, div_pred, method = "POST"):
        if div_pred == "ano":
            self.div_pred = div_pred
        else:
            self.div_pred = None            
        self.action = action
        self.method = method

#popis objektu třídy
    def __str__(self):
        if self.div_pred:
            class_ = input("Zadejte třídu divu:")
            vypis_div = f'<div class="{class_}">\n'
            vypis_form = f'<form action="{self.action}" method="{self.method}">'
            vypis_div_form = f"{vypis_div}{vypis_form}"           
            return Markup(vypis_div_form)
        else:
            vypis_form = f'<form action="{self.action}" method="{self.method}">'
            vypis = f"{vypis_form}"           
            return Markup(vypis)

#metoda pro tvorbu elementů input formuláře            
    def vytvor_inputy(self, pocet_input):
        hodnota = 0
        while hodnota < pocet_input:
            hodnota += 1
            print(f"Zadejte hodnoty u {hodnota} inputu:")
            type_input = input("zadejte type:\n")
            name_input = input("zadejte name:\n")
            id_input = input("zadejte id:\n")
            class_input = input("zadejte classu:\n")
            placeholder_input = input("zadejte placehoder:\n")
            input_objekt = Input(type=type_input, name=name_input, id=id_input, class_=class_input, placeholder=placeholder_input)
            self.seznam_inputu.append(input_objekt)

#metoda pro přidání definovaného elementu input do furmuláře
    def pridej_input(self, cislo):
        for index in self.seznam_inputu:
            index = cislo - 1
            return self.seznam_formular.append(self.seznam_inputu[index])        

#metoda pro tvorbu elementů select formuláře        
    def vytvor_selecty(self, pocet_select):
        hodnota = 0
        while hodnota < pocet_select:
            hodnota += 1
            print(f"Zadejte hodnoty u {hodnota} selectu:")
            name_select = input("zadejte name:\n")
            class_select = input("zadejte classu:\n")
            pokracovat = True
            while pokracovat:
                try:
                    pocet_moznosti_select = int(input(f"zadejte počet možností u  {hodnota} selectu\n"))
                    objekt_select = Select(name=name_select, class_=class_select)
                    self.seznam_selectu.append(objekt_select.vypis_moznosti(pocet_moznosti_select))
                    pokracovat = False
                except ValueError:
                    print("Nezadali jste číslo")
                    pokracovat = True

#metoda pro přidání definovaného elementu select do furmuláře
    def pridej_select(self, cislo):
        for index in self.seznam_selectu:
            index = cislo - 1
            return self.seznam_formular.append(self.seznam_selectu[index])        

#metoda pro tvorbu elementů div formuláře     
    def vytvor_divy(self, pocet_divu):
        hodnota = 0
        while hodnota < pocet_divu:
            hodnota += 1
            print(f"Zadejte hodnoty u {hodnota} divu:")
            class_div = input("zadejte classu:\n")
            objekt_div = Div(class_=class_div)
            self.seznam_divu.append(objekt_div)

#metoda pro přidání definovaného elementu div do furmuláře
    def pridej_div(self, cislo):
        for index in self.seznam_divu:
            index = cislo - 1
            return self.seznam_formular.append(self.seznam_divu[index])        

#metoda pro přidání uzavíracího elementu div do formuláře
    def pridej_uzavri_div(self):
        uzavri_div = f'</div>'
        return self.seznam_formular.append(Markup(uzavri_div))

#metoda pro tvorbu img elementu formuláře
    def vytvor_img(self, pocet_img):
        hodnota = 0
        while hodnota < pocet_img:
            hodnota += 1
            print(f"Zadejte hodnoty u {hodnota} img:")
            src_img = input("Zadejte src:\n")
            class_img = input("Zadejte classu:\n")
            width_img = input("Zadejte hodnotu width:\n")
            height_img = input("Zadejte hodnotu height:\n")
            alt_img = input("Zadejte alt:\n")
            objekt_img = Img(src=src_img, class_=class_img, width=width_img, height=height_img, alt=alt_img)
            self.seznam_img.append(objekt_img)

#metoda pro přidání definovaného img elementu do furmuláře
    def pridej_img(self, cislo):
        for index in self.seznam_img:
            index = cislo - 1
            return self.seznam_formular.append(self.seznam_img[index])        

#metoda pro tvorbu elementů anchor formuláře
    def vytvor_anchor(self, pocet_anchor):
        hodnota = 0
        while hodnota < pocet_anchor:
            hodnota += 1
            print(f"Zadejte hodnoty u {hodnota} anchor:")
            text_anchor = input("Zadejte text:\n")
            url_anchor = input("Zadejte odkaz:\n")
            class_anchor = input("zadejte classu:\n")
            anchor_objekt = Anchor(text=text_anchor, url=url_anchor, class_=class_anchor)
            self.seznam_anchor.append(anchor_objekt)

#metoda pro přidání definovaného elementu anchor do furmuláře
    def pridej_anchor(self, cislo):
        for index in self.seznam_anchor:
            index = cislo - 1
            return self.seznam_formular.append(self.seznam_anchor[index])        

#metoda pro přidání uzavíracího elementu anchor do formuláře
    def pridej_uzavri_anchor(self):
        uzavri_anchor = f'</a>'
        return self.seznam_formular.append(Markup(uzavri_anchor))

#metoda pro přidání uzavíracího elementu form do formuláře
    def pridej_uzavri_form(self):
        uzavri_form = f'</form>'
        return self.seznam_formular.append(Markup(uzavri_form))