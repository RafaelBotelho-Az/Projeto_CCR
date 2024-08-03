from PySide6 import QtCore
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog, QMessageBox, QComboBox, QTableWidget
from ui_main import Ui_MainWindow
from funcs import converter_unidade
from styles_module import apply_styles, set_label_style, table_style
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
        self.setWindowTitle('SCCR - Sistema para Calcular o Custo de Receitas')
        self.lista_produtos = []
        self.load_products()
        self.lista_nomes = [item['nome'] for item in self.lista_produtos]
        self.setFixedSize(950, 660)
        apply_styles(self.tableWidget_criar)
        set_label_style(self.label_vt)
        set_label_style(self.label_vtl)
        set_label_style(self.label_vu)
        table_style(self.tableWidget_receitas)
        table_style(self.tableWidget_produtos)

        self.tableWidget_receitas.setColumnWidth(0, 558)
        self.tableWidget_criar.setColumnWidth(0, 475)
        self.tableWidget_criar.setColumnWidth(1, 67)
        self.tableWidget_criar.setColumnWidth(2, 90)
        self.tableWidget_criar.setColumnWidth(3, 60)
        self.tableWidget_produtos.setColumnWidth(0, 330)
        self.tableWidget_produtos.setColumnWidth(1, 67)
        self.tableWidget_produtos.setColumnWidth(2, 90)
        self.tableWidget_produtos.setColumnWidth(3, 60)
################  PAGINAS  #############################################################################
        self.btn_menu_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_menu_receitas.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_receitas))
        self.btn_menu_criar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_criar))
        self.btn_menu_cadastrar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastrar))
        self.btn_precificar.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_precifica))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
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
        self.btn_receitas_abrir.clicked.connect(self.open_receita)
        self.btn_limpar.clicked.connect(self.reset_page)
        self.btn_receitas_excluir.clicked.connect(self.del_receita)
        self.define_taxa()
        self.comboBox_precif.currentIndexChanged.connect(self.define_taxa)
        self.lineEdit_precf_preco.textChanged.connect(self.calcular_taxa)
        self.comboBox_precif.currentIndexChanged.connect(self.calcular_taxa)
        self.calcular_taxa()
