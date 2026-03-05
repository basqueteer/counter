
import flet as ft

def main(page):
    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greeting = ft.Text()

    def btn_click(e):
        greeting.value = f"Welcome, {first_name.value} {last_name.value}!"
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.Button(content="Get started", on_click=btn_click),
        greeting,
    )

ft.run(main)