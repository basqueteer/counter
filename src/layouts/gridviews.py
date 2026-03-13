import flet as ft

def main(page: ft.Page):
    page.title = "GridView"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.update()

    images = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=200,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    page.add(images)

    for i in range(0, 600):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/300/300?{i}",
                fit=ft.BoxFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()

ft.run(main)