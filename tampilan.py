# saya makhi zainul urfi mengerjakan TP3
# dalam mata kuliah DPBO untuk keberkahan-Nya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.
from tkinter import*
import tkinter.messagebox
import tkinter.font
from tkinter.messagebox import askyesno, askquestion

root = Tk()
root.title("INDekos")

####################################define nama, no telp, profesi##################################
lnama = Label(root, text = "Nama")
lnama.grid(row = 0, column = 0)
# lnama.pack()

lno_telp = Label(root, text = "No Telepon")
lno_telp.grid(row = 1, column = 0)
# lno_telp.pack()

lprofesi = Label(root, text = "Profesi")
lprofesi.grid(row = 2, column = 0)
# lprofesi.pack()

#######################################define inputan###########################################
nama_isi = StringVar()
nama_input = Entry(root, textvariable = nama_isi)
nama_input.grid(row = 0, column = 1, columnspan = 2)
# nama_input.pack()

no_telp_isi = StringVar()
no_telp_input = Entry(root, textvariable = no_telp_isi)
no_telp_input.grid(row = 1, column = 1, columnspan = 2)
# no_telp_input.pack()

profesi_isi = StringVar()
profesi_input = Entry(root, textvariable = profesi_isi)
profesi_input.grid(row = 2, column = 1, columnspan = 2)
# profesi_input.pack()

#############################################define jenis kelamin (radio)#########################################
ljk = Label(root, text = "Jenis Kelamin")
ljk.grid(row = 3, column = 0)
# ljk.pack()

# jeniskelamin = [
# 	("L", "Laki - laki"),
# 	("P", "Perempuan")
# ]

jk = StringVar()
jk.set("Laki-laki")

Radiobutton(root, text="L", variable=jk, value="Laki-laki").grid(row = 3, column = 1)
Radiobutton(root, text="P", variable=jk, value="Perempuan").grid(row = 3, column = 2)

#############################################define lama tinggal (combo box)########################################
ltinggal = Label(root, text = "Lama tinggal")
ltinggal.grid(row = 4, column = 0)
# ltinggal.pack()

# lama = [
# 	("6 bulan", "6 bulan"),
# 	("1 tahun, 1 tahun"),
# 	("2 tahun, 2 tahun"),
# 	("> 2 tahun", "> 2 tahun")
# ]

tinggal = StringVar()
tinggal.set("6 bulan")

pil1 = IntVar()
pil2 = IntVar()
pil3 = IntVar()
pil4 = IntVar()

Checkbutton(root, text="6 bulan", variable=pil1, onvalue=1, offvalue=0).grid(row = 4, column = 1)
Checkbutton(root, text="1 tahun", variable=pil2, onvalue=1, offvalue=0).grid(row = 5, column = 1)
Checkbutton(root, text="2 tahun", variable=pil3, onvalue=1, offvalue=0).grid(row = 6, column = 1)
Checkbutton(root, text="> 2 tahun", variable=pil4, onvalue=1, offvalue=0).grid(row = 7, column = 1)

# i=4
# for i in range(3):
# 	for text, topping, in lama:
#     	Radiobutton(root, text=text, variable=tinggal, value=topping).grid(column = 1, row = i+3)


###########################################define status(dropdown)#############################################
lstatus = Label(root, text = "Status")
lstatus.grid(row = 8, column = 0)
# lstatus.pack()

def show():
    myLabel = Label(root, text=clicked.get()).grid(row = 7)
    # myLabel = Label(root, text=clicked.get()).pack()

options = [
	"Jomblo",
	"Menikah",
	"Cari Jodoh",
	"Santai"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.grid(row = 8, column = 1, columnspan = 2)
# drop.pack()

# myButton = Button(root, text="Show Selection", command=show)
# myButton.grid(row = 6, column = 0)

########################################define submit############################
submit = Button(root, text = "submit", bg = "green")
submit.grid(row = 9, column = 1, columnspan = 2)


#####################################define nama aplikasi#########################################
judul = Label(root, text = "INDEkos")
judul.grid(row = 0, column = 3)
# judul.pack()

desc = Label(root, text = "kosan berbasis Python (administrasinya doang)", height = 2)
desc.grid(row = 1, column = 3)
# desc.pack()

##############################################define show all, delete, about########################################


show = Button(root, text = "Liat Tetangga")
show.grid(row = 3, column = 3)
# show.pack()

show1 = Button(root, text = "Hapus Semua")
show1.grid(row = 4, column = 3)
# show1.pack()

def tentang():
    tkinter.messagebox.showinfo("Tentang",  "Halo calon penghuni silahkan isi data, ato bisa klik Liat Tetangga barangkali ada temen disini")

show2 = Button(root, text = "Tentang", command = tentang)
show2.grid(row = 5, column = 3)
# show.pack()

#############################################define exit###################################################
def confirm():
    answer = askyesno(title='Konfirmasi',
                    message='Yakin mau keluar?')
    if answer:
        root.destroy()

keluar = Button(root, text = "exit", command = confirm, bg = "red", fg = "white")
keluar.grid(row = 9, column = 3)

root.mainloop()