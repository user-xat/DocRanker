class Term(object):
    def __init__(self, id, term:str, normalized_list:list[str]) -> None:
        self.id = id
        self.name = term
        self.normalized_list = normalized_list
        self.normalized = ' '.join(normalized_list)

    def __str__(self) -> str:
        return self.name
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, __o: object) -> bool:
        if __o is None:
            return False
        if self.__class__ != __o.__class__:
            return False
        return self.name == __o.name