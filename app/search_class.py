# you need to install Biopython:
# pip install biopython

# Full discussion:
# https://marcobonzanini.wordpress.com/2015/01/12/searching-pubmed-with-python/

from Bio import Entrez

from lxml import objectify, etree
import json
import itertools
class Search:
    def __init__(self):
        self.count = '20'
    def search(self, query, count):
        Entrez.email = 'your.email@example.com'
        handle = Entrez.esearch(db='pubmed', 
                                sort='relevance', 
                                retmax=count,
                                retmode='xml', 
                                term=query)
        results = Entrez.read(handle)
        return results

    def fetch_details(self, id_list):
        ids = ','.join(id_list)
        Entrez.email = 'your.email@example.com'
        handle = Entrez.efetch(db='pubmed',
                            retmode='xml',
                            id=ids)
        results = Entrez.read(handle)
        return results
    def query(self, query, count):
        bio = Search()
        results = bio.search(query, count)
        id_list = results['IdList']
        papers = bio.fetch_details(id_list)
        title = []
        abstract = []
        for i, paper in enumerate(papers['PubmedArticle']): 
            T = "%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle'])
            A = "%d) %s" % (i+1, paper['MedlineCitation']['Article']['Abstract']['AbstractText'])
            b = A.split('StringElement(')
            C = []
            for i in b:
                 A = i.split(', attributes=')
                 
                 
                 A[:] = [x for x in A if not x.startswith('{')]
                 C.append(A)
            
            if len(C) > 1:
                joinedlst = []
                for g in C:
                    d = [x.strip("'") for x in g]
                    joinedlst = joinedlst + d
                C = joinedlst
                #print(C)
                C = ' '.join(C)
                print(C)
                #print(C)
                C = [[C]]
                

            title.append(T)
            #print(C)
            abstract.append(C)
        return title, abstract
            


    
# if __name__ == '__main__':
#     bio = Search()
#     title, abstract = bio.query("MMP-13 inhibitors", '4')