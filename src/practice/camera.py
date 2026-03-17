import flet as ft
import flet_camera as fc
# import flet_permission_handler as fph

# -----------------------------------------------------------------------------
# Demo app inspired by the screenshots provided by the user.
# Goal: show a clean way to build a small Flet app with:
#   1) route-based navigation
#   2) a bottom NavigationBar
#   3) reusable UI helpers
#   4) code written to study and extend later
# -----------------------------------------------------------------------------

ACCENT = "#CC5500"
BACKGROUND = "#F3F3F3"
CARD_BG = ft.Colors.WHITE
TEXT_MAIN = "#333333"
TEXT_SOFT = "#6E6E6E"

TAB_ROUTES = ["/clave", "/gestiones", "/ayuda", "/ajustes"]
TAB_LABELS = {
    "/clave": "Cl@ve",
    "/gestiones": "Gestiones",
    "/ayuda": "Ayuda",
    "/ajustes": "Ajustes",
}


def main(page: ft.Page):
    # -------------------------
    # Global page configuration
    # -------------------------
    page.title = "Cl@ve"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = BACKGROUND
    page.padding = 0
    page.window.width = 390
    page.window.height = 844
    page.window.resizable = True


    qr_photo_bytes = None

    camera_status = ft.Text("Waiting...", color=ft.Colors.WHITE, size=12)

    camera_preview = fc.Camera(
        expand=True,
        preview_enabled=True,
        content=ft.Container(
            bgcolor=ft.Colors.BLACK,
            alignment=ft.Alignment.CENTER,
            content=ft.ProgressRing(color=ft.Colors.WHITE),
        ),
    )

    async def on_camera_state_change(e: fc.CameraStateEvent):
        if e.has_error:
            camera_status.value = f"Camera error: {e.error_description}"
        elif e.is_taking_picture:
            camera_status.value = "Taking picture..."
        elif e.is_preview_paused:
            camera_status.value = "Preview paused"
        else:
            camera_status.value = "Camera ready"
        page.update()

    camera_preview.on_state_change = on_camera_state_change

    async def close_camera_dialog(e=None):
        page.pop_dialog()
        page.update()

    async def take_qr_photo(e):
        nonlocal qr_photo_bytes
        qr_photo_bytes = await camera_preview.take_picture()
        page.pop_dialog()
        page.update()
        show_message("Photo captured correctly.")

    async def open_camera_dialog(e):
        camera_status.value = "Opening camera..."

        camera_dialog = ft.AlertDialog(
            modal=True,
            content_padding=0,
            inset_padding=ft.padding.all(12),
            content=ft.Container(
                width=340,
                height=460,
                bgcolor=ft.Colors.BLACK,
                content=ft.Stack(
                    expand=True,
                    controls=[
                        camera_preview,
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            padding=10,
                            content=camera_status,
                        ),
                    ],
                ),
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_camera_dialog),
                ft.TextButton("Tomar foto", on_click=take_qr_photo),
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        page.show_dialog(camera_dialog)
        page.update()

        try:
            cameras = await camera_preview.get_available_cameras()
            print("Available cameras:", cameras)

            if not cameras:
                page.pop_dialog()
                page.update()
                show_message("No camera found on this device.")
                return

            camera_status.value = f"Initializing {cameras[0].name}..."
            page.update()

            await camera_preview.initialize(
                description=cameras[0],
                resolution_preset=fc.ResolutionPreset.MEDIUM,
                enable_audio=False,
            )

        except Exception as ex:
            camera_status.value = f"Init error: {ex}"
            page.update()
            print("Camera init error:", ex)

    def show_message(message: str):
        page.snack_bar = ft.SnackBar(ft.Text(message), open=True)
        page.update()

    def go_to_tab(index: int):
        page.go(TAB_ROUTES[index])

    def on_nav_change(e: ft.ControlEvent):
        # selected_index comes from NavigationBar
        go_to_tab(e.control.selected_index)

    def nav_bar(current_route: str) -> ft.NavigationBar:
        selected_index = TAB_ROUTES.index(current_route)
        return ft.NavigationBar(
            selected_index=selected_index,
            indicator_color=ft.Colors.with_opacity(0.10, ACCENT),
            label_behavior=ft.NavigationBarLabelBehavior.ALWAYS_SHOW,
            on_change=on_nav_change,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.LOCK_OUTLINE,
                    selected_icon=ft.Icons.LOCK,
                    label="Cl@ve",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.EDIT_NOTE_OUTLINED,
                    selected_icon=ft.Icons.EDIT_NOTE,
                    label="Gestiones",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.HELP_OUTLINE,
                    selected_icon=ft.Icons.HELP,
                    label="Ayuda",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icons.SETTINGS,
                    label="Ajustes",
                ),
            ],
        )

    def brand_title(text: str) -> ft.Row:
        return ft.Row(
            spacing=8,
            controls=[
                ft.Icon(ft.Icons.ADB, color=ACCENT, size=22),
                ft.Text(text, size=18, weight=ft.FontWeight.W_500, color=ACCENT),
            ],
        )

    def build_appbar(route: str) -> ft.AppBar:
        actions = []
        if route == "/clave":
            actions = [
                ft.IconButton(
                    icon=ft.Icons.REFRESH,
                    icon_color=ACCENT,
                    on_click=lambda _: show_message("Refreshing demo screen..."),
                ),
                ft.IconButton(
                    icon=ft.Icons.PERSON_OUTLINE,
                    icon_color=ACCENT,
                    on_click=lambda _: show_message("User profile placeholder."),
                ),
            ]

        return ft.AppBar(
            title=brand_title(TAB_LABELS[route]),
            bgcolor=BACKGROUND,
            center_title=False,
            elevation=0,
            actions=actions,
        )

    def icon_badge(icon_name, size: int = 26) -> ft.Container:
        return ft.Container(
            width=48,
            height=48,
            border_radius=14,
            bgcolor=ft.Colors.with_opacity(0.08, ACCENT),
            alignment=ft.Alignment.CENTER,
            content=ft.Icon(icon_name, color=ACCENT, size=size),
        )

    def trailing_icon(icon_name):
        return ft.Icon(icon_name, color=ACCENT, size=22)

    def menu_card(
        title: str,
        icon_name,
        subtitle: str | None = None,
        trailing=None,
        on_click=None,
    ) -> ft.Card:
        return ft.Card(
            margin=ft.margin.only(bottom=14),
            elevation=2,
            bgcolor=CARD_BG,
            shape=ft.RoundedRectangleBorder(radius=18),
            content=ft.Container(
                padding=6,
                content=ft.ListTile(
                    leading=icon_badge(icon_name),
                    title=ft.Text(
                        title,
                        size=16,
                        weight=ft.FontWeight.W_500,
                        color=ACCENT,
                    ),
                    subtitle=ft.Text(subtitle, color=TEXT_SOFT) if subtitle else None,
                    trailing=trailing,
                    min_height=72,
                    on_click=on_click,
                ),
            ),
        )

    def section_container(*controls: ft.Control) -> ft.Container:
        return ft.Container(
            padding=ft.padding.symmetric(horizontal=16, vertical=10),
            content=ft.ListView(
                expand=True,
                spacing=0,
                controls=list(controls),
            ),
            expand=True,
        )

    # -------------------------
    # Screen builders
    # -------------------------
    def build_clave_screen() -> ft.Control:
        logo_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
            controls=[
                # ft.Text("cl", size=34, weight=ft.FontWeight.W_500, color=TEXT_MAIN),
                # ft.Container(
                #     width=48,
                #     height=48,
                #     border_radius=12,
                #     bgcolor=ft.Colors.with_opacity(0.10, ACCENT),
                #     alignment=ft.Alignment.CENTER,
                #     content=ft.Icon(ft.Icons.ADB, color=ACCENT, size=28),
                # ),
                # ft.Text("ve", size=34, weight=ft.FontWeight.W_500, color=TEXT_MAIN),
                ft.Text("cl@ve", size=34, weight=ft.FontWeight.W_500, color=TEXT_MAIN),
                ft.Text("móvil", size=18, color=TEXT_SOFT),
            ],
        )

        main_card = ft.Card(
            elevation=2,
            margin=ft.margin.only(top=10, bottom=12),
            bgcolor=CARD_BG,
            shape=ft.RoundedRectangleBorder(radius=20),
            content=ft.Container(
                padding=24,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        logo_row,
                        ft.TextButton(
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=6,
                                controls=[
                                    ft.Text("¿Cómo funciona?", color=ACCENT),
                                    ft.Icon(ft.Icons.OPEN_IN_NEW, color=ACCENT, size=18),
                                ],
                            ),
                            on_click=lambda _: show_message(
                                "This would open a help page or tutorial."
                            ),
                        ),
                        ft.FilledButton(
                            content="ESCANEAR CÓDIGO QR",
                            width=320,
                            height=52,
                            style=ft.ButtonStyle(
                                bgcolor=ACCENT,
                                color=ft.Colors.WHITE,
                                shape=ft.RoundedRectangleBorder(radius=28),
                            ),
                            on_click=open_camera_dialog,
                        ),
                    ],
                ),
            ),
        )

        return section_container(main_card)

    def build_gestiones_screen() -> ft.Control:
        return section_container(
            menu_card(
                title="Iniciar sesión",
                icon_name=ft.Icons.LOGIN,
                on_click=lambda _: show_message("Login flow placeholder."),
            ),
            menu_card(
                title="Mis datos en Cl@ve",
                icon_name=ft.Icons.BADGE_OUTLINED,
                on_click=lambda _: show_message("Personal data screen placeholder."),
            ),
            menu_card(
                title="Cl@ve permanente",
                icon_name=ft.Icons.PASSWORD,
                trailing=trailing_icon(ft.Icons.HELP_OUTLINE),
                on_click=lambda _: show_message("Permanent password flow placeholder."),
            ),
            menu_card(
                title="Revocar el certificado de Cl@ve Firma",
                icon_name=ft.Icons.CANCEL_OUTLINED,
                trailing=trailing_icon(ft.Icons.HELP_OUTLINE),
                on_click=lambda _: show_message("Certificate revoke flow placeholder."),
            ),
        )

    def build_ayuda_screen() -> ft.Control:
        return section_container(
            menu_card(
                title="Contacta con nosotros",
                icon_name=ft.Icons.SUPPORT_AGENT,
                on_click=lambda _: show_message("Contact form placeholder."),
            ),
            menu_card(
                title="Ayuda sobre la APP Cl@ve",
                icon_name=ft.Icons.HELP_CENTER_OUTLINED,
                on_click=lambda _: show_message("App help placeholder."),
            ),
            menu_card(
                title="Conoce Cl@ve",
                icon_name=ft.Icons.INFO_OUTLINE,
                on_click=lambda _: show_message("About Cl@ve placeholder."),
            ),
        )

    def build_ajustes_screen() -> ft.Control:
        return section_container(
            menu_card(
                title="Idioma de la APP",
                icon_name=ft.Icons.LANGUAGE,
                on_click=lambda _: show_message("Language selection placeholder."),
            ),
            menu_card(
                title="Notificaciones push",
                icon_name=ft.Icons.NOTIFICATIONS_NONE,
                trailing=trailing_icon(ft.Icons.OPEN_IN_NEW),
                on_click=lambda _: show_message("Push settings placeholder."),
            ),
            menu_card(
                title="Condiciones y políticas",
                icon_name=ft.Icons.POLICY_OUTLINED,
                on_click=lambda _: show_message("Policies screen placeholder."),
            ),
            menu_card(
                title="Acerca de la APP Cl@ve",
                icon_name=ft.Icons.INFO_OUTLINE,
                on_click=lambda _: show_message("About app placeholder."),
            ),
            menu_card(
                title="Salir",
                icon_name=ft.Icons.LOGOUT,
                on_click=lambda _: show_message("Exit action placeholder."),
            ),
        )

    def build_view(route: str) -> ft.View:
        if route == "/gestiones":
            content = build_gestiones_screen()
        elif route == "/ayuda":
            content = build_ayuda_screen()
        elif route == "/ajustes":
            content = build_ajustes_screen()
        else:
            route = "/clave"
            content = build_clave_screen()

        return ft.View(
            route=route,
            bgcolor=BACKGROUND,
            appbar=build_appbar(route),
            navigation_bar=nav_bar(route),
            controls=[content],
            padding=0,
            spacing=0,
        )

    # -------------------------
    # Routing: the heart of SPA navigation in Flet
    # -------------------------
    def route_change(e: ft.RouteChangeEvent):
        current_route = e.route if e.route in TAB_ROUTES else "/clave"

        # Single source of truth:
        # views are rebuilt entirely from the active route.
        page.views.clear()
        page.views.append(build_view(current_route))
        page.update()

    def view_pop(e: ft.ViewPopEvent):
        # For this app all screens are top-level tabs, so when a view is popped
        # we simply go back to the last known top-level route.
        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)
        else:
            page.go("/clave")

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Start on a valid route.
    page.go(page.route if page.route in TAB_ROUTES else "/clave")


if __name__ == "__main__":
    ft.app(target=main)