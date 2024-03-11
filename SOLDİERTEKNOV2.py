import speech_recognition as sr
import time
import threading

class AskeriRobot:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.commands = {
            "ileri git": self.move_forward,
            "geri gel": self.move_backward,
            "sola git": self.move_left,
            "sağa git": self.move_right,
            "zıpla": self.jump,
            "ateş et": self.fire,
            "ağları kes": self.cut_networks,
            "teknolojik aletleri etkisiz hale getir": self.disable_technologies,
            "termal sensörü etkinleştir": self.activate_thermal_sensor,
            "hızlı algılama": self.enable_fast_detection
        }
        self.active_commands = {command: False for command in self.commands}
        self.thermal_sensor_status = False
        self.fast_detection_status = False
        self.network_status = True
        self.technology_status = True

    def listen_for_commands(self):
        with self.microphone as source:
            print("Komut bekleniyor...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                command = self.recognizer.recognize_google(audio, language="tr-TR")
                print("Algılanan komut:", command)
                if command in self.commands:
                    self.commands[command]()
                else:
                    print("Anlaşılamayan komut.")
            except sr.UnknownValueError:
                print("Üzgünüm, komut anlaşılamadı.")
            except sr.RequestError as e:
                print("Ses hizmeti başarısız; {0}".format(e))

    def move_forward(self):
        if not self.active_commands["ileri git"]:
            print("İleri gitme başladı...")
            self.active_commands["ileri git"] = True
            threading.Thread(target=self._move_forward).start()
        else:
            print("Zaten ileri gidiliyor.")

    def _move_forward(self):
        time.sleep(3)
        print("İleri gitme tamamlandı.")
        self.active_commands["ileri git"] = False

    def move_backward(self):
        if not self.active_commands["geri gel"]:
            print("Geri gelme başladı...")
            self.active_commands["geri gel"] = True
            threading.Thread(target=self._move_backward).start()
        else:
            print("Zaten geri geliniyor.")

    def _move_backward(self):
        time.sleep(3)
        print("Geri gelme tamamlandı.")
        self.active_commands["geri gel"] = False

    def move_left(self):
        if not self.active_commands["sola git"]:
            print("Sola gitme başladı...")
            self.active_commands["sola git"] = True
            threading.Thread(target=self._move_left).start()
        else:
            print("Zaten sola gidiliyor.")

    def _move_left(self):
        time.sleep(3)
        print("Sola gitme tamamlandı.")
        self.active_commands["sola git"] = False

    def move_right(self):
        if not self.active_commands["sağa git"]:
            print("Sağa gitme başladı...")
            self.active_commands["sağa git"] = True
            threading.Thread(target=self._move_right).start()
        else:
            print("Zaten sağa gidiliyor.")

    def _move_right(self):
        time.sleep(3)
        print("Sağa gitme tamamlandı.")
        self.active_commands["sağa git"] = False

    def jump(self):
        print("Zıplama işlemi gerçekleştiriliyor...")

    def fire(self):
        print("Ateş etme işlemi gerçekleştiriliyor...")

    def cut_networks(self):
        if not self.network_status:
            print("Ağları kesme işlemi başlatılıyor...")
            self.network_status = True
            self.network_status = False
        else:
            print("Ağlar zaten kesik durumda.")

    def disable_technologies(self):
        if not self.technology_status:
            print("Teknolojik aletleri etkisiz hale getirme başlatılıyor...")
            self.technology_status = True
            self.technology_status = False
        else:
            print("Teknolojik aletler zaten etkisiz durumda.")

    def activate_thermal_sensor(self):
        if not self.thermal_sensor_status:
            print("Termal sensör aktifleştiriliyor...")
            self.thermal_sensor_status = True
        else:
            print("Termal sensör zaten aktif.")

    def enable_fast_detection(self):
        if not self.fast_detection_status:
            print("Hızlı algılama etkinleştiriliyor...")
            self.fast_detection_status = True
        else:
            print("Hızlı algılama zaten etkin.")

    def run(self):
        while True:
            self.listen_for_commands()
            time.sleep(0.5)

if __name__ == "__main__":
    robot = AskeriRobot()
    robot.run()
