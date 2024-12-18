"""Basic class"""
class PowerUnit:
    def __init__(self):
        super().__init__()
        self.__power = 60

    def submit_voltage(self):
        return f"Блок питания:\nподает напряжение {self.__power} ватт."


class MotherBoard:
    def __init__(self):
        super().__init__()
        self.__chipset = "Intel Z790"

    def redistribute_voltage(self):
        return f"Чипсет {self.__chipset}:\nперераспределить напряжение от БП по компонентам"


class CPU:
    def __init__(self):
        super().__init__()
        self.__clock_frequency = "4 ГГц"
        self.__cores = 6

    def turbo_mode(self):
        return (f"Центральный процессор:\n"
                f"Тактовая частота: {self.__clock_frequency}\nКоличество ядер: {self.__cores}\n"
                f"Активирует турбо режим")


class RAM:
    def __init__(self):
        super().__init__()
        self.__memory_capacity = "16 ГБ"
        self.__memory_frequency = "3200 МГц"

    def load_upload_data(self):
        return (f"Оперативная память:\n"
                f"Объем памяти: {self.__memory_capacity}\nЧастота памяти: {self.__memory_frequency}\n"
                f"Загружает данные, выгружает данные")


class SSD:
    def __init__(self):
        super().__init__()
        self.__volume = "512ГБ"

    def save_data(self):
        return (f"SSD:\nОбьем памяти: {self.__volume}\n"
                f"Сохраняет данные, удаляет данные")


class VideoCard:
    def __init__(self):
        self.__model = "GeForce RTX 4090"
        self.__volume = "2 GB"

    def display_image(self):
        return (f"Видеокарта:\nМодель видеокарты:{self.__model}\n"
                f"Объем памяти: {self.__volume}\n"
                f"вывести изображение на экран")


"""Composition"""
class Computer1:
    print("Этот 1-класс компьютер реализовано при помощи композиции")
    def __init__(self):
        self.__power = PowerUnit()
        self.__mother = MotherBoard()
        self.__cpu = CPU()
        self.__ram = RAM()
        self.__ssd = SSD()
        self.__video_card = VideoCard()

    def power(self):
        return self.__power.submit_voltage()

    def mother(self):
        return self.__mother.redistribute_voltage()

    def cpu(self):
        return self.__cpu.turbo_mode()

    def ram(self):
        return self.__ram.load_upload_data()

    def ssd(self):
        return self.__ssd.save_data()

    def video_card(self):
        return self.__video_card.display_image()


computer1 = Computer1()
print(computer1.power())
print()
print(computer1.mother())
print()
print(computer1.cpu())
print()
print(computer1.ram())
print()
print(computer1.ssd())
print()
print(computer1.video_card())
print("".center(200, "*"))
print()


"""Multiple inheritance"""
class Computer2(PowerUnit, MotherBoard, CPU, RAM, SSD, VideoCard):
    print("Этот 2-класс компьютер реализовано"
          " при помощи множественного наследования")

    # def power(self):
    #     return self.submit_voltage()
    #
    # def mother(self):
    #     return self.redistribute_voltage()
    #
    # def cpu(self):
    #     return self.turbo_mode()
    #
    # def ram(self):
    #     return self.load_upload_data()
    #
    # def ssd(self):
    #     return self.save_data()
    #
    # def video_card(self):
    #     return self.display_image()


computer2 = Computer2()
# print(computer2.power())
# print()
# print(computer2.mother())
# print()
# print(computer2.cpu())
# print()
# print(computer2.ram())
# print()
# print(computer2.ssd())
# print()
# print(computer2.video_card())

print(computer2.submit_voltage())
print()
print(computer2.redistribute_voltage())
print()
print(computer2.turbo_mode())
print()
print(computer2.load_upload_data())
print()
print(computer2.save_data())
print()
print(computer2.display_image())
