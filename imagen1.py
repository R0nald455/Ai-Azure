import azure.ai.vision as sdk

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
key = "d876a5f5153b415daad195249dc49e4b"
endpoint = "https://anlisistextov2.cognitiveservices.azure.com/"



service_options = sdk.VisionServiceOptions(endpoint=endpoint,key=key)


vision_source = sdk.VisionSource(
    url="https://www.elespectador.com/resizer/3yL8RLSWj0wNQNiqAi0miA8teU8=/arc-anglerfish-arc2-prod-elespectador/public/ST67MWA4BFCQRP3WLYKEO2E5WE.jpg")

analysis_options = sdk.ImageAnalysisOptions()

analysis_options.features = (
    sdk.ImageAnalysisFeature.CAPTION |
    sdk.ImageAnalysisFeature.TEXT |
    sdk.ImageAnalysisFeature.TAGS
)

analysis_options.language = "en"

analysis_options.gender_neutral_caption = True

image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)

result = image_analyzer.analyze()

if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:

    #frase de la imagen
    if result.caption is not None:
        print(" Caption:")
        print("   '{}', Confidence {:.4f}".format(result.caption.content, result.caption.confidence))

    #analisis de texto en la imagen
    if result.text is not None:
        print(" Text:")
        for line in result.text.lines:
            points_string = "{" + ", ".join([str(int(point)) for point in line.bounding_polygon]) + "}"
            print("   Line: '{}', Bounding polygon {}".format(line.content, points_string))
            for word in line.words:
                points_string = "{" + ", ".join([str(int(point)) for point in word.bounding_polygon]) + "}"
                print("     Word: '{}', Bounding polygon {}, Confidence {:.4f}"
                      .format(word.content, points_string, word.confidence))
                
    #etiquetas recomendadas 
    if result.tags is not None:
        print("\nTags Result:")
        for tag in result.tags:
            print(tag.name)
            
else:

    error_details = sdk.ImageAnalysisErrorDetails.from_result(result)
    print(" Analysis failed.")
    print("   Error reason: {}".format(error_details.reason))
    print("   Error code: {}".format(error_details.error_code))
    print("   Error message: {}".format(error_details.message))