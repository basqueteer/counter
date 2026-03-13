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
            ft.dropdown.Option("C"),
            ft.dropdown.Option("C++"),
            ft.dropdown.Option("C#"),
            ft.dropdown.Option("Java"),
            ft.dropdown.Option("Rust"),
        ],
    )

    submit_btn = ft.Button("Submit", on_click=button_clicked)

    page.add(my_dropdown, submit_btn, output_text)

ft.run(main)