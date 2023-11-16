import json
import requests
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self, category = "Binnen Potten"):
        self.category = category
        self.links = []
        self.filter_links_list = []
        self.bol_links_list = []
        self.bol_links_list_filtered = []
        self.bol_url = "https://www.bol.com"
        self.bol_search_page_url =  'https://www.bol.com/nl/nl/s/?page=1&searchtext=Binnen+potten&view=list'

    def page_flipper(self, page):
        self.bol_search_page_url = 'https://www.bol.com/nl/nl/s/?page=' + str(page) + '&searchtext=Binnen+potten&view=list'
        print(str(page) + " link :" + self.bol_search_page_url)

    def scrape_hrefs(self):
        response = requests.get(self.bol_search_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.links = [a['href'] for a in soup.find_all('a', href=True) if a['href']]
    
    def create_bol_links(self):
        self.bol_links_list = []
        for link in self.links:
            self.bol_links_list.append(self.bol_url + link)
        print("length links = " + str(len(self.links)))
    
    def filter_bol_links(self):
        for link in self.bol_links_list:
            if link not in self.filter_links_list and "searchtext" not in link:
                self.bol_links_list_filtered.append(link)        

    def page_scraper(self, start_page, end_page):
        for i in range(start_page, end_page):
            self.page_flipper(1)
            self.scrape_hrefs()
            self.create_bol_links()
            self.filter_bol_links()

    def get_filter_links(self):
        new_filter_list = []
        self.page_flipper(1)
        self.scrape_hrefs()
        self.create_bol_links()
        self.filter_links_list = self.bol_links_list
        self.page_flipper(50)
        self.scrape_hrefs()
        self.create_bol_links()

        for link in self.filter_links_list:
            if link in self.bol_links_list:
                new_filter_list.append(link)

        self.filter_links_list = new_filter_list

    def save_links_as_text(self):
        string_bol = ""
        for link in self.bol_links_list:
            string_bol += link + "\n"
        string_filter = ""
        for link in self.filter_links_list:
            string_filter += link + "\n"        
        string_bol_filtered = ""
        for link in self.bol_links_list_filtered:
            string_bol_filtered += link + "\n"

        with open('bol_links.txt', 'w') as f:
            f.write(string_bol)
        with open('filter_links.txt', 'w') as f:
            f.write(string_filter)
        with open('bol_links_filtered.txt', 'w') as f:
            f.write(string_bol_filtered)

    def save_links_filter(self):
        with open('filter_links.json', 'w') as f:
            json.dump(self.filter_links_list, f)

    def save_links_bol(self):
        category_str = self.category.replace(" ","_")
        save_name = 'bol_links_' + category_str + '.json'
        try:            
            with open('data.json', 'r') as f:
                data = json.load(f)
        except:
            data = []
        
        list(data).append(self.bol_links_list)

        with open(save_name, 'w') as f:
            json.dump(self.bol_links_list, f)


class Product_Scraper():
    def __init__(self):
        pass

    def load_links(self):
        pass

    def get_title(self):
        pass

    def get_price(self):
        pass

    def get_images(self):
        pass




Bol_scraper = Scraper()

Bol_scraper.get_filter_links()
Bol_scraper.filter_bol_links()
Bol_scraper.save_links_bol()
# Bol_scraper.save_links_as_text()