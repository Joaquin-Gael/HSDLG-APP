import flet as ft

# Definir el estilo del botón con diferentes estados (hover, default, etc.)
SDLGStyle = ft.ButtonStyle(
    color={
        ft.ControlState.HOVERED: ft.colors.BLACK,   # Color del texto en hover
        ft.ControlState.DEFAULT: ft.colors.WHITE,   # Color del texto por defecto
    },
    bgcolor={
        ft.ControlState.HOVERED: ft.colors.WHITE12,  # Color de fondo en hover
        ft.ControlState.DEFAULT: ft.colors.BLACK12,     # Color de fondo por defecto
    },
    padding={
        ft.ControlState.HOVERED: 20                  # Padding aumentado en hover
    },
    side={
        ft.ControlState.HOVERED: ft.BorderSide(2, ft.colors.BLACK12),   # Borde azul por defecto
        ft.ControlState.DEFAULT: ft.BorderSide(2, ft.colors.WHITE54),    # Borde rojo en hover
    },
    shape={
        ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=1),  # Bordes redondeados en hover
        ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=1),   # Bordes menos redondeados por defecto
    },
    elevation={
        "pressed": 0,  # Sin sombra cuando se presiona
        "": 1,         # Sombra pequeña por defecto
    },
    animation_duration=500,  # Duración de la animación
    overlay_color=ft.colors.TRANSPARENT,  # Color de superposición
)

class SDLGButton(ft.ElevatedButton):
    def __init__(self, text="Button", on_click=None):
        # Aplicar el estilo definido con diferentes estados
        super().__init__(
            text=text,
            style=SDLGStyle,
            color=ft.colors.WHITE,
            on_click=on_click
        )
