from app.search_class import Search

import re
class Csv_Parser:
    def __init__(self):
        self.val = 6
    def string_split(self, string):
        for i in string:
            string = ', '.join(i[0])
            m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', string)
            for sentence in m:
                term = "MMP-13"
                words = sentence.split()
                if term in words:
                    print(sentence)
if __name__ == '__main__':
    bio = Search()
    csv = Csv_Parser()
    title, abstract = bio.query("MMP-13 inhibitors", '4')
    csv.string_split(abstract)
