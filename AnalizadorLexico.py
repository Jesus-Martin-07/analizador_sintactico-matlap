import ply.lex as lex
import sys

# Alejandro Ortega, Nicole Rios, Jhon Edison Parra

# https://www.dabeaz.com/ply/ply.html#ply_nn6
from ply.lex import Lexer
reserved = {
    'disp': 'IMPRIMIR',
    'if': 'IF',
    'else': 'ELSE',
    'end': 'END',

}
tokens = list(reserved.values()) + [
    # Symbols

    'MAS',
    'MENOS',
    'MULTIPLICACION',
    'DIVISION',
    'IGUAL',
    'PARENTESIS_IZQUIERDO',
    'PARENTESIS_DERECHO',
    # Otros
    'VARIABLE',
    'NUMERO',
    'DOBLE_PUNTO',
    'STRING',
    'MENOR',
]

# Regular expressions rules for simple tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUAL = r'='
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'
t_DOBLE_PUNTO = r':'
t_MENOR = r'<'

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    ##t.value = float(t.value)
    return t


def t_VARIABLE(t):
    r'[a-z]([\w])*'
    if t.value in reserved:
        t.type = reserved[t.value]  # Check for reserved words
        return t
    else:
        return t
def t_STRING(t):
    r'"((?:[^"\\]|\\.)*)"'
    return t
# Check reserved words
# This approach greatly reduces the number of regular expression rules and is likely to make things a little faster.
def t_SALTO_LINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ESPACIO(t):
    r'\s+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Lexical error: " + str(t.value))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    i = 1  # Representa la línea
    while True:
        tok = lexer.token()
        if not tok:
            break
        print("\t" + str(i) + " - " + "Linea: " + str(tok.lineno) + "\t" + str(tok.type) + "\t-->  " + str(tok.value))
        i += 1
    # print(tok)


lexer: Lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'index.m'
    f = open(fin, 'r')
    data = f.read()
    # print (data)
    # lexer.input(data)
    test(data, lexer)
# input()