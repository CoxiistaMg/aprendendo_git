class ReNumAnouterPlace:
    '''meu sistema vai de 2 a 36 por causa disso,
    após você aumentar essa lista pode converter mais casas, 
    mas lembresse de editar o ConvertNumberPlace.__init__, porque se não vai 
    da error de qualquer jeito'''

    __dict_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I"
    "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    limit_number = []

    def __init__(self, place, number):
        self.place = place
        self.number = number
        self.limit_number = []

        for number in range(self.place):
            self.limit_number.append(f'{number}')

    def self_to_decimal(self):
        result_number = 0
        n = len(self.number) - 1

        for value in self.number:
            result_number += self.__dict_number.index(value) * self.place ** n
            n -= 1

        return ReNumAnouterPlace(10, result_number)

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other):
        x1 = f"{self.self_to_decimal()}"
        x2 = f"{other.self_to_decimal()}"
        return int(x1) + int(x2)

    def __sub__(self, other):
        x1 = f"{self.self_to_decimal()}"
        x2 = f"{other.self_to_decimal()}"
        return int(x1) - int(x2)

    def __mul__(self, other):
        x1 = f"{self.self_to_decimal()}"
        x2 = f"{other.self_to_decimal()}"
        return int(x1) * int(x2)

    def __truediv__(self, other):
        x1 = f"{self.self_to_decimal()}"
        x2 = f"{other.self_to_decimal()}"
        return int(int(x1) / int(x2))

    def __pow__(self, other):
        x1 = f"{self.self_to_decimal()}"
        x2 = f"{other.self_to_decimal()}"
        return int(x1) * int(x2)

    def __mod__(self, other):
        x1 = f"{self.self_to_decimal()}"
        x2 = f"{other.self_to_decimal()}"
        return int(int(x1) % int(x2))


class ConvertNumberPlace(ReNumAnouterPlace):
    number = None
    __num_list = [1]

    def __init__(self, place_value=2):

        ''' Essa classe serve para você criar numerais com bases decimais personalizaveis com valores de 2 a 36.
            Você apenas deve instanciar o valor da casa decimal que deseja exemplo:

            1-octal = ConvertNumberPlace(8)

            essa instancia gerou a base Octal, você agora de instanciar de novo mas agora passando o valor numerico,
            tem três formas de fazer essa instancia com numero inteiro, com numero em string e com outra base

            1- valor = octal(72) # neste caso ele vai entender que esse numero é decimal e vai converter para octal
            o resultado vai ser "110" em octal

            2-valor = octal("72") no  caso do parametro ser uma string  ele vai entender como uma literal
            o resultado vai ser "72" em octal

            4- bin = ConvertNumberPlace(2)
            3-valor = octal(bin("1000")) neste caso ele vai transformar o binario em octal
            o resultado vai ser "10" em octal, mas lembresse que caso você passe

            3- valor = octal(bin(10)) ele vai transformar antes esse 10 em binario pra depois transformar em octal

            obs: meu sistema de while funciona com a elevação de casas decimais tipo xⁿ ,
            no caso do 1 ia fazer não funcionar, mas é claro poderia resolve isso bem fácil, 
            era só fazer esses numeros que foram chegados se somarem tipo 1 elevado a 1 é igual a um
            então no proximo loop eu teria 2, e no proximo 3
            1 + 1 + 1 = 3, ou ate mesmo usar um if mas mesmo assim o numerais que iriam aparecer 
            seriam apenas 0, poderia trocar por outros mas quer saber, tá funcionando muito bem desse
            jeito é melhor deixar como tá 
        '''

        try:
            assert place_value < 36 and place_value > 1 and place_value%1 == 0
        except AssertionError:
            raise ValueError(f"Deve ser um numero maior que 1, menor ou igual a 36 e um numero inteiro\n\nConvertNumberPlace({place_value})")


        self.place = place_value
        super().__init__(place=place_value, number=None)
    
    def __generic_to_self(self, number):
        valor = number.self_to_decimal().number
        return self.__decimal_to_self(valor)
    

    def __decimal_to_self(self, number):
        n = self.place
        current_number = number

        self.__num_list = [1]

        # sistema de loop pra converter 
        while n <= number:
            self.__num_list.append(n)
            n *= self.place

        self.__num_list = self.__num_list[::-1]
        for pos, value in enumerate(self.__num_list):
            check = int(current_number / value //1)
            self.__num_list[pos] = self.limit_number[check]


            if check != 0:
                current_number -= value * check

        return ReNumAnouterPlace(self.place, "".join(self.__num_list))


    def __call__(self, number):
        if type(number) == int or type(number) == float:
            return self.__decimal_to_self(number)
    

        if type(number) == str:
            error_char = []
            numb = str(number)
            for num in numb:
                if num not in self.limit_number:
                    if num not in error_char:
                        error_char.append(num)

            if error_char:
                string_text = "\n=================================================================="

                for value in error_char:
                    string_text += f"\n-> {value}\n"
                    string_text += "=================================================================="

                string_text += f"\nCaracteres inválidos para essa operação\nOs caractes válidos são {self.limit_number}"
                raise ValueError(string_text)

            return ReNumAnouterPlace(self.place, f"{number}")

        return self.__generic_to_self(number)

bio = ConvertNumberPlace(2)
octa = ConvertNumberPlace(8)

print(bio(20))
print(bio(octa('20')))
print(bio(20) + octa("70"))
