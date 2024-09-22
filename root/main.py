import flet as ft
from flet import canvas as cv
from storage import Storage, StorageError
from components.buttons import SDLGButton

async def main(page: ft.Page):
    storage = Storage()
    page.adaptive = True
    page.window.height = 1230
    page.window.width = 520
    page.scroll = ft.ScrollMode.HIDDEN
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)

    page.appbar = ft.AppBar(
        leading=cv.Canvas(
                [
                cv.Path(
                    [
                        cv.Path.MoveTo(25, 25),
                        cv.Path.LineTo(105, 25),
                        cv.Path.LineTo(25, 105),
                    ],
                    paint=ft.Paint(
                        style=ft.PaintingStyle.FILL,
                    ),
                ),
                cv.Path(
                    [
                        cv.Path.MoveTo(125, 125),
                        cv.Path.LineTo(125, 45),
                        cv.Path.LineTo(45, 125),
                        cv.Path.Close(),
                    ],
                    paint=ft.Paint(
                        stroke_width=2,
                        style=ft.PaintingStyle.STROKE,
                    ),
                ),
            ],
            width=float("inf"),
            expand=True,
        ),
        title=ft.Text("Hospital-SDLG"),
        actions=[
            ft.CircleAvatar(
                content=ft.Text('SC')
            )
        ],
        bgcolor=ft.colors.with_opacity(0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.EXPLORE_OUTLINED,
                selected_icon=ft.icons.EXPLORE,
                label="Explore"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.CONTACT_EMERGENCY_OUTLINED, 
                selected_icon=ft.icons.CONTACT_EMERGENCY,
                label="Emergency"
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Bookmark",
            ),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0)
        ),
    )

    async def add_storage(e):
        try:
            storage.set(input_key.value, input_value.value)
            page.add(ft.Checkbox(label=storage.search(input_key.value)))
        except StorageError as e:
            print('Error: {}\nData: {}'.format(e.__class__, e.args))
            dialog = ft.AlertDialog(
                title=ft.Text(
                    'Error'
                ),
                content=ft.Text(e),
                    actions=[
                    ft.TextButton("OK", on_click=lambda e: page.close(dialog))
                ]
            )
            page.open(dialog)

        input_key.value = ''
        input_value.value = ''
        page.update()
        print(storage.data)

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    input_key := ft.TextField(
                        hint_text='Key:'
                    ),
                    input_value := ft.TextField(
                        hint_text='Value:'
                    ),
                    SDLGButton(
                        'ADD',
                        on_click=add_storage
                    )
                ]
            )
        )
    )

if __name__ == '__main__':
    ft.app(main)