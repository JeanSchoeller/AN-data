from bs4 import BeautifulSoup
import pandas as pd
from unicodedata import normalize
from os import listdir
from tqdm import tqdm

# Directory containing the XML files
directory = listdir("compteRendu/")

def data_generator():
    # Process each file in the directory
    for file in tqdm(directory, desc="Processing files"):
        with open("compteRendu/" + file, 'r') as f:
            # Parse the XML content incrementally to reduce memory usage
            soup = BeautifulSoup(f, "xml")

            # Extract president's name and session date
            president_xml = soup.find("presidentSeance")
            string_president = president_xml.get_text()
            president = string_president.replace("Présidence de ", "")
            date_jour = soup.find("dateSeanceJour").get_text()

            # Extract paragraphs directly
            for p in soup.find_all("paragraphe"):
                id_sen = p.find("id")
                text_xml = p.find("texte")
                names = p.find("nom")

                if id_sen and text_xml and names:
                    id_sen_txt = "PA" + id_sen.get_text()
                    text_app = text_xml.get_text()
                    names_txt = names.get_text()

                    if names_txt in ["M. le président", "Mme la présidente"]:
                        names_txt = president

                    # Yield data as a tuple
                    yield id_sen_txt, names_txt, date_jour, text_app

# Create a DataFrame from the collected data using a generator
df_final = pd.DataFrame(data_generator(), columns=['id', 'name', 'date', 'text'])

# Save DataFrame to CSV
df_final.to_csv("test.csv", index=False)
print(df_final.head())
