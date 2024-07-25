from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

def apply_styles(table_widget):
    for row in range(table_widget.rowCount()):
        item = table_widget.item(row, 3)
        if item is None:
            item = QTableWidgetItem()
            table_widget.setItem(row, 3, item)
        # item.setBackground(QColor("#ebeae8"))
        item.setFlags(Qt.ItemIsSelectable)

    table_widget.setStyleSheet("""
        QTableWidget::item:selected {
            background-color: #a266e9;  /* Cor de fundo quando o item está selecionado */
        }
        QTableWidget {
            border: 1px solid #CCCCCC;
            background-color: #575757;
}
    """)

def set_label_style(label):
    label.setStyleSheet("""
        color: red;
        font-size: 13;
        font-weight: bold;
    """)