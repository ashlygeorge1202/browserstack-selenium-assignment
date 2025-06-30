from googletrans import Translator

translator = Translator()

def translate_text(text):
    try:
        return translator.translate(text, src="es", dest="en").text
    except:
        return "[Translation Failed]"
