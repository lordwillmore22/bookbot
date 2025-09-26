def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_chars(book_text):
    data = {}
    for w in book_text:
        if w.lower() in data:
            data[w.lower()] += 1
        else:
            data[w.lower()] = 1
    return data

def sort_dict(dict):
    def sort_on(items):
        return items["num"]
    arr = []
    for key in dict:
        arr.append({"char":key,"num":dict[key]})
    arr.sort(reverse=True,key=sort_on)
    return arr
    