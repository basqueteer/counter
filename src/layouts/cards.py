
import flet as ft

def main(page):
    page.title = "Cards"
    page.add(
        ft.Card(
            shadow_color=ft.Colors.ON_SURFACE_VARIANT,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            bgcolor=ft.Colors.GREY_400,
                            leading=ft.Icon(ft.Icons.ONDEMAND_VIDEO),
                            title=ft.Text("Flet Crash Course"),
                            subtitle=ft.Text(
                                "Learn how to code in FLET with Python."
                            ),
                        ),
                        ft.Row(
                            controls = [
                                ft.TextButton("Start course"), 
                                ft.TextButton("More info")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )

ft.run(main)