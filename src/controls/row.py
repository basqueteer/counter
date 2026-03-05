import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text("1"),
            ft.Text("2"),
            ft.Text("3"),
            ft.Text("4"),
            ft.Text("5"),
        ])
    )

ft.run(main)