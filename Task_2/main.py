class Travel:
    def start(self):
        print("Начинаем путешествие")

    def visa(self):
        print("Информация о визе не указана")


class France(Travel):
    def visa(self):
        print("Франция: виза НЕ нужна (для ЕС)")


class Japan(Travel):
    def visa(self):
        print("Япония: нужна виза")


class Turkey(Travel):
    def visa(self):
        print("Турция: виза не нужна")


countries = [France(), Japan(), Turkey()]

for country in countries:
    country.start()
    country.visa()
    print()
