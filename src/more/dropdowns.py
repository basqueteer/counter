import flet as ft

def main(page: ft.Page):
    output_text = ft.Text()

    def button_clicked(e):
        output_text.value = f"Selected value is: {my_dropdown.value}"
        page.update()

    my_dropdown = ft.Dropdown(
        label="Programming language",
        hint_text="Choose your favourite language",
        options=[
            ft.dropdown.Option("Python"),
            ft.dropdown.Option("JavaScript"),
        ],
    )

    submit_btn = ft.Button("Submit", on_click=button_clicked)

    page.add(output_text, my_dropdown, submit_btn)

ft.run(main)