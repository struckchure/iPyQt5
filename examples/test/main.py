def main():
    from iPyQt5.app.app import App
    from routes import router

    window = App(
        router=router
    )
    window.mount()


if __name__ == '__main__':
    from pathlib import Path
    import sys

    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    CURRENT_DIR = Path(__file__).resolve().parent

    sys.path[0] = str(BASE_DIR)
    sys.path[1] = str(CURRENT_DIR)

    main()
