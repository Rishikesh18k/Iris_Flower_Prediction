from customtkinter import *
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import warnings
win = CTk()
win.title("Iris flower Classification")
win.geometry("343x610+500+40")
win.resizable(False, False)
win.config(bg="#333333")
def get_value():
    warnings.filterwarnings("ignore")
    sl = eval(sepal_length_value.get())
    sw = eval(sepal_width_value.get())
    pl = eval(petal_length_value.get())
    pw = eval(petal_width_value.get())
    load_data = load_iris()
    file = pd.DataFrame(load_data.data, columns=load_data.feature_names)
    file["species"] = load_data.target
    x = file.drop("species",axis=1)
    y = file["species"]
    train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2)
    model = KNeighborsClassifier()
    model.fit(train_x,train_y)
    prediction_value = model.predict([[sl,sw,pl,pw]])
    score_price = model.score(test_x,test_y)
    score = (score_price*100)
    if int(prediction_value[0])==0:
        iris_value.configure(text="Iris Setosa", text_color="#F5F5FA", font=("Franklin Gothic Demi Cond", 18))
    elif int(prediction_value[0])==1:
        iris_value.configure(text="Iris Versicolor", text_color="#F5F5FA", font=("Franklin Gothic Demi Cond", 18))
    elif int(prediction_value[0])==2:
        iris_value.configure(text="Iris Virginica", text_color="#F5F5FA", font=("Franklin Gothic Demi Cond", 18))
    else:
        iris_value.configure(text="None", text_color="#F5F5FA", font=("Franklin Gothic Demi Cond", 18))
    percentage_value.configure(text=f"{round(score, )}.00%", text_color="#F5F5FA", font=("Franklin Gothic Demi Cond", 20))
def clear():
    iris_value.delete(0, END)
    sepal_length_entry.delete(0, END)
    sepal_width_entry.delete(0, END)
    petal_length_entry.delete(0, END)
    petal_width_entry.delete(0, END)
    iris_value.configure(text="----------", font=("Franklin Gothic Demi Cond", 22), text_color="#737373")
    percentage_value.configure(text="000%", font=("Franklin Gothic Demi Cond", 22), text_color="#737373")
message_label = CTkLabel(win, text="Enter sepal length (cm)", font=("Franklin Gothic Demi Cond",16),
                         text_color="#EEEEEE", fg_color="#333333")
message_label.place(x=98, y=30)
message_label_x = CTkLabel(win, text="⬇", font=("Franklin Gothic Demi Cond", 20),
                           text_color="#EEEEEE", fg_color="#333333")
message_label_x.place(x=246, y=34)
sepal_length_value = StringVar()
sepal_length_entry = CTkEntry(win, text_color="#EEEEEE", font=("Franklin Gothic Demi Cond", 18), bg_color="#333333",
                       height=35, width=246, border_width=1.50, border_color="#737373",
                       corner_radius=4, fg_color="#444444", textvariable=sepal_length_value)
sepal_length_entry.place(x=50, y=60)
sepal_width_label = CTkLabel(win, text="Enter sepal width (cm)", font=("Franklin Gothic Demi Cond", 16),
                         text_color="#EEEEEE", fg_color="#333333")
sepal_width_label.place(x=98, y=110)
sepal_width_value = StringVar()
sepal_width_entry = CTkEntry(win, text_color="#EEEEEE", font=("Franklin Gothic Demi Cond", 18), bg_color="#333333",
                         height=35, width=246, border_width=1.50, border_color="#737373",
                         corner_radius=4, fg_color="#444444", textvariable=sepal_width_value)
sepal_width_entry.place(x=50, y=140)
petal_length_label = CTkLabel(win, text="Enter petal length (cm)", font=("Franklin Gothic Demi Cond", 16),
                     text_color="#EEEEEE", fg_color="#333333")
petal_length_label.place(x=98, y=185)
petal_length_value = StringVar()
petal_length_entry = CTkEntry(win, text_color="#EEEEEE", font=("Franklin Gothic Demi Cond", 16), bg_color="#333333",
                     height=35, width=246, border_width=1.50, border_color="#737373",
                     corner_radius=4, fg_color="#444444", textvariable=petal_length_value)
petal_length_entry.place(x=50, y=215)
petal_width_label = CTkLabel(win, text="Enter petal length (cm)", font=("Franklin Gothic Demi Cond", 16),
                     text_color="#EEEEEE", fg_color="#333333")
petal_width_label.place(x=98, y=260)
petal_width_value = StringVar()
petal_width_entry = CTkEntry(win, text_color="#EEEEEE", font=("Franklin Gothic Demi Cond", 16), bg_color="#333333",
                     height=35, width=246, border_width=1.50, border_color="#737373",
                     corner_radius=4, fg_color="#444444", textvariable=petal_width_value)
petal_width_entry.place(x=50, y=290)
done_btn = CTkButton(win, text="Done", font=("Franklin Gothic Demi Cond", 20), height=40,
                         width=120, text_color="#FFFFFF", fg_color="#009900", corner_radius=4,
                         border_color="#EEEEEE", border_width=1, hover_color="#00cc00",
                         cursor="hand2",command=get_value)
done_btn.place(x=50, y=335)
clear_btn = CTkButton(win, text="Clear", font=("Franklin Gothic Demi Cond", 18), height=40,
                      width=120, text_color="#000000", fg_color="#EEEEEE", corner_radius=4,
                      border_color="#EEEEEE", border_width=1, hover_color="#ffffff",
                      cursor="hand2", command=clear)
clear_btn.place(x=176, y=335)
details_frame = CTkFrame(win, width=246, height=195, fg_color="#404040", border_width=2,
                         border_color="#737373", bg_color="#333333")
iris_tittle = CTkLabel(details_frame, text="______Iris flower status______", font=("Franklin Gothic Demi Cond", 17),
                        width=242, text_color="#d9d9d9")
iris_tittle.place(x=2, y=15)
iris_value = CTkLabel(details_frame, text="----------", font=("Franklin Gothic Demi Cond", 22),
                       width=242, text_color="#737373")
iris_value.place(x=2, y=55)
percentage_tittle = CTkLabel(details_frame, text="______Accurate (%)______", font=("Franklin Gothic Demi Cond", 17),
                             width=242, text_color="#d9d9d9")
percentage_tittle.place(x=2, y=100)
percentage_value = CTkLabel(details_frame, text="000%", font=("Franklin Gothic Demi Cond", 22),
                            width=242, text_color="#737373")
percentage_value.place(x=2, y=140)
details_frame.place(x=50, y=388)
win.mainloop()