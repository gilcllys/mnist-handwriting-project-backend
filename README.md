## Português
# Projeto de Reconhecimento de Dígitos Manuscritos (MNIST)

Este projeto é uma aplicação de backend para reconhecimento de dígitos manuscritos usando o conjunto de dados **MNIST**. O backend foi desenvolvido com **FastAPI** e utiliza **WebSocket** como protocolo de comunicação para receber imagens em tempo real e retornar previsões. O modelo de reconhecimento foi treinado usando **TensorFlow** com **Keras**.

---

## Tecnologias Utilizadas

### Backend
- **FastAPI**: Framework moderno e rápido para construção de APIs em Python.
- **WebSocket**: Protocolo de comunicação bidirecional em tempo real, usado para receber imagens e enviar previsões.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.

### Machine Learning
- **TensorFlow**: Biblioteca de machine learning para treinamento de modelos.
- **Keras**: API de alto nível para construção e treinamento de redes neurais.
- **MNIST**: Conjunto de dados de dígitos manuscritos (0 a 9).

### Outras Ferramentas
- **NumPy**: Biblioteca para manipulação de arrays numéricos.
- **Pillow (PIL)**: Biblioteca para processamento de imagens.

---

## Funcionalidades do Backend

1. **Recepção de Imagens via WebSocket**:
   - O backend recebe imagens de dígitos manuscritos em tempo real via WebSocket.
   - As imagens são pré-processadas (redimensionadas e normalizadas) antes de serem passadas para o modelo.

2. **Previsão com o Modelo MNIST**:
   - O modelo treinado com TensorFlow/Keras faz a previsão do dígito na imagem recebida.
   - A previsão é enviada de volta ao cliente via WebSocket.

3. **API REST para Testes**:
   - Além do WebSocket, o backend oferece uma API REST para envio de imagens e recebimento de previsões.

---

## Estrutura do Projeto
```bash

backend/
├── train_model_process/ # Juypter notebook 
│ └── mnist-handwriting.ipynb # Modelo CNN
├── main.py # Aplicação FastAPI com WebSocket
│── cnn_model.h5 # Modelo CNN treinado no MNIST
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto
```
---

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior.
- Bibliotecas listadas no `requirements.txt`.

### Passos para Execução

1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/gilcllys/mnist-handwriting-project-backend.git
   cd mnist-handwriting-project-backend

2. **Instalar Dependências:**:
    ```bash
   pip install -r requirements.txt

3. **Executar o Backend:**:
    ```bash
    uvicorn src.main:app --reload

### O backend estará disponível em:
    API REST: http://localhost:8000
    WebSocket: ws://localhost:8000/ws
---

### Exemplos de Uso
## WebSocket

1.  Conecte-se ao WebSocket em ws://localhost:8000/ws.

2. Envie uma imagem codificada em base64.

3. Receba a previsão do dígito em tempo real.
---
# Licença

- Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
- Contato
    ``` bash
    Nome: Gilcllys Costa

    Email: gilcllyscosta@gmail.com

    GitHub: seu-usuario
---
## English
# Handwritten Digit Recognition Backend (MNIST)

This is a backend application for real-time handwritten digit recognition using the **MNIST** dataset. Built with **FastAPI**, the system leverages **WebSocket** for real-time communication and **TensorFlow/Keras** for digit classification.

---

## Technologies

### Backend
- **FastAPI** – A modern, high-performance web framework for building APIs with Python.
- **WebSocket** – Enables bidirectional, real-time communication between client and server.
- **Uvicorn** – ASGI server used to run the FastAPI application.

### Machine Learning
- **TensorFlow** – Machine learning framework used to train the model.
- **Keras** – High-level neural network API integrated with TensorFlow.
- **MNIST** – Benchmark dataset of handwritten digits (0-9).

### Utilities
- **NumPy** – Library for efficient numerical computations.
- **Pillow (PIL)** – Image processing library used to handle image input.

---

## Features

- **Real-time Digit Recognition via WebSocket**  
  Receives base64-encoded images via WebSocket, processes them, and returns model predictions in real time.

- **Digit Prediction with CNN Model**  
  The model, trained on MNIST using TensorFlow/Keras, outputs the predicted digit and its confidence score.

- **REST API Endpoint**  
  Alternative RESTful interface to send images and receive predictions for testing purposes.

---

## Project Structure
```bash
    backend/
    ├── train_model_process/       # Jupyter notebook with model training
    │   └── mnist-handwriting.ipynb
    ├── main.py                    # FastAPI application with WebSocket integration
    ├── cnn_model.h5               # Pre-trained CNN model on MNIST dataset
    ├── requirements.txt           # Project dependencies
    └── README.md                  # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.8+
- Packages listed in requirements.txt

### Installation & Execution

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gilcllys/mnist-handwriting-project-backend.git
   cd mnist-handwriting-project-backend

2. **Install dependencies**:
    ```bash
   pip install -r requirements.txt

3. **Run the application:**:
    ```bash
    uvicorn src.main:app --reload

### Application Endpoints:
    API REST: http://localhost:8000
    WebSocket: ws://localhost:8000/ws
---

### Usage
## WebSocket Workflow

1. Connect to ws://localhost:8000/ws.
2. Send a base64-encoded image of a handwritten digit.
3. Receive real-time prediction response.
---
# Licença

- This project is licensed under the MIT License. See the LICENSE file for details.
- Contact
    ```bash
    Name: Gilcllys Costa
    Email: gilcllyscosta@gmail.com
    GitHub: gilcllys