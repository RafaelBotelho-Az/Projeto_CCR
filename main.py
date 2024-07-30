from PySide6 import QtCore
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog, QMessageBox, QComboBox
from ui_main import Ui_MainWindow
from funcs import converter_unidade
from styles_module import apply_styles, set_label_style
import sys, json, os

class NoScrollComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

    def wheelEvent(self, event):
        # Ignorar eventos de rolagem
        event.ignore()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Az - Sistema para e calcular o custo de receitas')
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        self.setFixedSize(1300, 900)
        self.lista_produtos = []
        self.load_products()
        self.lista_nomes = [item['nome'] for item in self.lista_produtos]
        apply_styles(self.tableWidget_criar)
        set_label_style(self.label_vt)
        set_label_style(self.label_vtl)
        set_label_style(self.label_vu)

        self.tableWidget_receitas.setColumnWidth(0, 725)
        self.tableWidget_criar.setColumnWidth(0, 604)
        self.tableWidget_criar.setColumnWidth(2, 120)
        self.tableWidget_criar.setColumnWidth(3, 130)
        self.tableWidget_produtos.setColumnWidth(0, 500)
        self.tableWidget_produtos.setColumnWidth(2, 115)
        self.tableWidget_produtos.setColumnWidth(3, 145)
################  PAGINAS  #############################################################################
        self.btn_menu_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_menu_receitas.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_receitas))
        self.btn_menu_criar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_criar))
        self.btn_menu_cadastrar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastrar))
################  CONNECTIONS  #########################################################################
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        self.tableWidget_produtos.cellClicked.connect(self.on_cell_clicked)
        self.btn_alterar.clicked.connect(self.edit_selected_row)
        self.btn_excluir.clicked.connect(self.delete_selected_row)
        self.selected_row = -1 # Variável para armazenar a linha selecionada
        self.coloca_na_tabela(self.lista_produtos)
        self.btn_toggle_home.clicked.connect(self.leftMenu)
        self.tableWidget_criar.cellClicked.connect(self.table_comboboxes)
        self.init_comboboxes()
        self.btn_calcular.clicked.connect(self.valor_comboboxes)
        self.btn_calcular.clicked.connect(lambda: self.calcular(coluna=3))
        self.btn_salvar_receita.clicked.connect(self.salvar_receita)
        self.btn_menu_receitas.clicked.connect(self.listar_arquivos_json)
        self.btn_receitas_abrir.clicked.connect(self.reset_page)
        self.btn_receitas_abrir.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_criar))
        self.btn_limpar.clicked.connect(self.reset_page)
        self.btn_receitas_excluir.clicked.connect(self.del_receita)
################  FUNÇÃO HOME #########################################################################
    def leftMenu(self):
        width = self.left_container.width()

        if width == 0:
            newWidth = 250
        else:
            newWidth = 0
        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
#######################################################################################################
    def cadastrar(self):
        unidades_permitidas = ['kg', 'g', 'l', 'ml', 'und']

        nome = self.lineEdit_produto.text().strip().lower()
        unidade = self.lineEdit_unidade.text().strip().lower()
        quantidade = self.lineEdit_quantidade.text().strip().lower()
        valor = self.lineEdit_valor.text().strip().lower()

        if not nome or not unidade or not quantidade or not valor:
            self.error_label.setText("Todos os campos são obrigatórios!")
            self.error_label.setStyleSheet("color: red;")
            return

        if unidade not in unidades_permitidas:
            self.error_label.setText("UNIDADE não permitida, use: 'kg', 'g', 'l', 'ml', 'und'")
            self.error_label.setStyleSheet("color: red;")
            return

        try:
            quantidade = int(quantidade)
        except ValueError:
            self.error_label.setText("QUANTIDADE deve ser um número inteiro!")
            self.error_label.setStyleSheet("color: red;")
            return

        try:
            valor = float(valor)
        except ValueError:
            self.error_label.setText("VALOR deve ser um número decimal, por exemplo: 10.50 ou 5.20")
            self.error_label.setStyleSheet("color: red;")
            return

        try:
            self.lista_produtos.append({
                'nome': nome,
                'unidade': unidade,
                'quantidade': quantidade,
                'valor': valor
            })
            self.lineEdit_produto.clear()
            self.lineEdit_unidade.clear()
            self.lineEdit_quantidade.clear()
            self.lineEdit_valor.clear()
            self.error_label.clear()

        except Exception as e:
            self.error_label.setText(f'Erro: {str(e)}')
            self.error_label.setStyleSheet("color: red;")

        self.error_label.setText("Cadastrado com Sucesso!")
        self.error_label.setStyleSheet("color: green;")
        self.coloca_na_tabela(self.lista_produtos)
        self.save_products(self.lista_produtos)
        self.load_products()
        self.update_comboboxes()
