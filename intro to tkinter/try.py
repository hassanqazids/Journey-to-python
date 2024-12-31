
import tkinter as tk
def calculator(operation):
    try:

        num1 = int(entry1.get())
        num2 = int(entry2.get())

        # Perform the selected operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            result = "Invalid operation"

        # Display result in the label
        result_label.config(text=f"Result: {result}")

    # Handle errors
    except ValueError:
        result_label.config(text="Invalid Input")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero")
        
# GUI Setup
window = tk.Tk()
window.title("Simple Calculator")


tk.Label(window, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Number 2:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=10)


tk.Button(window, text="+", command=lambda: calculator('+'))    .grid(row=2, column=0, padx=5, pady=5)
tk.Button(window, text="-", command=lambda: calculator('-'))
tk.Button(window, text="*", command=lambda: calculator('*'))
tk.Button(window, text="/", command=lambda: calculator('/')).grid(row=2, column=1, padx=5, pady=5)
.grid(row=2, column=2, padx=5, pady=5)
.grid(row=2, column=3, padx=5, pady=5)




result_label = tk.Label(window, text="Result: ")
result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)


window.mainloop()

