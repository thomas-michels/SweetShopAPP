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
        self.tf_user_name = ft.Text(value=self.user_name)
        self.tf_tag = ft.Text(value=self.tag)
        self.tf_status = ft.Text(value=self.status)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.tf_user_name,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.AIRPLANE_TICKET,
                            tooltip="Editar",
                        ),
                    ],
                ),
            ],
        )

        # self.edit_view = ft.Row(
        #     visible=False,
        #     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        #     vertical_alignment=ft.CrossAxisAlignment.CENTER,
        #     controls=[
        #         self.edit_name,
        #         ft.IconButton(
        #             icon=ft.icons.DONE_OUTLINE_OUTLINED,
        #             icon_color=ft.colors.GREEN,
        #             tooltip="Update To-Do",
        #             on_click=self.save_clicked,
        #         ),
        #     ],
        # )
        return ft.Column(controls=[self.display_view])
