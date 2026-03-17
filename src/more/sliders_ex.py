import flet as ft

def main(page):

    def slider1_changed(e):
        #txt1.value = f"Slider changed to {e.control.value}"
        if int(e.control.value) >= 3:
            page.bgcolor = ft.Colors.RED
            txt1.value = "Danger!"
        else:
            page.bgcolor = ft.Colors.WHITE 
            txt1.value = "Normal"
        page.update()

    txt1 = ft.Text()

    page.add(
        ft.Text(""),
        ft.Slider(min=0, max=5, divisions=5, label="{value}%", on_change=slider1_changed),
        txt1)

ft.run(main)