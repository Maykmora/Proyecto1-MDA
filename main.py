import sys
import os
import json
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,QLabel, QPushButton, QLineEdit, QComboBox, QSpinBox, QFrame,QMessageBox, QColorDialog, QFileDialog)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

ARCHIVO_CONFIG = "config.json"
ARCHIVO_BACKUP = "config.bak"
ARCHIVO_TEMPORAL = "config.tmp"

VALORES_PREDETERMINADOS = {
    "nombre_usuario": "Mayk",
    "tema_interfaz": "Claro",
    "idioma": "es",
    "tamaño_fuente": 14,
    "color_barra_menu": "#1f2430",
    "color_letra": "#ffffff",
    "foto_perfil": None,
}


def cargar_configuracion_archivo():
    try:
        with open(ARCHIVO_CONFIG, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return VALORES_PREDETERMINADOS.copy()
    except json.JSONDecodeError:
        QMessageBox.warning(
            None,
            "Configuración corrupta",
            "El archivo de configuración tiene un formato inválido. Se cargarán los valores predeterminados."
        )
        return VALORES_PREDETERMINADOS.copy()
    except PermissionError:
        QMessageBox.warning(
            None,
            "Sin permisos",
            "No se tienen permisos para leer el archivo de configuración. Se cargarán los valores predeterminados."
        )
        return VALORES_PREDETERMINADOS.copy()


def crear_backup():
    if os.path.exists(ARCHIVO_CONFIG):
        with open(ARCHIVO_CONFIG, "r", encoding="utf-8") as original:
            contenido = original.read()
        with open(ARCHIVO_BACKUP, "w", encoding="utf-8") as respaldo:
            respaldo.write(contenido)


def guardar_configuracion_archivo(configuracion):
    crear_backup()
    with open(ARCHIVO_TEMPORAL, "w", encoding="utf-8") as archivo:
        json.dump(configuracion, archivo, ensure_ascii=False, indent=4)
    os.replace(ARCHIVO_TEMPORAL, ARCHIVO_CONFIG)


QSS_CLARO = """
QMainWindow {
    background-color: #f4f5f7;
}

#panelLateral {
    background-color: #1f2430;
    border-radius: 0px;
}

#tituloApp {
    color: #ffffff;
    font-weight: 700;
}

#nombreUsuarioLateral {
    color: #ffffff;
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
}

#botonNav:hover {
    background-color: #33394a;
    color: #ffffff;
}

#botonNav[activo="true"] {
    background-color: #33394a;
    color: #ffffff;
}

#tarjetaConfig {
    background-color: #ffffff;
    border-radius: 14px;
    border: 1px solid #e3e5ea;
}

#tituloConfig {
    font-weight: 600;
    color: #1f2430;
}

QLabel[etiquetaCampo="true"] {
    color: #5a5f6d;
    font-weight: 600;
}

QLineEdit, QComboBox, QSpinBox {
    background-color: #f7f8fa;
    border: 1px solid #d9dce3;
    border-radius: 8px;
    padding: 8px 10px;
    color: #1f2430;
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
}

#botonGuardar:hover {
    background-color: #4752c4;
}

#botonCancelar {
    background-color: #ffffff;
    color: #5a5f6d;
    font-weight: 600;
    padding: 10px 22px;
    border-radius: 8px;
    border: 1px solid #d9dce3;
}

#botonCancelar:hover {
    background-color: #f0f1f4;
}
"""

QSS_OSCURO = """
QMainWindow {
    background-color: #15171c;
}

#panelLateral {
    background-color: #1f2430;
    border-radius: 0px;
}

#tituloApp {
    color: #ffffff;
    font-weight: 700;
}

#nombreUsuarioLateral {
    color: #ffffff;
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
}

#botonNav:hover {
    background-color: #33394a;
    color: #ffffff;
}

#botonNav[activo="true"] {
    background-color: #33394a;
    color: #ffffff;
}

#tarjetaConfig {
    background-color: #20232b;
    border-radius: 14px;
    border: 1px solid #2c303a;
}

#tituloConfig {
    font-weight: 600;
    color: #f5f6fa;
}

QLabel[etiquetaCampo="true"] {
    color: #a9adba;
    font-weight: 600;
}

QLineEdit, QComboBox, QSpinBox {
    background-color: #2a2e38;
    border: 1px solid #3a3f4b;
    border-radius: 8px;
    padding: 8px 10px;
    color: #f5f6fa;
}

QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
    border: 1px solid #5865f2;
}

#botonColor {
    border-radius: 8px;
    border: 1px solid #3a3f4b;
    min-height: 34px;
}

#botonGuardar {
    background-color: #5865f2;
    color: #ffffff;
    font-weight: 600;
    padding: 10px 22px;
    border-radius: 8px;
}

#botonGuardar:hover {
    background-color: #4752c4;
}

#botonCancelar {
    background-color: #20232b;
    color: #a9adba;
    font-weight: 600;
    padding: 10px 22px;
    border-radius: 8px;
    border: 1px solid #3a3f4b;
}

#botonCancelar:hover {
    background-color: #2a2e38;
}
"""


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicación")
        self.resize(980, 620)

        self.config_actual = cargar_configuracion_archivo()

        self.construir_interfaz()
        self.aplicar_configuracion(self.config_actual)

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
        self.panel_lateral = panel
        panel.setFixedWidth(220)

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 24, 20, 30)
        layout.setSpacing(14)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        titulo_app = QLabel("Mi Aplicación")
        titulo_app.setObjectName("tituloApp")
        self.titulo_app = titulo_app
        layout.addWidget(titulo_app)

        layout.addSpacing(10)

        self.foto_perfil_label = QLabel()
        self.foto_perfil_label.setObjectName("fotoPerfil")
        self.foto_perfil_label.setFixedSize(90, 90)
        self.foto_perfil_label.setScaledContents(True)
        layout.addWidget(self.foto_perfil_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.label_nombre_lateral = QLabel(self.config_actual["nombre_usuario"])
        self.label_nombre_lateral.setObjectName("nombreUsuarioLateral")
        self.label_nombre_lateral.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.label_nombre_lateral)

        layout.addSpacing(16)

        self.boton_archivo = QPushButton("Archivo")
        self.boton_archivo.setObjectName("botonNav")
        self.boton_archivo.clicked.connect(self.accion_simulada)
        layout.addWidget(self.boton_archivo)

        self.boton_edicion = QPushButton("Edición")
        self.boton_edicion.setObjectName("botonNav")
        self.boton_edicion.clicked.connect(self.accion_simulada)
        layout.addWidget(self.boton_edicion)

        self.boton_ver = QPushButton("Ver")
        self.boton_ver.setObjectName("botonNav")
        self.boton_ver.clicked.connect(self.accion_simulada)
        layout.addWidget(self.boton_ver)

        self.boton_settings = QPushButton("⚙  Settings")
        self.boton_settings.setObjectName("botonNav")
        self.boton_settings.setProperty("activo", "true")
        layout.addWidget(self.boton_settings)

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

        self.campo_nombre_usuario = QLineEdit()
        layout_tarjeta.addWidget(self.crear_campo("Nombre de usuario", self.campo_nombre_usuario))

        self.combo_tema = QComboBox()
        self.combo_tema.addItems(["Claro", "Oscuro"])
        layout_tarjeta.addWidget(self.crear_campo("Tema", self.combo_tema))

        self.combo_idioma = QComboBox()
        self.combo_idioma.addItems(["es", "es-ES", "en", "en-US"])
        layout_tarjeta.addWidget(self.crear_campo("Idioma", self.combo_idioma))

        self.spin_fuente = QSpinBox()
        self.spin_fuente.setRange(8, 32)
        layout_tarjeta.addWidget(self.crear_campo("Tamaño de fuente", self.spin_fuente))

        fila_colores = QHBoxLayout()
        fila_colores.setSpacing(20)

        self.boton_color_barra = QPushButton()
        self.boton_color_barra.setObjectName("botonColor")
        self.boton_color_barra.clicked.connect(self.elegir_color_barra)
        fila_colores.addLayout(self.crear_campo_color("Color de barra", self.boton_color_barra))

        self.boton_color_letra = QPushButton()
        self.boton_color_letra.setObjectName("botonColor")
        self.boton_color_letra.clicked.connect(self.elegir_color_letra)
        fila_colores.addLayout(self.crear_campo_color("Color de letra", self.boton_color_letra))

        layout_tarjeta.addLayout(fila_colores)

        boton_foto = QPushButton("Cambiar foto de perfil")
        boton_foto.setObjectName("botonCancelar")
        boton_foto.clicked.connect(self.elegir_foto)
        layout_tarjeta.addWidget(boton_foto, alignment=Qt.AlignmentFlag.AlignLeft)

        layout_tarjeta.addSpacing(10)

        fila_botones = QHBoxLayout()
        fila_botones.addStretch()

        boton_cancelar = QPushButton("Cancelar")
        boton_cancelar.setObjectName("botonCancelar")
        boton_cancelar.clicked.connect(self.cancelar_configuracion)
        fila_botones.addWidget(boton_cancelar)

        boton_guardar = QPushButton("Guardar cambios")
        boton_guardar.setObjectName("botonGuardar")
        boton_guardar.clicked.connect(self.guardar_configuracion)
        fila_botones.addWidget(boton_guardar)

        layout_tarjeta.addLayout(fila_botones)

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

    def crear_campo_color(self, etiqueta_texto, boton_color):
        layout = QVBoxLayout()
        layout.setSpacing(4)

        etiqueta = QLabel(etiqueta_texto)
        etiqueta.setProperty("etiquetaCampo", "true")

        layout.addWidget(etiqueta)
        layout.addWidget(boton_color)

        return layout

    def elegir_color_barra(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_barra_pendiente = color.name()
            self.boton_color_barra.setStyleSheet(f"background-color: {self.color_barra_pendiente};")

    def elegir_color_letra(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_letra_pendiente = color.name()
            self.boton_color_letra.setStyleSheet(f"background-color: {self.color_letra_pendiente};")

    def elegir_foto(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Seleccionar foto de perfil", "", "Imágenes (*.png *.jpg *.jpeg)")
        if ruta:
            self.foto_pendiente = ruta
            self.foto_perfil_label.setPixmap(QPixmap(ruta))

    def guardar_configuracion(self):
        self.config_actual["nombre_usuario"] = self.campo_nombre_usuario.text()
        self.config_actual["tema_interfaz"] = self.combo_tema.currentText()
        self.config_actual["idioma"] = self.combo_idioma.currentText()
        self.config_actual["tamaño_fuente"] = self.spin_fuente.value()

        if hasattr(self, "color_barra_pendiente"):
            self.config_actual["color_barra_menu"] = self.color_barra_pendiente
        if hasattr(self, "color_letra_pendiente"):
            self.config_actual["color_letra"] = self.color_letra_pendiente
        if hasattr(self, "foto_pendiente"):
            self.config_actual["foto_perfil"] = self.foto_pendiente

        try:
            guardar_configuracion_archivo(self.config_actual)
            self.aplicar_configuracion(self.config_actual)
            QMessageBox.information(self, "Aviso", "Configuración guardada correctamente.")
        except PermissionError:
            QMessageBox.critical(
                self,
                "Error al guardar",
                "No se tienen permisos para guardar la configuración. Los cambios no se guardaron en disco."
            )

    def cancelar_configuracion(self):
        for atributo in ("color_barra_pendiente", "color_letra_pendiente", "foto_pendiente"):
            if hasattr(self, atributo):
                delattr(self, atributo)

        self.aplicar_configuracion(self.config_actual)

    def aplicar_configuracion(self, configuracion):
        self.campo_nombre_usuario.setText(configuracion["nombre_usuario"])
        self.combo_tema.setCurrentText(configuracion["tema_interfaz"])
        self.combo_idioma.setCurrentText(configuracion["idioma"])
        self.spin_fuente.setValue(configuracion["tamaño_fuente"])
        self.label_nombre_lateral.setText(configuracion["nombre_usuario"])

        self.boton_color_barra.setStyleSheet(f"background-color: {configuracion['color_barra_menu']};")
        self.boton_color_letra.setStyleSheet(f"background-color: {configuracion['color_letra']};")

        if configuracion["foto_perfil"]:
            self.foto_perfil_label.setPixmap(QPixmap(configuracion["foto_perfil"]))
        else:
            self.foto_perfil_label.setPixmap(QPixmap())

        self.setStyleSheet(QSS_OSCURO if configuracion["tema_interfaz"] == "Oscuro" else QSS_CLARO)

        fuente_app = QFont()
        fuente_app.setPointSize(configuracion["tamaño_fuente"])
        self.setFont(fuente_app)

        for widget in self.findChildren(QWidget):
            widget.setFont(fuente_app)

        self.panel_lateral.setStyleSheet(
            f"background-color: {configuracion['color_barra_menu']};"
        )

        color_letra = configuracion["color_letra"]
        self.titulo_app.setStyleSheet(f"color: {color_letra}; font-weight: 700;")
        self.label_nombre_lateral.setStyleSheet(
            f"color: {color_letra}; font-weight: 600;"
        )

        for boton in (
            self.boton_archivo,
            self.boton_edicion,
            self.boton_ver,
            self.boton_settings
        ):
            boton.setStyleSheet(
                f"color: {color_letra}; text-align: left; "
                "padding: 10px 16px; border-radius: 8px; "
                "background-color: transparent;"
            )


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(aplicacion.exec())