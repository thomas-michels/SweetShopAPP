import flet as ft
from app.layouts.list_orders import ListOrder


class CandyApp(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Settings")
        ]

        self.appbar = ft.AppBar(
            leading=ft.Image(
                src=f"/svgs/cupcake-home.svg",
                width=40,
                color=ft.colors.WHITE
            ),
            leading_width=50,
            title=ft.Text(
                value="Minha Confeitaria",
                size=24,
                text_align="center",
                weight=ft.FontWeight.BOLD
            ),
            center_title=True,
            toolbar_height=75,
            bgcolor=ft.colors.PINK_200,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items,
                        icon=ft.icons.MENU
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar

        self.page.bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.colors.WHITE,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.Image( # HOME
                        src=f"/svgs/home.svg",
                        width=40,
                        color=ft.colors.PINK_200,
                        tooltip="Inicio",
                        visible=True
                    ),
                    ft.Image( # CARRINHO
                        src=f"/svgs/carrinho-de-compras.svg",
                        width=40,
                        color=ft.colors.BLACK
                    ),
                    ft.Image( # BOTAO DE MAIS
                        src=f"/svgs/adicionar.svg",
                        width=40,
                        color=ft.colors.BLACK
                    ),
                    ft.Image( # PEDIDOS
                        src=f"/svgs/recibo.svg",
                        width=40,
                        color=ft.colors.BLACK
                    ),
                    ft.Image( # USER
                        src=f"/svgs/user.svg",
                        width=40,
                        color=ft.colors.BLACK
                    ),
                ]
            ),
        )

        self.orders = ListOrder()

    def build(self):
        return self.orders
