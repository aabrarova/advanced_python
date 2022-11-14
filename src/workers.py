import re
from typing import IO


class Worker:
    middle_name: str
    last_name: str
    first_name: str
    salary: int
    birth_year: int

    def __init__(self, first_name: str, last_name: str, middle_name: str, birth_year: int, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_year = birth_year
        self.salary = salary

    def worker_info(self) -> str:
        """Returns formatted worker information."""
        return f"ФИО: {self.short_name()} Год рождения: {self.birth_year} Зарплата: {self.salary}"

    def short_name(self):
        return join([self.last_name.capitalize(), shorten_name(self.first_name), shorten_name(self.middle_name)], " ")


def first_char(s: str) -> str:
    """Returns first characters of s or empty string if s is empty."""
    if len(s) > 0:
        return s[0]
    return ""


def shorten_name(s: str) -> str:
    if len(s) > 0:
        return first_char(s).capitalize() + "."
    return ""


def join(strings: list[str], delimiter: str) -> str:
    r = ""
    for string in strings:
        if len(string) > 0:
            if len(r) > 0:
                r += delimiter
            r += string
    return r


def input_workers(num: int) -> list[Worker]:
    """Inputs data from console and returns it as a list each item of which is of class Worker."""
    workers = []
    for i in range(0, num):
        print(f"Input worker #{i + 1}")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        middle_name = input("Middle name: ")
        birth_year = int(input("Birth year: "))
        salary = int(input("Salary: "))
        worker = Worker(first_name, last_name, middle_name, birth_year, salary)
        workers.append(worker)
    return workers


def output_workers(f: IO, workers: list[Worker]) -> None:
    """Prints workers into file f."""
    for worker in workers:
        f.write(worker.worker_info())
        f.write("\n")


def main():
    worker_num = int(input("Numer of workers: "))
    workers = input_workers(worker_num)

    f = open("worker.txt", mode="a", encoding="utf-8")
    try:
        output_workers(f, workers)
    finally:
        f.close()

    for worker in workers:
        if re.match("^\\s*2003\\s*$", str(worker.birth_year)):
            print(worker.worker_info())


if __name__ == "__main__":
    main()
