from datetime import datetime
from bs4 import BeautifulSoup
import requests


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'lxml')


class UfScraper:

    def __init__(self, date=None):
        self.errors = []
        self.data = []
        self.date = datetime.strptime(date, '%Y-%m-%d') if date else datetime.now()
        self.url = f'https://www.sii.cl/valores_y_fechas/uf/uf{self.date.year}.htm'
        self.soup = get_soup(self.url)

    def make(self):
        self.get_data()

        if len(self.data) < 1:
            self.errors.append('without data')
            return

        value: str = self.data[self.date.day - 1][self.date.month - 1]

        if not value:
            self.errors.append(f'UF not found for date {self.date}')

        return value

    def get_data(self):
        try:
            table = self.soup.find('div', id='mes_all').find('table')
            rows = table.find('tbody').findAll('tr')
            data = []

            for row in rows:
                columns = row.findAll('td')
                data_column = []

                for column in columns:
                    data_column.append(column.get_text(strip=True))

                data.append(data_column)

            self.data = data

        except (Exception,):
            self.errors.append('Error to get data from content and parse table')