#######################################################################################################
    def save_products(self, products, filename='products.json'):
        try:
            with open(filename, 'w', encoding='utf8') as file:
                json.dump(products, file, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f'Erro ao salvar produtos: {str(e)}')

    def load_products(self, filename='products.json'):
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf8') as file:
                    self.lista_produtos = json.load(file)
            else:
                print(f'Arquivo "{filename}" não encontrado.')
                self.lista_produtos = []
        except Exception as e:
            print(f'Erro ao carregar produtos: {str(e)}')
            self.lista_produtos = []
            
        self.lista_nomes = [item['nome'] for item in self.lista_produtos]
#######################################################################################################
    def coloca_na_tabela(self, lista_produtos):
        self.tableWidget_produtos.setRowCount(len(lista_produtos))

        for row, produto in enumerate(lista_produtos):
            for column, (key, value) in enumerate(produto.items()):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_produtos.setItem(row, column, item)
################  FUNÇÕES PARA EDITAR E EXCLUIR ITENS DA TABELA  ######################################
    def on_cell_clicked(self, row, column):
        self.selected_row = row  # Armazena a linha selecionada

    def edit_selected_row(self):
        if self.selected_row == -1:  # Verifica se uma linha foi selecionada
            QMessageBox.warning(self, "Nenhuma seleção", "Por favor, selecione uma linha para editar.")
            return

        produto = self.lista_produtos[self.selected_row]
        unidades_permitidas = ['kg', 'g', 'l', 'ml', 'und']
        
        for column, (key, value) in enumerate(produto.items()):
            if key == "nome":
                new_value, ok = QInputDialog.getText(self, f"Editar {key.capitalize()}", f"Novo valor para {key}:", text=str(value))
                if ok and new_value.strip():
                    self.lista_produtos[self.selected_row][key] = new_value.strip().lower()
                    self.tableWidget_produtos.item(self.selected_row, column).setText(str(new_value.strip().lower()))
                elif not new_value.strip():
                    QMessageBox.warning(self, "Valor inválido", f"{key.capitalize()} não pode ser vazio.")
                    return
            elif key == "unidade":
                new_value, ok = QInputDialog.getText(self, f"Editar {key.capitalize()}", f"Novo valor para {key}:", text=str(value))
                if ok and new_value.strip().lower() in unidades_permitidas:
                    self.lista_produtos[self.selected_row][key] = new_value.strip().lower()
                    self.tableWidget_produtos.item(self.selected_row, column).setText(str(new_value.strip().lower()))
                elif new_value.strip().lower() not in unidades_permitidas:
                    QMessageBox.warning(self, "Unidade inválida", f"Unidade não permitida, use: {', '.join(unidades_permitidas)}")
                    return
            elif key == "quantidade":
                new_value, ok = QInputDialog.getText(self, f"Editar {key.capitalize()}", f"Novo valor para {key}:", text=str(value))
                if ok and new_value.strip():
                    try:
                        new_value = int(new_value)
                        self.lista_produtos[self.selected_row][key] = new_value
                        self.tableWidget_produtos.item(self.selected_row, column).setText(str(new_value))
                    except ValueError:
                        QMessageBox.warning(self, "Valor inválido", "Quantidade deve ser um número inteiro.")
                        return
            elif key == "valor":
                new_value, ok = QInputDialog.getText(self, f"Editar {key.capitalize()}", f"Novo valor para {key}:", text=str(value))
                if ok and new_value.strip():
                    try:
                        new_value = float(new_value)
                        self.lista_produtos[self.selected_row][key] = new_value
                        self.tableWidget_produtos.item(self.selected_row, column).setText(f"{new_value:.2f}")
                    except ValueError:
                        QMessageBox.warning(self, "Valor inválido", "Valor deve ser um número decimal, por exemplo: 10.50 ou 5.20.")
                        return
        self.save_products(self.lista_produtos)
        self.load_products()
        self.update_comboboxes()

    def delete_selected_row(self):
        if self.selected_row == -1:  # Verifica se uma linha foi selecionada
            QMessageBox.warning(self, "Nenhuma seleção", "Por favor, selecione uma linha para excluir.")
            return

        self.tableWidget_produtos.removeRow(self.selected_row)
        del self.lista_produtos[self.selected_row]
        self.selected_row = -1  # Redefine a linha selecionada para -1
        self.save_products(self.lista_produtos)
        self.load_products()
        self.update_comboboxes()
