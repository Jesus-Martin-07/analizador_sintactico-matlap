
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftELSEleftMASMENOSleftMULTIPLICACIONDIVISIONrightNUMEROleftIFleftIMPRIMIRDIVISION DOBLE_PUNTO ELSE END IF IGUAL IMPRIMIR MAS MENOR MENOS MULTIPLICACION NUMERO PARENTESIS_DERECHO PARENTESIS_IZQUIERDO STRING VARIABLEdeclaracion : IMPRIMIR PARENTESIS_IZQUIERDO STRING PARENTESIS_DERECHOdeclaracion : IF expresiondeclaracion : ELSE declaracion : VARIABLE IGUAL expresiondeclaracion : expresion\n     expresion  :  expresion MAS expresion\n                |  expresion MENOS expresion\n                |  expresion MULTIPLICACION expresion\n                |  expresion DIVISION expresion\n                |  expresion MENOR expresion\n                | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MAS expresion\n                | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MENOS expresion\n                | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MULTIPLICACION expresion\n                | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO DIVISION expresion\n\n    expresion : NUMEROexpresion : VARIABLEexpresion : END'
    
_lr_action_items = {'IMPRIMIR':([0,],[2,]),'IF':([0,],[4,]),'ELSE':([0,],[6,]),'VARIABLE':([0,3,4,14,15,16,17,18,19,29,30,31,32,],[7,12,12,12,12,12,12,12,12,12,12,12,12,]),'PARENTESIS_IZQUIERDO':([0,2,3,4,14,15,16,17,18,19,29,30,31,32,],[3,10,3,3,3,3,3,3,3,3,3,3,3,3,]),'NUMERO':([0,3,4,14,15,16,17,18,19,29,30,31,32,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'END':([0,3,4,14,15,16,17,18,19,29,30,31,32,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'$end':([1,5,6,7,8,9,12,13,22,23,24,25,26,27,28,33,34,35,36,],[0,-5,-3,-16,-15,-17,-16,-2,-6,-7,-8,-9,-10,-4,-1,-11,-12,-13,-14,]),'MAS':([5,7,8,9,11,12,13,21,22,23,24,25,26,27,33,34,35,36,],[14,-16,-15,-17,14,-16,14,29,-6,-7,-8,-9,14,14,-11,-12,-13,-14,]),'MENOS':([5,7,8,9,11,12,13,21,22,23,24,25,26,27,33,34,35,36,],[15,-16,-15,-17,15,-16,15,30,-6,-7,-8,-9,15,15,-11,-12,-13,-14,]),'MULTIPLICACION':([5,7,8,9,11,12,13,21,22,23,24,25,26,27,33,34,35,36,],[16,-16,-15,-17,16,-16,16,31,16,16,-8,-9,16,16,16,16,-13,-14,]),'DIVISION':([5,7,8,9,11,12,13,21,22,23,24,25,26,27,33,34,35,36,],[17,-16,-15,-17,17,-16,17,32,17,17,-8,-9,17,17,17,17,-13,-14,]),'MENOR':([5,7,8,9,11,12,13,22,23,24,25,26,27,33,34,35,36,],[18,-16,-15,-17,18,-16,18,-6,-7,-8,-9,18,18,-11,-12,-13,-14,]),'IGUAL':([7,],[19,]),'PARENTESIS_DERECHO':([8,9,11,12,20,22,23,24,25,26,33,34,35,36,],[-15,-17,21,-16,28,-6,-7,-8,-9,-10,-11,-12,-13,-14,]),'STRING':([10,],[20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,3,4,14,15,16,17,18,19,29,30,31,32,],[5,11,13,22,23,24,25,26,27,33,34,35,36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> IMPRIMIR PARENTESIS_IZQUIERDO STRING PARENTESIS_DERECHO','declaracion',4,'p_declaracion_PUTS','AnalizadorSintactico.py',16),
  ('declaracion -> IF expresion','declaracion',2,'p_declaracion_IF','AnalizadorSintactico.py',19),
  ('declaracion -> ELSE','declaracion',1,'p_declaracion_ELSE','AnalizadorSintactico.py',22),
  ('declaracion -> VARIABLE IGUAL expresion','declaracion',3,'p_declaracion_expr','AnalizadorSintactico.py',26),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr2','AnalizadorSintactico.py',29),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',33),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',34),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',35),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',36),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',37),
  ('expresion -> PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MAS expresion','expresion',5,'p_expresion_operaciones','AnalizadorSintactico.py',38),
  ('expresion -> PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MENOS expresion','expresion',5,'p_expresion_operaciones','AnalizadorSintactico.py',39),
  ('expresion -> PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MULTIPLICACION expresion','expresion',5,'p_expresion_operaciones','AnalizadorSintactico.py',40),
  ('expresion -> PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO DIVISION expresion','expresion',5,'p_expresion_operaciones','AnalizadorSintactico.py',41),
  ('expresion -> NUMERO','expresion',1,'p_expression_NUMERO','AnalizadorSintactico.py',55),
  ('expresion -> VARIABLE','expresion',1,'p_expression_VARIABLE','AnalizadorSintactico.py',59),
  ('expresion -> END','expresion',1,'p_expresion_end','AnalizadorSintactico.py',62),
]
