import flet as ft

def main(page: ft.Page):
    page.title = "Login app"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def login_click(e):
        print("Login button clicked")

    page.add(
        ft.Container(
            #width=300,
            #padding=20,
            #bgcolor=ft.Colors.WHITE,
            #border_radius=ft.BorderRadius.all(10),
            content=ft.Column(
                controls=[
                    ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
                    ft.TextField(label="Username"),
                    ft.TextField(label="Password", password=True),
                    ft.ElevatedButton(text="Login", on_click=login_click),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
    )