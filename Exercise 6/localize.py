import json

class Localize:
    lang = 'en'
    strings = {}
    
    @staticmethod
    def set_lang(lang):
        Localize.lang = lang
    
    @staticmethod
    def get(text):
        if Localize.lang not in Localize.strings:
            Localize.strings[Localize.lang] = {}
            
        if text not in Localize.strings[Localize.lang]:
            Localize.strings[Localize.lang][text] = text
            
        return Localize.strings[Localize.lang][text]
    
    @staticmethod
    def load():
        with open('localizations.dat') as infile:
            Localize.strings = json.load(infile)
    
    @staticmethod
    def save():
        with open('localizations.dat', 'w') as outfile:
            json.dump(Localize.strings, outfile, sort_keys=True, indent=4)

# doesn't work if _ for some reason
language = Localize.get


#print(_("Clicks: "))

# TODO build file with translations
# render(_("Clicks: ") + str(clicks))

Localize.load()
#Localize.set_lang('en')

#print(Localize.strings)
#print (Localize.get("Clicks: "))
#print (Localize.get("Scores: "))

#Localize.set_lang('es')
#print (Localize.get("Vehicles: "))
#print (Localize.get("Car"))
#print (Localize.get("Truck"))
#print(Localize.strings)

#Localize.save()