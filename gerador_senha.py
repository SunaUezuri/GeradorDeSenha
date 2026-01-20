import random

def gerar_senha() -> str:
    '''
        Gera uma senha aleatória com pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial.

        Retorna:
            str: A senha gerada.
    '''

    maiusculas: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas: str = 'abcdefghijklmnopqrstuvwxyz'
    numeros: str = '0123456789'
    especiais: str = '!@#$%^&*'

    senha: list[str] = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiais)
    ] 

    todos_caracteres: str = maiusculas + minusculas + numeros + especiais
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)