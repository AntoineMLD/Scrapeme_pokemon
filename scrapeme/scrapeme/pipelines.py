
from itemadapter import ItemAdapter
import sqlite3
import re
from scrapy.exceptions import NotConfigured

class ScrapemePipeline:
     def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        

        # Converti le poids en un format numérique (int)
        poids = adapter['poids'].replace('kg', '').strip()
        adapter['poids'] = int(float(poids))  

        # Normalise le nom du Pokémon en minuscules
        adapter['nom_du_pokemon'] = adapter['nom_du_pokemon'].lower()

        # Modifie les catégories pour supprimer "Pokemon"
        adapter['categories'] = [cat for cat in adapter['categories'] if cat.lower() != 'pokemon']
        adapter['categories'] = ', '.join(adapter['categories'])

        # Transforme les tags en chaînes de caractères
        adapter['tags'] = ', '.join(adapter['tags'])

        # Converti la hauteur, la longueur et la largeur en int
        adapter['hauteur'] = int(adapter['hauteur'])
        adapter['longueur'] = int(adapter['longueur'])
        adapter['largeur'] = int(adapter['largeur'])

        # Converti le stock en int
        stock = adapter['en_stock'].replace('in stock', '').strip()
        adapter['en_stock'] = int(stock)

        
        return adapter.item


class SQLitePipeline(object):
    def __init__(self, sqlite_file):
        self.sqlite_file = sqlite_file

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.get('SQLITE_FILE'):
            raise NotConfigured("Missing 'SQLITE_FILE' setting")
        return cls(
            sqlite_file=crawler.settings.get('SQLITE_FILE')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cursor = self.conn.cursor()
        # Création de la table si elle n'existe pas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pokemons (
                nom_du_pokemon TEXT,
                prix REAL,
                description TEXT,
                en_stock INTEGER,
                tags TEXT,
                categories TEXT,
                sku INTEGER,
                poids INTEGER,
                longueur INTEGER,
                largeur INTEGER,
                hauteur INTEGER
            )
        ''')
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        data = (
            adapter['nom_du_pokemon'],
            adapter['prix'],
            adapter['description'],
            adapter['en_stock'],
            adapter['tags'],
            adapter['categories'],
            adapter['sku'],
            adapter['poids'],
            adapter['longueur'],
            adapter['largeur'],
            adapter['hauteur']
        )
        self.cursor.execute('''
            INSERT INTO pokemons (
                nom_du_pokemon, prix, description, en_stock, tags, categories, sku, poids, longueur, largeur, hauteur
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        self.conn.commit()
        return item
