from term import Term
import re

class Sentence(object):
    def __init__(self, number:int, text:str, words:list[str], normalized_list:list[str], buff_words:dict[str,str]) -> None:
        self.number = number
        self.text = text
        self.words = words
        self.normalized_list = normalized_list
        self.normalized = ' '.join(normalized_list)
        self.buff_words = buff_words
    
    def __str__(self) -> str:
        return self.text

    def has_term(self, term: Term) -> bool:
        return term.normalized in self.normalized

    def find_term(self, term: Term):
        regex = "^[a-zA-Z]+$"
        pattern = re.compile(regex)
        template = ''
        original_str = ''
        for word in self.words:
            if self.buff_words[word] in term.normalized_list or \
                (pattern.search(term.normalized) is not None and term.normalized in self.buff_words[word]):
                template += self.buff_words[word] + ' '
                original_str += word + ' '
            elif template:
                if template.strip() == term.normalized:
                    yield original_str.strip()
                elif term.normalized in original_str.lower():
                    coord = [(m.start(), m.end()) for m in re.finditer(term.normalized, original_str.lower())][0]
                    yield original_str[coord[0]:coord[1]]
                original_str = ''
                template = ''
