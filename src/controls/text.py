import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello IE!", color=ft.Colors.GREEN)
    page.controls.append(t)
    page.update()

ft.run(main)