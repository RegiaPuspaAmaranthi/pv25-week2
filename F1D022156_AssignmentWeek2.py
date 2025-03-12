from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, 
    QVBoxLayout, QHBoxLayout, QGroupBox, QFormLayout
)
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.resize(550, 500)

        # Identitas Section
        identitas_layout = QVBoxLayout()
        identitas_title = QLabel("Identitas")
        identitas_title.setStyleSheet("font-weight: bold;")

        identitas_box = QGroupBox()
        identitas_box.setStyleSheet(
            "QGroupBox { background-color: #f5f5f5; border-radius: 8px; padding: 10px; border: 1px solid #dcdcdc; }"
        )
        identitas_inner_layout = QVBoxLayout()
        identitas_inner_layout.addWidget(QLabel("Nama : Regia Puspa Amaranthi"))
        identitas_inner_layout.addWidget(QLabel("Nim : F1D022156"))
        identitas_inner_layout.addWidget(QLabel("Kelas : D"))
        identitas_box.setLayout(identitas_inner_layout)

        identitas_layout.addWidget(identitas_title)
        identitas_layout.addWidget(identitas_box)

        # Navigation Section
        navigation_section = QVBoxLayout()
        navigation_title = QLabel("Navigation")
        navigation_title.setStyleSheet("font-weight: bold;")

        navigation_box = QGroupBox()
        navigation_box.setStyleSheet(
            "QGroupBox { background-color: #f5f5f5; border-radius: 8px; padding: 10px; border: 1px solid #dcdcdc; }"
        )
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(QPushButton("Home"))
        navigation_layout.addWidget(QPushButton("About"))
        navigation_layout.addWidget(QPushButton("Contact"))
        navigation_box.setLayout(navigation_layout)

        navigation_section.addWidget(navigation_title)
        navigation_section.addWidget(navigation_box)

        # User Registration Section
        registration_section = QVBoxLayout()
        registration_title = QLabel("User Registration")
        registration_title.setStyleSheet("font-weight: bold;")

        registration_box = QGroupBox()
        registration_box.setStyleSheet(
            "QGroupBox { background-color: #f5f5f5; border-radius: 8px; padding: 10px; border: 1px solid #dcdcdc; }"
        )
        registration_layout = QFormLayout()

        # Full Name
        self.full_name = QLineEdit()
        registration_layout.addRow(QLabel("Full Name:"), self.full_name)

        # Email
        self.email = QLineEdit()
        registration_layout.addRow(QLabel("Email:"), self.email)

        # Phone
        self.phone = QLineEdit()
        registration_layout.addRow(QLabel("Phone:"), self.phone)

        # Gender Selection
        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        registration_layout.addRow(QLabel("Gender:"), gender_layout)

        # Country Selection
        self.country = QComboBox()
        self.country.addItems(["Select", "Indonesia", "USA", "Japan", "Malaysia", "Australia"])
        registration_layout.addRow(QLabel("Country:"), self.country)

        registration_box.setLayout(registration_layout)

        registration_section.addWidget(registration_title)
        registration_section.addWidget(registration_box)

        # Actions Section
        actions_section = QVBoxLayout()
        actions_title = QLabel("Actions")
        actions_title.setStyleSheet("font-weight: bold;")

        actions_box = QGroupBox()
        actions_box.setStyleSheet(
            "QGroupBox { background-color: #f5f5f5; border-radius: 8px; padding: 10px; border: 1px solid #dcdcdc; }"
        )
        actions_layout = QHBoxLayout()
        actions_layout.addWidget(QPushButton("Submit"))
        actions_layout.addWidget(QPushButton("Cancel"))
        actions_box.setLayout(actions_layout)

        actions_section.addWidget(actions_title)
        actions_section.addWidget(actions_box)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(identitas_layout)
        main_layout.addLayout(navigation_section)
        main_layout.addLayout(registration_section)
        main_layout.addLayout(actions_section)
        main_layout.addStretch()

        self.setLayout(main_layout)
        self.setStyleSheet("""
            QWidget { font-size: 14px; }
            QGroupBox { background-color: #f5f5f5; border-radius: 8px; padding: 10px; border: 1px solid #dcdcdc; }
            QLineEdit, QComboBox { padding: 4px; border: 1px solid #aaa; border-radius: 4px; }
            QRadioButton { margin-left: 5px; }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())
