from googletrans import Translator, LANGUAGES

# print(LANGUAGES)

translator = Translator()


def translate(text: str,src:str, dest:str):
    # dest -> язык на который перевести
    # src -> язык с которого перевести

    result = translator.translate(
        "Hello",
        dest="ru",
        src="en"
    )
    print(result.text)
    return result.text


