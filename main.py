import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QLineEdit, QComboBox, QSpinBox, QFrame,
    QMessageBox
)
from PyQt6.QtCore import Qt

QSS_ESTILO = """
QMainWindow {
    background-color: #f4f5f7;
}

QMenuBar {
    background-color: #1f2430;
    color: #ffffff;
    padding: 6px;
    font-size: 13px;
}

QMenuBar::item {
    background: transparent;
    padding: 6px 12px;
    border-radius: 6px;
}

QMenuBar::item:selected {
    background-color: #33394a;
}

QMenu {
    background-color: #ffffff;
    border: 1px solid #d9dce3;
    border-radius: 8px;
    padding: 6px;
}

QMenu::item {
    padding: 6px 20px;
    border-radius: 6px;
}

QMenu::item:selected {
    background-color: #e8ebf5;
}

#panelLateral {
    background-color: #1f2430;
    border-radius: 0px;
}

#nombreUsuarioLateral {
    color: #ffffff;
    font-size: 15px;
    font-weight: 600;
}

#fotoPerfil {
    background-color: #33394a;
    border-radius: 45px;
    min-width: 90px;
    max-width: 90px;
    min-height: 90px;
    max-height: 90px;
}

#botonNav {
    color: #c7cbd6;
    background-color: transparent;
    text-align: left;
    padding: 10px 16px;
    border-radius: 8px;
    font-size: 13px;
}

#botonNav:hover {
    background-color: #33394a;
    color: #ffffff;
}

#tarjetaConfig {
    background-color: #ffffff;
    border-radius: 14px;
    border: 1px solid #e3e5ea;
}

#tituloConfig {
    font-size: 20px;
    font-weight: 600;
    color: #1f2430;
}

QLabel[etiquetaCampo="true"] {
    font-size: 12px;
    color: #5a5f6d;
    font-weight: 600;
}

QLineEdit, QComboBox, QSpinBox {
    background-color: #f7f8fa;
    border: 1px solid #d9dce3;
    border-radius: 8px;
    padding: 8px 10px;
    font-size: 13px;
}

QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
    border: 1px solid #5865f2;
}

#botonColor {
    border-radius: 8px;
    border: 1px solid #d9dce3;
    min-height: 34px;
}

#botonGuardar {
    background-color: #5865f2;
    color: #ffffff;
    font-weight: 600;
    padding: 10px 22px;
    border-radius: 8px;
    font-size: 13px;
}

#botonGuardar:hover {
    background-color: #4752c4;
}
"""


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        self.resize(980, 620)
        self.setStyleSheet(QSS_ESTILO)

        self.crear_menu_superior()
        self.construir_interfaz()

    def crear_menu_superior(self):
        barra_menu = self.menuBar()

        menu_archivo = barra_menu.addMenu("Archivo")
        menu_archivo.addAction("Nuevo", self.accion_simulada)
        menu_archivo.addAction("Abrir", self.accion_simulada)
        menu_archivo.addSeparator()
        menu_archivo.addAction("Salir", self.close)

        menu_edicion = barra_menu.addMenu("Edición")
        menu_edicion.addAction("Deshacer", self.accion_simulada)
        menu_edicion.addAction("Rehacer", self.accion_simulada)

        menu_ver = barra_menu.addMenu("Ver")
        menu_ver.addAction("Pantalla completa", self.accion_simulada)
        menu_ver.addAction("Modo compacto", self.accion_simulada)

        barra_menu.addAction("Settings", self.accion_simulada)

    def accion_simulada(self):
        QMessageBox.information(self, "Aviso", "Esta opción es simulada y no tiene funcionalidad real.")

    def construir_interfaz(self):
        contenedor_central = QWidget()
        layout_general = QHBoxLayout(contenedor_central)
        layout_general.setContentsMargins(0, 0, 0, 0)
        layout_general.setSpacing(0)

        layout_general.addWidget(self.crear_panel_lateral())
        layout_general.addWidget(self.crear_panel_configuracion(), stretch=1)

        self.setCentralWidget(contenedor_central)

    def crear_panel_lateral(self):
        panel = QFrame()
        panel.setObjectName("panelLateral")
        panel.setFixedWidth(220)

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 30, 20, 30)
        layout.setSpacing(16)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        foto = QLabel()
        foto.setObjectName("fotoPerfil")
        foto.setFixedSize(90, 90)
        layout.addWidget(foto, alignment=Qt.AlignmentFlag.AlignHCenter)

        nombre = QLabel("Mayk")
        nombre.setObjectName("nombreUsuarioLateral")
        nombre.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(nombre)

        layout.addSpacing(20)

        boton_settings = QPushButton("⚙  Settings")
        boton_settings.setObjectName("botonNav")
        layout.addWidget(boton_settings)

        layout.addStretch()

        return panel

    def crear_panel_configuracion(self):
        contenedor = QWidget()
        layout_externo = QVBoxLayout(contenedor)
        layout_externo.setContentsMargins(30, 30, 30, 30)

        tarjeta = QFrame()
        tarjeta.setObjectName("tarjetaConfig")
        layout_tarjeta = QVBoxLayout(tarjeta)
        layout_tarjeta.setContentsMargins(30, 25, 30, 25)
        layout_tarjeta.setSpacing(14)

        titulo = QLabel("Configuración")
        titulo.setObjectName("tituloConfig")
        layout_tarjeta.addWidget(titulo)

        layout_tarjeta.addWidget(self.crear_campo("Nombre de usuario", QLineEdit()))

        combo_tema = QComboBox()
        combo_tema.addItems(["Claro", "Oscuro"])
        layout_tarjeta.addWidget(self.crear_campo("Tema", combo_tema))

        combo_idioma = QComboBox()
        combo_idioma.addItems(["es", "es-ES", "en", "en-US"])
        layout_tarjeta.addWidget(self.crear_campo("Idioma", combo_idioma))

        spin_fuente = QSpinBox()
        spin_fuente.setRange(8, 32)
        spin_fuente.setValue(14)
        layout_tarjeta.addWidget(self.crear_campo("Tamaño de fuente", spin_fuente))

        fila_colores = QHBoxLayout()
        fila_colores.setSpacing(20)
        fila_colores.addLayout(self.crear_campo_color("Color de barra", "#1f2430"))
        fila_colores.addLayout(self.crear_campo_color("Color de letra", "#ffffff"))
        layout_tarjeta.addLayout(fila_colores)

        layout_tarjeta.addSpacing(10)

        boton_guardar = QPushButton("Guardar cambios")
        boton_guardar.setObjectName("botonGuardar")
        boton_guardar.clicked.connect(self.guardar_pendiente)
        layout_tarjeta.addWidget(boton_guardar, alignment=Qt.AlignmentFlag.AlignRight)

        layout_externo.addWidget(tarjeta)
        layout_externo.addStretch()

        return contenedor

    def crear_campo(self, etiqueta_texto, widget_control):
        contenedor = QWidget()
        layout = QVBoxLayout(contenedor)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        etiqueta = QLabel(etiqueta_texto)
        etiqueta.setProperty("etiquetaCampo", "true")

        layout.addWidget(etiqueta)
        layout.addWidget(widget_control)

        return contenedor

    def crear_campo_color(self, etiqueta_texto, color_hex):
        layout = QVBoxLayout()
        layout.setSpacing(4)

        etiqueta = QLabel(etiqueta_texto)
        etiqueta.setProperty("etiquetaCampo", "true")

        boton_color = QPushButton()
        boton_color.setObjectName("botonColor")
        boton_color.setStyleSheet(f"background-color: {color_hex};")

        layout.addWidget(etiqueta)
        layout.addWidget(boton_color)

        return layout

    def guardar_pendiente(self):
        QMessageBox.information(self, "Aviso", "El guardado se implementará en el siguiente commit.")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(aplicacion.exec())