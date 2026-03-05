import flet as ft

def main(page: ft.Page):
    # Set page title, window width and window height
    page.title = "My app"
    page.window_width = 300
    page.window_height = 300

    # Center content vertically and horizontally
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    t = ft.Text(value="Hello IE!", color="green")
    page.controls.append(t)
    page.update()

ft.run(main)