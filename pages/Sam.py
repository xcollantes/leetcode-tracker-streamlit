import logging

from modules.user import user_template

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    TAB_NAME: str = "Sam"
    user_template(TAB_NAME)


if __name__ == "__main__":
    main()
