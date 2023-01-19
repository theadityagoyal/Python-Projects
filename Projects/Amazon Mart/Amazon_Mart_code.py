from tkinter import *
import random,time,os
from tkinter import messagebox



class Window1:

    def __init__(self, root):
        self.root = root
        self.root.title("WELCOME TO AMAZON MART")
        self.root.geometry('1531x800+0+0')

        self.root.configure(bg='black')

        self.frame = Frame(self.root, bg='black')
        self.frame.pack()


        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text='AMAZON MART', font=('Century', 45, 'bold'), bg='black',
                              fg='cyan')

        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=60)

        # ==============================================================================================================

        self.LoginFrame1 = LabelFrame(self.frame, font=('arial', 15, 'bold'),
                                      bg='black', bd=3)
        self.LoginFrame1.grid(row=2, column=1)

        self.LoginFrame2 = LabelFrame(self.frame, font=('arial', 20, 'bold'),
                                      bg='black', bd=0)
        self.LoginFrame2.grid(row=3, column=1)

        # ================================================= Label & Entry===============================================

        self.lblUsername = Label(self.LoginFrame1, text='Username', font=('arial', 20, 'bold'), bd=22, bg='black',
                                 fg='deeppink')
        self.lblUsername.grid(row=0, column=0)

        self.txtUsername = Entry(self.LoginFrame1, font=('century', 20), textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1, padx=119)

        self.lblPassword = Label(self.LoginFrame1, text='Password', font=('arial', 20, 'bold'), bd=22, bg='black',
                                 fg='deeppink')
        self.lblPassword.grid(row=1, column=0)

        self.txtPassword = Entry(self.LoginFrame1, font=('century', 20), show="*", textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1, columnspan=2, pady=30)

        # ====================================================  Button==================================================
        self.btnLogin = Button(self.LoginFrame2, text='Login', width=17, font=('arial', 20, 'bold'),bg='black',fg='red',
                               command=self.Login_System)
        self.btnLogin.grid(row=3, column=0, pady=30, padx=8)

        self.btnReset = Button(self.LoginFrame2, text='Reset', width=17, font=('arial', 20, 'bold'),bg='black',fg='red',
                               command=self.Reset)
        self.btnReset.grid(row=3, column=1, pady=30, padx=8)

    # ==================================================================================================================

    def Login_System(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u == str('Amazon') and p == str(12345)):
            self.newWindow = Toplevel(self.root)
            self.app = Bill_App(self.newWindow)

        else:
            messagebox.showerror("Login Systems", "Invalid login detail")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()


