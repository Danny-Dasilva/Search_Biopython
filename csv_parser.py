from app.search_class import Search

import re
class Csv_Parser:
    def __init__(self):
        self.val = 6
    def find_keyword(self, string):
        key_sentence = []
        for i in string:
            string = ', '.join(i[0])
            m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', string)
            for sentence in m:
                terms = ['MMP-13', 'inhibitor', 'orange', 'lemon']
                words = sentence.split()
                if any(word in words for word in terms):
                    key_sentence.append(sentence)
        return key_sentence
if __name__ == '__main__':
    bio = Search()
    csv = Csv_Parser()
    title, abstract = bio.query("MMP-13 inhibitors", '10')
    
    sentence = csv.find_keyword(abstract)
    for i in sentence:
        print(i)