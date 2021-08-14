from src.application import Application
from concurrent.futures import ThreadPoolExecutor


def main():
    executor = ThreadPoolExecutor(max_workers=30)
    Application(executor).run()


if __name__ == "__main__":
    main()