class Bill_App:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1531x800+0+0")
        self.root.title("Amazon mart")
        bg_color = "black"
        self.root.iconbitmap(r'mart.ico')
        self.root.config(background="black")
        date1 = StringVar()
        time1 = StringVar()

        date1.set(time.strftime("%a, %b %d, %Y"))
        time1.set(time.strftime("%I:%M:%S: %p"))



        title = Label(self.root, text="AMAZON MART ", bd=12, relief=GROOVE, bg=bg_color, fg="Red",
                      font=("century", 33, "bold"), pady=2).pack(fill=BOTH)
        title = Label(self.root, textvariable=time1, bd=4, bg=bg_color, fg="TOMATO",
                      font=("Bradley Hand ITC", 20, "bold"), pady=2).place(x=1340, y=20)
        title = Label(self.root, textvariable=date1, bd=4, bg=bg_color, fg="TOMATO",
                      font=("Bradley Hand ITC", 20, "bold"), pady=2).place(x=15, y=20)

        #    ++++++++++++++++++++++++++         """"" variables""""         ====================================

        #  _________________________________      KID ____________________________________
        self.baby_soap = IntVar()
        self.baby_cream = IntVar()
        self.babycare_kit = IntVar()
        self.baby_diapers = IntVar()
        self.baby_oil = IntVar()
        self.baby_blankets = IntVar()
        #  _________________________________       MEN    ____________________________________
        self.menbodycare_kit = IntVar()
        self.menshaving_kit = IntVar()
        self.men_wallet = IntVar()
        self.men_trimmers = IntVar()
        self.men_belts = IntVar()
        self.men_sunglasses = IntVar()

        #  _________________________________      WOMEN   _____________________________________
        self.makeup_kit = IntVar()
        self.womenskincare_kit = IntVar()
        self.women_purse = IntVar()
        self.women_perfumes = IntVar()
        self.women_haircarekit = IntVar()
        self.womencosmetic_kit = IntVar()

        # __________________________________     Total product price And Tax variable        ________________________
        self.total_kids_price = StringVar()
        self.total_men_price = StringVar()
        self.total_women_price = StringVar()

        self.total_kids_tax = StringVar()
        self.total_men_tax = StringVar()
        self.total_women_tax = StringVar()

        # _____________________________________   Customer details variables                 ______________________
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.search_bill = StringVar()

        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        # ========================      Custumor details Frame     =======================================

        f1 = LabelFrame(self.root, text="Customer Details", bg=bg_color, fg="gold", bd=10, relief=GROOVE,
                        font=("times new roman", 15, "bold"))
        f1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(f1, text="Customer Name", bg=bg_color, fg="white",
                          font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(f1, bg="white", fg="black", bd=7, relief=SUNKEN, width=15, textvariable=self.c_name,
                          font=("Century", 18, "bold")).grid(row=0, column=1, padx=10, pady=5)

        cphn_lbl = Label(f1, text="Phone number", bg=bg_color, fg="white",
                         font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(f1, bg="white", fg="black", bd=7, relief=SUNKEN, width=15, textvariable=self.c_phone,
                         font=("Century", 18, "bold")).grid(row=0, column=3, padx=10, pady=5)

        cbill_lbl = Label(f1, text="Bill number", bg=bg_color, fg="white",
                          font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(f1, bg="white", fg="black", bd=7, relief=SUNKEN, width=15, textvariable=self.search_bill,
                          font=("Century", 18, "bold")).grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(f1, text="SEARCH", command=self.find_bill, bd=7, bg=bg_color, width=11, fg="red",
                          font=("arial", 15, "bold")).grid(row=0, column=6, padx=10, pady=5)

        # =====================================  Kids Frame++++++============================

        f2 = LabelFrame(self.root, text="Kids", bg=bg_color, fg="gold", bd=10, relief=GROOVE,
                        font=("times new roman", 15, "bold"))
        f2.place(x=5, y=180, width=325, height=415)

        k1_lbl = Label(f2, text="Baby soap", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        k1_txt = Entry(f2, bd=5, relief=SUNKEN, width=7, textvariable=self.baby_soap,
                       font=("Century", 16, "bold")).grid(row=0, column=1, padx=10, pady=10)

        k2_lbl = Label(f2, text="Baby cream", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        k2_txt = Entry(f2, bd=5, relief=SUNKEN, width=7, textvariable=self.baby_cream,
                       font=("Century", 16, "bold")).grid(row=1, column=1, padx=10, pady=10)

        k3_lbl = Label(f2, text="Baby Care Kit", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        k3_txt = Entry(f2, bd=5, relief=SUNKEN, width=7, textvariable=self.babycare_kit,
                       font=("Century", 16, "bold")).grid(row=2, column=1, padx=10, pady=10)

        k4_lbl = Label(f2, text="Baby Diapers", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        k4_txt = Entry(f2, bd=5, relief=SUNKEN, width=7, textvariable=self.baby_diapers,
                       font=("Century", 16, "bold")).grid(row=3, column=1, padx=10, pady=10)

        k5_lbl = Label(f2, text="Baby Oil", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        k5_txt = Entry(f2, bd=5, relief=SUNKEN, width=7, textvariable=self.baby_oil,
                       font=("Century", 16, "bold")).grid(row=4, column=1, padx=10, pady=10)

        k6_lbl = Label(f2, text="Baby blankets", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        k6_txt = Entry(f2, bd=5, relief=SUNKEN, width=7, textvariable=self.baby_blankets,
                       font=("Century", 16, "bold")).grid(row=5, column=1, padx=10, pady=10)

        # =====================================  Men Frame++++++============================

        f3 = LabelFrame(self.root, text="Men", bg=bg_color, fg="gold", bd=10, relief=GROOVE,
                        font=("times new roman", 15, "bold"))
        f3.place(x=330, y=180, width=325, height=415)

        m1_lbl = Label(f3, text="Men face wash", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        m1_txt = Entry(f3, bd=5, relief=SUNKEN, width=7, textvariable=self.menbodycare_kit,
                       font=("Century", 16, "bold")).grid(row=0, column=1, padx=10, pady=10)

        m2_lbl = Label(f3, text="Shaving kit", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        m2_txt = Entry(f3, bd=5, relief=SUNKEN, width=7, textvariable=self.menshaving_kit,
                       font=("Century", 16, "bold")).grid(row=1, column=1, padx=10, pady=10)

        m3_lbl = Label(f3, text="Wallets", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        m3_txt = Entry(f3, bd=5, relief=SUNKEN, width=7, textvariable=self.men_wallet,
                       font=("Century", 16, "bold")).grid(row=2, column=1, padx=10, pady=10)

        m4_lbl = Label(f3, text="Trimmer", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        m4_txt = Entry(f3, bd=5, relief=SUNKEN, width=7, textvariable=self.men_trimmers,
                       font=("Century", 16, "bold")).grid(row=3, column=1, padx=10, pady=10)

        m5_lbl = Label(f3, text="Belt", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        m5_txt = Entry(f3, bd=5, relief=SUNKEN, width=7, textvariable=self.men_belts,
                       font=("Century", 16, "bold")).grid(row=4, column=1, padx=10, pady=10)

        m6_lbl = Label(f3, text="Sunglasses", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        m6_txt = Entry(f3, bd=5, relief=SUNKEN, width=7, textvariable=self.men_sunglasses,
                       font=("Century", 16, "bold")).grid(row=5, column=1, padx=10, pady=10)

        # =====================================  WOMEN Frame++++++============================

        f4 = LabelFrame(self.root, text="Women", bg=bg_color, fg="gold", bd=10, relief=GROOVE,
                        font=("times new roman", 15, "bold"))
        f4.place(x=655, y=180, width=325, height=415)

        w1_lbl = Label(f4, text="Makeup Kit", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        w1_txt = Entry(f4, bd=5, relief=SUNKEN, width=7, textvariable=self.makeup_kit,
                       font=("Century", 16, "bold")).grid(row=0, column=1, padx=10, pady=10)

        w2_lbl = Label(f4, text="SkinCare Kit", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        w2_txt = Entry(f4, bd=5, relief=SUNKEN, width=7, textvariable=self.womenskincare_kit,
                       font=("Century", 16, "bold")).grid(row=1, column=1, padx=10, pady=10)

        w3_lbl = Label(f4, text="Purse", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        w3_txt = Entry(f4, bd=5, relief=SUNKEN, width=7, textvariable=self.women_purse,
                       font=("Century", 16, "bold")).grid(row=2, column=1, padx=10, pady=10)

        w4_lbl = Label(f4, text="Perfumes", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
        w4_txt = Entry(f4, bd=5, relief=SUNKEN, width=7, textvariable=self.women_perfumes,
                       font=("Century", 16, "bold")).grid(row=3, column=1, padx=10, pady=10)

        w5_lbl = Label(f4, text="Hair care kit", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky="w")
        w5_txt = Entry(f4, bd=5, relief=SUNKEN, width=7, textvariable=self.women_haircarekit,
                       font=("Century", 16, "bold")).grid(row=4, column=1, padx=10, pady=10)

        w6_lbl = Label(f4, text="Cosmetic kit", bg=bg_color, fg="white",
                       font=("times new roman", 18, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky="w")
        w6_txt = Entry(f4, bd=5, relief=SUNKEN, width=7, textvariable=self.womencosmetic_kit,
                       font=("Century", 16, "bold")).grid(row=5, column=1, padx=10, pady=10)

        # ++++++++++++++++++++++++++++++++++++++++   Bill Area   +++++++++++++++++++++++++++++++++++++++

        f5 = Frame(self.root, bd=10, relief=GROOVE)
        f5.place(x=985, y=180, width=540, height=420)

        bil_title = Label(f5, text="Bill Area", bd=7, relief=GROOVE,
                          font=("times new roman", 20, "bold"), bg="MAROON", fg="white").pack(fill=X)
        scroll_y = Scrollbar(f5, orient=VERTICAL)

        self.txtarea = Text(f5, yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ___________________________________________  Button Frame________________________________________

        f6 = LabelFrame(self.root, text="Bill Menu", bg=bg_color, fg="gold", bd=10, relief=GROOVE,
                        font=("times new roman", 15, "bold"))
        f6.place(x=0, y=600, relwidth=1, height=200)

        #            +++++++++++++++Total bill for KID ,MEN and WOMEN+++++++++++++++++++++++++++

        m1_lbl = Label(f6, text="Total Kids Price", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="white").grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(f6, width=18, font=("arial", 11, "bold"), bd=4, relief=SUNKEN,
                       textvariable=self.total_kids_price).grid(row=0, column=1, padx=10,
                                                                pady=7)

        m2_lbl = Label(f6, text="Total Men Price", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(f6, width=18, font=("arial", 11, "bold"), bd=4, relief=SUNKEN,
                       textvariable=self.total_men_price).grid(row=1, column=1, padx=10,
                                                               pady=7)
        m3_lbl = Label(f6, text="Total Women Price", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(f6, width=18, font=("arial", 11, "bold"), bd=4, relief=SUNKEN,
                       textvariable=self.total_women_price).grid(row=2, column=1, padx=10,
                                                                 pady=7)

        #                  ++++++++++++++  +Total Tax for Kid , Men , Women + ++++++++++++++++++++++++++

        tax1_lbl = Label(f6, text="Total Kids tax", font=("times new roman", 14, "bold"), bg=bg_color,
                         fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="w")
        tax1_txt = Entry(f6, width=18, font=("arial", 10, "bold"), bd=5, relief=SUNKEN,
                         textvariable=self.total_kids_tax).grid(row=0, column=3, padx=10,
                                                                pady=1)

        tax2_lbl = Label(f6, text="Total Men tax", font=("times new roman", 14, "bold"), bg=bg_color,
                         fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="w")
        tax2_txt = Entry(f6, width=18, font=("arial", 10, "bold"), bd=5, relief=SUNKEN,
                         textvariable=self.total_men_tax).grid(row=1, column=3, padx=10,
                                                               pady=12)
        tax3_lbl = Label(f6, text="Total Women tax", font=("times new roman", 14, "bold"), bg=bg_color,
                         fg="white").grid(row=2, column=2, padx=20, pady=1, sticky="w")
        tax3_txt = Entry(f6, width=18, font=("arial", 10, "bold"), bd=5, relief=SUNKEN,
                         textvariable=self.total_women_tax).grid(row=2, column=3, padx=10,
                                                                 pady=1)

        #                 ==============Buttons for total bill,generate bill,clearBill and Exit===============

        btn_F = Frame(f6, bd=0, relief=GROOVE, bg="mistyrose")
        btn_F.place(x=780, y=20, width=720, height=100)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="maroon", fg="lavenderblush", pady=15, width=11,
                           bd=4,
                           font=("arial", 15, "bold")).grid(row=0, column=0, padx=18, pady=13, sticky="w")

        generate_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="maroon", fg="lavenderblush",
                              pady=15,
                              width=11, bd=4,
                              font=("arial", 15, "bold")).grid(row=0, column=1, padx=15, pady=13, sticky="w")

        clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="maroon", fg="lavenderblush", pady=15,
                           width=11, bd=4,
                           font=("arial", 15, "bold")).grid(row=0, column=2, padx=15, pady=13, sticky="w")

        exit_btn = Button(btn_F, text="Exit", command=self.exit_app, bg="maroon", fg="lavenderblush", pady=15, width=11,
                          bd=4,
                          font=("arial", 15, "bold")).grid(row=0, column=3, padx=15, pady=13, sticky="w")



        self.welcome_bill()

    # ++++++++++++++++++++++++++++++++++            working on total button       ++++++++++++++++++++++++++++++++++++
    ''' 
    This function will calulate the entire amount of 
    kids, men and women price when we click 
    the total button
    '''

    def total(self):
        self.c_s_p = self.baby_soap.get() * 49
        self.c_c_p = self.baby_cream.get() * 69
        self.c_bc_p = self.babycare_kit.get() * 189
        self.c_d_p = self.baby_diapers.get() * 39
        self.c_o_p = self.baby_oil.get() * 59
        self.c_bl_p = self.baby_blankets.get() * 169

        self.kids_prices = float(
            self.c_s_p +
            self.c_c_p +
            self.c_bc_p +
            self.c_d_p +
            self.c_o_p +
            self.c_bl_p
        )
        self.total_kids_price.set("Rs: " + str(self.kids_prices))

        # The below code is for the discout  offer
        self.c_tax = round(self.kids_prices * 0.10, 2)
        self.total_kids_tax.set("Rs: " + str(self.c_tax))

        self.g_r_p = self.menbodycare_kit.get() * 189
        self.g_f_p = self.menshaving_kit.get() * 119
        self.g_d_p = self.men_wallet.get() * 99
        self.g_w_p = self.men_trimmers.get() * 229
        self.g_s_p = self.men_belts.get() * 69
        self.g_t_p = self.men_sunglasses.get() * 129
        self.men_prices = float(
            self.g_r_p
            + self.g_f_p
            + self.g_d_p
            + self.g_w_p
            + self.g_s_p
            + self.g_t_p

        )
        self.total_men_price.set("Rs: " + str(self.men_prices))

        # The below line calulate the offer of men product
        self.g_tax = round(self.men_prices * 0.25, 2)
        self.total_men_tax.set("Rs: " + str(self.g_tax))
        self.d_m_p = self.makeup_kit.get() * 249
        self.d_c_p = self.womenskincare_kit.get() * 199
        self.d_f_p = self.women_purse.get() * 149
        self.d_t_p = self.women_perfumes.get() * 99
        self.d_l_p = self.women_haircarekit.get() * 139
        self.d_s_p = self.womencosmetic_kit.get() * 399

        self.women_prices = float(
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_l_p +
            self.d_s_p
        )

        self.total_women_price.set("Rs: " + str(self.women_prices))

        # The below line calulate the offer of women
        self.d_tax = round(self.women_prices * 0.15, 2)
        self.total_women_tax.set("Rs: " + str(self.d_tax))

        self.Total_bill = float(self.kids_prices +
                                self.men_prices +
                                self.women_prices +
                                self.c_tax +
                                self.g_tax +
                                self.d_tax)
        self.Total_bill_Round = round(self.Total_bill, 2)

    def welcome_bill(self):

        self.txtarea.delete('1.0', END)
        self.today = time.asctime(time.localtime(time.time()))
        # self.current_time = time.strftime('%I:%M:%S:%p')

        self.txtarea.insert(END, "\t\t     WELCOME TO AMAZON MART\n\n")
        # self.txtarea.insert(END, f"\t\t\t\t\t    Time  {self.current_time}\n")
        self.txtarea.insert(END, f" {self.today}\n")

        self.txtarea.insert(END, f"\n BILL NUMBER   : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n CUSTUMER NAME : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n PHONE NUMBER  : {self.c_phone.get()} ")
        self.txtarea.insert(END, f"\n =============================================================")
        self.txtarea.insert(END, f"\n PRODUCTS\t\t\tOUANTITY\t\t\tPRICE")
        self.txtarea.insert(END, f"\n =============================================================")

    def bill_area(self):

        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "enter name and phone number")
        elif self.total_kids_price.get() == "Rs: 0.0" and self.total_men_price.get() == "Rs: 0.0" and self.total_women_price.get() == "Rs: 0.0":
            messagebox.showerror("Error", "No products purchased")

        else:
            self.welcome_bill()

            # =================== ====  =================       Kids                     #######

            if self.baby_soap.get() != 0:
                self.txtarea.insert(END, f"\n Baby Soap\t\t\t{self.baby_soap.get()}\t\t\t{self.c_s_p}")

            if self.baby_cream.get() != 0:
                self.txtarea.insert(END, f"\n Baby Cream\t\t\t{self.baby_cream.get()}\t\t\t{self.c_c_p}")

            if self.babycare_kit.get() != 0:
                self.txtarea.insert(END, f"\n Babycare Kit\t\t\t{self.babycare_kit.get()}\t\t\t{self.c_bc_p}")

            if self.baby_diapers.get() != 0:
                self.txtarea.insert(END, f"\n Baby diaper\t\t\t{self.baby_diapers.get()}\t\t\t{self.c_d_p}")

            if self.baby_oil.get() != 0:
                self.txtarea.insert(END, f"\n Baby oil\t\t\t{self.baby_oil.get()}\t\t\t{self.c_o_p}")

            if self.baby_blankets.get() != 0:
                self.txtarea.insert(END, f"\n Baby Blankets\t\t\t{self.baby_blankets.get()}\t\t\t{self.c_bl_p}")

            # ==================================             Men         ==========================================

            if self.menbodycare_kit.get() != 0:
                self.txtarea.insert(END, f"\n Men Facewash\t\t\t{self.menbodycare_kit.get()}\t\t\t{self.g_r_p}")
            if self.menshaving_kit.get() != 0:
                self.txtarea.insert(END, f"\n Shaving kit\t\t\t{self.menshaving_kit.get()}\t\t\t{self.g_f_p}")
            if self.men_wallet.get() != 0:
                self.txtarea.insert(END, f"\n Wallet\t\t\t{self.men_wallet.get()}\t\t\t{self.g_d_p}")
            if self.men_trimmers.get() != 0:
                self.txtarea.insert(END, f"\n Trimmers\t\t\t{self.men_trimmers.get()}\t\t\t{self.g_w_p}")
            if self.men_belts.get() != 0:
                self.txtarea.insert(END, f"\n Belts\t\t\t{self.men_belts.get()}\t\t\t{self.g_s_p}")
            if self.men_sunglasses.get() != 0:
                self.txtarea.insert(END, f"\n Sunglasses\t\t\t{self.men_sunglasses.get()}\t\t\t{self.g_t_p}")

            # ============================            Women                 =================================

            if self.makeup_kit.get() != 0:
                self.txtarea.insert(END, f"\n Makeup kit\t\t\t{self.makeup_kit.get()}\t\t\t{self.d_m_p}")
            if self.womenskincare_kit.get() != 0:
                self.txtarea.insert(END, f"\n Skincare kit\t\t\t{self.womenskincare_kit.get()}\t\t\t{self.d_c_p}")
            if self.women_purse.get() != 0:
                self.txtarea.insert(END, f"\n Purse\t\t\t{self.women_purse.get()}\t\t\t{self.d_f_p}")
            if self.women_perfumes.get() != 0:
                self.txtarea.insert(END, f"\n Perfumes\t\t\t{self.women_perfumes.get()}\t\t\t{self.d_t_p}")
            if self.women_haircarekit.get() != 0:
                self.txtarea.insert(END, f"\n Haircare kit\t\t\t{self.women_haircarekit.get()}\t\t\t{self.d_l_p}")
            if self.womencosmetic_kit.get() != 0:
                self.txtarea.insert(END, f"\n Cosmetic Kit\t\t\t{self.womencosmetic_kit.get()}\t\t\t{self.d_s_p}")
            self.txtarea.insert(END, f"\n ------------------------------------------------------------")

            if self.total_kids_tax.get() != "Rs: 0.0":
                self.txtarea.insert(END, f"\n Kids tax\t\t\t\t\t        {self.total_kids_tax.get()}")

            if self.total_men_tax.get() != "Rs: 0.0":
                self.txtarea.insert(END, f"\n Men tax\t\t\t\t\t        {self.total_men_tax.get()}")

            if self.total_women_tax.get() != "Rs: 0.0":
                self.txtarea.insert(END, f"\n Women tax\t\t\t\t\t        {self.total_women_tax.get()}")
            self.txtarea.insert(END, f"\n ------------------------------------------------------------")

            self.txtarea.insert(END, f"\n\n Total Bill\t\t\t\t\t Rs: {self.Total_bill_Round}\n\n")

            self.txtarea.insert(END, f"\t\t  Thank You For Shopping With Us\n\n")
            self.txtarea.insert(END, f"\t\t\t HAVE A GREAT DAY \n\n")

            self.txtarea.insert(END,
                                f"Contact Details :\n\n9521255282\naashirwadk7@gmail.com\n\n8319602957\ngoyallala02@gmail.com\n\n7987740520\namangupta09032001@gmail.com\n\namzonmart@gmail.com\nsupport@Digital_India\n\n\nFor online order:\nCheck our Website:\namazon.com (24x7) ")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save bill", "Do you really want to save bill")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no {self.bill_no.get()} has been saved")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)

                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "invalid bill NO.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear data")

        if op > 0:

            #  _________________________________      Kids       ____________________________________
            self.baby_soap.set(0)
            self.baby_cream.set(0)
            self.babycare_kit.set(0)
            self.baby_diapers.set(0)
            self.baby_oil.set(0)
            self.baby_blankets.set(0)
            #  _________________________________       Men      ________________________________________________________
            self.menbodycare_kit.set(0)
            self.menshaving_kit.set(0)
            self.men_wallet.set(0)
            self.men_trimmers.set(0)
            self.men_belts.set(0)
            self.men_sunglasses.set(0)

            #  _________________________________      Women     _____________________________________
            self.makeup_kit.set(0)
            self.womenskincare_kit.set(0)
            self.women_purse.set(0)
            self.women_perfumes.set(0)
            self.women_haircarekit.set(0)
            self.womencosmetic_kit.set(0)

            # __________________________________     Total product price And offer  variable        ________________________
            self.total_kids_price.set("")
            self.total_men_price.set("")
            self.total_women_price.set("")
            self.total_kids_tax.set("")
            self.total_men_tax.set("")
            self.total_women_tax.set("")

            # _____________________________________   Kids details variables                 ______________________
            self.c_name.set("")
            self.c_phone.set("")
            self.search_bill.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit")

        if op > 0:
            self.root.destroy()

root = Tk()
root.iconbitmap(r'mart.ico')
app= Window1(root)
root.mainloop()
