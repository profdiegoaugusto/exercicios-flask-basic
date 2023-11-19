class Paciente:
    """Representa um paciente da clínica"""

    MASCULINO = "M"
    FEMININO = "F"

    def __init__(self, nome: str = "", sexo: str = "", altura: float = 0.0, peso: float = 0.0):
        self.__nome = nome
        self.__sexo = sexo.upper()
        self.__altura = altura
        self.__peso = peso

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        self.__altura = value

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, value):
        self.__peso = value

    def obter_imc(self) -> float:
        """
        Calcula o Índice de Massa Corporal (IMC)
        :return:
        """
        return self.__peso / (self.__altura * self.__altura)

    @staticmethod
    def obter_classificacao_imc(imc):
        """
        Obtém a classificação do paciente conforme o IMC
        :param imc: Índice de Massa Corporal (IMC)
        :return: uma string com a situação atual do paciente
        """
        if imc < 17.00:
            return "Muito abaixo do peso."
        elif imc < 18.50:
            return "Abaixo do peso."
        elif imc < 25.00:
            return "Peso normal."
        elif imc < 30.00:
            return "Acima do peso"
        elif imc < 35.00:
            return "Obesidade I"
        elif imc < 40.00:
            return "Obesidade II (Severa)"
        else:
            return "Obesidade III (Mórbida)"

    def obter_peso_ideal(self) -> float:
        """
        Obtém o peso ideal do paciente
        :return: o peso ideal do paciente em kg
        """

        if self.__sexo == self.MASCULINO:
            return (72.7 * self.__altura) - 58
        else:
            return (62.1 * self.__altura) - 44.7


