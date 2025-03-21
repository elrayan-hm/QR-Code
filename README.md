> This project is a Python-based QR code generator that encodes custom data into QR codes and provides a data reader for scanning and extracting information from QR codes. It demonstrates basic data encoding/decoding and image generation using the qrcode library in Python. Perfect for learning QR code generation and data handling.

# QR Code Generator and Reader

This Python script allows users to:
1. **Generate QR Codes**: Input a reference ID to generate a QR code that links to a specific URL or a random message.
2. **Read QR Codes**: Upload an image containing a QR code to decode and view its data.

The script provides a simple graphical user interface (GUI) built with `tkinter` for easy interaction.

## Features
- Generate a QR code by entering a reference ID.
- Upload an image to extract and view the data from a QR code.
- Save the generated QR code as a PNG image.
- Error handling for missing input or invalid QR codes in uploaded images.

## Prerequisites
To run this script, you'll need to install the following Python libraries:

- `qrcode`: To generate QR codes.
- `pyzbar`: To decode QR codes from images.
- `Pillow`: To handle image operations in Python.
- `tkinter`: For the graphical user interface (usually included with Python).

To install the required libraries, use the following command:

```bash
pip install ... 😴
