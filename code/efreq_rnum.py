from ontology import Ontology
from document import Document
from sentence import Sentence
from term import Term
import numpy as np
import math
import re

class EfreqRnum(object):
    def __init__(self, ontology:Ontology, doc: Document, n:int, k:int, beta:int) -> None:
        self.ontology = ontology
        self.doc = doc
        self.c_terms = list(doc.key_terms.keys())
        self.e = self.__get_e_metrics(self.c_terms, k)
        self.b_i = self.__get_bi_metrics(self.e, beta)
        self.b_j = self.__get_bj_metrics(self.e, beta)
        self.mu_b = self.__get_mu_b_metrics(self.b_i)
        self.p = self.__get_p_metrics(self.c_terms, ontology, n)
        self.s = self.__get_semantic_proximity(self.c_terms, self.e, self.p, self.b_i, self.b_j, self.mu_b)
        self.s_norm = self.__normalize_semantic_proximity(self.s)
        self.r = self.__get_final_assessment(self.s_norm)

    def __count_concordance(self, f_term:Term, s_term:Term, k:int) -> int:
        e = 0
        for sentence in self.doc.key_terms[f_term]:
            num_sent = sentence.number

            if num_sent - k < 0:
                start_sent = 0
            else:
                start_sent = num_sent - k
            
            if num_sent + k + 1 > len(self.doc.sentences):
                end_sent = len(self.doc.sentences)
            else:
                end_sent = num_sent + k + 1

            for i in range(start_sent, end_sent):
                if s_term.normalized in self.doc.sentences[i].normalized:
                    coord = [m.start() for m in re.finditer(s_term.normalized, self.doc.sentences[i].normalized)]
                    e += len(coord)
        return e


    def __get_e_metrics(self, c_terms: list[Term], k: int) -> np.ndarray[np.float64, np.float64]:
        e = np.zeros((len(c_terms), len(c_terms)))
        for i in range(len(c_terms)):
            for j in range(i + 1, len(c_terms)):
                eij = self.__count_concordance(c_terms[i], c_terms[j], k)
                e[i, j] = eij
                e[j, i] = eij
        return e


    def __get_bi_metrics(self, e:np.ndarray[np.float64, np.float64], beta:int) -> np.ndarray[np.float64]:
        b_i = np.zeros((e.shape[0]), dtype=np.int64)
        for i in range(e.shape[0]):
            for j in range(e.shape[1]):
                if e[i, j] >= beta:
                    b_i[i] += 1
        return b_i


    def __get_bj_metrics(self, e:np.ndarray[np.float64, np.float64], beta:int) -> np.ndarray[np.float64]:
        b_j = np.zeros((e.shape[1]), dtype=np.int64)
        for j in range(e.shape[1]):
            for i in range(e.shape[0]):
                if e[i, j] >= beta:
                    b_j[j] += 1
        return b_j

    def __get_mu_b_metrics(self, b_i:np.ndarray[np.float64]) -> float:
        return b_i.sum()/b_i.size


    def __get_p_metrics(self, c_terms: list[Term], ontology:Ontology, n: int) -> np.ndarray[np.float64, np.float64]:
        p = np.zeros((len(c_terms), len(c_terms)), dtype=np.int64)
        for i in range(p.shape[0]):
            for j in range(i + 1, p.shape[1]):
                count_path = ontology.get_num_of_different_paths(c_terms[i].id, c_terms[j].id, n)
                p[i,j] = count_path
                p[j,i] = count_path
        return p


    def __get_semantic_proximity(self, c_terms: list[Term], e:np.ndarray[np.float64, np.float64], p:np.ndarray[np.int64, np.int64], b_i:np.ndarray[np.int64], b_j:np.ndarray[np.int64], mu_b: float):
        s = np.zeros((len(c_terms), len(c_terms)))
        for i in range(s.shape[0]):
            for j in range(s.shape[1]):
                numerator = math.sqrt(p[i,j]) * (2*mu_b*e[i,j])
                denominator = (b_i[i] + b_j[j])
                if denominator == 0:
                    s[i,j] = 0
                else:
                    s[i,j] = numerator / denominator
        return s


    def __normalize_semantic_proximity(self, s:np.ndarray[np.float64, np.float64]) -> np.ndarray[np.float64, np.float64]:
        # [print(s[i]) for i in range(s.shape[0])]
        if np.max(s) == 0:
            return s
        return (s - np.min(s))/np.max(s)

    def __get_final_assessment(self, s_norm: np.ndarray[np.float64, np.float64]):
        r = 0
        n = 0
        for i in range(s_norm.shape[0]):
            for j in range(i + 1, s_norm.shape[1]):
                r += s_norm[i,j]
                n += 1
        return r / n