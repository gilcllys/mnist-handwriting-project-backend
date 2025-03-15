from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64

app = FastAPI()

# Carregar o modelo treinado
model = tf.keras.models.load_model('modelo_treinado.h5')


# Rota para teste de conexão
@app.get("/")
def read_root():
    return HTMLResponse(content="<h1> API de reconhecimento de letra</h1>")

# WebSocket para receber imagens e enviar previsões


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Recebe a imagem codificada em base64 do frontend
            data = await websocket.receive_text()

            # Decodifica a imagem base64
            image_data = base64.b64decode(data.split(",")[1])
            image = Image.open(io.BytesIO(image_data)).convert(
                'L')  # Converte para tons de cinza
            image = image.resize((28, 28))  # Redimensiona para 28x28 pixels

            # Pré-processamento da imagem
            image_array = np.array(image).reshape(
                1, 28, 28, 1).astype('float32') / 255

            # Faz a previsão usando o modelo
            prediction = model.predict(image_array)
            predicted_digit = np.argmax(prediction)

            # Acurácia (probabilidade)
            predicted_accuracy = float(np.max(prediction))

            # Envia o número predito e a acurácia de volta para o frontend
            response = {
                "predicted_number": int(predicted_digit),
                "predicted_accuracy": predicted_accuracy
            }
            await websocket.send_json(response)

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        await websocket.close()

# Iniciar o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
