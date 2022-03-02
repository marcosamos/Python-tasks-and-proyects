import tkinter as tk
import number_entry as numy
from math import pi

def main():
    # Create the Tk root object.
    root = tk.Tk()

    window = tk.Frame(root)
    window.master.title("Area of a circle")
    window.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    labels_window(window)

    root.mainloop()

variable = "Area is equal to π(3.1416) times radius squared"

def labels_window(window):
    # labels
    introduction = tk.Label(window, text="In this activity we go to compute the area of a circle, this is the formula")
    circle_formula = tk.Label(window, text="Formula of a circle: a = π * (r**2)")
    formula_explanation = tk.Label(window, text= variable)
    indication = tk.Label(window, text="Please enter a number radius")
    ent_radius = numy.IntEntry(window, 1, 10000, width=5)
    text_result = tk.Label(window, text="Result :")
    result = tk.Label(window, width=8,fg="green")
    clear_buttom = tk.Button(window, text="Clear",width=12,bg="red")


    # Layout all the labels, entry boxes, and buttons in a grid.
    introduction.grid(  row=0, column=0, padx=3, pady=3)
    circle_formula.grid(  row=1, column=0, padx=3, pady=3)
    formula_explanation.grid(row=2, column=0, padx=3, pady=3)
    indication.grid(row=3, column=0, padx=3, pady=3)
    ent_radius.grid(row=3, column=1, padx=3, pady=3)
    text_result.grid(row=4, column=0,padx=3, pady=3)
    result.grid(row=4,column=1, padx=3,pady=3)
    clear_buttom.grid(row=5, column=0,padx=3,pady=3)


    def calc(event):
        try:
            radius = ent_radius.get()
            compute_result = pi * (radius**2)
            result.config(text=f"{compute_result:.2f}")
        except ValueError:
            # When the user deletes all the digits in the radius
            # entry box, clear the result
            result.config(text="")
            
    def clear():
        """Clear all the inputs and outputs."""
        ent_radius.delete(0, tk.END)
        result.config(text="")
        ent_radius.focus()


    ent_radius.bind("<KeyRelease>", calc)
    clear_buttom.config(command=clear)
    ent_radius.focus()
    
    


if __name__ == "__main__":
    main()