from markupsafe import Markup
class Select:
    
    def __init__(self, name, class_ ):
        self.name = name
        self.class_ = class_
        
    def vypis_moznosti(self, moznost):
        moznost = int(moznost)
        moznosti = []
        hodnota = 0
        while hodnota < moznost:
            hodnota +=1
            text = f'<option value="moznost{hodnota}">Možnost {hodnota}</option>\n'
            moznosti.append(text)
        moznosti_text = ""
        for moznost in moznosti:
            moznosti_text += f"\t{moznost}"
        vypis_select = f'<select name="{self.name}" class="{self.class_}">\n{moznosti_text}</select>'
        return Markup(vypis_select)                
                
        
            
