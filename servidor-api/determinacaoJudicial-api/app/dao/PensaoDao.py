from app import db


class PensaoDao(object):

    @staticmethod
    def incluir(pensao):
        db.session.add(pensao)
        db.session.commit()

        return pensao
