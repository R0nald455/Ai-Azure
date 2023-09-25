#intalar el sdk pip install azure-cognitiveservices-speech cambiar a en-ES para español
import azure.cognitiveservices.speech as speechsdk

# Configura las claves y el punto de conexión
key = "4baf4501910d46fcab901eb20cacae43"
endpoint = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

# Crea un objeto de configuración
speech_config = speechsdk.translation.SpeechTranslationConfig(subscription=key, region="eastus")
speech_config.speech_recognition_language="es-ES"


target_language="en"
speech_config.add_target_language(target_language)
translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_config)

print("Habla algo...")
translation_recognition_result = translation_recognizer.recognize_once()


if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
    print("Recognized: {}".format(translation_recognition_result.text))
    print("""Translated into '{}': {}""".format(
    target_language, 
    translation_recognition_result.translations[target_language]))
elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = translation_recognition_result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