################ FUNÇÕES DAS COMBO BOXES ##############################################################
    def init_comboboxes(self):
        options_col1 = ([""] + self.lista_nomes)
        
        options_col2 = ["", 'kg', 'g', 'l', 'ml', 'und' ]

        for row in range(self.tableWidget_criar.rowCount()):
            combobox_col1 = NoScrollComboBox()
            combobox_col1.addItems(options_col1)
            self.tableWidget_criar.setCellWidget(row, 0, combobox_col1)
            self.tableWidget_criar.setItem(row, 0, QTableWidgetItem(""))
            self.tableWidget_criar.item(row, 0).setTextAlignment(Qt.AlignCenter)

            combobox_col2 = NoScrollComboBox()
            combobox_col2.addItems(options_col2)
            self.tableWidget_criar.setCellWidget(row, 1, combobox_col2)
            self.tableWidget_criar.setItem(row, 1, QTableWidgetItem(""))
            self.tableWidget_criar.item(row, 1).setTextAlignment(Qt.AlignCenter)

        for row in range(self.tableWidget_criar.rowCount()):
            item = self.tableWidget_criar.item(row, 3)
            if item is None:
                item = QTableWidgetItem()
                self.tableWidget_criar.setItem(row, 3, item)
            item.setFlags(Qt.ItemIsSelectable)

    def valor_comboboxes(self):
        for row in range(self.tableWidget_criar.rowCount()):
            combobox_col1 = self.tableWidget_criar.cellWidget(row, 0)
            if combobox_col1 is not None:
                produto_selecionado = combobox_col1.currentText()
                valor_prod = next((item["valor"] for item in self.lista_produtos if item["nome"] == produto_selecionado), 0.0)
                und_prod = next((item["unidade"] for item in self.lista_produtos if item["nome"] == produto_selecionado), None)
                qtd_prod = next((item["quantidade"] for item in self.lista_produtos if item["nome"] == produto_selecionado), None)

                combobox_und_prod_rc = self.tableWidget_criar.cellWidget(row, 1)
                item_qtd_prod_rc = self.tableWidget_criar.item(row, 2)

                if combobox_und_prod_rc is not None and item_qtd_prod_rc is not None:
                    try:
                        und_prod_rc = combobox_und_prod_rc.currentText()
                        qtd_prod_rc = float(item_qtd_prod_rc.text())
                        qtd_convert = converter_unidade(qtd_prod_rc, und_prod_rc, und_prod)
                        valor_prop = (qtd_convert / qtd_prod) * valor_prod
                        item = QTableWidgetItem(f"{valor_prop:.2f}")
                        item.setFlags(Qt.ItemIsSelectable)

                        self.tableWidget_criar.setItem(row, 3, item)
                    except (ValueError, TypeError) as e:
                        self.show_error_message(f"Erro ao calcular valor: {e}")

    def table_comboboxes(self, row, column):
        # Mostrar popup do NoScrollComboBox quando uma célula das duas primeiras colunas for clicada
        if column in [0, 1]:
            current_widget = self.tableWidget_criar.cellWidget(row, column)
            if isinstance(current_widget, QComboBox):
                current_widget.showPopup()

    def update_comboboxes(self):
        options_col1 = ([""] + self.lista_nomes)

        for row in range(self.tableWidget_criar.rowCount()):
            combobox_col1 = self.tableWidget_criar.cellWidget(row, 0)
            if isinstance(combobox_col1, NoScrollComboBox):
                combobox_col1.clear()
                combobox_col1.addItems(options_col1)

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle("Erro")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
#######################################################################################################
    def calcular(self, coluna):
        valor_total = 0
        for row in range(self.tableWidget_criar.rowCount()):
            item = self.tableWidget_criar.item(row, coluna)
            if item and item.text():  # Verifica se o item não está vazio e contém texto
                try:
                    valor = float(item.text())
                    valor_total += valor
                except ValueError:
                    print(f"Erro ao converter o valor da célula na linha {row}, coluna {coluna}: '{item.text()}'")
        try:
            valor_mais_lucro = valor_total + (valor_total * int(self.lineEdit_lucro.text()) / 100)
            valor_unitario_lucro = valor_mais_lucro / int(self.lineEdit_qtd.text())


            self.label_vt.setText(f' R$ {valor_total:.2f}')
            self.label_vtl.setText(f' R$ {valor_mais_lucro:.2f}')
            self.label_vu.setText(f' R$ {valor_unitario_lucro:.2f}')

        except ValueError:
            self.show_error_message('Os campos LUCRO e QUANTIDADE não podem estar vazios, digite numeros inteiros')


        return valor_total
