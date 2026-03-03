import flet as ft

def main(page: ft.Page):
    page.title = "Login App"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    username = ft.TextField(label="Username", width=300)
    password = ft.TextField(label="Password", password=True, width=300)
    message = ft.Text()

    def login_click(e):
        if username.value == "admin" and password.value == "1234":
            message.value = "Login successful!"
            message.color = ft.Colors.GREEN
        else:
            message.value = "Invalid username or password"
            message.color = ft.Colors.RED
        page.update()

    page.add(
        ft.Container(
            width=350,
            padding=30,
            border_radius=10,
            bgcolor=ft.Colors.BLACK_54,  # fixed deprecation
            content=ft.Column(
                controls=[
                    ft.Text("PaaScual", size=30, weight=ft.FontWeight.BOLD),
                    username,
                    password,
                    ft.Button(  # new API
                        content=ft.Text("Login"),
                        width=300,
                        on_click=login_click,
                    ),
                    message,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            ),
        )
    )

ft.run(main)