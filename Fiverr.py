import datetime
import json
import os

from fake_useragent import UserAgent
from selenium.webdriver import Keys
from seleniumwire import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

import random
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC





def generate_name_with_timestamp(base_name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}.xlsx"

# Exemple d'utilisation


def DataScraping(search, home_directory):

    # Options pour Firefox
    options = Options()

    # Ajouter l'extension
    options.add_argument("--headless")
    options.set_preference("webgl.disabled", True)
    options.set_preference("media.peerconnection.enabled", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference('useAutomationExtension', False)
    options.set_preference("general.platform.override", "Win32")
    options.set_preference("intl.accept_languages", "en-US, en")
    # options.set_preference("intl.locale.matchOS", False)
    #options.add_argument('-private')
    # Désactiver le chargement automatique des images
    # options.set_preference("permissions.default.image", 2)

    # Activer la mise en cache
    # options.set_preference("browser.cache.disk.enable", True)
    # options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0")
    # options.add_argument('-private')  # Activer le mode de navigation privée

    # Charger l'extension
    # options.add_argument(f'--load-extension=C:\\Users\\hamza\\Downloads\\urban_vpn-3.14.0.xpi')

    # Configurer le service GeckoDriver

    # Démarrer Firefox avec Selenium
    driver = webdriver.Firefox( options=options)

    # Exécuter des scripts JavaScript pour rendre Selenium encore plus indétectable
    driver.execute_script('''
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined })
    ''')



    # Ouvrir une page web
    driver.get(f'https://www.google.com/search?ibp=htl;jobs&q={search}')
    #time.sleep(4)

    Data_value = []

    while True:
        try:
            #Data_value.clear()
            # Vérifie si l'élément est affiché
            if driver.find_element(By.XPATH, "//img[@jsname='R26PWc']").is_displayed():
                break  # Sortir de la boucle si l'élément est affiché
        except:
            # Si l'élément n'est pas trouvé, continuer à défiler
            pass

        # Faire défiler la page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    time.sleep(4)
    a = driver.find_elements(By.XPATH, "//div[@jsname='iTtkOe']//div[1]//div[@class='EimVGf']")
    for element in a:
        print("element")
        print(element.get_attribute("outerHTML"))
        lien=element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        #print(lien)
        b=element.find_elements(By.XPATH,".//div[@class='GoEOPd']")

        for i in b:
            print("i")
            print(i.get_attribute("outerHTML"))
            divs = i.find_elements(By.TAG_NAME, 'div')
            Titre=divs[0].text
            Entreprise=divs[1].text
            SourceEtLieu= divs[2].text
            Data_value.append({
                'Lien':lien,
                'Titre': divs[0].text.strip(),
                'Entreprise': divs[1].text.strip(),
                'Source Et Lieu': divs[2].text.strip()
            })
    df = pd.DataFrame(Data_value)
    print(Data_value)
    new_name = generate_name_with_timestamp("JobsData")
    # Définir le chemin complet pour enregistrer le fichier Excel
    file_path = os.path.join(home_directory, f"{new_name}")

    # Exporter vers un fichier Excel dans le répertoire personnel de l'utilisateur
    df.to_excel(file_path, index=False)
    print(file_path)
    driver.quit()
