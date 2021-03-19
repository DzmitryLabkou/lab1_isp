import logging


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    logging.info(fibonacci(12))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.error("Err", exc_info=True)
