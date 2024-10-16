from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from keras.utils import to_categorical
from keras.models import load_model
import uvicorn
# Load the model (make sure to specify the correct path)
conditional_autoencoder = load_model("conditional_autoencoder.keras")


app = FastAPI()

# Allow CORS for the frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"]
    allow_origins=["https://digit2image-frontend.onrender.com/"]
    allow_origins=["*"],  # Adjust this in production for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your trained model here (ensure the model is saved and loaded correctly)
# from your_model_file import conditional_autoencoder

def add_noise(images, noise_factor):
    noisy_images = images + noise_factor * np.random.normal(size=images.shape)
    return np.clip(noisy_images, 0., 1.)

def generate_image_digit(digit, num_iterations=10, noise_level=0.5):
    noise_image = np.random.normal(0, 1, (1, 28, 28, 1))
    noisy_image = np.clip(noise_image + noise_level * np.random.normal(0, 1, noise_image.shape), 0., 1.)
    images_dict = []  # List to store denoised images at each iteration

    # Create one-hot encoded label for the digit
    label = to_categorical(digit, num_classes=10).reshape(1, -1)

    for i in range(num_iterations):
        denoised_image = conditional_autoencoder.predict([noisy_image, label])

        # Append the denoised image to the list as a list (convert from ndarray to list)
        images_dict.append((denoised_image[0] * 255).astype(np.uint8).tolist())  # Scale to 0-255 for visualization and convert to list

        # Prepare for the next iteration with some randomness
        if np.random.rand() < 0.5:  # Randomly decide to add some noise
            denoised_image += noise_level * np.random.normal(size=denoised_image.shape)

        # Prepare for the next iteration
        noisy_image = add_noise(denoised_image, noise_level)

    return images_dict  # Return the list containing all denoised images


@app.get("/generate/{digit}")
async def generate(digit: int):
    if 0 <= digit <= 9:
        images = generate_image_digit(digit)  # Generate images
        return JSONResponse(content={"images": images})  # Return as JSON response
    return JSONResponse(content={"error": "Digit must be between 0 and 9"}, status_code=400)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}@app.get("/")
async def root():
    return {"message": "Hello, World!"}


# if __name__ == "__main__":
#
#     uvicorn.run(app, host="0.0.0.0", port=8000)
