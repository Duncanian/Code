# pyinstaller --onefile --windowed VolumeSizer.py
import tkinter as tk
import locale

locale.setlocale(locale.LC_ALL, '')

# Configure the window
window = tk.Tk()
window.geometry("500x510")
window.configure(background="turquoise")
window.title("VOLUME SIZER v1.0")


def calculate_volume():
    try:
        pip_value = float(pip_value_entry.get())
        percentage = float(percentage_entry.get())
        breather = float(breather_entry.get())
        balance = float(balance_entry.get())

        perc = percentage / 100
        breather_value = breather * pip_value
        risk_capital = perc * balance
        raw_volume = risk_capital / breather_value
        volume = round(raw_volume, 2)

        result = f"""\nBalance: Ksh.{round(balance * 100, 2):n} \n\nRisk capital: Ksh.{round(risk_capital * 100, 2):n} \n\nVolume: {volume} \n\nRaw: ({raw_volume})\n"""  # noqa E501

        # Displays the results
        text_answer = tk.Text(master=window, height=12, width=25, font=('arial', 15, 'bold'))  # noqa E501
        text_answer.grid(column=1, row=6)
        text_answer.insert(tk.END, result)
    except Exception as e:
        print(e)


pip_value_label = tk.Label(text="Pip Value", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='turquoise')  # noqa E501
pip_value_label.grid(column=0, row=1)

pip_value_entry = tk.Entry()
pip_value_entry.grid(column=1, row=1, padx=10, pady=10)

percentage_label = tk.Label(text="Percentage (#)", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='turquoise')  # noqa E501
percentage_label.grid(column=0, row=2)

percentage_entry = tk.Entry()
percentage_entry.grid(column=1, row=2, padx=10, pady=10)

breather_label = tk.Label(text="Breather Pips", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='turquoise')  # noqa E501
breather_label.grid(column=0,row=3)

breather_entry = tk.Entry()
breather_entry.grid(column=1, row=3, padx=10, pady=10)

balance_label = tk.Label(text="Acc Balance ($)", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='turquoise')  # noqa E501
balance_label.grid(column=0, row=4)

balance_entry = tk.Entry()
balance_entry.grid(column=1, row=4, padx=10, pady=10)

calc_button =tk.Button(window, command=calculate_volume, text="Calculate", padx=10, pady=6, fg='black', font=('arial', 15,'bold'), bg='khaki')  # noqa E501
calc_button.grid(column=1, row=5)


window.mainloop()
