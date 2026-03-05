import flet as ft

def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 400
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Joe")),
                        ft.DataCell(ft.Text("Bloggs")),
                        ft.DataCell(ft.Text("30")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("21")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Harry")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("42")),
                    ],
                ),
            ],
        ),
    )

ft.run(main)