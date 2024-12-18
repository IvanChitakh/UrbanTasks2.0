import re

class WordsFinder:
    file_names = []

    def __init__(self, *file_param):
        for item in file_param:
            self.file_names.append(item)

    def get_all_words(self):
        all_words = {}
        da_list = [',', '.', '=', '!', '?', ';', ':', '(', ')', '"', "'", '...']
        pattern = r"[^\w'\s]"

        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                string_type = file.read().lower()
                string_type = re.sub(pattern, ' ', string_type)
                list_type = string_type.split()
                all_words[file_name] = list_type

        return all_words

    def find(self, word):
        word_ind = {}
        for name, words in self.get_all_words().items():
            for idx, w in enumerate(words):
                if w.lower() == word.lower():
                    word_ind[name] = idx + 1
                    return word_ind
        return 'Нет его'

    def count(self, word):
        word_ind = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            count = sum(1 for w in words if w.lower() == word)
            if count > 0:
                word_ind[name] = count
        return word_ind if word_ind else 'Нет его'

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего