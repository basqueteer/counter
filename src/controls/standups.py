import flet as ft
import asyncio

async def main(page: ft.Page):
    t = ft.Text("Time: 0", color=ft.Colors.GREEN, size=24)

    task = ft.TextField(hint_text="Task...", width=250)
    tasks = ft.Column()

    async def start(e):
        for i in range(20):
            t.value = f"Time: {i}"
            page.update()
            await asyncio.sleep(1)

        t.value = "Time's up!"
        t.color = ft.Colors.RED
        page.update()

    def add_task(e):
        text = (task.value or "").strip()
        if text:
            tasks.controls.append(ft.Checkbox(label=text))
            task.value = ""
            page.update()

    page.add(
        ft.Column(
            [
                ft.Row([t], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.ElevatedButton("Start timer", on_click=start)],
                       alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([task, ft.ElevatedButton("Add task", on_click=add_task)],
                       alignment=ft.MainAxisAlignment.CENTER),
                tasks,
            ],
            spacing=10,
        )
    )

ft.run(main)