import flet as ft
import pandas as pd

URL = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

iris_df = pd.read_csv(URL)
rows_list = []
for row in iris_df.iterrows():
    rows_list.append(
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(row[1][0]))),
                ft.DataCell(ft.Text(str(row[1][1]))),
                ft.DataCell(ft.Text(str(row[1][2]))),
                ft.DataCell(ft.Text(str(row[1][3]))),
                ft.DataCell(ft.Text(str(row[1][4]))),
            ],
        )
    )

def main(page: ft.Page):

    page.title = "IRIS"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(n)) for n in iris_df.columns
            ],
            rows=[
                *rows_list,
            ],
        ),
    )

ft.run(main)