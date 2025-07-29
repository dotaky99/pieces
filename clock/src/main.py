import flet as ft
import datetime
import asyncio

async def main(page: ft.Page):
    page.title = "카드형 시계"
    page.window_resizable = False
    page.window_bgcolor = "#F0F0F0"
    page.bgcolor = "#F0F0F0"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # 카드 크기 설정
    card_width = 300
    card_height = 160
    padding = 20  # 카드 패딩

    # 페이지 창 크기를 카드 크기에 맞춤
    page.window.width = card_width + padding
    page.window.height = card_height + padding + 40  # 약간 여유 추가

    date_text = ft.Text(
        value="",
        size=30,
        weight=ft.FontWeight.W_400,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER
    )

    time_text = ft.Text(
        value="",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_900,
        text_align=ft.TextAlign.CENTER
    )

    # 카드형 컨테이너
    card = ft.Container(
        content=ft.Column(
            controls=[date_text, time_text],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        padding=padding,
        width=card_width,
        height=card_height,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=12,
            color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
            offset=ft.Offset(0, 4)
        )
    )

    page.add(card)

    # 시계 갱신
    def update_clock():
        now = datetime.datetime.now()
        date_text.value = now.strftime("%Y-%m-%d")
        time_text.value = now.strftime("%H:%M:%S")
        page.update()

    # 1초마다 반복 실행
    async def clock_task():
        while True:
            update_clock()
            await asyncio.sleep(1)

    page.run_task(clock_task)

ft.app(target=main)
