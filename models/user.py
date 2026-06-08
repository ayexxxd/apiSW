class user:
    idUser: int
    nombreUser: str
    amountTokens: int
    #start
    def __init__(self, idUser, nombreUser, amountTokens):
        self.idUser = idUser
        self.nombreUser = nombreUser
        self.amountTokens = amountTokens
    def to_dict(self):
        return {
            "idUser" : self.idUser,
            "nombreUser" : self.nombreUser,
            "amountTokens" : self.amountTokens
        }
