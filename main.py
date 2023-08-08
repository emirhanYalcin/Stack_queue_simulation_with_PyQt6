import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QFont, QIcon
from design import Ui_Form

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Stack & Queue Simulator")
        self.setWindowIcon(QIcon("icon.png"))
        self.initialize_buttons()


    def initialize_buttons(self):
        self.ui.push_button.clicked.connect(self.push)
        self.ui.stack_pop.clicked.connect(self.pop)
        self.ui.stack_input.returnPressed.connect(self.push)
        self.ui.enqueue_button.clicked.connect(self.enqueue)
        self.ui.dequeue_button.clicked.connect(self.dequeue)
        self.ui.queue_input.returnPressed.connect(self.enqueue)

    def push(self):
        
        self.ui.stack_input.setFocus()
        input_item = self.ui.stack_input.text()
        if not input_item:
            return
        self.ui.stack_label.setStyleSheet("color: black; font-weight: normal;")
        self.ui.stack_listWidget.addItem(input_item)
        self.ui.stack_input.clear()
        self.ui.stack_label.setText(f"{input_item} was pushed into the Stack.")
        self.ui.stack_input.setFocus()

    def pop(self):
        if (self.ui.stack_listWidget.count()):
            pop_item = self.ui.stack_listWidget.takeItem(self.ui.stack_listWidget.count() - 1)
            self.ui.stack_label.setText(f"{pop_item.text()} was popped from the stack.")
            self.ui.stack_input.setFocus()
        else:
            self.ui.stack_label.setText("Stack is Empty!")
            self.ui.stack_label.setStyleSheet("color: red; font-weight: bold;")
        pass

    def enqueue(self):
        
        self.ui.queue_input.setFocus()
        input_item = self.ui.queue_input.text()
        if not input_item:
            return
        self.ui.queue_label.setStyleSheet("color: black; font-weight: normal;")
        self.ui.queue_listWidget.addItem(input_item)
        self.ui.queue_input.clear()
        self.ui.queue_input.setFocus()
        self.ui.queue_label.setText(f"{input_item} enqueued.")

    def dequeue(self):
        if (self.ui.queue_listWidget.count()):
            first_item = self.ui.queue_listWidget.takeItem(0).text()
            self.ui.queue_label.setText(f"{first_item} dequeued.")
            self.ui.queue_input.setFocus()
        else:
            self.ui.queue_label.setText("Queue is Empty!")
            self.ui.queue_label.setStyleSheet("color: red; font-weight: bold;")


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
