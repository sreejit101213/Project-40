import tkinter as tk

# Function to convert inches to cm
def convert_length():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except:
        result_label.config(text="Invalid input")

# Create window
window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")
window.configure(bg="#ffe5e5")  # light red background

# Title label
title_label = tk.Label(window, text="Length Converter", font=("Arial", 16, "bold"), bg="#ffe5e5", fg="#b30000")
title_label.pack(pady=20)

# Input label
input_label = tk.Label(window, text="Enter length in inches:", font=("Arial", 12), bg="#ffe5e5", fg="#800000")
input_label.pack()

# Entry box (Courier)
entry = tk.Entry(window, font=("Courier New", 12), bd=2, relief="solid")

entry.pack(pady=10)

# Convert button
convert_button = tk.Button(window, text="Convert to cm", font=("Arial", 12, "bold"), bg="#cc0000", fg="white", activebackground="#990000", command=convert_length)
convert_button.pack(pady=10)

# Result label (Courier)
result_label = tk.Label(window, text="", font=("Courier New", 14, "bold"), bg="#ffe5e5", fg="#b30000")
result_label.pack(pady=20)

# Run app
window.mainloop()