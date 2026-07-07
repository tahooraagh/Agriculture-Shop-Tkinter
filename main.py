"""
==========================================
       فروشگاه ابزار کشاورزی 🌾
==========================================

پروژه پایان‌ترم درس کامپیوتر

طراح: طهورا آقایی

زبان برنامه‌نویسی:
Python

کتابخانه:
Tkinter

==========================================
"""
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox 
import time 

#ساخت صفحه اصلی پروژه

window = tk.Tk()

window.title("فروشگاه ابزار کشاورزی🌾")

window.geometry("1200x750")

window.configure(bg="#F1F8E9")

window.resizable(False, False)

#هدر برنامه 

header = tk.Frame(
    window,
    bg="#2E7D32",
    height=90
)

header.pack(fill="x")

title = tk.Label(
    header,
    text="فروشگاه ابزار کشاورزی🌾",
    bg="#2E7D32",
    fg="white",
    font=("Helvetica", 24, "bold")
)
title.pack(side="left", padx=20, pady=20)

today = time.strftime("%Y/%m/%d")

date_Label= tk.Label(
    header,
    text=f"📅{today}",
    bg="#2E7D32",
    fg="white",
    font=("Helvetica", 24, "bold")
)
date_Label.pack(side="right", padx=20)

invoice_number=int(time.time())

invoice_label = tk.Label(
    header, 
    text=f"شماره فاکتور : {invoice_number}",
    bg="#2E7D32",
    fg="white",
    font=("Helvetica", 14)
)

invoice_label.pack(side="right", padx=20)

#فرم اطلاعات مشتری 

customer_frame = tk.LabelFrame(
    window,
    text="اطلاعات مشتری 👤",
    font=("Arial", 14, "bold"),
    bg="#F1F8E9", 
    fg="black",
    padx=15,
    pady=15
)
customer_frame.pack(fill="x", padx=20, pady=15)

tk.Label(
    customer_frame,
    text="نام مشتری",
    bg="#F1F8E9",
    fg="black",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10)

name_entry = tk.Entry(
    customer_frame,
    width=25,
    font=("Arial", 12)
)
name_entry.grid(row=0,
                 column=1,
                 padx=10,
                 ipady=4
)

tk.Label(
    customer_frame,
    text="شماره تماس",
    bg="#F1F8E9",
    fg="black",
    font=("Arial", 12)
).grid(row=0, column=2, padx=10)

phone_entry = tk.Entry(
    customer_frame,
    width=25,
    font=("Arial", 12)
)

phone_entry.grid(row=0, column=3, padx=10)

tk.Label(
    customer_frame,
    text="استان",
    bg="#F1F8E9",
    fg="black",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=10)

province_combo = ttk.Combobox(
    customer_frame,
    width=25,
    state="readonly"
)
province_combo["values"]=(
    "تهران",
    "اصفهان",
    "فارس",
    "خراسان رضوی",
    "گیلان",
    "مازندران",
    "آذربایجان شرقی",
)
province_combo.current(0)

province_combo.grid(row=1, column=1, padx=10)

tk.Label(
    customer_frame,
    text="آدرس",
    bg="#F1F8E9",
    fg="black",
    font=("Arial", 12)
).grid(row=1, column=2, padx=10)

address_entry = tk.Entry(
    customer_frame,
    width=40,
    font=("Arial", 12)
)
address_entry.grid(row=1, column=3, padx=10)

#فرم اطلاعات کالا 

item_frame = tk.LabelFrame(
    window,
    text="اطلاعات کالا🌾",
    font=("Arial", 14, "bold"),
    bg="#F1F8E9",
    fg="black",
    padx=15,
    pady=15
)

item_frame.pack(fill="x", padx=20, pady=10)

tk.Label(
    item_frame,
    text="نام کالا",
    bg="#F1F8E9",
    fg="black",
    font=("Arial, 12")
).grid(row=0, column=0, padx=10, pady=10)

item_entry = tk.Entry(
    item_frame,
    width=20,
    font=("Arial", 12)
)
item_entry.grid(row=0, column=1, padx=10)

tk.Label(
    item_frame,
    text="تعداد",
    bg="#F1F8E9",
    fg="black",
    font=("Arial", 13)
).grid(row=0, column=2, padx=10)

quantity_entry = tk.Entry(
    item_frame,
    width=10,
    font=("Arial", 12)
)
quantity_entry.grid(row=0, column=3, padx=10)

tk.Label(
    item_frame,
    text="قیمت",
    bg="#F1F8E9",
    fg="black",
    font=("Arial", 12),
).grid(row=0, column=4, padx=10)

price_entry = tk.Entry(
    item_frame,
    width=15,
    font=("Arial", 12)
)

price_entry.grid(row=0, column=5, padx=10)

add_btn = tk.Button(
    item_frame,
    text="افزودن کالا➕",
    bg="#2E7D32",
    fg="black",
    font=("Arial", 12, "bold"),
)

