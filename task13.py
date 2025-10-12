def get_year_name(year):
    offset = year - 1984

    colors = ["зелёный", "красный", "жёлтый", "белый", "чёрный"]

    # Животных добавляем в родительном падеже
    animals_ = [
        "крысы", "коровы", "тигра", "зайца", "дракона", "змеи",
        "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"
    ]

    # Род животного: "муж" или "жен" — нужен для согласования цвета
    animal_genders = [
        "жен", "жен", "муж", "муж", "муж", "жен",
        "жен", "жен", "жен", "жен", "жен", "жен"
    ]

    color_index = (offset % 10) // 2
    animal_index = offset % 12

    color = colors[color_index]
    animal = animals_[animal_index]
    gender = animal_genders[animal_index]

    # Формы цвета в родительном падеже (согласование по роду)
    color_forms = {
        "зелёный": {"муж": "зелёного", "жен": "зелёной"},
        "красный": {"муж": "красного", "жен": "красной"},
        "жёлтый": {"муж": "жёлтого", "жен": "жёлтой"},
        "белый": {"муж": "белого", "жен": "белой"},
        "чёрный": {"муж": "чёрного", "жен": "чёрной"}
    }

    color_genitive = color_forms[color][gender]
    return f"год {color_genitive} {animal}"


def main():
    while True:
        try:
            year_input = input("Введите год: ").strip()
            if not year_input:
                print("Ошибка: пустой ввод. Попробуйте снова.")
                continue

            year = int(year_input)

            if year <= 0:
                print("Ошибка: год должен быть положительным числом (например, 1984).")
                continue

            break

        except ValueError:
            print("Ошибка: введите корректное целое число.")
        except KeyboardInterrupt:
            print("\nВыход из программы.")
            return

    result = get_year_name(year)
    print(f"{year} — {result}")


if __name__ == "__main__":
    main()