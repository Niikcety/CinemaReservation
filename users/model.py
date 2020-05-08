class UserModel():

    def __init__(self, id=0, nm=None, tp=None):
        self.id = id
        self.nm = nm
        self.tp = tp

    @classmethod
    def from_db_record(cls, record):

        id = record[0]
        nm = record[1]
        tp = record[2]

        return cls(id, nm, tp)

    def make_reservation(self):
        print('resres')
