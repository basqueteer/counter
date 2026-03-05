import flet as ft
import asyncio

async def main(page: ft.Page):
    t = ft.Text("Time: 0", color=ft.Colors.GREEN)
    page.add(t)

    for i in range(11):
        t.value = f"Time: {i}"
        page.update()
        await asyncio.sleep(1)

    t.value = "Time's up!"
    page.update()

ft.run(main)