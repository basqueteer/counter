import flet as ft

def main(page: ft.Page):
    page.title = "Multi-Page App Example"

    # 1. Define the function that handles route changes
    def route_change(route):
        page.views.clear() # Clear the current views stack
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Home Page"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Text("Welcome to the Home Page!"),
                    ft.ElevatedButton("Go to Page 2", on_click=lambda e: page.go("/page2")),
                ],
            )
        )
        if page.route == "/page2":
            page.views.append(
                ft.View(
                    "/page2",
                    [
                        ft.AppBar(title=ft.Text("Page 2"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Welcome to Page 2!"),
                        ft.ElevatedButton("Go Home", on_click=lambda e: page.go("/")),
                    ],
                )
            )
        page.update() # Update the page to reflect the changes

    # 2. Define the function that handles view popping (going back)
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1] # Get the previous view
        page.go(top_view.route) # Navigate to the previous view's route

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route) # Set the initial route

ft.app(target=main)