#######################################################################################################  FUNÇÃO HOME #########################################################################
    def leftMenu(self):
        width = self.left_container.width()

        if width == 0:
            newWidth = 150
        else:
            newWidth = 0
        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def cadastrar(self):
        unidades_permitidas = ['kg', 'g', 'l', 'ml', 'und']

        nome = self.lineEdit_produto.text().strip().lower()
        unidade = self.lineEdit_unidade.text().strip().lower()
        quantidade = self.lineEdit_quantidade.text().strip().lower()
        valor = self.lineEdit_valor.text().strip().lower()

        if not nome or not unidade or not quantidade or not valor:
            QMessageBox.warning(self, "Atenção", "Todos os campos são obrigatórios!")
            return

        if unidade not in unidades_permitidas:
            QMessageBox.warning(self, "Atenção", "UNIDADE não permitida, use: 'kg', 'g', 'l', 'ml', 'und'")
            return

        try:
            quantidade = int(quantidade)
        except ValueError:
            QMessageBox.warning(self, "Atenção", "QUANTIDADE deve ser um número inteiro!")
            return

        try:
            valor = float(valor)
        except ValueError:
            QMessageBox.warning(self, "Atenção", "VALOR deve ser um número inteiro ou decimal, por exemplo: 10 ou 10.50")
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

        QMessageBox.warning(self, "Atenção", "Cadastrado com Sucesso!")
        self.coloca_na_tabela(self.lista_produtos)
        self.save_products(self.lista_produtos)
        self.load_products()
        self.update_comboboxes()

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
################  FUNÇÕES PARA EDITAR E EXCLUIR ITENS DA TABELA  ######################################
    def coloca_na_tabela(self, lista_produtos):
        self.tableWidget_produtos.setRowCount(len(lista_produtos))

        for row, produto in enumerate(lista_produtos):
            for column, (key, value) in enumerate(produto.items()):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_produtos.setItem(row, column, item)
                self.tableWidget_produtos.setEditTriggers(QTableWidget.NoEditTriggers)

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

        reply = QMessageBox.question(
            self, 'Confirmação',
            f"Tem certeza de que deseja excluir esse produto?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.tableWidget_produtos.removeRow(self.selected_row)
            del self.lista_produtos[self.selected_row]
            self.selected_row = -1  # Redefine a linha selecionada para -1
            self.save_products(self.lista_produtos)
            self.load_products()
            self.update_comboboxes()
        else:
            QMessageBox.information(self, "Cancelado", "A operação de exclusão foi cancelada.")
################ FUNÇÕES DAS COMBO BOXES ##############################################################
    def init_comboboxes(self):
        options_col1 = ([""] + self.lista_nomes)
        
        options_col2 = ["", 'kg', 'g', 'l', 'ml', 'und' ]

        for row in range(self.tableWidget_criar.rowCount()):
            combobox_col1 = NoScrollComboBox()
            combobox_col1.setStyleSheet("QComboBox {color: #ffffff;}QAbstractItemView {color: #ffffff;}")
            combobox_col1.addItems(options_col1)
            self.tableWidget_criar.setCellWidget(row, 0, combobox_col1)
            self.tableWidget_criar.setItem(row, 0, QTableWidgetItem(""))
            self.tableWidget_criar.item(row, 0).setTextAlignment(Qt.AlignCenter)

            combobox_col2 = NoScrollComboBox()
            combobox_col2.setStyleSheet("QComboBox {color: #ffffff;}QAbstractItemView {color: #ffffff;}")
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
            self.show_error_message('Os campos "Lucro" e "Quantidade" devem conter número válidos e não podem estar vazios')


        return valor_total

    def salvar_receita(self):
        self.lista_receita = []

        nom_receita = self.lineEdit_nome.text().strip()
        if not nom_receita:
            QMessageBox.warning(self, "Atenção", "O nome da receita não pode estar vazio.")
            return

        lucro_receita = self.lineEdit_lucro.text().strip()
        if not lucro_receita:
            QMessageBox.warning(self, "Atenção", "O lucro da receita deve ser um número válido.")
            return

        qtd_receita = self.lineEdit_qtd.text().strip()
        if not qtd_receita:
            QMessageBox.warning(self, "Atenção", "A quantidade da receita deve ser um número válida.")
            return

        receita_core = {'nome_receita': nom_receita, 'lucro': lucro_receita, 'qtd_receita': qtd_receita}
        self.lista_receita.append(receita_core)

        rows = self.tableWidget_criar.rowCount()
        keys = ['produto', 'unidade', 'quantidade']

        for row in range(rows):
            item_dict = {}
            for col in range(3):
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

        file_name = nom_receita.replace(' ', '_') + '.json'

        user_documents_path = os.path.expanduser("~/Documents")
        folder_path = os.path.join(user_documents_path, 'receitas')

        if not os.path.exists(folder_path):
            try:
                os.makedirs(folder_path)
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao criar pasta: {e}")
                return

        file_path = os.path.join(folder_path, file_name)

        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(self.lista_receita, json_file, ensure_ascii=False, indent=4)
            self.label_msg_salvo.setText('Receita salva com sucesso!')
            self.label_msg_salvo.setStyleSheet("color: green; font-weight: bold;")
        except Exception as e:
            self.label_msg_salvo.setText(f'Não foi possível salvar a receita: {e}')
            self.label_msg_salvo.setStyleSheet("color: red; font-weight: bold;")
            QMessageBox.critical(self, "Erro", f"Não foi possível salvar a receita: {e}")

    def listar_arquivos_json(self, diretorio):
        user_documents_path = os.path.expanduser("~/Documents")
        folder_path = os.path.join(user_documents_path, 'receitas')
        diretorio = folder_path

        if not os.path.exists(folder_path):
            try:
                os.makedirs(folder_path)
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao criar pasta: {e}")
                return

        all_files = os.listdir(diretorio)
        arquivos_json = [arquivo for arquivo in all_files if arquivo.endswith('.json')]
        arquivos_formatados = [arquivo[:-5].replace('_', ' ') for arquivo in arquivos_json]

        self.tableWidget_receitas.setRowCount(len(arquivos_formatados))
        for row, arquivo in enumerate(arquivos_formatados):
            self.tableWidget_receitas.setItem(row, 0, QTableWidgetItem(arquivo))
        self.tableWidget_receitas.setEditTriggers(QTableWidget.NoEditTriggers)
        return arquivos_formatados

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

    def del_receita(self):
        selected_items = self.tableWidget_receitas.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Atenção", "Nenhum arquivo selecionado.")
            return

        arquivo_formatado = selected_items[0].text()
        arquivo = arquivo_formatado.replace(' ', '_') + '.json'

        user_documents_path = os.path.expanduser("~/Documents")
        folder_path = os.path.join(user_documents_path, 'receitas')
        caminho_arquivo = os.path.join(folder_path, arquivo)

        reply = QMessageBox.question(
            self, 'Confirmação',
            f"Tem certeza de que deseja deletar a receita '{arquivo_formatado}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            if os.path.exists(caminho_arquivo):
                try:
                    os.remove(caminho_arquivo)
                    self.tableWidget_receitas.removeRow(selected_items[0].row())
                    QMessageBox.information(self, "Sucesso", f"A receita '{arquivo_formatado}' foi deletada.")
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Não foi possível deletar o arquivo: {e}")
            else:
                QMessageBox.warning(self, "Erro", f"O arquivo '{arquivo_formatado}' não foi encontrado no diretório.")
        else:
            QMessageBox.information(self, "Cancelado", "A operação de exclusão foi cancelada.")

    def open_receita(self):
        selected_items = self.tableWidget_receitas.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Atenção", "Nenhum arquivo selecionado.")
            return

        arquivo_formatado = selected_items[0].text()
        arquivo = arquivo_formatado.replace(' ', '_') + '.json'

        user_documents_path = os.path.expanduser("~/Documents")
        folder_path = os.path.join(user_documents_path, 'receitas')
        caminho_arquivo = os.path.join(folder_path, arquivo)

        if not os.path.exists(caminho_arquivo):
            QMessageBox.warning(self, "Erro", f"Arquivo {arquivo} não encontrado.")
            return
        
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                list_dict = json.load(arquivo)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível abrir o arquivo: {e}")
            return

        if list_dict:
            self.lineEdit_nome.setText(list_dict[0].get('nome_receita', ''))
            self.lineEdit_lucro.setText(list_dict[0].get('lucro', ''))
            self.lineEdit_qtd.setText(list_dict[0].get('qtd_receita', ''))

            for row_index, dicionario in enumerate(list_dict[1:]):
                self.tableWidget_criar.insertRow(row_index)

                combo_produto = NoScrollComboBox()
                combo_produto.setStyleSheet("QComboBox {color: #ffffff;}QAbstractItemView {color: #ffffff;}")
                combo_produto.addItems(self.lista_nomes)
                index_produto = combo_produto.findText(dicionario.get('produto', ''))
                if index_produto != -1:
                    combo_produto.setCurrentIndex(index_produto)
                self.tableWidget_criar.setCellWidget(row_index, 0, combo_produto)

                combo_unidade = NoScrollComboBox()
                combo_unidade.setStyleSheet("QComboBox {color: #ffffff;}QAbstractItemView {color: #ffffff;}")
                combo_unidade.addItems(["", 'kg', 'g', 'l', 'ml', 'und'])
                index_unidade = combo_unidade.findText(dicionario.get('unidade', ''))
                if index_unidade != -1:
                    combo_unidade.setCurrentIndex(index_unidade)
                self.tableWidget_criar.setCellWidget(row_index, 1, combo_unidade)

                item_quantidade = QTableWidgetItem(str(dicionario.get('quantidade', '')))
                self.tableWidget_criar.setItem(row_index, 2, item_quantidade)

            # Ajusta a coluna 4 para não poder ser selecionada
            for row in range(self.tableWidget_criar.rowCount()):
                item = self.tableWidget_criar.item(row, 3)
                if item is None:
                    item = QTableWidgetItem()
                    self.tableWidget_criar.setItem(row, 3, item)
                item.setFlags(Qt.ItemIsSelectable)

            self.btn_calcular.click()  # Simula o clique do botão para calcular

    def define_taxa(self):
        if self.comboBox_precif.currentText() == 'Entrega Própria':
            self.label_precif_taxa.setText('16.69')
            self.label_precif_taxa_info_1.setText(
                'Comissão Entrega Própria (12%) + Taxa de Pagamento Online (3,2%) +')
            self.label_precif_taxa_info_2.setText(
                'Taxa de Antecipação de Repasse (1,49%).')
        else:
            self.label_precif_taxa.setText('27.69')
            self.label_precif_taxa_info_1.setText(
                'Comissão Entrega Parceira (23%) + Taxa de Pagamento Online (3,2%) +')
            self.label_precif_taxa_info_2.setText(
                'Taxa de Antecipação de Repasse (1,49%).')

    def calcular_taxa(self):
        try:
            texto_preco = self.lineEdit_precf_preco.text()

            if texto_preco == "":
                preco = 0
            else:
                preco = float(texto_preco)

            taxa = float(self.label_precif_taxa.text())
            resultado = preco * 100 / (100 - taxa)
            resultado_formatado = "R$ {:.2f}".format(resultado)

            estilo_css = """
            font-size: 60px;
            color: #2d2d2d;
            font-weight: bold;
            """
            self.label_precif_preco_venda.setStyleSheet(estilo_css)

            self.label_precif_preco_venda.setText(resultado_formatado)
        except ValueError:
            self.label_precif_preco_venda.setText("Erro")

        self.label_precif_preco_info_1.setText(
            f'Vendendo esse item por R$ {resultado_formatado} a taxa será de R$ {taxa}')
        self.label_precif_preco_info_2.setText(
            f'você receberá um repasse líquido de R$ {texto_preco}.')


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QMessageBox {
        background-color: #333;
        color: #a266e9;
    }

    QMessageBox QLabel {
        color: white;
    }

    QMessageBox QPushButton {
        color: white;
        background-color: #007bff;
        border: 1px solid #0056b3;
        border-radius: 5px;
        padding: 5px;
    }

    QMessageBox QPushButton:hover {
        background-color: #0056b3;
    }

    QMessageBox QPushButton:pressed {
        background-color: #003f7f;
    }
""")
    window = MainWindow()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(current_dir, "icons", "icone.ico")
    app.setWindowIcon(QIcon(icon_path))


    window.show()
    sys.exit(app.exec())