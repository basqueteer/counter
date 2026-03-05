import flet as ft

def main(page: ft.Page):
    page.title = "Containers"
    # Center content vertically and horizontally
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("Non-clickable container"),
                    margin=10,
                    padding=10,
                    bgcolor=ft.Colors.RED_500,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Clickable container without Ink (ripple)"),
                    margin=10,
                    padding=10,
                    bgcolor=ft.Colors.GREEN_400,
                    width=150,
                    height=150,
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink was clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Clickable container with Ink (ripple)"),
                    margin=10,
                    padding=10,
                    bgcolor=ft.Colors.BLUE_400,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink was clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Transparent clickable container with Ink"),
                    margin=10,
                    padding=10,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Transparent clickable container with Ink clicked!"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

ft.run(main)