# Простая консольная версия с меню (обновленная)

def cm_to_m(cm):
    return cm / 100


def kg_to_g(kg):
    return kg * 1000


def mm_to_cm(mm):
    return mm / 10


def km_to_m(km):
    return km * 1000


def main():
    while True:
        print("\n" + "=" * 40)
        print("🔄 КОНВЕРТЕР ВЕЛИЧИН")
        print("=" * 40)
        print("1. Сантиметры → Метры")
        print("2. Килограммы → Граммы")
        print("3. Миллиметры → Сантиметры")  # ОБНОВЛЕНО
        print("4. Километры → Метры")
        print("5. Выход")
        print("-" * 40)

        choice = input("Выберите операцию (1-5): ")

        if choice == '5':
            print("До свидания!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("❌ Неверный выбор! Попробуйте снова.")
            continue

        try:
            value = float(input("Введите значение: "))

            if choice == '1':
                result = cm_to_m(value)
                print(f"✅ {value} см = {result} м")
            elif choice == '2':
                result = kg_to_g(value)
                print(f"✅ {value} кг = {result} г")
            elif choice == '3':
                result = mm_to_cm(value)
                print(f"✅ {value} мм = {result} см")
            elif choice == '4':
                result = km_to_m(value)
                print(f"✅ {value} км = {result} м")

        except ValueError:
            print("❌ Ошибка! Введите число.")


if __name__ == "__main__":
    main()