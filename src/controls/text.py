import flet as ft
import asyncio

max_time = 10

async def main(page: ft.Page):
    for i in range(max_time, 0, -1):
        t = ft.Text(value=f"Bomb in {i} seconds", color=ft.Colors.GREEN)
        page.controls.append(t)
        page.update()
        await asyncio.sleep(1)
        page.controls.remove(t)
        page.update()
    t = ft.Text(value=f"BOOOOM!", color=ft.Colors.RED)
    page.controls.append(t)
    page.update()

ft.run(main)