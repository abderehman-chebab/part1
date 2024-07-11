import re

def extract_nutrition_values(text):
    # Regular expression to match nutritional values and their units
    pattern = re.compile(r'([\w\s\(\)\-]+)\s*:\s*([\d,\.]+\s*[a-zA-Z%]+)')

    # Find all matches in the text
    matches = pattern.findall(text)

    # Build the dictionary from the matches
    nutrition_dict = {match[0].strip(): match[1].strip() for match in matches}

    return nutrition_dict

text = """
Additifs nutritionnels : Vitamine C-D3 : 160 UI, Fer (3b103) : 4mg, Iode (3b202) : 0,28 mg, Cuivre (3b405, 3b406) : 2,2 mg,
Manganèse (3b502, 3b503, 3b504) : 1,1 mg, Zinc (3b603,3b605, 3b606) : 11 mg – Clinoptilolite d’origine sédimentaire : 2 g. 
Protéine : 11,0 % - Teneur en matières grasses : 4,5 % - Cendres brutes : 1,7 % - Cellulose brute : 0,5 % - Humidité : 80,0 %.
"""

nutrition_values = extract_nutrition_values(text)
print(nutrition_values)



