def calculate_frequences(text: str):
    prohibited_marks = ['-', '.', ',', '!', '?', '"', "'", ':', ';']
    splitted = (text.replace('\n', ' ')).split(' ')
    res = []
    for word in splitted:
        if not word.isdigit() and word not in prohibited_marks:
            clear_word = ''
            for el in word:
                if el not in prohibited_marks:
                    clear_word += el
            if clear_word is not '':
                res.append(clear_word)
    d = {}
    for key in res:
        if key in d:
            value = d[key]
            d[key] = value + 1
        else:
            d[key] = 1
    return d

def filter_stop_words(d, stop_words):
    for key in list(d.keys()):
        if key in stop_words:
            del d[key]
    return d

def get_top_n(dict_clear, top_n):
    list_dict = list(dict.items())
    list_dict.sort(key= lambda x: -x[1])
    ind = 0
    done = list()
    for i in list_dict:
        if ind <= top_n:
            done.append(list_dict[ind])
            ind += 1
        else:
            break       
    print (done)
start = open('text.txt', 'r')
text = start.read().lower()

dict = calculate_frequences(text)
stop_words = ('a', 'the', 'for', 'and', 'is', 'to',)
print(filter_stop_words(dict, stop_words))

dict_clear = filter_stop_words(dict, stop_words)
top_n = 5
get_top_n(dict_clear, top_n)
