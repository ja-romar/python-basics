from flask import Flask, render_template, request, jsonify
import spacy
from spacy import displacy

# Cargamos el modelo de spacy para realizar el recnocimiento de entidades nombradas
nlp = spacy.load('es_core_news_sm')


# Inicializamos la applicación Flask
app = Flask(__name__)


# Endpoint para la API en la ruta '/ner' que acepta solicitudes POST
@app.route('/ner', methods=['POST'])
def recognize_entities():
    # Obtenemos los datos JSON de la solicitud POST
    data = request.get_json()
    # Obtenemos la lista de oraciones del JSON proporcionado
    sentences = data.get("oraciones", [])
    # Creamos una lista para almacenar los resultado del reconocimiento de entidades nombradas
    results = []
    # Iteramos a través de cada oración en la lista
    for sentence in sentences:
        # Aplicamos el modelo de spacy nlp a cada oracion
        doc = nlp(sentence)
        # Creamos un diccionario de entidades encontradas en la oración (texto y tipo(etiqueta))
        entities = {ent.text: ent.label_ for ent in doc.ents}
        # Agregamos el resultado de la oración a la lista de resultados
        results.append({"oración": sentence, "entidades": entities})
    # Devolvemos el resultado en formato JSON como respuesta
    return jsonify({"resultado": results})


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)