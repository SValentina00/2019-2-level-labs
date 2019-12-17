import math



REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    corpus = []
    if not isinstance(texts, list):
        return []
    for text in texts:
        if isinstance(text, str):
            text = text.lower()
            text = text.replace('\n', ' ')
            text = text.replace('<br />', ' ')
            text = text.replace('  ', ' ')
            clear_text = ''
            for el in text:
                if el.isalpha() or el == ' ':
                    clear_text += el
            clear_text = clear_text.split()
            corpus.append(clear_text)
    return corpus

class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = []

    def calculate_tf(self):
        if not isinstance(self.corpus, list):
            return []
        for doc in self.corpus:
            if isinstance(doc, list):
                dictionary = {}
                word_count = len(doc)
                for word in doc:
                    if not isinstance(word, str):
                        word_count -= 1
                for word in doc:
                    if isinstance(word, str):
                        if word not in dictionary:
                            dictionary[word] = doc.count(word)/word_count
                self.tf_values += [dictionary]
        return self.tf_values

    def calculate_idf(self):
        if self.corpus:
            for doc in self.corpus:
                if not doc:
                    continue
                clean_corpus = []
                for word in doc:
                    if isinstance(word, str) and word not in clean_corpus:
                        clean_corpus += [word]
                count_w = {}
                for word in clean_corpus:
                    count_word = 0
                    for text in self.corpus:
                        if not text or word in text:
                            count_word += 1
                    count_w[word] = count_word
                    if count_w.get(word) != 0:
                        docs_len = len(self.corpus)
                        self.idf_values[word] = math.log(docs_len/count_w.get(word))
            return self.idf_values

    def calculate(self):
        if not self.tf_values or not self.idf_values:
            return []
        for doc in self.tf_values:
            dictionary = {}
            for word in doc:
                dictionary[word] = doc[word] * self.idf_values[word]
            self.tf_idf_values.append(dictionary)

    def report_on(self, word, document_index):
        if document_index >= len(self.corpus) or not self.tf_idf_values:
            return ()
        tf_idf = [self.tf_idf_values[document_index][word]]
        sorting = list(self.tf_idf_values[document_index].items())
        sorting.sort(key=lambda word: -word[1])
        ind = -1
        for el in sorting:
            if el[0] == word:
                ind = sorting.index(el)
                break
        if ind != -1:
            tf_idf.append(ind)
        return tuple(tf_idf)


if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    test_texts = clean_tokenize_corpus(REFERENCE_TEXTS)
    tf_idf = TfIdfCalculator(test_texts)
    tf_idf.calculate_tf()
    tf_idf.calculate_idf()
    tf_idf.calculate()
    print(tf_idf.report_on('good', 0))
    print(tf_idf.report_on('and', 1))
