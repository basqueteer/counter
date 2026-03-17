import flet as ft

def main(page: ft.Page):
    output_text = ft.Text()

    def button_clicked(e):
        output_text.value = f"Selected value is: {language_radio.value}"
        page.update()

    language_radio = ft.RadioGroup(
        content=ft.Row(
            [
                ft.Radio(value="Python", label="Python"),
                ft.Radio(value="JavaScript", label="JavaScript"),
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