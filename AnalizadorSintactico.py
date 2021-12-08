from ntpath import join
import ply.yacc as yacc
from AnalizadorLexico import  tokens
import sys
import ply.lex as lex
resultado_gramatica = []
precedence = (
    ('left', 'ELSE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('right', 'NUMERO'),
    ('left','IF'),
    ('left','IMPRIMIR')
)

def p_declaracion_PUTS(t):
    'declaracion : IMPRIMIR PARENTESIS_IZQUIERDO STRING PARENTESIS_DERECHO'
    t[0] = t[1]
def p_declaracion_IF(t):
    'declaracion : IF expresion'
    t[0] = t[1]
def p_declaracion_ELSE(t):
    'declaracion : ELSE '
    t[0] = t[1]

def p_declaracion_expr(t):
    'declaracion : VARIABLE IGUAL expresion'
    t[0] = t[1]
def p_declaracion_expr2(t):
    'declaracion : expresion'
    t[0] = t[1]
def p_expresion_operaciones(t):
    '''
     expresion  :  expresion MAS expresion
                |  expresion MENOS expresion
                |  expresion MULTIPLICACION expresion
                |  expresion DIVISION expresion
                |  expresion MENOR expresion
                | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MAS expresion
                | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MENOS expresion
                | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MULTIPLICACION expresion
                | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO DIVISION expresion

    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    if t[2] == '-':
        t[0] = t[1] + t[3]
    if t[2] == '*':
        t[0] = t[1] + t[3]
    if t[2] == '/':
        t[0] = t[1] + t[3]
    if t[2] == '<':
        t[0] = t[1] < t[3]
def p_expression_NUMERO(t):
    'expresion : NUMERO'
    t[0] = t[1]

def p_expression_VARIABLE(t):
    'expresion : VARIABLE'
    t[0] = t[1]
def p_expresion_end(t):
    'expresion : END'
    t[0] = t[1]
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))#Define donde se encuentra el error sintactico
    else:
        resultado = "Error sintactico {}".format(t) #Muestra un error de sintaxis
    resultado_gramatica.append(resultado)

parser = yacc.yacc()
# Proceso de analisis del codigo
def prueba_sintactica(data):
    global resultado_gramatica

    for item in data.splitlines():  # Saltos que da el puntero de analisis
        if item:
            gram = parser.parse(item)  # Analiza cada item con respecto a la libreria yacc
            if gram:
                resultado_gramatica
        else:
            print()
    return resultado_gramatica


try:
    file_name = 'index.m'  # Lectura del archivo
    archivo = open(file_name, "r")
except:
    print("el archivo no se encontro")  # En caso de encontrar el archivo
    quit()

text = ""
for linea in archivo:  # Lee el archivo linea a linea
    text += linea

prueba_sintactica(text)
print("")
print('BUSQUEDA DE ERRORES...')
print("")
if not prueba_sintactica:
    print()
else:
    print('\n'.join(list(map(''.join, resultado_gramatica))))  # Emite una lista con los resultados del analisis