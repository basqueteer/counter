import flet as ft
import asyncio

async def main(page: ft.Page):
    for i in range(20):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        await asyncio.sleep(2)

ft.run(main)