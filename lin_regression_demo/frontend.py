from fastapi import FastAPI

from nicegui import ui


def init(app: FastAPI) -> None:
    @ui.page('/show')
    def show():
        
        str = r'''
<!DOCTYPE html>
<html>
    <head>
        <title>Example</title>
    </head>
    <body>
        <p>This is an example of a simple HTML page with one paragraph.</p>
    </body>
</html>
'''
        ui.html(str)
        ui.html('<button>Click me!</button>')

        ui.label(str)

    ui.run_with(app)