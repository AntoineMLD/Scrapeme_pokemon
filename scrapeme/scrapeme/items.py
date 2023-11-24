# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy




class PokemonItem(scrapy.Item):
    nom_du_pokemon= scrapy.Field()
    prix = scrapy.Field()
    description = scrapy.Field()
    en_stock = scrapy.Field()
    tags = scrapy.Field()
    categories = scrapy.Field()
    sku = scrapy.Field()
    poids = scrapy.Field()
    longueur = scrapy.Field()
    largeur = scrapy.Field()
    hauteur = scrapy.Field()
    