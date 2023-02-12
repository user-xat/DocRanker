import natasha as nat
from sentence import Sentence
from term import Term
from ontology import Ontology


class NatashaWrap(object):
    def __init__(self) -> None:
        self.segmenter = nat.Segmenter()
        self.emb = nat.NewsEmbedding()
        self.morph_tagger = nat.NewsMorphTagger(self.emb)
        self.morph_vocab = nat.MorphVocab()
        self.buff_term = dict()

    def normalize_text(self, text:str) -> nat.Doc:
        doc = self.__segmentate_text(text)
        doc = self.__get_lemmas(doc)
        return doc

    def __segmentate_text(self, text: str) -> nat.Doc:
        doc = nat.Doc(text)
        doc.segment(self.segmenter)
        # print([ob.text for ob in doc.sents])
        return doc

    def __get_lemmas(self, doc: nat.Doc) -> nat.Doc:
        doc.tag_morph(self.morph_tagger)
        for token in doc.tokens:
            token.lemmatize(self.morph_vocab)
        return doc

    def __to_list(self, doc: nat.Doc) -> list[str]:
        return [(sent.text, ' '.join([token.lemma for token in sent.tokens])) for sent in doc.sents]

    def get_sentences(self, text:str) -> list[Sentence]:
        doc = self.normalize_text(text)
        buff_words = dict()
        for token in doc.tokens:
            if token.text not in buff_words:
                buff_words[token.text] = token.lemma
        for i, sent in enumerate(doc.sents):
            yield Sentence(i, sent.text, [token.text for token in sent.tokens], [token.lemma for token in sent.tokens], buff_words)

    
    def get_terms(self, ontology: Ontology) -> list[Term]:
        for id, name in ontology.get_nodes_names():
            if id not in self.buff_term:
                doc = self.normalize_text(name)
                self.buff_term[id] = Term(id, name, [token.lemma for token in doc.tokens])
            yield self.buff_term[id]



if __name__ == '__main__':
    # text = MyStemWrap.normalize_text('Инструментальное средство')
    text = NatashaWrap().normalize_text("""В этой статье C++ исследуется возможность построения модели предметной области. Семантический, синтаксический и морфологический анализы текстов стали основой гибридного метода. Он должен выявить достоинства и недостатки уже существующих методов. Гибридный способ основан на извлечении отношений из текста. Отношение представляет собой глагол или отглагольную часть речи. В статье рассматривается извлечение отношений типа «быть-являться». Показан C++ способ извлечения отношений и объектов отношений из токенов. Описан общий ход всего алгоритма гибридной модели построения предметной области.""")
    # text = NatashaWrap().normalize_text('Инструментальное средство')
    
    print(text)

# import subprocess
# import json

# class MyStemWrap(object):
#     @staticmethod
#     def __run_mystem(text: str) -> list[dict]:
#         pass
#         # complete_proc = subprocess.run(['./mystem', '--format', 'json'], input=text, text=True, capture_output=True)
#         # print(complete_proc.stdout)
#         # return json.loads(complete_proc.stdout)
    
#     @staticmethod
#     def normalize_text(text:str) -> list[str]:
#         norm_lst = MyStemWrap.__run_mystem(text)
#         result = list()
#         for word in norm_lst:
#             if not word['analysis']:
#                 result.append(word['text'])
#             else:
#                 result.append(word['analysis'][0]['lex'])
#         return ' '.join(result)