add_btn.grid(row=0, column=6, padx=20)


search_frame = tk.Frame(
    window,
    bg="#F1F8E9"
)

search_frame.pack(fill="x", padx=20, pady=5)

#بخش جستجوی کالا

tk.Label(
    search_frame,
    text="🔍 جستجوی کالا:",
    bg="#F1F8E9",
    fg="black",
    font=("Arial",12,"bold")
).pack(side="left")

search_entry = tk.Entry(
    search_frame,
    width=30,
    font=("Arial",12)
)

search_entry.pack(side="left", padx=10)

search_btn = tk.Button(
    search_frame,
    text="جستجو",
    bg="#1976D2",
    fg="black",
    font=("Arial",11,"bold")
)

search_btn.pack(side="left")

table_frame = tk.Frame(window, bg="#F1F8E9")
table_frame.pack(fill="both", padx=20, pady=10)

columns = (
    "name" ,
    "quantity" , 
    "price" , 
    "total" ,
)

#جدول نمایش کالا 

table = ttk.Treeview(
    table_frame,
    columns=columns, 
    show="headings",
    height=8
    
)

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical"
)
scrollbar.config(command=table.yview)

table.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")

table.heading("name", text="نام کالا")
table.heading("quantity", text="تعداد")
table.heading("price", text="قیمت واحد")
table.heading("total", text="مبلغ کل")

table.column("name", width=250, anchor="center")

table.column("quantity", width=100, anchor="center")

table.column("price", width=180, anchor="center")

table.column("total", width=180, anchor="center")

table.pack(fill="x")


def add_item():

    name = item_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    if name == "" or quantity == "" or price == "":
        messagebox.showwarning("خطا", "تمام فیلدها را پر کنید.")
        return

    total = int(quantity) * int(price)

    table.insert(
        "",
        "end",
        values=(name, quantity, price, total)
    )

    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    calculate_total()
    status_var.set(f"✅ کالا '{name}' با موفقیت اضافه شد.")
    

def delete_item():

    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "خطا",
            "ابتدا یک کالا را انتخاب کنید."
        )
        return

    table.delete(selected)
    
    
    calculate_total()
add_btn.config(command=add_item)

delete_btn = tk.Button(
    item_frame,
    text="🗑 حذف کالا",
    bg="#D32F2F",
    fg="black",
    font=("Arial",12,"bold"),
    width=12,
    command=delete_item
)

delete_btn.grid(row=0,column=7,padx=10)

edit_btn = tk.Button(
    item_frame,
    text="✏️ ویرایش",
    bg="#F9A825",
    fg="black",
    font=("Arial",12,"bold"),
    width=12
)

edit_btn.grid(row=0, column=8, padx=10)

# ============================
# محاسبات فاکتور
# ============================

total_frame = tk.LabelFrame(
    window,
    text="💰 محاسبات فاکتور",
    font=("Arial",14,"bold"),
    bg="#F1F8E9",
    fg="black",
    padx=15,
    pady=15
)

total_frame.pack(fill="x", padx=20, pady=10)

total_var = tk.StringVar()
tax_var = tk.StringVar()
final_var = tk.StringVar()

total_var.set("0")
tax_var.set("0")
final_var.set("0")

tk.Label(
    total_frame,
    text="جمع کل:",
    bg="#F1F8E9",
    fg="black",
    font=("Arial",13,"bold")
).grid(row=0,column=0,padx=20,pady=10)

tk.Label(
    total_frame,
    textvariable=total_var,
    bg="#F1F8E9",
    fg="blue",
    font=("Arial",13,"bold")
).grid(row=0,column=1)

tk.Label(
    total_frame,
    text="مالیات (9٪):",
    bg="#F1F8E9",
    fg="black",
    font=("Arial",13,"bold")
).grid(row=0,column=2,padx=20)

tk.Label(
    total_frame,
    textvariable=tax_var,
    bg="#F1F8E9",
    fg="red",
    font=("Arial",13,"bold")
).grid(row=0,column=3)

tk.Label(
    total_frame,
    text="مبلغ نهایی:",
    bg="#F1F8E9",
    fg="black",
    font=("Arial",13,"bold")
).grid(row=0,column=4,padx=20)

tk.Label(
    total_frame,
    textvariable=final_var,
    bg="#F1F8E9",
    fg="green",
    font=("Arial",13,"bold")
).grid(row=0,column=5)

def calculate_total():

    total = 0

    for row in table.get_children():

        values = table.item(row)["values"]

        total += int(values[3])

    tax = total * 0.09

    final = total + tax

    total_var.set(f"{total:,}")

    tax_var.set(f"{tax:,.0f}")

    final_var.set(f"{final:,.0f}")

def select_item(event):

    selected = table.focus()

    if selected == "":
        return

    values = table.item(selected, "values")

    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

    item_entry.insert(0, values[0])
    quantity_entry.insert(0, values[1])
    price_entry.insert(0, values[2])
