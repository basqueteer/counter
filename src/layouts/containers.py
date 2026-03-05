import flet as ft

def main(page: ft.Page):
    page.title = "Containers with different background colours"

    c1 = ft.Container(
        content=ft.Button(content="Elevated Button inside Container"),
        bgcolor=ft.Colors.YELLOW,
        padding=10,
    )

    c2 = ft.Container(
        content=ft.Button(
            content="Elevated Button with 0.5 opacity inside Container", 
            opacity=0.5
        ),
        bgcolor=ft.Colors.GREEN,
        padding=10,
    )

    c3 = ft.Container(
        content=ft.OutlinedButton(content="Outlined Button inside Container"),
        bgcolor=ft.Colors.BLUE,
        padding=10,
        margin=20,
    )
    page.add(c1, c2, c3)


ft.run(main)