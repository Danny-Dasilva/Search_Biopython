from app.search_class import Search

import re
class Csv_Parser:
    def __init__(self):
        self.val = 6
    def string_split(self, string):
        for i in string:
            m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', i)
            for i in m:
                print(i)
if __name__ == '__main__':
    bio = Search()
    csv = Csv_Parser()
    title, abstract = bio.query("MMP-13 inhibitors", '5')
    csv.string_split(abstract)