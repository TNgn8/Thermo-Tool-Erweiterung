import math
from tkinter.ttk import Combobox, Entry, Label, Scale
from tkinter.messagebox import showinfo
from tkinter import *
import tkinter as tk

class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
    def init_main(self):
        self.add_img = PhotoImage(file='button_title.png') # Picture for button
        btn_open_dialog = Button(root, command=self.open_dialog, compound=TOP, image=self.add_img)
        btn_open_dialog.place(x=50, y=550)
        title_image = PhotoImage(file='Title.png') # Picture for title
        title_label = Label(root, bg='#DFE0DF', pady=(20))
        title_label.image=title_image
        title_label['image']=title_label.image
        title_label.pack(anchor=N)
            # Labels for pressure (p), volume (v), temperature (t) and entropy(s) both initial and final gas states
        heading_label = Label(root, text="Pressure: 1",font=" Pt 12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=170)
        heading_label = Label(root, text="atm", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=140, y=170)
        heading_label = Label(root, text="Volume: 3", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=200)
        heading_label = Label(root, text="L", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=130, y=200)
        heading_label = Label(root, text="Temperature: 298", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=230)
        heading_label = Label(root, text="K", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=190, y=230)
        heading_label = Label(root, text="Entropy: 700", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=260)
        heading_label = Label(root, text="J/(kg*K)", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=150, y=260)
        heading_label = Label(root, text="Pressure:", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=230, y=170)
        heading_label = Label(root, text="atm", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=345, y=170)
        heading_label = Label(root, text="Volume:", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=230, y=200)
        heading_label = Label(root, text="L", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=335, y=200)
        heading_label = Label(root, text="Temperature:", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=230, y=230)
        heading_label = Label(root, text="K", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=380, y=230)
        heading_label = Label(root, text="Entropy:", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=230, y=260)
        heading_label = Label(root, text="J/(kg*K)", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=340, y=260)
            # Labels for Heat transfer = q, Internal Energy = u, Thermodynamic work = w, Enthalpy = h, Entropy = s
        heading_label = Label(root, text="Heat transfer:", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=340)
        heading_label = Label(root, text="kJ/kg", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=200, y=340)
        heading_label = Label(root, text="Change in internal Energy:", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=370)
        heading_label = Label(root, text="kJ/kg", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=300, y=370)
        heading_label = Label(root, text="Thermodynamic work:", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=400)
        heading_label = Label(root, text="kJ/kg", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=280, y=400)
        heading_label = Label(root, text="Change in entropy:", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=430)
        heading_label = Label(root, text="J/(kg*K)", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=240, y=430)
        heading_label = Label(root, text="Change in enthalpy:", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=460)
        heading_label = Label(root, text="kJ/(kg*K)", font="Pt  12 bold italic", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=265, y=460)
            # Labels for scales
        heading_label = Label(root, text="Pressure", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=770, y=410)
        heading_label = Label(root, text="Volume", font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=510, y=60)
        heading_label = Label(root, text="Temperature",  font="Pt  12 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=1025, y=60)
            # Other labels
        initial_state = Label(root, text="INITIAL STATE:", font="Cambria 14 bold", fg="#005B47", bg='#DFE0DF')
        initial_state.place(x=50, y=145)
        final_state = Label(root, text="FINAL STATE:", font="Cambria 14 bold", fg="#005B47", bg='#DFE0DF')
        final_state.place(x=220, y=145)
        initial_state = Label(root, text="ENERGY BALANCE:", font="Cambria 14 bold", fg="#005B47", bg='#DFE0DF')
        initial_state.place(x=80, y=315)
            # Label for Combobox
        heading_label = Label(root, text="CHOOSE THE GAS PROCESS:", font="Cambria 14 bold", fg="#005B47", bg='#DFE0DF')
        heading_label.place(x=50, y=50)
            # Entry widgets :P
            # pressure (p), volume (v), temperature (t) and entropy (s) both initial and final gas states
        p2_field = Entry(root, font="Pt  12 bold italic", fg="#025B47", bg='#DFE0DF', width=4, bd=0, disabledbackground="#DFE0DF", disabledforeground="#667C74")
        p2_field.place(x=310, y=172)
        v2_field = Entry(root, font="Pt  12 bold italic", fg="#025B47", bg='#DFE0DF', width=4, bd=0, disabledbackground="#DFE0DF", disabledforeground="#667C74")
        v2_field.place(x=300, y=202)
        t2_field = Entry(root, font="Pt  12 bold italic", fg="#025B47", bg='#DFE0DF', width=3, bd=0, disabledbackground="#DFE0DF", disabledforeground="#667C74")
        t2_field.place(x=340, y=232)
        s2_field = Entry(root, font="Pt  12 bold italic", fg="#025B47", bg='#DFE0DF', width=4, bd=0, disabledbackground="#DFE0DF", disabledforeground="#667C74")
        s2_field.place(x=305, y=262)
        s2_field.configure(state=NORMAL)
        s2_field.delete(0, END)
        s2_field.insert(0, 700)
            # Energy balance components: q, w, u, s, h, Heat transfer = q, Internal Energy = u, Thermodynamic work = w, Enthalpy = h, Entropy = s
        q_field = Entry(root, font="Pt  12 bold italic", fg="#025B47", bg='#DFE0DF', width=4, bd=0)
        q_field.place(x=160, y=342)
        u_field = Entry(root, font="Pt  12 bold italic", fg="#025B47", bg='#DFE0DF', width=4, bd=0)
        u_field.place(x=260, y=372)
        w_field = Entry(root, font="Pt  12 bold italic", fg="#025B47", bg='#DFE0DF', width=5, bd=0)
        w_field.place(x=230, y=402)
        s_field = Entry(root, font="Pt  12 bold italic", fg="#025B47", bg='#DFE0DF', width=4, bd=0)
        s_field.place(x=200, y=432)
        h_field = Entry(root, font="Pt  12 bold italic", fg="#025B47", bg='#DFE0DF', width=6, bd=0)
        h_field.place(x=210, y=462)
            # Combobox
        global combobox_field
        combobox_field = Combobox(root,
                                  values=[u'Isothermal', u'Isochoric',
                                          u'Isobaric', u'Adiabatic'],
                                state="readonly" )
        combobox_field.configure(font="Pt  12 bold")
        combobox_field.place( x=50, y=80)
            #Scales <3
            # Scale for pressure
        def onScale_p(val):
            p = float(val)
            var_p.set(p)
            p2_field.delete(0, END)
            p2_field.insert(0, p)
            global graph, graph2
            for dot in graph:
                canvas.delete(dot)
            for dot2 in graph2:
                c.delete(dot2)
            # Manometer animation
            if p <= 0.55:
                manometer_image = PhotoImage(file='Manometer/Manometer0.5.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif 0.55 < p <= 0.65:
                manometer_image = PhotoImage(file='Manometer/Manometer0.6.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 0.65 and p <= 0.75:
                manometer_image = PhotoImage(file='Manometer/Manometer0.7.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 0.75 and p <= 0.85:
                manometer_image = PhotoImage(file='Manometer/Manometer0.8.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 0.85 and p <= 0.95:
                manometer_image = PhotoImage(file='Manometer/Manometer0.9.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 0.95 and p <= 1.05: # initial state
                manometer_image = PhotoImage(file="Manometer/Manometer1.png")
                #canvas.create_image(60,80, image=manometer_image)
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.05 and p <= 1.15:
                manometer_image = PhotoImage(file='Manometer/Manometer1.1.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.15 and p <= 1.25:
                manometer_image = PhotoImage(file='Manometer/Manometer1.2.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.25 and p <= 1.35:
                manometer_image = PhotoImage(file='Manometer/Manometer1.3.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.35 and p <= 1.45:
                manometer_image = PhotoImage(file='Manometer/Manometer1.4.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.45 and p <= 1.55:
                manometer_image = PhotoImage(file='Manometer/Manometer1.5.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.55 and p <= 1.65:
                manometer_image = PhotoImage(file='Manometer/Manometer1.6.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.65 and p <= 1.75:
                manometer_image = PhotoImage(file='Manometer/Manometer1.7.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.75 and p <= 1.85:
                manometer_image = PhotoImage(file='Manometer/Manometer1.7.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.85 and p <= 1.95:
                manometer_image = PhotoImage(file='Manometer/Manometer1.8.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.75 and p <= 1.85:
                manometer_image = PhotoImage(file='Manometer/Manometer1.7.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 1.95 and p <= 2.05:
                manometer_image = PhotoImage(file='Manometer/Manometer2.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 2.05 and p <= 2.15:
                manometer_image = PhotoImage(file='Manometer/Manometer2.1.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 2.15 and p <= 2.25:
                manometer_image = PhotoImage(file='Manometer/Manometer2.2.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 2.25 and p <= 2.35:
                manometer_image = PhotoImage(file='Manometer/Manometer2.3.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 2.35 and p <= 2.45:
                manometer_image = PhotoImage(file='Manometer/Manometer2.4.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)
            elif p > 2.45:
                manometer_image = PhotoImage(file='Manometer/Manometer2.5.png')
                manometer_label = Label(root, bg='#DFE0DF')
                manometer_label.image = manometer_image
                manometer_label['image'] = manometer_label.image
                manometer_label.place(x=596, y=200)

            if combobox_field.current() == 0: # isotherm
                new_v = 1 * 101325 * 3 * 0.01 / p /101325 / 0.01
                scale_v.set(new_v)
                log = math.log(new_v/3)
                new_q = 287*298*log/1000 # R=287 J/(kg*K)
                new_w = - new_q
                new_s = 287 * log
                new_s2 = new_s + 700
                new_u= 0
                new_h = 0
                q_field.delete(0, END)
                q_field.insert(0, round(new_q))
                u_field.delete(0, END)
                u_field.insert(0, round(new_u))
                w_field.delete(0, END)
                w_field.insert(0, round(new_w))
                s_field.delete(0, END)
                s_field.insert(0, round(new_s))
                h_field.delete(0, END)
                h_field.insert(0, round(new_h,1))
                s2_field.delete(0, END)
                s2_field.insert(0, round(new_s2))
                # p-v diagram
                def frange(begin, end, step):
                    x = begin
                    t = []
                    while x <= end:
                        t.append(x)
                        x += step
                    return t
                def graph_generator(x_tmp):
                    y_tmp = []
                    for x in x_tmp:
                        y = 300 / x
                        y_tmp.append(y)
                    return y_tmp
                if new_v > 3:
                    shift_step = 35
                    graph_start = 30
                    graph_end = new_v * 10
                elif new_v < 3:
                    shift_step = new_v * 10 + 5
                    graph_start = new_v * 10
                    graph_end = 30
                else:
                    shift_step = 35
                    graph_start = 30
                    graph_end = 30
                x_list = frange(graph_start, graph_end, 0.1)
                y_graph = graph_generator(x_list)
                graph = graph_dot(x_list, y_graph, shift_step)

                #T-s diagram
                def frange2(begin2, end2, step2):
                    x2 = begin2
                    t2 = []
                    while x2 <= end2:
                        t2.append(x2)
                        x2 += step2
                    return t2
                def graph_generator2(x_tmp2):
                    y_tmp2 = []
                    for x2 in x_tmp2:
                        y2 = 29.8 + 0 * x2
                        y_tmp2.append(y2)
                    return y_tmp2
                if new_s > 0:
                    shift_step2 = 80
                    graph_start2 = 70
                    graph_end2 = (new_s+700) / 10
                elif new_s < 0:
                    shift_step2 = (new_s+700) / 10 + 10
                    graph_start2 = (new_s+700) / 10
                    graph_end2 = 70
                else:
                    shift_step2 = 80
                    graph_start2 = 70
                    graph_end2 = 70
                x_list2 = frange2(graph_start2, graph_end2, 0.1)
                y_graph2 = graph_generator2(x_list2)
                graph2 = graph_dot2(x_list2, y_graph2, shift_step2)

            elif combobox_field.current() == 1: # isochor
                new_t = p * 101325 * 298 / 1 / 101325
                scale_t.set(new_t)
                new_q = 717*(new_t - 298)/1000 # R=287 J/(kg*K), cv = 717 J/(kg*K), cp = 1004 J/(kg*K)
                new_w = 0
                new_s = 717 * math.log(new_t / 298)
                new_s2=new_s+700
                new_u = new_q
                new_h = 1004*(new_t - 298)/1000
                q_field.delete(0, END)
                q_field.insert(0, round(new_q))
                u_field.delete(0, END)
                u_field.insert(0, round(new_u))
                w_field.delete(0, END)
                w_field.insert(0, round(new_w))
                s_field.delete(0, END)
                s_field.insert(0, round(new_s))
                h_field.delete(0, END)
                h_field.insert(0, round(new_h,1))
                s2_field.delete(0, END)
                s2_field.insert(0, round(new_s2))

                #p-v diagram
                def frange(begin, end, step): # x list
                    i=begin
                    t=[]
                    while i<=end:
                        t.append(3)
                        i+=step
                    return t
                def graph_generator(begin, end, step): # y list
                    y=begin
                    y_tmp = []
                    while y<=end:
                        y_tmp.append(y)
                        y+=step
                    return y_tmp
                if p > 1:
                    shift_step=35
                    graph_start = 10
                    graph_end = p * 10
                elif p < 1:
                    shift_step = 35
                    graph_start = p * 10
                    graph_end = 10
                else:
                    shift_step = 35
                    graph_start = 10
                    graph_end = 10
                x_list = frange(graph_start, graph_end, 0.1)
                y_graph = graph_generator(graph_start, graph_end, 0.1)
                graph = graph_dot(x_list, y_graph, shift_step)

                # T-s diagram
                def frange2(begin2, end2, step2):
                    x2 = begin2
                    t2 = []
                    while x2 <= end2:
                        t2.append(x2)
                        x2 += step2
                    return t2
                def graph_generator2(x_tmp2):
                    y_tmp2 = []
                    for x2 in x_tmp2:
                        y2 = 298 * math.exp((x2*10  - 700) / 717)/10
                        y_tmp2.append(y2)
                    return y_tmp2
                if new_s > 0:
                    shift_step2 = 80
                    graph_start2 = 70
                    graph_end2 = (new_s+700) / 10
                elif new_s < 0:
                    shift_step2 = (new_s+700) / 10 + 10
                    graph_start2 = (new_s+700) / 10
                    graph_end2 = 70
                else:
                    shift_step2 = 80
                    graph_start2 = 70
                    graph_end2 = 70
                x_list2 = frange2(graph_start2, graph_end2, 0.1)
                y_graph2 = graph_generator2(x_list2)
                graph2 = graph_dot2(x_list2, y_graph2, shift_step2)

            elif combobox_field.current() == 3: # adiabatic
                for dot in graph:
                    canvas.delete(dot)
                new_t = 298 * (p)**(0.4/1.4)
                scale_t.set(new_t)
                new_v = 3*(1/p)**(1/1.4)
                scale_v.set(new_v)
                new_q = 0  # R=287 , cv = 717 cp = 1004
                new_w = 717*(new_t-298)/1000
                new_s = 0
                new_u = new_w
                new_h = 1004 * (new_t - 298)/1000
                q_field.delete(0, END)
                q_field.insert(0, round(new_q))
                u_field.delete(0, END)
                u_field.insert(0, round(new_u))
                w_field.delete(0, END)
                w_field.insert(0, round(new_w))
                s_field.delete(0, END)
                s_field.insert(0, round(new_s))
                h_field.delete(0, END)
                h_field.insert(0, round(new_h,1))

                # p-v Diagram
                def frange(begin, end, step):
                    x = begin
                    t = []
                    while x <= end:
                        t.append(x)
                        x += step
                    return t
                def graph_generator(x_tmp):
                    y_tmp = []
                    for x in x_tmp:
                        y = 10*(30/ x) ** 1.4
                        y_tmp.append(y)
                    return y_tmp
                if new_v > 3:
                    shift_step = 35
                    graph_start = 30
                    graph_end = new_v * 10
                elif new_v < 3:
                    shift_step = new_v * 10 + 5
                    graph_start = new_v * 10
                    graph_end = 30
                else:
                    shift_step = 35
                    graph_start = 30
                    graph_end = 30
                x_list = frange(graph_start, graph_end, 0.1)
                y_graph = graph_generator(x_list)
                graph = graph_dot(x_list, y_graph, shift_step)

                # T-s diagram
                def frange2(begin2, end2, step2): # x list
                    i2=begin2
                    t2=[]
                    while i2<=end2:
                        t2.append(700)
                        i2+=step2
                    return t2
                def graph_generator2(begin2, end2, step2): # y list
                    y2=begin2
                    y_tmp2 = []
                    while y2<=end2:
                        y_tmp2.append(y2)
                        y2+=step2
                    return y_tmp2
                if new_t > 298:
                    shift_step2=80
                    graph_start2 = 29.8
                    graph_end2 = new_t / 10
                elif new_t < 298:
                    shift_step2 = 80
                    graph_start2 = new_t/ 10
                    graph_end2 = 29.8
                else:
                    shift_step2 = 80
                    graph_start2 = 29.8
                    graph_end2 = 29.8
                x_list2 = frange2(graph_start2, graph_end2, 0.1)
                y_graph2 = graph_generator2(graph_start2, graph_end2, 0.1)
                graph2 = graph_dot2(x_list2, y_graph2, shift_step2)

        scale_p = Scale(root, from_=0.5, to=2.5, length=280,
                        width=10,  resolution=0.01, command=onScale_p,
                        orient=HORIZONTAL, font="Pt  12 bold",
                        fg="#443A32", bg='#DFE0DF', highlightthickness=0)
        scale_p.place(x=660, y=370)
        scale_p.set(float(1))
        var_p = DoubleVar()

            # Scale for volume
        def onScale_v(val):
            v = float(val)
            var_v.set(v)
            v2_field.delete(0, END)
            v2_field.insert(0, v)
            global graph, graph2

            if v <= 0.625:
                cylinder_image = PhotoImage(file='Cylinder/cylinder0.5.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 0.625 and v <= 0.875:
                cylinder_image = PhotoImage(file='Cylinder/cylinder0.75.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 0.875 and v <= 1.125: # initial state of gas
                cylinder_image = PhotoImage(file='Cylinder/cylinder1.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 1.125 and v <= 1.375:
                cylinder_image = PhotoImage(file='Cylinder/cylinder1.25.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 1.375 and v <= 1.625:
                cylinder_image = PhotoImage(file='Cylinder/cylinder1.5.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 1.625 and v <= 1.875:
                cylinder_image = PhotoImage(file='Cylinder/cylinder1.75.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 1.875 and v <= 2.125:
                cylinder_image = PhotoImage(file='Cylinder/cylinder2.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 2.125 and v <= 2.375:
                cylinder_image = PhotoImage(file='Cylinder/cylinder2.25.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 2.375 and v <= 2.625:
                cylinder_image = PhotoImage(file='Cylinder/cylinder2.5.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 2.625 and v <= 2.875:
                cylinder_image = PhotoImage(file='Cylinder/cylinder2.75.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 2.875 and v <= 3.125:
                cylinder_image = PhotoImage(file='Cylinder/cylinder3.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 3.125 and v <= 3.375:
                cylinder_image = PhotoImage(file='Cylinder/cylinder3.25.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 3.375 and v <= 3.625:
                cylinder_image = PhotoImage(file='Cylinder/cylinder3.5.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 3.625 and v <= 3.875:
                cylinder_image = PhotoImage(file='Cylinder/cylinder3.75.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 3.875 and v <= 4.125:
                cylinder_image = PhotoImage(file='Cylinder/cylinder4.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 4.125 and v <= 4.375:
                cylinder_image = PhotoImage(file='Cylinder/cylinder4.25.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 4.375 and v <= 4.625:
                cylinder_image = PhotoImage(file='Cylinder/cylinder4.5.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 4.625 and v <= 4.875:
                cylinder_image = PhotoImage(file='Cylinder/cylinder4.75.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 4.875 and v <= 5.125:
                cylinder_image = PhotoImage(file='Cylinder/cylinder5.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 5.125 and v <= 5.375:
                cylinder_image = PhotoImage(file='Cylinder/cylinder5.25.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 5.375 and v <= 5.625:
                cylinder_image = PhotoImage(file='Cylinder/cylinder5.5.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 5.625 and v <= 5.875:
                cylinder_image = PhotoImage(file='Cylinder/cylinder5.75.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)
            elif v > 5.875:
                cylinder_image = PhotoImage(file='Cylinder/cylinder6.png')
                cylinder_label = Label(root, bg='#DFE0DF')
                cylinder_label.image = cylinder_image
                cylinder_label['image'] = cylinder_label.image
                cylinder_label.place(x=720, y=90)

            if combobox_field.current() == 0: #isotherm
                scale_v.configure(from_=6, to=1.2)
                new_p = 3 / v
                scale_p.set(new_p)

            elif combobox_field.current() == 2: #isobar
                for dot2 in graph2:
                    c.delete(dot2)
                scale_v.configure(from_=6, to=1.51)
                new_t = v * 298 / 3
                scale_t.set(new_t)
                new_q = 1004 * (new_t - 298)/1000  # R=287 , cv = 717 cp = 1004
                new_w = -1 * 101325 * (v - 3) * 1000 / 1000 /1000 / 3.56 # 3.56 *10**(-3) kg - masse der Luft im Zylinder
                new_s = 1004 * math.log(new_t / 298)
                new_s2=new_s + 700
                new_u=717*(new_t-298)/1000
                #new_u = new_q + new_w
                new_h = 1004 * (new_t - 298)/1000
                q_field.delete(0, END)
                q_field.insert(0, round(new_q))
                u_field.delete(0, END)
                u_field.insert(0, round(new_u))
                w_field.delete(0, END)
                w_field.insert(0, round(new_w,2))
                s_field.delete(0, END)
                s_field.insert(0, round(new_s))
                h_field.delete(0, END)
                h_field.insert(0, round(new_h,1))
                s2_field.delete(0, END)
                s2_field.insert(0, round(new_s2))

                # T-s diagram
                def graph_generator2(x_tmp2):
                    y_tmp2 = []
                    for x2 in x_tmp2:
                        y2 = 298 * math.exp((x2*10  - 700) / 1004)/10
                        y_tmp2.append(y2)
                    return y_tmp2
                if new_s > 0:
                    shift_step2 = 80
                    graph_start2 = 70
                    graph_end2 = (new_s+700) / 10
                elif new_s < 0:
                    shift_step2 = (new_s+700) / 10 + 10
                    graph_start2 = (new_s+700) / 10
                    graph_end2 = 70
                else:
                    shift_step2 = 80
                    graph_start2 = 70
                    graph_end2 = 70
                x_list2 = frange2(graph_start2, graph_end2, 0.1)
                y_graph2 = graph_generator2(x_list2)
                graph2 = graph_dot2(x_list2, y_graph2, shift_step2)

            elif combobox_field.current() == 3: #adiabat
                scale_v.configure(from_=4.92, to=1.56)
                new_t = 298*(3/v)**0.4
                scale_t.set(new_t)
                new_p = (3/v)**1.4
                scale_p.set(new_p)
        scale_v = Scale(root, from_=6, to=0.5, length=280, width=10,  resolution=-0.01, command=onScale_v, orient=VERTICAL, font="Pt  12 bold", fg="#443A32", bg='#DFE0DF', highlightthickness=0)
        scale_v.place(x=500, y=90)
        scale_v.set(3)

        var_v = DoubleVar()

            # Scale for temperature
        def onScale_t(val):
            t = float(val)
            var_t.set(t)
            t2_field.delete(0, END)
            t2_field.insert(0, t)
            global graph, graph2

            # Thermometer animation
            if t <= 165:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer150K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 165 and t <= 195:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer180K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 195 and t <= 225:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer210K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 225 and t <= 255:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer240K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 255 and t <= 285:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer240K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 255 and t <= 285:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer270K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 285 and t <= 315: # initial state of gas
                thermometer_image = PhotoImage(file='Thermometer/Thermometer300K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 315 and t <= 345:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer330K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 345 and t <= 375:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer360K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 375 and t <= 405:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer390K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 405 and t <= 435:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer420K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 435 and t <= 465:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer450K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 465 and t <= 495:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer480K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 495 and t <= 525:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer510K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 525 and t <= 555:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer540K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 555 and t <= 585:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer570K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 585 and t <= 615:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer600K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 615 and t <= 645:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer630K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 645 and t <= 675:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer660K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 675 and t <= 705:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer690K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 705 and t <= 735:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer720K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)
            elif t > 735:
                thermometer_image = PhotoImage(file='Thermometer/Thermometer750K.png')
                thermometer_label = Label(root, bg='#DFE0DF')
                thermometer_label.image = thermometer_image
                thermometer_label['image'] = thermometer_label.image
                thermometer_label.place(x=914, y=200)

                # Calculations
            if combobox_field.current() == 1: # isochor
                scale_t.configure(from_=745, to=150)
                new_p = t * 1 * 101325 / 298 / 101325
                scale_p.set(new_p)
            elif combobox_field.current() == 2: # isobar
                for dot in graph:
                    canvas.delete(dot)
                scale_t.configure(from_=596, to=150)
                new_v = t * 3 / 298
                scale_v.set(new_v)
                def graph_generator(x_tmp):
                    y_tmp = []
                    for x in x_tmp:
                        y=10 + 0 * x
                        y_tmp.append(y)
                    return y_tmp
                if new_v > 3:
                    shift_step = 35
                    graph_start = 30
                    graph_end = new_v * 10
                elif new_v < 3:
                    shift_step = new_v * 10 + 5
                    graph_start = new_v * 10
                    graph_end = 30
                else:
                    shift_step = 35
                    graph_start = 30
                    graph_end = 30
                x_list = frange(graph_start, graph_end, 0.1)
                y_graph = graph_generator(x_list)
                graph = graph_dot(x_list, y_graph, shift_step)
            elif combobox_field.current() == 3: #adiabat
                scale_t.configure(from_=387, to=244)
                new_v = 3*(298/t)**(1/0.4)
                scale_v.set(new_v)
                new_p = (t/298)**(1.4/0.4)
                scale_p.set(new_p)
        scale_t = Scale(root, from_=750, to=150, length=280, width=10, resolution=1, command=onScale_t, orient=VERTICAL, font="Pt  12 bold", fg="#443A32", bg='#DFE0DF', highlightthickness=0)
        scale_t.place(x=1040, y=90)
        scale_t.set(298)
        var_t = DoubleVar()



        def change(event):
            # print(combobox_field.current())
            if  combobox_field.current() == 0:
                t2_field.configure(state=NORMAL)
                t2_field.delete(0, END)
                t2_field.insert(0, 298)
                t2_field.configure(state=DISABLED)
                scale_t.configure(state=NORMAL)
                scale_t.set(298)
                scale_t.configure(state=DISABLED)
                scale_v.set(3)
                scale_p.set(1)
                s2_field.configure(state=NORMAL)
                s2_field.delete(0, END)
                s2_field.insert(0, 700)
            else:
                t2_field.configure(state=NORMAL)
                scale_t.configure(state=NORMAL)
            if combobox_field.current() == 1:
                v2_field.configure(state=NORMAL)
                v2_field.delete(0, END)
                v2_field.insert(0, 3)
                v2_field.configure(state=DISABLED)
                scale_v.configure(state=NORMAL)
                scale_v.set(3)
                scale_v.configure(state=DISABLED)
                scale_p.set(1)
                scale_t.set(298)
                s2_field.configure(state=NORMAL)
                s2_field.delete(0, END)
                s2_field.insert(0, 700)
            else:
                v2_field.configure(state=NORMAL)
                scale_v.configure(state=NORMAL)
            if combobox_field.current() == 2:
                p2_field.configure(state=NORMAL)
                p2_field.delete(0, END)
                p2_field.insert(0 , 1)
                p2_field.configure(state=DISABLED)
                scale_p.configure(state=NORMAL)
                scale_p.set(1)
                scale_p.configure(state=DISABLED)
                scale_v.set(3)
                scale_t.set(298)
                s2_field.configure(state=NORMAL)
                s2_field.delete(0, END)
                s2_field.insert(0, 700)
            else:
                p2_field.configure(state=NORMAL)
                scale_p.configure(state=NORMAL)
            if combobox_field.current() == 3:
                s2_field.configure(state=NORMAL)
                s2_field.delete(0, END)
                s2_field.insert(0, 700)
                s2_field.configure(state=DISABLED)
                scale_p.set(1)
                scale_v.set(3)
                scale_t.set(298)

        combobox_field.bind("<<ComboboxSelected>>", change)

    def open_dialog(self):
        Child()

class Child(tk.Toplevel):

    def __init__(self):
        super().__init__(root)
        self.radio_selection = tk.IntVar(value=1)
        self._after_id = None  # Initialize a variable to keep track of the after method
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Various Gas States Calculator')
        self.geometry('800x600+350+250')
        self.resizable(False, False)
        self.configure(bg='#DFE0DF')
        title_image = PhotoImage(file='title2.png') # Picture for title
        title_label = Label(self, bg='#DFE0DF', pady=(20))
        title_label.image=title_image
        title_label['image']=title_label.image
        title_label.pack(anchor=N)
        # Labels for p,v,t
        heading_label = Label(self, text="Pressure (atm)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=150)
        heading_label = Label(self, text="Volume (L)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=190)
        heading_label = Label(self, text="Temperature (K)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=230)
        heading_label = Label(self, text="Mass (kg)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=270)
        heading_label = Label(self, text="Pressure (atm)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=200, y=150)
        heading_label = Label(self, text="Volume (L)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=200, y=190)
        heading_label = Label(self, text="Temperature (K)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=200, y=230)

        #Labels for cp,cv,k
        heading_label = Label(self, text="Cp (J/kgK)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=400, y=190)
        heading_label = Label(self, text="k", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=400, y=230)
        heading_label = Label(self, text="Cv (J/kg)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=550, y=190)

        # Labels for Combobox
        heading_label = Label(self, text="CHOOSE GAS PROCESS:",font="Cambria 13 bold", fg="#005B47", bg='#DFE0DF')
        heading_label.place(x=50, y=50)
        heading_label = Label(self, text="WHAT WILL BE CHANGED?", font="Cambria 13 bold", fg="#005B47", bg='#DFE0DF')
        heading_label.place(x=400, y=50)

        # Labels for Heat transfer = q, Internal Energy = u,
        # Thermodynamic work = w, Enthalpy = h, Entropy = s
        heading_label = Label(self, text="Heat transfer (kJ/kg)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=410)
        heading_label = Label(self, text="Change in internal energy  (kJ/kg)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=450)
        heading_label = Label(self, text="Thermodynamic work  (kJ/kg)", font="Pt  11  bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=50, y=490)
        heading_label = Label(self, text="Change in entropy (J/(kg*K))", font="Pt  11  bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=300, y=410)
        heading_label = Label(self, text="Change in enthalpy (kJ/(kg*K)", font="Pt  11 bold", fg="#443A32", bg='#DFE0DF')
        heading_label.place(x=300, y=450)

        # Other labels
        initial_state = Label(self, text="INITIAL STATE:", font="Cambria 13 bold", fg="#005B47", bg='#DFE0DF')
        initial_state.place(x=50, y=120)
        final_state = Label(self,text="FINAL STATE:", font="Cambria 13 bold", fg="#005B47", bg='#DFE0DF')
        final_state.place(x=200, y=120)
        energy_balance = Label(self, text="ENERGY BALANCE:", font="Cambria 13 bold", fg="#005B47", bg='#DFE0DF')
        energy_balance.place(x=180, y=370)
        energy_balance = Label(self, text="SPECIFIC HEAT CAPACITIES, ADIABATIC INDEX:", font="Cambria 13 bold", fg="#005B47", bg='#DFE0DF')
        energy_balance.place(x=400, y=120)

        # Radiobuttons
        rb_standard = tk.Radiobutton(self, text="Default (dry air)", variable=self.radio_selection,
                                     value=1, command=self.update_entries)
        rb_standard.place(x=400, y=160)

        rb_selectable = tk.Radiobutton(self, text="Choose own values", variable=self.radio_selection,
                                       value=2, command=self.update_entries)
        rb_selectable.place(x=550, y=160)

        # Entry widgets :P
        # pressure (p), volume (v) and temperature (t) both initial and final states
        p1_f = Entry(self)
        p1_f.place(x=50, y=170)
        v1_f = Entry(self)
        v1_f.place(x=50, y=210)
        t1_f = Entry(self)
        t1_f.place(x=50, y=250)
        p2_f = Entry(self)
        p2_f.place(x=200, y=170)
        v2_f = Entry(self)
        v2_f.place(x=200, y=210)
        t2_f = Entry(self)
        t2_f.place(x=200, y=250)
        m_f = Entry(self)
        m_f.place(x=50, y=290)

        # cp, cv, κ Entry
        self.cp_f = Entry(self)
        self.cp_f.place(x=400, y=210)
        self.k_f = Entry(self)
        self.k_f.place(x=400, y=250)
        self.cv_f = Entry(self)
        self.cv_f.place(x=550, y=210)

        # Add trace methods to Entry widgets
        self.cp_f_var = tk.StringVar()
        self.cp_f.configure(textvariable=self.cp_f_var)
        self.cp_f_var.trace("w", lambda name, index, mode, sv=self.cp_f_var: self.calculate())

        self.cv_f_var = tk.StringVar()
        self.cv_f.configure(textvariable=self.cv_f_var)
        self.cv_f_var.trace("w", lambda name, index, mode, sv=self.cv_f_var: self.calculate())

        # Update trace method for self.k_f Entry widget to include the new calculations
        self.k_f_var = tk.StringVar()
        self.k_f.configure(textvariable=self.k_f_var)
        self.k_f_var.trace("w", lambda name, index, mode, sv=self.k_f_var: self.calculate())

        # Set default values for cp, cv, and k
        self.cp_f.insert(0, '1004')
        self.cv_f.insert(0, '717')
        self.k_f.insert(0, '1.4')

        # Heat transfer = q, Internal Energy = u, Thermodynamic work = w, Enthalpy = h, Entropy = s
        q_f = Entry(self)
        q_f.place(x=50, y=430)
        u_f = Entry(self)
        u_f.place(x=50, y=470)
        w_f = Entry(self)
        w_f.place(x=50, y=510)
        s_f = Entry(self)
        s_f.place(x=300, y=430)
        h_f = Entry(self)
        h_f.place(x=300, y=470)

        # Combobox with gas processes
        combobox_f = Combobox(self, values=[u'Isothermal', u'Isochoric', u'Isobaric', u'Adiabatic'], state="readonly")
        combobox_f.configure(font="Pt  12 bold")
        combobox_f.place(x=50, y=80)
        #Combobox with parameters what can be changed
        changed_variable_f = Combobox(self, values=[u'Pressure', u'Volume', u'Temperature',u'Heat transfer', u'Change in internal energy', u'Thermodynamic work', u'Change in entropy', u'Change in enthalpy'], state="readonly", width=25)
        changed_variable_f.configure(font="Pt  12 bold")
        changed_variable_f.place(x=400, y=80)

        def changed(event):
            # print(combobox_field.current())
            p2_f.delete(0, END)
            v2_f.delete(0, END)
            t2_f.delete(0, END)
            q_f.delete(0, END)
            u_f.delete(0, END)
            w_f.delete(0, END)
            s_f.delete(0, END)
            h_f.delete(0, END)
            if (
                    combobox_f.current() == 0 or changed_variable_f.current() == 0 or changed_variable_f.current() == 1 or changed_variable_f.current() == 3 or changed_variable_f.current() == 5 or changed_variable_f.current() == 7):
                t2_f.configure(state=NORMAL)
                t2_f.delete(0, END)
                t2_f.configure(state=DISABLED)
            else:
                t2_f.configure(state=NORMAL)
                t2_f.delete(0, END)
            if (
                    combobox_f.current() == 1 or changed_variable_f.current() == 0 or changed_variable_f.current() == 2 or changed_variable_f.current() == 3 or changed_variable_f.current() == 4 or changed_variable_f.current() == 6 or changed_variable_f.current() == 7):
                v2_f.configure(state=NORMAL)
                v2_f.delete(0, END)
                v2_f.configure(state=DISABLED)
            else:
                v2_f.configure(state=NORMAL)
                v2_f.delete(0, END)
            if (
                    combobox_f.current() == 2 or changed_variable_f.current() == 1 or changed_variable_f.current() == 2 or changed_variable_f.current() == 3 or changed_variable_f.current() == 4 or changed_variable_f.current() == 5 or changed_variable_f.current() == 6 or changed_variable_f.current() == 7):
                p2_f.configure(state=NORMAL)
                p2_f.delete(0, END)
                p2_f.configure(state=DISABLED)
            else:
                p2_f.configure(state=NORMAL)
                p2_f.delete(0, END)

        def changedv(event):
            p2_f.delete(0, END)
            v2_f.delete(0, END)
            t2_f.delete(0, END)
            q_f.delete(0, END)
            u_f.delete(0, END)
            w_f.delete(0, END)
            s_f.delete(0, END)
            h_f.delete(0, END)
            if changed_variable_f.current() == 0: # pressure will be changed
                t2_f.configure(state=DISABLED)
                v2_f.configure(state=DISABLED)
                q_f.configure(state=DISABLED)
                u_f.configure(state=DISABLED)
                w_f.configure(state=DISABLED)
                s_f.configure(state=DISABLED)
                h_f.configure(state=DISABLED)
                m_f.delete(0, END)
                m_f.configure(state=NORMAL)
                v1_f.delete(0, END)
                if combobox_f.current() == 2: # isobaric process
                    p2_f.configure(state=DISABLED)
                else:
                    p2_f.configure(state=NORMAL)

            elif changed_variable_f.current() == 1: # volume will be changed
                p2_f.configure(state=DISABLED)
                t2_f.configure(state=DISABLED)
                q_f.configure(state=DISABLED)
                u_f.configure(state=DISABLED)
                w_f.configure(state=DISABLED)
                s_f.configure(state=DISABLED)
                h_f.configure(state=DISABLED)
                m_f.delete(0, END)
                m_f.configure(state=DISABLED)
                v1_f.delete(0, END)
                if combobox_f.current() == 1: # isochoric
                    v2_f.configure(state=DISABLED)
                    w_f.configure(state=NORMAL)
                    w_f.insert(0)
                    w_f.configure(state=DISABLED)
                else:
                    v2_f.configure(state=NORMAL)
                    #w_f.configure(state=NORMAL)
            elif changed_variable_f.current() == 2: # temperature will be changed
                p2_f.configure(state=DISABLED)
                v2_f.configure(state=DISABLED)
                q_f.configure(state=DISABLED)
                u_f.configure(state=DISABLED)
                w_f.configure(state=DISABLED)
                s_f.configure(state=DISABLED)
                h_f.configure(state=DISABLED)
                m_f.delete(0, END)
                m_f.configure(state=NORMAL)
                v1_f.delete(0, END)
                if combobox_f.current() == 0: # isothermal
                    t2_f.configure(state=DISABLED)
                    u_f.configure(state=DISABLED)
                    h_f.configure(state=DISABLED)
                else:
                    t2_f.configure(state=NORMAL)
                    #u_f.configure(state=NORMAL)
                    #h_f.configure(state=NORMAL)
            elif changed_variable_f.current() == 3: # heat transfer will be changed
                p2_f.configure(state=DISABLED)
                v2_f.configure(state=DISABLED)
                t2_f.configure(state=DISABLED)
                u_f.configure(state=DISABLED)
                w_f.configure(state=DISABLED)
                s_f.configure(state=DISABLED)
                h_f.configure(state=DISABLED)
                m_f.delete(0, END)
                m_f.configure(state=NORMAL)
                v1_f.delete(0, END)
                if combobox_f.current() == 3: # adiabatic
                    q_f.configure(state=DISABLED)
                    s_f.configure(state=DISABLED)
                else:
                    q_f.configure(state=NORMAL)
                    #s_f.configure(state=NORMAL)
            elif changed_variable_f.current() == 4: # change in internal energy will be changed
                p2_f.configure(state=DISABLED)
                v2_f.configure(state=DISABLED)
                t2_f.configure(state=DISABLED)
                q_f.configure(state=DISABLED)
                w_f.configure(state=DISABLED)
                s_f.configure(state=DISABLED)
                h_f.configure(state=DISABLED)
                m_f.delete(0, END)
                m_f.configure(state=NORMAL)
                v1_f.delete(0, END)
                if combobox_f.current() == 0: # isothermal
                    u_f.configure(state=DISABLED)
                    h_f.configure(state=DISABLED)
                    t2_f.configure(state=DISABLED)
                else:
                    u_f.configure(state=NORMAL)
                    #h_f.configure(state=NORMAL)
                    #t2_f.configure(state=NORMAL)
            elif changed_variable_f.current() == 5: # thermodynamic work will be changed
                p2_f.configure(state=DISABLED)
                v2_f.configure(state=DISABLED)
                t2_f.configure(state=DISABLED)
                q_f.configure(state=DISABLED)
                u_f.configure(state=DISABLED)
                s_f.configure(state=DISABLED)
                h_f.configure(state=DISABLED)
                m_f.delete(0, END)
                m_f.configure(state=NORMAL)
                v1_f.delete(0, END)
                if combobox_f.current() == 1: # isochoric
                    w_f.configure(state=DISABLED)
                    v2_f.configure(state=DISABLED)
                else:
                    w_f.configure(state=NORMAL)
                    #v2_f.configure(state=NORMAL)
            elif changed_variable_f.current() == 6: # entropy transfer will be changed
                p2_f.configure(state=DISABLED)
                v2_f.configure(state=DISABLED)
                t2_f.configure(state=DISABLED)
                q_f.configure(state=DISABLED)
                u_f.configure(state=DISABLED)
                w_f.configure(state=DISABLED)
                h_f.configure(state=DISABLED)
                m_f.delete(0, END)
                m_f.configure(state=NORMAL)
                v1_f.delete(0, END)
                if combobox_f.current() == 3: # adiabatic
                    s_f.configure(state=DISABLED)
                    q_f.configure(state=DISABLED)
                else:
                    s_f.configure(state=NORMAL)
                    #q_f.configure(state=NORMAL)
            elif changed_variable_f.current() == 7: # change in enthalpy will be changed
                p2_f.configure(state=DISABLED)
                v2_f.configure(state=DISABLED)
                t2_f.configure(state=DISABLED)
                q_f.configure(state=DISABLED)
                u_f.configure(state=DISABLED)
                w_f.configure(state=DISABLED)
                s_f.configure(state=DISABLED)
                m_f.delete(0, END)
                m_f.configure(state=NORMAL)
                v1_f.delete(0, END)
                if combobox_f.current() == 0: # isothermal
                    u_f.configure(state=DISABLED)
                    h_f.configure(state=DISABLED)
                    t2_f.configure(state=DISABLED)
                else:
                    #u_f.configure(state=NORMAL)
                    h_f.configure(state=NORMAL)
                    #t2_f.configure(state=NORMAL)

        combobox_f.bind("<<ComboboxSelected>>", changed)
        changed_variable_f.bind("<<ComboboxSelected>>", changedv)
        #calculate_button = Button(self, text="Calculate", command=lambda: self.input_keyboard(p1_f, v1_f, t1_f, p2_f, v2_f, t2_f, combobox_f, changed_variable_f))


        self.add_img = PhotoImage(file='button_title2.png') # Picture for button
        calculate_button = Button(self, command=lambda: self.input_keyboard(p1_f, v1_f, t1_f, p2_f, v2_f, t2_f, m_f, q_f, u_f, w_f, h_f, s_f, combobox_f, changed_variable_f), compound=TOP, image=self.add_img)
        calculate_button.place(x=540, y=500)

       # self.mainloop()
        self.grab_set()
        self.focus_set()

        # Button to clear the inputs of k_f, cp_f, and cv_f Entry widgets
        self.clear_button = tk.Button(self, text='Clear Inputs', command=self.clear_inputs)
        self.clear_button.place(x=400, y=280)  # Adjust the x and y coordinates as needed

    def clear_inputs(self):
    # Clear the contents of the Entry widgets cp, cv und k
        self.k_f.delete(0, tk.END)
        self.cp_f.delete(0, tk.END)
        self.cv_f.delete(0, tk.END)

    def update_entries(self):
    # Bind the entry widgets of cp, cv und k to the entry Widgets
        if self.radio_selection.get() == 1:
            # Assuming cp_f and cv_f are the names of your Entry widgets
            self.cp_f.delete(0, END)
            self.cp_f.insert(0, "1005")
            self.cv_f.delete(0, END)
            self.cv_f.insert(0, "718")
            self.k_f.delete(0, END)
            self.k_f.insert(0, "1.4")
        elif self.radio_selection.get() == 2:
            # Clear the entries or handle the 'Auswählbar' selection differently
            self.cp_f.delete(0, END)
            self.cv_f.delete(0, END)
            self.k_f.delete(0, END)
            self.calculate()

    def calculate(self):
        # Only proceed if Radiobutton 'Choose own Value' is selected
        if self.radio_selection.get() == 2:
            # Cancel any existing scheduled call
            if self._after_id is not None:
                self.after_cancel(self._after_id)

            # Schedule the new call with a delay
            self._after_id = self.after(1000, self.perform_calculation)

    def perform_calculation(self):
            # calculations
            try:
                # Initialize values as None
                cp, cv, k = (None, None, None)

                # Try to get the values if they have been input
                if self.cp_f.get():
                    cp = float(self.cp_f.get())
                if self.cv_f.get():
                    cv = float(self.cv_f.get())
                if self.k_f.get():
                    k = float(self.k_f.get())

                # Calculate missing values if possible
                if cp is not None and cv is not None:
                    k = cp / cv
                    self.k_f.delete(0, tk.END)
                    self.k_f.insert(0, round(k, 2))
                elif k is not None and cp is not None:
                    cv = cp / k
                    self.cv_f.delete(0, tk.END)
                    self.cv_f.insert(0, round(cv, 2))
                elif k is not None and cv is not None:
                    cp = cv * k
                    self.cp_f.delete(0, tk.END)
                    self.cp_f.insert(0, round(cp, 2))
            except ValueError:
                # If one of the values is not convertible to float, do nothing (might mean the field is empty).
                pass


    def input_keyboard(self, p1_f, v1_f, t1_f, p2_f, v2_f, t2_f, m_f, q_f, u_f, w_f, h_f, s_f, combobox_f, changed_variable_f):
        # Define Variables as String
        p1 = p1_f.get()
        t1 = t1_f.get()
        v1 = v1_f.get()
        m = m_f.get()
        cp = self.cp_f.get()
        cv = self.cv_f.get()
        k = self.k_f.get()
        # Create a List of what need to be checked
        fields_to_check = [t1_f, p1_f, self.cp_f, self.cv_f, self.k_f]
        # Checking if these fields are filled
        for field in fields_to_check:
            if not field.get():
                showinfo(title="Error", message="All fields must be filled with a value.")
                return
        # Only one of them need to be filled
        if not m_f.get() and not v1_f.get():
            showinfo(title="Error", message="Either 'm_f' or 'v1_f' must be filled.")
            return

        try: # Check if the Values are numeric
            t1 = float(t1)
            p1 = float(p1)
            cp = float(cp)
            cv = float(cv)
            k = float(k)
            # optionale Entrys
            m = float(m) if m else None
            v1 = float(v1) if v1 else None

        except ValueError:
            showinfo(title="Error", message="The fields can only contain numeric values")

        else:
            # If m is given, calculate v1
            if m:
                # Calculate v1 with the ideal gas equation: pV = mRT, R = cp-cv
                v1 = ((m/1000 * (cp - cv) * t1) / (p1 * 100000)) * 1000
                #
                v1_f.configure(state=NORMAL)
                v1_f.delete(0, END)
                v1_f.insert(0, round(v1, 2))
            else:
                # If m is not given
                v1 = float(v1)

            if combobox_f.current() == 0: #isothertmal

                if changed_variable_f.current() == 0: #pressure will be changed/input
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t1))
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0,0)
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0,0)
                    try:
                        p2 = float(p2_f.get())
                    except ValueError:
                       showinfo(title="Error", message="The fields can only contain numeric values")
                    else:
                        p2 = float(p2_f.get())
                        v2 = p1 * v1 / p2
                        v2_f.configure(state=NORMAL)
                        v2_f.delete(0, END)
                        v2_f.insert(0, round(v2,2))
                        q= (cp-cv) * t1 * math.log(v2/v1)/1000
                        q_f.configure(state=NORMAL)
                        q_f.delete(0, END)
                        q_f.insert(0, round(q))
                        w = -(cp-cv) * t1 * math.log(v2 / v1) / 1000
                        w_f.configure(state=NORMAL)
                        w_f.delete(0, END)
                        w_f.insert(0, round(w))
                        s = (cp-cv) * math.log(v2 / v1)
                        s_f.configure(state=NORMAL)
                        s_f.delete(0, END)
                        s_f.insert(0, round(s))
                elif changed_variable_f.current() == 1: # volume will be changed
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t1))
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0,0)
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0,0)
                    try:
                        v2 = float(v2_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    else:
                        v2 = float(v2_f.get())
                        p2 = p1 * v1 / v2
                        p2_f.configure(state=NORMAL)
                        p2_f.delete(0, END)
                        p2_f.insert(0, round(p2, 2))
                        q = (cp-cv) * t1 * math.log(v2 / v1) / 1000
                        q_f.configure(state=NORMAL)
                        q_f.delete(0, END)
                        q_f.insert(0, round(q))
                        w = -(cp-cv) * t1 * math.log(v2 / v1) / 1000
                        w_f.configure(state=NORMAL)
                        w_f.delete(0, END)
                        w_f.insert(0, round(w))
                        s = (cp-cv) * math.log(v2 / v1)
                        s_f.configure(state=NORMAL)
                        s_f.delete(0, END)
                        s_f.insert(0, round(s))
                elif changed_variable_f.current() == 2: # temperature will be changed, not possible -> error message
                    showinfo(title="Error", message="It is an isothermal process. You can't change temperature.")
                elif changed_variable_f.current() == 3: #heat transfer will be changed/input
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t1))
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0,0)
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0,0)
                    try:
                        q = float(q_f.get())
                    except ValueError:
                       showinfo(title="Error", message="The fields can only contain numeric values")
                    else:
                        q = float(q_f.get())
                        v2=v1*math.exp(q*1000/((cp-cv)*t1))
                        p2 = p1*v1/v2
                        v2_f.configure(state=NORMAL)
                        v2_f.delete(0, END)
                        v2_f.insert(0, round(v2,2))
                        p2_f.configure(state=NORMAL)
                        p2_f.delete(0, END)
                        p2_f.insert(0, round(p2,2))
                        w = -(cp-cv) * t1 * math.log(v2 / v1) / 1000
                        w_f.configure(state=NORMAL)
                        w_f.delete(0, END)
                        w_f.insert(0, round(w))
                        s = (cp-cv) * math.log(v2 / v1)
                        s_f.configure(state=NORMAL)
                        s_f.delete(0, END)
                        s_f.insert(0, round(s))
                elif changed_variable_f.current() == 4: #change in internal energy will be changed/input, not possible -> error message
                    showinfo(title="Error", message="It is an isothermal process. The change in internal energy is zero and cannot be changed.")
                elif changed_variable_f.current() == 5: #thermodynamic work will be changed/input
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t1))
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, 0)
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, 0)
                    try:
                        w = float(w_f.get())
                    except ValueError:
                       showinfo(title="Error", message="The fields can only contain numeric values")
                    else:
                        w = float(w_f.get())
                        v2=v1*math.exp((-1)*w*1000/((cp-cv)*t1))
                        p2 = p1*v1/v2
                        p2_f.configure(state=NORMAL)
                        p2_f.delete(0, END)
                        p2_f.insert(0, round(p2, 2))
                        v2_f.configure(state=NORMAL)
                        v2_f.delete(0, END)
                        v2_f.insert(0, round(v2, 2))
                        q = (cp-cv) * t1 * math.log(v2 / v1) / 1000
                        q_f.configure(state=NORMAL)
                        q_f.delete(0, END)
                        q_f.insert(0, round(q))
                        s = (cp-cv) * math.log(v2 / v1)
                        s_f.configure(state=NORMAL)
                        s_f.delete(0, END)
                        s_f.insert(0, round(s))
                elif changed_variable_f.current() == 6: # entropy will be changed/input
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t1))
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, 0)
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, 0)
                    try:
                        s = float(s_f.get())
                    except ValueError:
                       showinfo(title="Error", message="The fields can only contain numeric values")
                    else:
                        s = float(s_f.get())
                        v2=v1*math.exp(s/(cp-cv))
                        p2 = p1*v1/v2
                        p2_f.configure(state=NORMAL)
                        p2_f.delete(0, END)
                        p2_f.insert(0, round(p2, 2))
                        v2_f.configure(state=NORMAL)
                        v2_f.delete(0, END)
                        v2_f.insert(0, round(v2, 2))
                        q = (cp-cv) * t1 * math.log(v2 / v1) / 1000
                        q_f.configure(state=NORMAL)
                        q_f.delete(0, END)
                        q_f.insert(0, round(q))
                        w = -(cp-cv) * t1 * math.log(v2 / v1) / 1000
                        w_f.configure(state=NORMAL)
                        w_f.delete(0, END)
                        w_f.insert(0, round(w))
                elif changed_variable_f.current() == 7: #enthalpy will be changed/input. Not possible, error message
                    showinfo(title="Error", message="It is an isothermal process. The change in enthalpy is zero and cannot be changed.")

            elif combobox_f.current() == 1: #isochoric
                if changed_variable_f.current() == 0: # pressure will be changed
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, v1)
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, 0)
                    try:
                        p2 = float(p2_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    p2 = float(p2_f.get())
                    t2 = p2 * t1 / p1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    q = cv * (t2-t1) / 1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    u = cv * (t2-t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    s = cv * math.log(t2 / t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 1: # volume will be changed, error
                    showinfo(title="Error", message="It is an isochoric process. You can't change volume.")
                elif changed_variable_f.current() == 2: # temperature will be changed
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, v1)
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, 0)
                    try:
                        t2 = float(t2_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    t2 = float(t2_f.get())
                    p2 = p1 * t2 / t1
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, p2)
                    q = cv * (t2 - t1) / 1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    u = cv * (t2 - t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    s = cv * math.log(t2 / t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 3: # heat transfer will be changed
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, v1)
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, 0)
                    try:
                        q = float(q_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    q = float(q_f.get())
                    t2=q*1000/cv+t1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    p2 = p1 * t2 / t1
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, round(p2,2))
                    u = cv * (t2 - t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    s = cv * math.log(t2 / t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 4: # internal energy will be changed
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, v1)
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, 0)
                    try:
                        u = float(u_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    u = float(u_f.get())
                    t2=u*1000/cv+t1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    p2 = p1 * t2 / t1
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, round(p2,2))
                    q = cv * (t2 - t1) / 1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    s = cv * math.log(t2 / t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 5: # thermodynamic work will be changed
                    showinfo(title="Error", message="It is an isochoric process. The thermodynamic work is zero and cannot be changed.")
                elif changed_variable_f.current() == 6:  # entropy will be changed
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, v1)
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, 0)
                    try:
                        s = float(s_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    s = float(s_f.get())
                    t2=t1*math.exp(s/cv)
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    p2 = p1 * t2 / t1
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, round(p2,2))
                    q = cv * (t2 - t1) / 1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    u = cv * (t2 - t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 7:  # enthalpy will be changed
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, v1)
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, 0)
                    try:
                        h = float(h_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    h = float(h_f.get())
                    t2=h*1000/cp+t1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    p2 = p1 * t2 / t1
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, round(p2,2))
                    q = cv * (t2 - t1) / 1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    u = cv * (t2 - t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    s = cv * math.log(t2 / t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))

            elif combobox_f.current() == 2: # isobaric
                if changed_variable_f.current() == 0: # pressure will be changed
                    showinfo(title="Error", message="It is an isobaric process. You can't change pressure.")
                elif changed_variable_f.current() == 1: # volume will be changed
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, p1)
                    try:
                        v2 = float(v2_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    v2 = float(v2_f.get())
                    t2 = v2 * t1 / v1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    q = cp*(t2-t1)/1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    u = cv*(t2-t1)/1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    s = cp*math.log(t2/t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))
                    h = cp*(t2-t1)/ 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                    w=-(v2 - v1)*8.314*t1 / v1 /(28.96/1000)/1000 # M=28.96/1000 kg/mol; r=8.314

                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w,2))
                elif changed_variable_f.current() == 2: # temperature will be changed
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, p1)
                    try:
                        t2 = float(t2_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    t2 = float(t2_f.get())
                    v2 = t2 * v1 / t1
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2,2))
                    q = cp*(t2-t1)/1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    u = cv*(t2-t1)/1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    s = cp*math.log(t2/t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))
                    h = cp*(t2-t1)/ 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                    print(v2)
                    print(v1)
                    print(t1)
                    w = -(v2 - v1) * 8.314 * t1 / v1 / (28.96 / 1000) / 1000  # M=28.96/1000 kg/mol; r=8.314

                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w, 2))
                elif changed_variable_f.current() == 3: # heat transfer will be changed
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, p1)
                    try:
                        q = float(q_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    q = float(q_f.get())
                    t2 = q*1000/cp+t1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    v2=t2*v1/t1
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2,2))
                    u = cv*(t2-t1)/1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    s = cp*math.log(t2/t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))
                    h = cp*(t2-t1)/ 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                    w = -(v2 - v1) * 8.314 * t1 / v1 / (28.96 / 1000) / 1000  # M=28.96/1000 kg/mol; r=8.314

                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w, 2))
                elif changed_variable_f.current() == 4: # internal energy will be changed
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, p1)
                    try:
                        u= float(u_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    u = float(u_f.get())
                    t2 =u*1000/cv+t1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    v2 = t2 * v1 / t1
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2, 2))
                    q = cp*(t2-t1)/1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    s = cp*math.log(t2/t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))
                    h = cp*(t2-t1)/ 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                    w = -(v2 - v1) * 8.314 * t1 / v1 / (28.96 / 1000) / 1000  # M=28.96/1000 kg/mol; r=8.314
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w, 2))
                elif changed_variable_f.current() == 5: # t.work will be changed
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, p1)
                    try:
                        w = float(w_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    w = float(w_f.get())
                  #  w = -(v2 - v1) * 8.314 * t1 / v1 / (28.96 / 1000) / 1000  # M=28.96/1000 kg/mol; r=8.314
                    v2=(v1/1000-(v1/1000)*(28.96/1000)*(w*1000)/8.314/t1)*1000
                    #v2 = ((-1)*1000*w * (3.56/1000) /(p1*101325)+v1/1000)*1000  # 3.56 *10**(-3) kg - masse der Luft im Zylinder
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2, 2))
                    t2 = t1 * v2 / v1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    q = cp*(t2-t1)/1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    u = cv*(t2-t1)/1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    s = cp*math.log(t2/t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))
                    h = cp*(t2-t1)/ 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 6: # entropy will be changed
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, p1)
                    try:
                        s = float(s_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    s = float(s_f.get())
                    t2 = t1*math.exp(s/cp)
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    v2 = t2 * v1 / t1
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2, 2))
                    q = cp*(t2-t1)/1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    u = cv*(t2-t1)/1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    h = cp*(t2-t1)/ 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                    w = -(v2 - v1) * 8.314 * t1 / v1 / (28.96 / 1000) / 1000  # M=28.96/1000 kg/mol; r=8.314

                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w, 2))
                elif changed_variable_f.current() == 7: # enthalpy will be changed
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, p1)
                    try:
                        h = float(h_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    h = float(h_f.get())
                    t2 = h*1000/cp+t1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    v2 = t2 * v1 / t1

                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2, 2))
                    q = cp*(t2-t1)/1000
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, round(q))
                    u = cv*(t2-t1)/1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    s = cp*math.log(t2/t1)
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, round(s))

                    w = -(v2 - v1) * 8.314 * t1 / v1 / (28.96 / 1000) / 1000  # M=28.96/1000 kg/mol; r=8.314

                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w, 2))


            elif combobox_f.current() == 3: # adiabatic
                if changed_variable_f.current() == 0: # pressure
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, 0)
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, 0)
                    try:
                        p2 = float(p2_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    p2 = float(p2_f.get())
                    v2 = v1 * (p1 / p2) ** (1 / k)
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2,2))
                    t2 = t1 * (p2 / p1) ** ((k - 1) / k)
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    u = cv * (t2 - t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    w = cv * (t2 - t1) / 1000
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 1: #volume
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, 0)
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, 0)
                    try:
                        v2 = float(v2_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    v2 = float(v2_f.get())
                    p2 = p1 * (v1 / v2) ** k
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, p2)
                    t2 = t1 * (v1 / v2) ** (k - 1)
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, t2)
                    u = cv * (t2 - t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    w = cv * (t2 - t1) / 1000
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 2: #temperature
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, 0)
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, 0)
                    try:
                        t2 = float(t2_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    t2 = float(t2_f.get())
                    p2 = p1 * (t2 / t1) ** (k / (k - 1))
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, round(p2,2))
                    v2 = v1 * (t1 / t2) ** (1 / (k - 1))
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2,2))
                    u = cv * (t2 - t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    w = cv * (t2 - t1) / 1000
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 3: #heat transfer
                    showinfo(title="Error",
                             message="It is an adiabatic process. The heat transfer is zero and cannot be changed.")
                elif changed_variable_f.current() == 4:  # int. energy
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, 0)
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, 0)
                    try:
                        u= float(u_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    u = float(u_f.get())
                    t2=u*1000/cv+t1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    p2 = p1 * (t2 / t1) ** (k / (k - 1))
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, round(p2,2))
                    v2 = v1 * (t1 / t2) ** (1 / (k - 1))
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2,2))
                    w = cv * (t2 - t1) / 1000
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 5:  # t.work
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, 0)
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, 0)
                    try:
                        w= float(w_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    w = float(w_f.get())
                    t2=w*1000/cv+t1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    p2 = p1 * (t2 / t1) ** (k / (k - 1))
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, round(p2,2))
                    v2 = v1 * (t1 / t2) ** (1 / (k - 1))
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2,2))
                    u = cv * (t2 - t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    h = cp * (t2 - t1) / 1000
                    h_f.configure(state=NORMAL)
                    h_f.delete(0, END)
                    h_f.insert(0, round(h))
                elif changed_variable_f.current() == 6:  # entropy
                    showinfo(title="Error",
                             message="It is an adiabatic process. The entropy transfer is zero and cannot be changed.")
                elif changed_variable_f.current() == 7:  # enthalpy
                    s_f.configure(state=NORMAL)
                    s_f.delete(0, END)
                    s_f.insert(0, 0)
                    q_f.configure(state=NORMAL)
                    q_f.delete(0, END)
                    q_f.insert(0, 0)
                    try:
                        h= float(h_f.get())
                    except ValueError:
                        showinfo(title="Error", message="The fields can only contain numeric values")
                    h = float(h_f.get())
                    t2=h*1000/cp+t1
                    t2_f.configure(state=NORMAL)
                    t2_f.delete(0, END)
                    t2_f.insert(0, round(t2))
                    p2 = p1 * (t2 / t1) ** (k / (k - 1))
                    p2_f.configure(state=NORMAL)
                    p2_f.delete(0, END)
                    p2_f.insert(0, round(p2,2))
                    v2 = v1 * (t1 / t2) ** (1 / (k - 1))
                    v2_f.configure(state=NORMAL)
                    v2_f.delete(0, END)
                    v2_f.insert(0, round(v2,2))
                    u = cv * (t2 - t1) / 1000
                    u_f.configure(state=NORMAL)
                    u_f.delete(0, END)
                    u_f.insert(0, round(u))
                    w = cv * (t2 - t1) / 1000
                    w_f.configure(state=NORMAL)
                    w_f.delete(0, END)
                    w_f.insert(0, round(w))


if __name__ == "__main__":
    root=tk.Tk()
    app = Main(root)
    app.pack()
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    w=int(width/2-600)
    h=int(height / 2 - 410)
    root.title("Ideal Gas Law Simulation")
    root.geometry("1200x750+{}+{}".format(w, h))
    root.resizable(False, False)
    root.configure(bg='#DFE0DF')

    # diagram p-v

    canvas_h=300
    canvas_w=300
    global canvas
    canvas = tk.Canvas(root, width=canvas_w, height=canvas_h, bg='#FFF6EA')
    canvas.place(x=470, y=440, width=canvas_w, height=canvas_h)

    def draw_axis( x_left, x_right, y_bottom, y_top):
        dx = canvas_w / (x_right - x_left)
        dy = canvas_h / (y_top - y_bottom)
        cx = -x_left * dx
        cy = y_top * dy
        canvas.create_line( 0, cy, canvas_w, cy, fill='#BBA79C')
        canvas.create_line( cx, 0, cx, canvas_h, fill='#BBA79C')
        canvas.create_text(70, 15, text="Pressure (atm)", font="Pt 9 bold italic", fill='#443A32')
        canvas.create_text(260, 240, text="Volume (L)", font="Pt 9 bold italic", fill='#443A32')
        canvas.create_text(35*dx+40, 20.5*dy-20, text="[1 atm, 3 L]", font="Pt 9 bold italic", fill='#443A32')
        canvas.create_oval(34*dx, 19.5*dy, 36*dx, 20.5*dy, fill="#7F6589", outline="#7F6589")
        x_step = (x_right-x_left)/14
        x=x_left+5
        while x<=x_right-5:
            x_canvas=(x-x_left)*dx
            canvas.create_line(x_canvas,cy-1, x_canvas, cy+1, fill='#443A32')
            canvas.create_text(x_canvas, cy+15, text=str(round(x/10,1)), font="Pt 8 ", fill='#443A32')
            x+=x_step
        y_step = (y_top-y_bottom)/7
        y=y_top-5
        while y>=y_bottom+10:
            y_canvas=(y-y_top)*dy
            canvas.create_line(cx-1,-y_canvas,  cx+1, -y_canvas, fill='#443A32')
            canvas.create_text(cx+15, -y_canvas,  text=str(round(y/10,1)), font="Pt 8 ", fill='#443A32')
            y-=y_step
        return dx, dy
    def frange(begin, end, step):
        x=begin
        t=[]
        while x<=end:
            t.append(x)
            x+=step
        return t
    def graph_generator(x_tmp):
        y_tmp=[]
        for x in x_tmp:
            y=x*100    # multiplication with 100 because of x_left and x_right are integer
            y_tmp.append(y)
        return y_tmp
    global shift_step
    shift_step = 35
    def graph_dot(x_tmp, y_tmp, shift):
        dot_list =[]
        i=0
        for x in x_tmp:
            y=y_tmp[i]
            x = (x - x_tmp[0] + shift) * dx
            y=(y-y_top)*dy
            dot = canvas.create_oval(x-1, -(y-1), x+1,-(y+1), fill="#7F6589", outline="#7F6589")
            dot_list.append(dot)
            i+=1
        return dot_list
    x_left, x_right = -5, 65  # test
    y_bottom, y_top = -5, 30
    dx, dy = draw_axis(x_left, x_right, y_bottom, y_top)
    global graph_start, graph_end, p_start, p_end
    graph_start = 3
    graph_end =3
    p_start = 1
    p_end = 1
    x_list = frange(graph_start, graph_end, 0.01)
    y_graph = graph_generator(x_list)
    graph = graph_dot(x_list, y_graph, shift_step)

    # diagram T-S
    global c
    c = tk.Canvas(root, width=canvas_w, height=canvas_h, bg='#FFF6EA')
    c.place(x=850, y=440, width=canvas_w, height=canvas_h)
    def draw_axis2( x_left2, x_right2, y_bottom2, y_top2):
        dx2 = canvas_w / (x_right2 - x_left2)
        dy2 = canvas_h / (y_top2 - y_bottom2)

        cx2 = -x_left2 * dx2
        cy2 = y_top2 * dy2

        c.create_line( 0, cy2, canvas_w, cy2, fill='#BBA79C')
        c.create_line( cx2, 0, cx2, canvas_h, fill='#BBA79C')
        c.create_text(90, 15, text="Temperature (K)", font="Pt 9 bold italic", fill='#443A32')
        c.create_text(240, 250, text="Entropy (J/(kg*K))", font="Pt 9 bold italic", fill='#443A32')
        c.create_text(82*dx2+60, 51*dy2+10, text="[298 K, 700 J/(kg*K)]", font="Pt 9 bold italic", fill='#443A32')
        c.create_oval(78*dx2, 49*dy2, 82*dx2, 51*dy2, fill="#7F6589", outline="#7F6589")
        x_step2 = (x_right2-x_left2)/10
        x2=x_left2+10
        while x2<=x_right2-5:
            x_canvas2=(x2-x_left2)*dx2
            c.create_line(x_canvas2,cy2-1, x_canvas2, cy2+1, fill='#443A32')
            c.create_text(x_canvas2, cy2+15, text=str(round(x2*10)), font="Pt 8 ", fill='#443A32')
            x2+=x_step2
        y_step2 = (y_top2-y_bottom2)/9
        y2=y_top2-5

        while y2>=y_bottom2+15:
            y_canvas2=(y2-y_top2)*dy2
            c.create_line(cx2-1,-y_canvas2,  cx2+1, -y_canvas2, fill='#443A32')
            c.create_text(cx2+15, -y_canvas2,  text=str(round(y2*10)), font="Pt 8 ", fill='#443A32')
            y2-=y_step2

        return dx2, dy2

    def frange2(begin2, end2, step2):
        x2=begin2
        t2=[]
        while x2<=end2:
            t2.append(x2)
            x2+=step2
        return t2

    def graph_generator2(x_tmp2):
        y_tmp2=[]
        for x2 in x_tmp2:
            y2=x2*1000            # multiplication with 100 because of x_left and x_right are integer
            y_tmp2.append(y2)
        return y_tmp2

    def graph_dot2(x_tmp2, y_tmp2, shift2):
        dot_list2 =[]
        i2=0
        for x2 in x_tmp2:
            y2=y_tmp2[i2]
            x2 = (x2 - x_tmp2[0] + shift2) * dx2
            y2=(y2-y_top2)*dy2
            dot2 = c.create_oval(x2-1, -(y2-1), x2+1,-(y2+1), fill="#7F6589", outline="#7F6589")
            dot_list2.append(dot2)
            i2+=1
        return dot_list2

    global shift_step2
    shift_step2 = 35

    x_left2, x_right2 = -10, 190
    y_bottom2, y_top2 = -10, 80
    global graph_start2, graph_end2, p_start2, p_end2
    graph_start2 = 3
    graph_end2 =3
    p_start2 = 1
    p_end2 = 1

    dx2, dy2 = draw_axis2(x_left2, x_right2, y_bottom2, y_top2)
    x_list2 = frange2(x_left2, x_right2, 0.01)
    #x_list2 = frange(graph_start2, graph_end2, 0.01)
    y_graph2 = graph_generator2(x_list2)
    graph2 = graph_dot2(x_list2, y_graph2, shift_step2)

root.mainloop()
