import flet as ft

def main(page: ft.Page):
    output_text = ft.Text()

    def button_clicked(e):
        output_text.value = f"Selected value is: {language_radio.value}"
        page.update()

    language_radio = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value="Python", label="Python"),
                ft.Radio(value="JavaScript", label="JavaScript"),
                ft.Radio(value="C", label="C"),
                ft.Radio(value="C++", label="C++"),
                ft.Radio(value="C#", label="C#"),
                ft.Radio(value="Java", label="Java"),
                ft.Radio(value="Rust", label="Rust"),
            ]
        )
    )

    submit_btn = ft.ElevatedButton("Submit", on_click=button_clicked)

    page.add(
        ft.Text("Programming language"),
        language_radio,
        submit_btn,
        output_text,
    )

ft.run(main)