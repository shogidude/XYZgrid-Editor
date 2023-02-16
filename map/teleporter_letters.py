# ChatGPT wrote the base singleton for me. I modified it to fit my needs.
class TeleporterLetters:
    __instance = None

    def __new__(cls):
        if TeleporterLetters.__instance is None:
            TeleporterLetters.__instance = object.__new__(cls)
            TeleporterLetters.__instance.__teleporter_letters = []
        return TeleporterLetters.__instance

    @classmethod
    def set_teleporter_letters(cls, letters):
        TeleporterLetters.__instance.__teleporter_letters = map(str.strip, letters.split(','))

    @classmethod
    def get_teleporter_letters(cls):
        return ','.join(TeleporterLetters.__instance.__teleporter_letters)