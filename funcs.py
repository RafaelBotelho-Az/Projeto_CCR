from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTableWidgetItem

def converter_unidade(quantidade, unidade_origem, unidade_destino):
    conversao = {
        'kg': 1000,
        'g': 1,
        'l': 1000,
        'ml': 1,
        'und': 1
    }

    conversoes_permitidas = {
        ('kg', 'g'),
        ('g', 'kg'),
        ('l', 'ml'),
        ('ml', 'l'),
        ('kg', 'kg'),
        ('g', 'g'),
        ('l', 'l'),
        ('ml', 'ml'),
        ('und', 'und')
    }
   
    if (unidade_origem, unidade_destino) in conversoes_permitidas:
        return quantidade * (conversao[unidade_origem] / conversao[unidade_destino])
    else:
        raise ValueError("Unidade de medida não suportada para conversão.")
