from PyQt6.QtWidgets import (QMainWindow, QPushButton, QGroupBox, QGridLayout,
                             QLineEdit, QLabel, QMenu, QTableWidget, QTableWidgetItem, QComboBox)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction

from db_proc.db_facade import ComponentDB


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = ComponentDB()
        self.setWindowTitle("db_application")
        self.showMaximized()

        self.label_rpm = QLabel("criterion 1")
        self.label_K = QLabel("criterion 2")
        self.motor_rpm = QLineEdit(f"{1200}")
        self.retarder_1_rpm = QLineEdit(f"{1150}")
        self.retarder_2_rpm = QLineEdit(f"{1250}")
        self.retarder_3_rpm = QLineEdit(f"{2330}")

        self.motor_K = QLineEdit(f"{1.051}")
        self.retarder_1_K = QLineEdit(f"{1.1}")
        self.retarder_2_K = QLineEdit(f"{1.2}")
        self.retarder_3_K = QLineEdit(f"{1.3}")

        self.group_box_top = QGroupBox("Primary select rules")
        grid_top = QGridLayout()
        grid_top.setSpacing(1)

        grid_top.addWidget(QLabel("rule 1"), 0, 1)
        grid_top.addWidget(QLabel("rule 2"), 0, 2)
        grid_top.addWidget(QLabel("rule 3"), 0, 3)
        grid_top.addWidget(QLabel("rule 4"), 0, 4)

        grid_top.addWidget(self.label_rpm, 1, 0)
        grid_top.addWidget(self.motor_rpm, 1, 1)
        grid_top.addWidget(self.retarder_1_rpm, 1, 2)
        grid_top.addWidget(self.retarder_2_rpm, 1, 3)
        grid_top.addWidget(self.retarder_3_rpm, 1, 4)

        grid_top.addWidget(self.label_K, 2, 0)
        grid_top.addWidget(self.motor_K, 2, 1)
        grid_top.addWidget(self.retarder_1_K, 2, 2)
        grid_top.addWidget(self.retarder_2_K, 2, 3)
        grid_top.addWidget(self.retarder_3_K, 2, 4)

        self.group_box_top.setLayout(grid_top)

        self.new_m_K = QLineEdit(f"{1.0}")
        self.new_r1_K = QLineEdit(f"{1.0}")
        self.new_r2_K = QLineEdit(f"{1.0}")
        self.new_r3_K = QLineEdit(f"{1.0}")

        self.button_upload = QPushButton("upload")
        self.button_upload.setFixedSize(QSize(155, 50))
        self.button_upload.clicked.connect(self.on_button_upload)

        self.group_box_middle = QGroupBox("ComponentDB:")
        self.group_box_bottom = QGroupBox("Table data:")
        grid_middle = QGridLayout()
        grid_middle.setSpacing(1)
        grid_bottom = QGridLayout()
        grid_bottom.setSpacing(1)

        self.tableWidget = QTableWidget(1, 1)

        self.select_db = QComboBox()
        self.select_db.addItems(self.db.table_list_names)
        self.select_db_index_changed(self.select_db.currentIndex())

        self.select_db.currentIndexChanged.connect(self.select_db_index_changed)
        grid_middle.addWidget(self.select_db, 0, 0)

        grid_bottom.addWidget(self.tableWidget, 0, 0)
        grid_middle.addWidget(self.button_upload, 0, 4)
        self.group_box_middle.setLayout(grid_middle)
        self.group_box_bottom.setLayout(grid_bottom)

        grid = QGridLayout()
        grid.addWidget(self.group_box_top, 0, 0)
        grid.addWidget(self.group_box_middle, 1, 0)
        grid.addWidget(self.group_box_bottom, 2, 0)

        self.group_box = QGroupBox()
        self.group_box.setLayout(grid)

        self.setCentralWidget(self.group_box)

    def select_db_index_changed(self, index):
        self.db.queue_table_data(index)
        self.update_table_dimensions()
        self.update_table_data()

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("Select", self))
        context.addAction(QAction("Edit", self))
        context.addAction(QAction("Delete", self))
        context.exec(e.globalPos())

    def on_button_upload(self):

        pass

    def update_table_data(self):
        row = 0
        data = self.db.get_table_data()

        for one_row in data:
            column = 0
            row_data = one_row.get_items_tuple()
            for item in row_data:
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
            row += 1

    def update_table_dimensions(self):
        if self.db.row_count > 0:
            self.tableWidget.setRowCount(self.db.row_count)
        else:
            self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(self.db.column_count)
        self.tableWidget.setHorizontalHeaderLabels(self.db.column_names)
