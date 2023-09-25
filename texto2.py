#Instalar el adicional de text analitycs

key = "d876a5f5153b415daad195249dc49e4b"
endpoint = "https://anlisistextov2.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

documents = [
    """
    Washington, D.C. Autumn in DC is a uniquely beautiful season. The leaves fall from the trees
    in a city chock-full of forests, leaving yellow leaves on the ground and a clearer view of the
    blue sky above...
    """,
    """
    Redmond, WA. In the past few days, Microsoft has decided to further postpone the start date of
    its United States workers, due to the pandemic that rages with no end in sight...
    """,
    """
    Lionel Andrés Messi Cuccittini, conocido como Leo Messi, es un futbolista argentino que juega como 
    delantero o centrocampista y su equipo actual es el Inter Miami de la MLS de Estados Unidos
    """
]

# Example method for detecting the language of text
def language_detection_example(client):
    try:
    

        """ analisis de sentimientos """
        resultados = client.analyze_sentiment(documents = documents, show_opinion_mining=True)
        for idx, doc in enumerate(resultados):
            if not doc.is_error:
                print(f"Overall sentiment: {doc.sentiment}")

        """ deteccion de idioma """
        resultados=client.detect_language(documents = documents, country_hint = 'es')
        for idx, doc in enumerate(resultados):
            if not doc.is_error:
                print("Language: ", doc.primary_language.name)


        """   deteccion de palabras clave """
        result = client.extract_key_phrases(documents)
        for idx, doc in enumerate(result):
            if not doc.is_error:
                print("Key phrases in article #{}: {}".format(
                    idx + 1,
                    ", ".join(doc.key_phrases)
                ))

    except Exception as err:
        print("Encountered exception. {}".format(err))

#se llama a la funcion
language_detection_example(client)