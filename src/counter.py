import flet as ft

def main(page: ft.Page):
    counter = ft.Text("0", size=100, data=0)

    def reset(e):
        counter.data = 0
        counter.value = str(counter.data)
        page.update()

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        page.update()

    def decrease_click(e):
        counter.data -= 1
        counter.value = str(counter.data)
        page.update()

    page.floating_action_button = ft.Row(
        [
            ft.FloatingActionButton(
                icon=ft.Icons.REMOVE,
                on_click=decrease_click,
            ),
            ft.FloatingActionButton(
                icon=ft.Icons.REFRESH,
                on_click=reset,
            ),
            ft.FloatingActionButton(
                icon=ft.Icons.ADD,
                on_click=increment_click,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=counter,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


ft.run(main)
