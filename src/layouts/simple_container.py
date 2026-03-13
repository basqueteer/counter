import flet as ft

def main(page: ft.Page):
    
    page.title = "Red container"

    c1 = ft.Container(
        content=ft.Text("Container with red background", color=ft.Colors.BLACK, size=42),
        bgcolor=ft.Colors.RED,
        padding=30,
    )
    page.add(c1)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

ft.run(main)