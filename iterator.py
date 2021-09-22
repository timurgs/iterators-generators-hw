import json


HOST = 'https://en.wikipedia.org/wiki/'


class Countries:
    def __init__(self):
        self.i = 0
        with open('countries.json') as f1:
            self.data = json.load(f1)

    def __iter__(self):
        return self

    def __next__(self):
        item = self.data[self.i]
        country_name = item['name']['common']
        if len(country_name.split()) > 1:
            url = f'{HOST}{"_".join(country_name.split())}'
        else:
            url = f'{HOST}{country_name}'
        with open('result.txt', 'a', encoding='utf-8') as f2:
            f2.write(f'{country_name} - {url}\n')
        self.i += 1
        if self.data[-1] == item:
            raise StopIteration


countries = Countries()

for country in countries:
    pass
