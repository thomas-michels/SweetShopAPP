import flet as ft


class NewOrder(ft.UserControl):

    def __init__(self, new_order_function) -> None:
        super().__init__()
        self.new_order_function = new_order_function

    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                height=64,
                controls=[
                    ft.Icon(
                        name=ft.icons.WAVING_HAND_ROUNDED,
                        size=48,
                        color=ft.colors.PINK_200
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(
                                value="Olá Nathália!",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                value="O que vamos preparar hoje?",
                                color=ft.colors.GREY_500
                            ),
                        ],
                        alignment=ft.alignment.center_left,
                    ),
                    ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ADD,
                                icon_size=48,
                                on_click=self.new_order_function,
                                tooltip="Criar novo pedido",
                                height=48,
                                width=48
                            ),
                        ],
                        alignment=ft.alignment.center_right,
                    ),
                ],
            ),
            bgcolor=ft.colors.WHITE,
            padding=16,
            alignment=ft.alignment.center,
            border_radius=16,
            border=ft.border.only(bottom=ft.border.BorderSide(width=2, color=ft.colors.GREY_500))
        )
