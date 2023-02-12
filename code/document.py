from natasha_wrap import NatashaWrap
from ontology import Ontology
from sentence import Sentence
from term import Term

class Document(object):
    def __init__(self, filepath:str) -> None:
        self.filepath = filepath
        self.filename = filepath.split('/')[-1]
        self.natasha = NatashaWrap()
        self.sentences = []
        
        with open(filepath, encoding='utf-8') as fin:
            self.text = fin.read().replace('\n', ' ')

    
    def __str__(self) -> str:
        return self.filename

    def get_key_term(self, ontology: Ontology) -> dict[Term, Sentence]:
        if hasattr(self, 'key_terms'):
            return self.key_terms
        key_terms = dict()
        for sentence in self.natasha.get_sentences(self.text):
            self.sentences.append(sentence)
            for term in self.natasha.get_terms(ontology):
                if sentence.has_term(term):
                    if term in key_terms:
                        key_terms[term].append(sentence)
                    else:
                        key_terms[term] = [sentence]
        self.key_terms = key_terms
        return key_terms


    def key_term_ids(self) -> list[str]:
        return [term.id for term in self.key_terms]



if __name__ == '__main__':
    onto = Ontology('./documents/IZ_Kolesnikov_A_S__PMI-2-22.ont')
    doc = Document('./documents/Dokument_1.txt')
    # key_terms = doc.get_key_term(onto)
    # for key in key_terms:
    #     print(key)
    #     [print(sentence) for sentence in doc.key_terms[key]]



    # def __normalize_text1(self, text:str) -> list[list[str]]:
    #     norm_lst = MyStemWrap.normalize_text(text)
    #     result = list()
    #     for word in norm_lst:
    #         lex_lst = []
    #         if not word['analysis']:
    #             lex_lst.append(word['text'])
    #         else:
    #             for lex in word['analysis']:
    #                 lex_lst.append(lex['lex'])
    #         result.append(lex_lst)
    #     return result

    # def get_key_term1(self, ontology: Ontology):
    #     key_terms = dict()
    #     for sentence in self.get_sentences():
    #         for term in self.get_terms(ontology):
    #             if sentence.has_term(term):
    #                 if term in key_terms:
    #                     key_terms[term].append(sentence)
    #                 else:
    #                     key_terms[term] = [sentence]
    #     return key_terms