import flet as ft
from app.pages.home import CandyApp


async def home_page(page: ft.Page):
    page.title = "Candy APP"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 24
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.GREY_200

    await page.add_async(CandyApp())


ft.app(
    target=home_page,
    view=ft.WEB_BROWSER, port=4200,
    assets_dir="./app/assets",
)
