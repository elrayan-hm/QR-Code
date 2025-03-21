import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


def generate_qrcode():
    ref_id = ref_id_entry.get()

    if not ref_id:
        messagebox.showerror("Error", "Please type your message.")
        return

    data = f"{ref_id}"
    
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{ref_id}.png")

    messagebox.showinfo("Success", f"QR Code has been saved as {ref_id}.png")


def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    
    if not file_path:
        return
    
    try:
        img = Image.open(file_path)
        decoded_objects = decode(img)

        if decoded_objects:
            decoded_data = decoded_objects[0].data.decode('utf-8')
            messagebox.showinfo("QR Code Data", f"Data from QR Code: {decoded_data}")
        else:
            messagebox.showerror("Error", "No QR code found in the image.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Create main window
root = tk.Tk()
root.title("QR Code Generator and Reader")
root.geometry("400x300")

# Create widgets
label = tk.Label(root, text="Please type your message")
label.pack(pady=10)

ref_id_entry = tk.Entry(root, width=30)
ref_id_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qrcode)
generate_button.pack(pady=10)

upload_button = tk.Button(root, text="Upload Image to Read QR Code", command=upload_image)
upload_button.pack(pady=10)

# Run the application
root.mainloop()
