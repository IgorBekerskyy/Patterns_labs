from random import randint
import csv

NAME = ["Roman", "Dana", "Suzana", "Nazar", "Svitlana", "Oksana", "Marjana",
        "Snizhana", "Hanna", "Larysa", "Kolia", "Kostyk", "Mykola", "Max", "Nastia", "Serhii",
        "Dmytro", "Marjan", "Pavlo", "Petro", "Davyd", "Nadia", "Maryna", "Sofia",
        "Katya", "Nelia", "Liza", "Khrystyna", "Andrii", "Bob", "John", "Lia"
        ]

ICON = ["Home", "Compensation", "Info"]


def generate_data():
    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "icon"])
        for i in range(1000):
            request_data = []

            chapter_id = i + 1
            request_data.append(chapter_id)

            name = NAME[randint(0, 2)]
            request_data.append(name)

            icon = ICON[randint(0, len(ICON) - 1)]
            request_data.append(icon)

            writer.writerow(request_data)


generate_data()