#######################################################################################################
    def salvar_receita(self): # Adiciona os dados da receita em uma lista e salva em .json
        self.lista_receita = []

        nom_receita = self.lineEdit_nome.text().strip()
        lucro_receita = self.lineEdit_lucro.text().strip()
        qtd_receita = self.lineEdit_lucro.text().strip()
        receita_core = {'nome_receita': nom_receita, 'lucro': lucro_receita, 'qtd_receita': qtd_receita}

        self.lista_receita.append(receita_core)

        rows = self.tableWidget_criar.rowCount()
        keys = ['produto', 'unidade', 'quantidade']

        for row in range(rows):
            item_dict = {}

            for col in range(3):
                # Verifica se a célula contém um QComboBox
                cell_widget = self.tableWidget_criar.cellWidget(row, col)
                if isinstance(cell_widget, QComboBox):
                    item_text = cell_widget.currentText().strip()
                else:
                    item = self.tableWidget_criar.item(row, col)
                    item_text = item.text().strip() if item is not None else ""

                if item_text:
                    item_dict[keys[col]] = item_text

            if item_dict:
                self.lista_receita.append(item_dict)

        file_name = self.lista_receita[0]['nome_receita'].replace(' ', '_') + '.json'
        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(script_dir, 'receitas')
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(self.lista_receita, json_file, ensure_ascii=False, indent=4)
            self.label_msg_salvo.setText('Receita salva com Sucesso!')
            self.label_msg_salvo.setStyleSheet("color: green; font-weight: bold;")
        except: 
            self.label_msg_salvo.setText('Não foi possivel salvar a receita!')
            self.label_msg_salvo.setStyleSheet("color: red; font-weight: bold;")
            pass # validar possiveis errors
#######################################################################################################
    def listar_arquivos_json(self, diretorio):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(script_dir, 'receitas')
        diretorio = folder_path

        all_files = os.listdir(diretorio)
        arquivos_json = [arquivo for arquivo in all_files if arquivo.endswith('.json')]
        arquivos_formatados = [arquivo[:-5].replace('_', ' ') for arquivo in arquivos_json]

        # Adiciona a lista de arquivos na QTableWidget
        self.tableWidget_receitas.setRowCount(len(arquivos_formatados))
        for row, arquivo in enumerate(arquivos_formatados):
            self.tableWidget_receitas.setItem(row, 0, QTableWidgetItem(arquivo))

        return arquivos_formatados
#######################################################################################################
    def reset_page(self):
        self.tableWidget_criar.clearContents()
        self.lineEdit_nome.clear()
        self.lineEdit_lucro.clear()
        self.lineEdit_qtd.clear()
        self.label_vt.setText("")
        self.label_vtl.setText("")
        self.label_vu.setText("")
        self.label_msg_salvo.setText("")
        self.init_comboboxes()
#######################################################################################################
    def del_receita(self):
        selected_items = self.tableWidget_receitas.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Atenção", "Nenhum arquivo selecionado.")
            return

        arquivo_formatado = selected_items[0].text()
        arquivo = arquivo_formatado.replace(' ', '_') + '.json'

        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(script_dir, 'receitas')
        caminho_arquivo = os.path.join(folder_path, arquivo)

        # Exibe uma caixa de diálogo de confirmação
        reply = QMessageBox.question(
            self, 'Confirmação',
            f"Tem certeza de que deseja deletar a receita '{arquivo_formatado}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            if os.path.exists(caminho_arquivo):
                os.remove(caminho_arquivo)
                self.tableWidget_receitas.removeRow(selected_items[0].row())
                QMessageBox.information(self, "Sucesso", f"A receita '{arquivo_formatado}' foi deletada.")
            else:
                QMessageBox.warning(self, "Erro", f"O arquivo '{arquivo_formatado}' não foi encontrado no diretório.")
        else:
            QMessageBox.information(self, "Cancelado", "A operação de exclusão foi cancelada.")




if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()