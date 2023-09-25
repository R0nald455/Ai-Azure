#intalar el sdk pip install azure-cognitiveservices-speech cambiar a en-ES para español
import azure.cognitiveservices.speech as speechsdk

# Configura las claves y el punto de conexión
key = "4baf4501910d46fcab901eb20cacae43"
endpoint = "https://eastus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

# Crea un objeto de configuración
speech_config = speechsdk.SpeechConfig(subscription=key, region="eastus")

# Crea un objeto de reconocimiento de audio
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

# Inicia el reconocimiento de voz desde el micrófono
print("Habla algo...")
result = speech_recognizer.recognize_once()

# Comprueba el resultado
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Texto reconocido: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No se encontró ninguna coincidencia")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Reconocimiento cancelado: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error de reconocimiento: {}".format(cancellation_details.reason_details))

# Cierra el reconocimiento de voz
speech_recognizer.stop_continuous_recognition()

