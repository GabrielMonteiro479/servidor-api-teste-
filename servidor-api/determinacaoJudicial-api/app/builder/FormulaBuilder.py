from app.models.Formula import Formula


class FormulaBuilder(object):

    @staticmethod
    def build(dados):
        formula = Formula()

        formula.codigo = dados['codigo']
        formula.codigo_liminar = dados['codigo_liminar']

        return formula