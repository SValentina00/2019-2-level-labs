"""
Labour work #1.1
Count frequencies dictionary by the given arbitrary text
"""
def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    prohibited_marks = ['-','.',',','!','?','"',"'", ':',';']
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
    frequencies = {}
    for key in res:
        if key in frequencies:
            value = frequencies[key]
            frequencies[key] = value+1
        else:
            frequencies[key]=1
    return frequencies
    pass


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    for key in list(frequencies.keys()):
        if key in stop_words:
            del frequencies[key]
    return frequencies
    pass

def get_top_n(frequencies: dict, top_n: int) -> tuple:
    """
    Takes first N popular words
    """
    list_dict = list(frequencies.items())
    list_dict.sort(key=lambda i: (i[1],i[0]), reverse=True)
    ind = 0
    done = list()
    for i in list_dict:
        if ind < top_n:
            done.append(list_dict[ind])
            ind += 1
        else:
            break
    print (done)
    pass


start = open ('text.txt', 'r')
text = start.read().lower()

dict = calculate_frequences(text)
stop_words = stop_words = ('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 
'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 
'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 
'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 
'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 
'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 
'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 
'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 
'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 
'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 
'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 
'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 
'it', 'how', 'further', 'was', 'here', 'than')
print (filter_stop_words(dict, stop_words))

dict_clear = filter_stop_words(dict, stop_words)
top_n = 5
get_top_n(dict_clear, top_n)  
        
