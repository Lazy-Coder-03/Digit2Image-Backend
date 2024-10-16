


# Digit2Image

Digit2Image is a project that generates images of digits using a conditional autoencoder. This repository includes a frontend application built with p5.js for visualizing the generated images, alongside a backend server for handling image generation requests.

## Project Structure

```
Digit2Image/
├── frontend/
│   ├── index.js          # Main JavaScript file for the frontend application
│   ├── style.css         # Styles for the frontend application
│   └── sketch.js         # p5.js sketch for rendering images
├── conditional_autoencoder.keras  # Keras model file for the conditional autoencoder
├── requirements.txt      # Python package dependencies
├── text_2_image.ipynb    # Jupyter notebook for experimenting with text-to-image generation
└── test_server.py        # Backend server for handling requests
```

## Getting Started

### Prerequisites

- Python 3.x
- Node.js (for frontend)
- p5.js library

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Lazy-Coder-03/Digit2Image.git
   cd Digit2Image
   ```

2. **Set up the backend**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set up the frontend**:
   - Navigate to the `frontend` directory:
     ```bash
     cd frontend
     ```
   - (Optional) Install additional Node.js packages if required.

### Running the Project

1. **Start the backend server**:
   ```bash
   python test_server.py
   ```

2. **Open the frontend application**:
   - Open the `index.js` file in a browser or set up a local server to serve the `frontend` directory.

### Usage

- Enter a digit in the input field on the frontend, and click the generate button to create an image of the digit using the conditional autoencoder.
- The generated images will be displayed on the canvas, with a fade effect transitioning between images.

### Customization

You can customize the behavior of the project by modifying the following files:

- **`sketch.js`**: Adjust the p5.js code for rendering and image handling.
- **`test_server.py`**: Modify the backend server logic for image generation.

### Contributing

Contributions are welcome! If you'd like to contribute to this project, please open an issue or submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Thank you to the contributors of the libraries and frameworks used in this project.
