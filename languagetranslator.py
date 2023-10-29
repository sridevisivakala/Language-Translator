from google.cloud import translate_v2 as translate

# Set up Google Cloud Translation API client
client = translate.Client()

def translate_text(text, target_language, format_=None):
    try:
        # Translate the text to the target language
        result = client.translate(text, target_language=target_language, format_=format_)

        # Extract the translated text from the response
        translated_text = result['translatedText']

        return translated_text

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Input text to be translated
    input_text = "Hello, how are you?"

    # Target language (e.g., 'es' for Spanish)
    target_language = 'es'

    # Optionally, you can specify the format of the text (e.g., 'html' or 'text')
    text_format = 'text'

    # Translate the text
    translated_text = translate_text(input_text, target_language, text_format)

    if translated_text:
        print(f"Original Text: {input_text}")
        print(f"Translated Text: {translated_text}")
    else:
        print("Translation failed.")
