# you need to install Biopython:
# pip install biopython

# Full discussion:
# https://marcobonzanini.wordpress.com/2015/01/12/searching-pubmed-with-python/

from Bio import Entrez

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
        for i, paper in enumerate(papers['PubmedArticle']): 
            print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['Abstract']['AbstractText']))

if __name__ == '__main__':
    bio = Search()

    bio.query("MMP-13 inhibitors", '5')
    
