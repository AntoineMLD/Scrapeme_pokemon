
from scrapeme.items import PokemonItem
import scrapy
import re

class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    #
    allowed_domains = ['scrapeme.live']
    start_urls = ['https://scrapeme.live/shop/']
    
    custom_settings = {
        'FEEDS' : {
            'pokemon_data.json' : {'format': 'json', 'overwrite': True},
        }
        


    }

    def parse(self, response):
        pokemons = response.xpath('.//ul[contains(@class, "products")]/li')
        
        for pokemon in pokemons:
            
            pokemon_url = pokemon.xpath('.//a/@href').get()
            yield response.follow(pokemon_url,self.parse_pokemon)
        
            for page_number in range(2,49):
                next_page_url = f'https://scrapeme.live/shop/page/{page_number}'
                yield response.follow(next_page_url, callback=self.parse)
                
            
    def parse_pokemon(self, response):
        pokemon_item = PokemonItem()
        dimension = response.xpath('.//td[@class="product_dimensions"]/text()').get()
        longueur = largeur = hauteur = None
        if dimension:
            pattern = re.search(r'(\d+) x (\d+) x (\d+)', dimension)
            
            if pattern:
                longueur = pattern.group(1)
                largeur = pattern.group(2)
                hauteur = pattern.group(3)
            
                
        
        pokemon_item["nom_du_pokemon"] = response.xpath('.//h1[contains(@class,"product_title")]//text()').get()
        pokemon_item["prix"] = response.xpath('.//p[contains(@class, "price")]/span/text()').get()
        pokemon_item["description"] = response.xpath('//div[contains(@class, "product-details")]/p/text()').get()
        pokemon_item["en_stock"] = response.xpath('//p[contains(@class,"stock")]//text()').get()
        pokemon_item["tags" ] = response.xpath('//span[contains(@class,"tagged")]/a/text()').getall()
        pokemon_item["categories" ] = response.xpath('//span[contains(@class, "posted")]/a/text()').getall()
        pokemon_item["sku"] = response.xpath('//span[@class="sku"]/text()').get()
        pokemon_item["poids"] = response.xpath('//td[@class="product_weight"]/text()').get()
        pokemon_item["longueur"] = longueur
        pokemon_item["largeur"] = largeur
        pokemon_item["hauteur" ] = hauteur
        
        yield pokemon_item