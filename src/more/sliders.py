import flet as ft

def main(page):

    def slider1_changed(e):
        txt1.value = f"Slider changed to {e.control.value}"
        page.update()

    def slider2_changed(e):
        txt2.value = f"Slider changed to {e.control.value}"
        page.update()

    txt1 = ft.Text()
    txt2 = ft.Text()

    page.add(
        ft.Text("Basic slider:"),
        ft.Slider(min=0, max=100, on_change=slider1_changed),
        txt1,
        ft.Text("Slider with values:"),
        ft.Slider(min=0, max=100, divisions=10, label="{value}%", on_change=slider2_changed),
        txt2)

ft.run(main)