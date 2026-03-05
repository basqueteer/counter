import flet as ft

def main(page: ft.Page):
    container1 = ft.Container(
        content=ft.Text("Container 1"),
        width=100,
        height=100,
        bgcolor=ft.Colors.BLUE,
        border_radius=ft.border_radius.all(5),
    )

    container2 = ft.Container(
        content=ft.Text("Container 2"),
        width=100,
        height=100,
        bgcolor=ft.Colors.BLUE,
        border_radius=ft.border_radius.all(5),
    )

    column = ft.Column(spacing=40, controls=(container1, container2))
    
    page.add(ft.Column([ ft.Text("Containers in a row:")]), column)

ft.app(target=main)