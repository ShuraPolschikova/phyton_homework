import string
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.word_dict = {}

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation + "—"))
                words = text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        find_pos = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            word = word.lower()
            if word in words:
                find_pos[file_name] = words.index(word)+1  #+1 так как счёт начинается с нуля
            else:
                print(f'слово {word} отсутствует в файле')

        return find_pos

    def count(self, word):
        word_count = {}
        all_words = self.get_all_words()
        word = word.lower()
        for file_name, words in all_words.items():
            word_count[file_name] = words.count(word)

        return word_count


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего