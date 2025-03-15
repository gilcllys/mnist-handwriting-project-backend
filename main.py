from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64

app = FastAPI()

# load the trained model
model = tf.keras.models.load_model('cnn_model.h5')


# Main route
@app.get("/")
def read_root():
    return HTMLResponse(content="<h1> API: handwritten digits recognition </h1>")

# WebSocket route


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receives the base64 encoded image from frontend
            data = await websocket.receive_text()

            # Decodes the base64 image
            image_data = base64.b64decode(data.split(",")[1])
            # Convert to grayscale
            image = Image.open(io.BytesIO(image_data)).convert(
                'L')
            # Resize to 28x28 pixels
            image = image.resize((28, 28))

            # Pre-processing of the image
            image_array = np.array(image).reshape(
                1, 28, 28, 1).astype('float32') / 255

            # Do the prediction using the trained model
            prediction = model.predict(image_array)
            predicted_digit = np.argmax(prediction)

            # Accuracy
            predicted_accuracy = float(np.max(prediction))

            # Sends the predicted number and accuracy back to the frontend
            response = {
                "predicted_number": int(predicted_digit),
                "predicted_accuracy": predicted_accuracy
            }
            await websocket.send_json(response)

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        await websocket.close()

# Start the server with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