table.bind("<<TreeviewSelect>>", select_item)
    
def edit_item():

    selected = table.focus()

    if selected == "":
        messagebox.showwarning(
            "خطا",
            "ابتدا یک کالا را انتخاب کنید."
        )
        return

    name = item_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    if name == "" or quantity == "" or price == "":
        messagebox.showwarning(
            "خطا",
            "تمام فیلدها را پر کنید."
        )
        return

    total = int(quantity) * int(price)

    table.item(
        selected,
        values=(name, quantity, price, total)
    )

    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    calculate_total()
    status_var.set("🗑 کالا حذف شد.")

edit_btn.config(command=edit_item)

def new_invoice():

    # پاک کردن اطلاعات مشتری
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

    province_combo.current(0)

    # پاک کردن اطلاعات کالا
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

    # پاک کردن جدول
    for item in table.get_children():
        table.delete(item)

    # صفر کردن محاسبات
    total_var.set("0")
    tax_var.set("0")
    final_var.set("0")

button_frame = tk.Frame(
    window,
    bg="#F1F8E9"
)

button_frame.pack(pady=15)

new_btn = tk.Button(
    button_frame,
    text="🆕 فاکتور جدید",
    bg="#1976D2",
    fg="black",
    font=("Arial",12,"bold"),
    width=15,
    command=new_invoice
)

new_btn.grid(row=0, column=0, padx=10)

def save_invoice():

    if len(table.get_children()) == 0:
        messagebox.showwarning(
            "خطا",
            "هیچ کالایی در فاکتور وجود ندارد."
        )
        return

    messagebox.showinfo(
        "ثبت فاکتور",
        "✅ فاکتور با موفقیت ثبت شد."
    )
save_btn = tk.Button(
    button_frame,
    text="✅ ثبت",
    bg="#388E3C",
    fg="black",
    font=("Arial",12,"bold"),
    width=12,
    command=save_invoice
)

save_btn.grid(row=0, column=1, padx=10)

def print_invoice():

    if len(table.get_children()) == 0:
        messagebox.showwarning(
            "خطا",
            "فاکتور خالی است."
        )
        return

    print("========== فاکتور فروش ==========")
    print("نام مشتری:", name_entry.get())
    print("شماره تماس:", phone_entry.get())
    print("استان:", province_combo.get())
    print("آدرس:", address_entry.get())
    print("--------------------------------")

    for row in table.get_children():

        values = table.item(row)["values"]

        print(
            values[0],
            values[1],
            values[2],
            values[3]
        )

    print("--------------------------------")
    print("جمع کل:", total_var.get())
    print("مالیات:", tax_var.get())
    print("مبلغ نهایی:", final_var.get())

    messagebox.showinfo(
        "چاپ",
        "🖨 اطلاعات فاکتور در ترمینال چاپ شد."
    )
print_btn = tk.Button(
    button_frame,
    text="🖨 چاپ",
    bg="#6A1B9A",
    fg="black",
    font=("Arial",12,"bold"),
    width=12,
    command=print_invoice
)

print_btn.grid(row=0, column=2, padx=10)

def exit_program():

    answer = messagebox.askyesno(
        "خروج",
        "آیا مطمئن هستید که می‌خواهید خارج شوید؟"
    )

    if answer:
        window.destroy()

exit_btn = tk.Button(
    button_frame,
    text="خروج",
    bg="#C62828",
    fg="black",
    font=("Arial",12,"bold"),
    width=12,
    command=exit_program
)

exit_btn.grid(row=0, column=3, padx=10)

status_var = tk.StringVar()
status_var.set("🌾 برنامه آماده ثبت فاکتور است.")

status_bar = tk.Label(
    window,
    textvariable=status_var,
    bg="#2E7D32",
    fg="white",
    font=("Arial", 11),
    anchor="w",
    padx=10
)

status_bar.pack(side="bottom", fill="x")

def show_statistics():

    count = len(table.get_children())

    messagebox.showinfo(
        "📊 آمار فروش",
        f"""
تعداد کالاها : {count}

جمع کل : {total_var.get()} تومان

مالیات : {tax_var.get()} تومان

مبلغ نهایی : {final_var.get()} تومان
"""
    )
time_label = tk.Label(
    header,
    bg="#2E7D32",
    fg="white",
    font=("Helvetica",13,"bold")
)

time_label.pack(side="right", padx=20)

stats_btn = tk.Button(
    button_frame,
    text="📊 آمار",
    bg="#00897B",
    fg="black",
    font=("Arial",12,"bold"),
    width=12,
    command=show_statistics
)

stats_btn.grid(row=0, column=4, padx=10)

def update_clock():

    current = time.strftime("%H:%M:%S")

    time_label.config(text=f"🕒 {current}")

    window.after(1000, update_clock)

update_clock()









window.mainloop()
