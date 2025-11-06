from googletrans import Translator

from services.history import HistoryMenager

translator = Translator()

menager = HistoryMenager()

def translate(from_lang, text, to_lang):
    result = translator.translate(
        text,
        dest=to_lang,
        src=from_lang
    )

    return result.text

