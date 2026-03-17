import flet as ft

def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    d = ft.Dropdown(
                options=[
                    ft.dropdown.Option("Python"),
                    ft.dropdown.Option("Javascript"),])
    r = ft.RadioGroup(
                content=ft.Row(
                    [
                        ft.Radio(value="Beginner", label="Beginner"),
                        ft.Radio(value="Intermediate", label="Intermediate"),
                    ]
                )
            )

    f = ft.Row(controls=[d,r,])

    def handle_banner_close(e: ft.Event[ft.TextButton]):
        page.pop_dialog()

    action_button_style = ft.ButtonStyle(color=ft.Colors.BLUE)
    b = ft.Banner(
        bgcolor=ft.Colors.AMBER_100,
        leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
        content=ft.Text(
            value="Please complete all selections",
            color=ft.Colors.BLACK,
        ),
        actions=[
            ft.TextButton(
                content="Close",
                style=action_button_style,
                on_click=handle_banner_close,
                data="close",
            ),
        ],
    )

    def show_message(e):
        if d.value == "" and r.value == "":
            b.content = ft.Text("No value entered")
        else:
            b.content = ft.Text(f"[{d.value}, {r.value}]")
        page.show_dialog(b)

    t = ft.Button("Show Banner", on_click=show_message)
    page.add(f, t, b)


ft.run(main)