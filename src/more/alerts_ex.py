import flet as ft

def main(page: ft.Page):

    n = ft.TextField(label="Name")
    d = ft.AlertDialog(
        modal=True,
        title=ft.Text("Greeting"),
        content=ft.Text(""),
        alignment=ft.Alignment.CENTER,
        actions=[
            ft.TextButton("Yes", on_click=lambda e: page.pop_dialog()),
            ft.TextButton("No", on_click=lambda e: page.pop_dialog()),
        ],
        on_dismiss=lambda e: print("Dialog dismissed!"),
        title_padding=ft.Padding.all(25),
    )

    def show_message(e):
        if n.value.strip() == "":
            d.content = ft.Text("No name entered")
        else:
            d.content = ft.Text(f"Hello {n.value}")
        page.show_dialog(d)

    b = ft.Button("Submit", on_click=show_message)

    page.add(n, b)

ft.run(main)