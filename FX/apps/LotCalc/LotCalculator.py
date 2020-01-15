# pyinstaller --onefile --windowed LotCalculator.py
import tkinter as tk
import locale

locale.setlocale(locale.LC_ALL, '')

# Configure the window
window = tk.Tk()
window.geometry("500x510")
window.configure(background="OliveDrab1")
window.title("LOT CALCULATOR v1.0")


def calculate_lot():
    try:
        pip_value = float(pip_value_entry.get())
        max_risk = float(max_risk_entry.get())
        sl_pips = float(sl_pips_entry.get())
        tp_pips = float(tp_pips_entry.get())

        risk_reward = round(tp_pips / sl_pips, 2)
        raw_volume = max_risk / (sl_pips * pip_value)
        volume = round(raw_volume, 2)
        result = f"""\nR/R ratio: {risk_reward} \n\nMax risk: Ksh.{max_risk * 100 :n} \n\nMax win: Ksh.{(max_risk * risk_reward) * 100 :n} \n\nVolume: {volume} \n\nRaw: ({raw_volume})\n"""  # noqa E501

        # Displays the results
        text_answer = tk.Text(master=window, height=12, width=25, font=('arial', 15, 'bold'))  # noqa E501
        text_answer.grid(column=1, row=6)
        text_answer.insert(tk.END, result)
    except Exception as e:
        print(e)


pip_value_label = tk.Label(text="Pip Value", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='OliveDrab1')  # noqa E501
pip_value_label.grid(column=0, row=1)

pip_value_entry = tk.Entry()
pip_value_entry.grid(column=1, row=1, padx=10, pady=10)

max_risk_label = tk.Label(text="Max Risk ($)", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='OliveDrab1')  # noqa E501
max_risk_label.grid(column=0, row=2)

max_risk_entry = tk.Entry()
max_risk_entry.grid(column=1, row=2, padx=10, pady=10)

sl_pips_label = tk.Label(text="SL Pips", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='OliveDrab1')  # noqa E501
sl_pips_label.grid(column=0,row=3)

sl_pips_entry = tk.Entry()
sl_pips_entry.grid(column=1, row=3, padx=10, pady=10)

tp_pips_label = tk.Label(text="TP Pips", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='OliveDrab1')  # noqa E501
tp_pips_label.grid(column=0, row=4)

tp_pips_entry = tk.Entry()
tp_pips_entry.grid(column=1, row=4, padx=10, pady=10)

calc_button =tk.Button(window, command=calculate_lot, text="Calculate", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='khaki')  # noqa E501
calc_button.grid(column=1, row=5)


window.mainloop()
