import json
import wikipedia


class New_Iterator:
    def __init__(self, file):
        with open(file, encoding='utf-8') as f:
            self.json_file = json.load(f)
        self.start = int()
        self.end = len(self.json_file)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        try:
            name_country = self.json_file[self.start - 1]['name']['common']
            try:
                page_country = wikipedia.page(name_country)
            except wikipedia.exceptions.DisambiguationError:
                page_country = wikipedia.page(name_country + '(country)')
            url_country = page_country.url
            result = name_country + ' - ' + url_country

            with open('final.txt', 'a', encoding='utf-8') as f:
                f.write(result + '\n')

            if self.start > self.end:
                raise StopIteration

            return result

        except IndexError:
            raise StopIteration


def main():
    for x in New_Iterator('countries.json'):
        print(x)


if __name__ == '__main__':
    main()
