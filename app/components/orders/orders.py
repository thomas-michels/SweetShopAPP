import flet as ft
from typing import List


class Order(ft.UserControl):

    def __init__(
        self, status: str, user_name: str, items: List[dict], tag: str, price: float
    ):
        super().__init__()
        self.status = status
        self.user_name = user_name
        self.items = items
        self.tag = tag
        self.price = price

    def build(self):

        self.display_view = ft.Container(
            content=ft.Column(
                spacing=1,
                controls=[
                    self.__get_header(),
                    self.__mount_items(),
                    ft.Divider(height=2, color=ft.colors.GREY_200),
                ]
            )
        )

        return self.display_view

    def __get_header(self):
        self.tf_user_name = ft.Text(
            value=self.user_name,
            size=18,
            weight=ft.FontWeight.BOLD,
            max_lines=1
        )

        self.tf_tag = ft.Text(
            value=self.tag,
            size=10,
            tooltip="Tag",
            max_lines=1
        )

        self.tf_status = ft.Text(
            value=self.status,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREEN_300,
            tooltip="Status do pedido",
            max_lines=1,
        )

        return ft.Row(
            controls=[
                self.tf_user_name,
                self.tf_tag,
                self.tf_status,
                self.__get_popup_menu(),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

    def __get_popup_menu(self) -> ft.PopupMenuButton:
        return ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Alterar Status", icon=ft.icons.ADJUST_SHARP),
                ft.PopupMenuItem(text="Editar", icon=ft.icons.EDIT),
                ft.PopupMenuItem(text="Excluir", icon=ft.icons.CLEAR),
            ]
        )

    def __mount_items(self) -> ft.Column:
        items = []

        for item in self.items:
            items.append(ft.Row(
                controls=[
                    ft.Text(
                        value=f"{item['quantity']}x",
                        color=ft.colors.GREY_500,
                        size=12,
                        max_lines=1
                    ),
                    ft.Text(
                        value=item['name'].capitalize(),
                        color=ft.colors.GREY_500,
                        size=12,
                        max_lines=1
                    )
                ],
                spacing=4
            ))

        return ft.Column(controls=items)
