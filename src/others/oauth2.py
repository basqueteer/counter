import os
import flet as ft
from flet.auth.providers import GitHubOAuthProvider
import asyncio

GITHUB_CLIENT_ID = "Ov23licvKPfuV0PPLl7w"
GITHUB_CLIENT_SECRET = "3ab24cd97d43acaca77e66c44dad9c5b37d26308"

async def main(page: ft.Page):
    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url="http://localhost:8888/api/oauth/redirect",
    )

    async def login_click(e):
        await page.login(provider)

    def on_login(e):
        print("Login error:", e.error)
        print("Access token:", page.auth.token.access_token)
        print("User ID:", page.auth.user.id)

    page.on_login = on_login
    page.add(ft.Button("Login with GitHub", on_click=login_click))

ft.run(main)