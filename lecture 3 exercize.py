corpora=["A","A","A","B","A","C","B","A","B","B","B","C","C","A","C","B","C","C"]
corp = "AAABACBABBBCCACBCC"

def unigram (word, text):
    for word in text:
        return text.count(word)/len(text)


unigram("A", corp)


def bigram (word,previous_word,text):
    for word in text:
        return (text.count(word-1 )= previous_word)/len(text)

bigram("A",corpora)

