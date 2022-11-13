import re


class Worker:
    def __init__(self, first_name, last_name, middle_name, birth_year, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_year = birth_year
        self.salary = salary

    def worker_info(self):
        return f"ФИО: {self.last_name} {self.first_name} {self.middle_name} Год рождения: {self.birth_year} Зарплата: {self.salary}"


def input_workers(num):
    workers = []
    for i in range(0, num):
        print(f"Input worker 1#{i + 1}")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        middle_name = input("Middle name: ")
        birth_year = int(input("Birth year: "))
        salary = int(input("Salary: "))
        worker = Worker(first_name, last_name, middle_name, birth_year, salary)
        workers.append(worker)
    return workers


def output_workers(f, workers):
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
