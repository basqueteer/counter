import flet as ft

def main(page: ft.Page):
    page.title = "Buttons demo"

    msg = ft.Text(value="Ready.", color="green")

    def on_click(e: ft.ControlEvent):
        msg.value = "Hello IE!"
        page.update()

    b = ft.Button(content="Press here", on_click=on_click)

    page.controls.append(msg)
    page.controls.append(b)
    page.update()

ft.run(main)