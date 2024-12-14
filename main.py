class PowerUnit:
    def __init__(self, power=60):
        self.__power = power

    def get_voltage(self):
        return f"Блок питания:\nподает напряжение {self.__power} ватт."


class MotherBoard:
    def __init__(self, chipset="Intel Z790"):
        self.__chipset = chipset

    def get_chipset(self):
        return (f"Материнская плата:\n"
                f"Чипсет '{self.__chipset}' координирует работу всего оборудования"
                f" подключенного к материнской плате а также "
                f"перераспределить напряжение от БП по компонентам")


class CPU:
    def __init__(self, frequency="4 ГГц", cores=6):
        self.__clock_frequency = frequency
        self.__cores = cores

    def get_cpu(self):
        return (f"Центральный процессор:\n"
                f"тактовая частота: {self.__clock_frequency}"
                f"\nколичество ядер:{self.__cores}")

    @staticmethod
    def get_turbo(active="off"):
        if  active == "active":
            print("Турбо режим активировано!")
        else:
            print("Турбо режим отключено!")


class RAM:
    def __init__(self, capacity="16 ГБ", frequency="3200 МГц"):
        self.__memory_capacity = capacity
        self.__memory_frequency = frequency

    def get_ram(self):
        return (f"Оперативная память:\n"
                f"объем памяти: {self.__memory_capacity}\n"
                f"частота памяти: {self.__memory_frequency}")


class SSD:
    def __init__(self, volume="512ГБ"):
        self.__volume = volume

    def get_ssd(self):
        return f"SSD\nобъем: {self.__volume}"


class VideoCard:
    def __init__(self, model="GeForce RTX 4090", volume="2 GB"):
        self.__model = model
        self.__volume = volume

    def get_card(self):
        return f"Video card:\nмодель: {self.__model}\nобъем памяти: {self.__volume}"


class Computer:
    def __init__(self):
        self.__power_unit = PowerUnit()
        self.__motherboard = MotherBoard()
        self.__cpu = CPU()
        self.__ram = RAM()
        self.__ssd = SSD()
        self.__video_card = VideoCard()

    def power_unit(self):
        return self.__power_unit.get_voltage()

    def motherboard(self):
        return self.__motherboard.get_chipset()

    def cpu(self):
        return self.__cpu.get_cpu()

    def ram(self):
        return self.__ram.get_ram()

    def ssd(self):
        return self.__ssd.get_ssd()

    def video_card(self):
        return self.__video_card.get_card()

    def turbo_mode(self, active="off"):
        self.__cpu.get_turbo(active)


computer = Computer()
print(computer.power_unit())
print()
print(computer.motherboard())
print()
print(computer.cpu())
print()
print(computer.ram())
print()
print(computer.ssd())
print()
print(computer.video_card())
print()
computer.turbo_mode("active")