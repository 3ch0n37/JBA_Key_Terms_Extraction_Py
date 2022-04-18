import nltk
from lxml import etree
from collections import Counter


def main():
    root = etree.parse('news.xml').getroot()
    corpus = root[0]
    stories = {}
    for news in corpus:
        head = None
        text = None
        for value in news:
            name = value.get('name')
            if name == 'head':
                head = value.text
            elif name == 'text':
                text = value.text
        tokens = nltk.tokenize.word_tokenize(text.lower())
        tokens = sorted(tokens, reverse=True)
        stories[head] = Counter(tokens).most_common(5)
    for head in stories:
        print(head + ':')
        for common in stories[head]:
            print(common[0], end=' ')
        print('\n')


if __name__ == '__main__':
    main()
