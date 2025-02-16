import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def load_spectrum_scr(filename):
    """Load a ZX Spectrum .scr file and return the pixel and attribute data."""
    with open(filename, 'rb') as f:
        data = f.read()
    
    if len(data) != 6912:
        raise ValueError("Invalid .scr file size, expected 6912 bytes.")
    
    pixel_data = np.zeros((192, 256), dtype=np.uint8)
    attr_data = np.zeros((24, 32), dtype=np.uint8)
    
    # Decode pixel data (bitmap, first 6144 bytes)
    for y in range(192):
        real_y = ((y & 0xC0) | ((y & 0x07) << 3) | ((y & 0x38) >> 3))
        for x in range(32):
            byte = data[real_y * 32 + x]
            for bit in range(8):
                pixel_data[y, x * 8 + (7 - bit)] = 255 if (byte & (1 << bit)) else 0
    
    # Decode attribute data (last 768 bytes)
    attr_data[:] = np.frombuffer(data[6144:], dtype=np.uint8).reshape((24, 32))
    
    return pixel_data, attr_data

def apply_attributes(pixel_data, attr_data):
    """Apply attribute colors to the pixel data."""
    image_data = np.zeros((192, 256, 3), dtype=np.uint8)
    ink_colors = [
        (0, 0, 0), (0, 0, 205), (205, 0, 0), (205, 0, 205),
        (0, 205, 0), (0, 205, 205), (205, 205, 0), (205, 205, 205)
    ]
    bright_colors = [
        (0, 0, 0), (0, 0, 255), (255, 0, 0), (255, 0, 255),
        (0, 255, 0), (0, 255, 255), (255, 255, 0), (255, 255, 255)
    ]
    
    for attr_y in range(24):
        for attr_x in range(32):
            attr = attr_data[attr_y, attr_x]
            ink = attr & 0x07
            paper = (attr >> 3) & 0x07
            bright = (attr >> 6) & 0x01
            flash = (attr >> 7) & 0x01  # Ignored in this static rendering
            
            ink_color = bright_colors[ink] if bright else ink_colors[ink]
            paper_color = bright_colors[paper] if bright else ink_colors[paper]
            
            for y in range(8):
                for x in range(8):
                    px = attr_x * 8 + x
                    py = attr_y * 8 + y
                    image_data[py, px] = ink_color if pixel_data[py, px] else paper_color
    
    return image_data

def open_file():
    filename = filedialog.askopenfilename(filetypes=[("ZX Spectrum Screen", "*.scr")])
    if filename:
        display_spectrum_scr(filename)

def display_spectrum_scr(filename):
    pixel_data, attr_data = load_spectrum_scr(filename)
    image_data = apply_attributes(pixel_data, attr_data)
    image = Image.fromarray(image_data, 'RGB')
    image = image.resize((512, 384), Image.NEAREST)  # Scale up for visibility
    img_tk = ImageTk.PhotoImage(image)
    
    label.config(image=img_tk)
    label.image = img_tk

def create_gui():
    global label
    root = tk.Tk()
    root.title("ZX Spectrum SCR Viewer")
    
    btn_open = tk.Button(root, text="Open .SCR File", command=open_file)
    btn_open.pack()
    
    label = tk.Label(root)
    label.pack()
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
