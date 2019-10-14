"""
Labour work #1.1
Count frequencies dictionary by the given arbitrary text
"""

def calculate_frequences(text):
    prohibited_marks = ['.', ',', '!', '?', ';', ':', '"', "'", '—', '-',
                        '$', '%', '*', '@', '^', '&', '~', '*', '+', '=']
    if isinstance(text, str):
        text = text.lower()
        for word in text:
            if word.isdigit() or word in prohibited_marks:
                text = text.replace(word, ' ')
        splitted = (text.replace('\n', ' ')).split()
        dictionary = {}
        for key in splitted:
            if key in dictionary:
                value = dictionary[key]
                dictionary[key] = value + 1
            else:
                dictionary[key] = 1
        return dictionary
    return {}
def filter_stop_words(dictionary, stop_words):
    if dictionary and stop_words is not None:
        dict_clear = dictionary.copy()
        for key in dictionary:
            if not isinstance(key, str):
                del dict_clear[key]
        for key in list(dict_clear.keys()):
            if key in stop_words:
                del dict_clear[key]
        return dict_clear
    return {}

def get_top_n(dict_clear, top_n):
    list_dict = list(dict_clear.items())
    list_dict.sort(key=lambda x: -x[1])
    ind = 0
    res = [х[0] for х in list_dict]
    top = list()
    if top_n > 0:
        
        for i in res:
            if ind < top_n:
                top.append(res[ind])
                ind += 1
        done = tuple(top)
        return done
