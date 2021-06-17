def main():
    from app.app import App
    from routes import router

    window = App(
        router=router
    )
    window.mount()


if __name__ == '__main__':
    from pathlib import Path
    import sys
    import os

    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    sys.path.append(str(BASE_DIR))

    for path in os.listdir(BASE_DIR):
        try:
            os.listdir(os.path.join(BASE_DIR, path))
            if not path.startswith('.') and not path.startswith('_'):
                sys.path.append(os.path.join(BASE_DIR, path))
        except NotADirectoryError:
            pass

    main()
