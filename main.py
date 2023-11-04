from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(height=200,width=300)
window.update()

screen_x = window.winfo_width()
screen_y = window.winfo_height()
window.config(pady=25)

labelWeight = Label(text="Weight (Kg.)")
labelWeight.update()
labelWeight.pack()

entryWeight = Entry(width=15)
entryWeight.update()
entryWeight.pack()

labelHeight = Label(text="Height (cm.)")
labelHeight.update()
labelHeight.pack()

entryHeight = Entry(width=15)
entryHeight.update()
entryHeight.pack()

def bmi_calculate():
    weight = entryWeight.get()
    height = entryHeight.get()
    if weight == "" or height == "":
        resultLabel.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            resultLabel.config(text=write_result(bmi))
        except:
            resultLabel.config(text="Enter a valid number!")

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string

button = Button(text="Calculate",command=bmi_calculate)
button.update()
button.pack()

resultLabel = Label(text="")
resultLabel.pack()
window.mainloop()