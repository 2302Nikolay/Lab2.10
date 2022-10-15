#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


def print_scores(student, *scores):
    print(f"Имя студента: {student}")
    for score in scores:
        print(score)


def print_pet_names(owner, **pets):
    print(f"Owner name: {owner}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")


if __name__ == '__main__':
    print_scores("Джонатан", 100, 95, 88, 92, 99)
    print_pet_names(
        "Джонатан",
        dog="Брок", fish=["Ларри", "Кёрли", "Моё"],
        turtle="Шелдон"
    )
