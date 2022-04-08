from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, Tk
import random
import os
import pandas as pd
from datetime import date
import winsound
from playsound import playsound

#remove copy warning pandas
pd.options.mode.chained_assignment = None

root = Tk()
root.title('Welcome to KAKE House home schooling.')
root.iconbitmap('images/gun_icon.ico')
root.geometry('648x432')
root["cursor"]="@images/cursors/crosshair_black.cur"

#variables for global
math_workbook=[]
spelling_workbook=[]

#WHEN YOU HOVER OVER A BUTTON
def button_hover(button):
    if button["state"] != DISABLED:
        button["bg"] = 'white'
        button["cursor"] = '@images/cursors/crosshair_red.cur'
        if button == math_button:
            status_label.config(text="Click for math options.")
        if button == spelling_button:
            status_label.config(text="Click for spelling options.")
        if button == home_button:
            status_label.config(text="Click to return home.")
        if button == math_workbook:
            status_label.config(text="Click for some math practice.")
        if button == spelling_workbook:
            status_label.config(text="Click for some spelling practice.")
        if button == math_game:
            status_label.config(text="Click for a math game.")
        if button == spelling_game:
            status_label.config(text="Click for a spelling game.")
        playsound('sounds/reload.wav', block=False)

#WHEN YOU STOP HOVERING OVER A BUTTON
def button_leave(button):
    if button == home_button:
        button["bg"] = 'orange'
    else:
        button["bg"] = 'black'
    status_label.configure(text='Hello Evelynn! Welcome to home school! When you are able to read this, you get a present!')

#wHEN YOU CLOSE A TOPLEVEL()
def on_closing(window):
        winsound.PlaySound('sounds/bg_song.wav', winsound.SND_FILENAME| winsound.SND_ASYNC )
        window.destroy()

#MATH OPTIONS
def math_options():
    global home_button
    global math_button
    global spelling_button
    global status_label
    global button_list
    global math_workbook
    global math_game
    status_label.config(text="Welcome to math.")
    for i in button_list:
        i.place_forget()
    math_workbook=Button(root, bg='black',text = '', image = photoimage, command=lambda: [winsound.PlaySound('sounds/shoot.wav', winsound.SND_FILENAME| winsound.SND_ASYNC),math_work()])
    math_workbook.place(x=400, y=125)
    math_workbook.bind("<Enter>", lambda event: button_hover(math_workbook))
    math_workbook.bind("<Leave>", lambda event: button_leave(math_workbook))
    math_game=Button(root, state=DISABLED, bg='black',text = '', image = game_photo_image, command=lambda: [winsound.PlaySound('sounds/shoot.wav', winsound.SND_FILENAME| winsound.SND_ASYNC),spelling_game()])
    math_game.place(x=505, y=125)    
    math_game.bind("<Enter>", lambda event: button_hover(math_game))
    math_game.bind("<Leave>", lambda event: button_leave(math_game))
    home_button.place(x=463,y=265)
    button_list=[math_workbook, home_button, math_game]

#SPELLING OPTIONS
def spelling_options():
    global home_button
    global math_button
    global spelling_button
    global status_label
    global button_list
    global spelling_workbook
    global spelling_game
    status_label.config(text="Welcome to spelling.")
    for i in button_list:
        i.place_forget()
    spelling_workbook=Button(root, bg='black',text = '', image = photoimage, command=lambda: [winsound.PlaySound('sounds/shoot.wav', winsound.SND_FILENAME| winsound.SND_ASYNC),spelling_work()]) 
    spelling_workbook.place(x=400, y=125)    
    spelling_workbook.bind("<Enter>", lambda event: button_hover(spelling_workbook))
    spelling_workbook.bind("<Leave>", lambda event: button_leave(spelling_workbook))
    spelling_game=Button(root, state=DISABLED, bg='black',text = '', image = game_photo_image, command=lambda: [winsound.PlaySound('sounds/shoot.wav', winsound.SND_FILENAME| winsound.SND_ASYNC),spelling_game()]) 
    spelling_game.place(x=505, y=125)
    spelling_game.bind("<Enter>", lambda event: button_hover(spelling_game))
    spelling_game.bind("<Leave>", lambda event: button_leave(spelling_game))
    home_button.place(x=463,y=265)
    button_list=[home_button, spelling_workbook, spelling_game]

#HOME BUTTON CALL
def home():
    global math_button
    global spelling_button
    global home_button
    global status_label
    global button_list
    status_label.configure(text='Hello Andrew! Welcome to home school! When you are able to read this, you get a present!')
    for i in button_list:
        i.place_forget()
    math_button.place(x=450, y=125)
    spelling_button.place(x=450, y=230)
    button_list=[math_button, spelling_button]

#math practice reset
def app_reset(app_root,where_from):
    winsound.PlaySound('sounds/reset.wav', winsound.SND_FILENAME| winsound.SND_ASYNC )
    app_root.destroy()
    eval(where_from)

#MATH PRACTICE
def math_work():
    global on_closing
    global button_list2
    global num_correct
    global num_wrong 
    global current_wrong
    global question_num
    global victory_mp
    global gun_bg
    mwork = Toplevel()
    mwork.title('Math Practice.')
    mwork.iconbitmap('images/gun_icon.ico')
    mwork.geometry('500x500')
    mwork["cursor"]="@images/cursors/crosshair_green.cur"
    background_image2=ImageTk.PhotoImage(file='images/background2.jpg')
    background_label2 = Label(mwork, image=background_image2)
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)

    #VARIABLES
    max_var = IntVar()
    max_var.set(0)
    add_var = StringVar() 
    add_var.set('`')   
    sub_var = StringVar()
    sub_var.set('`')  
    mult_var = StringVar()
    mult_var.set('`')  
    div_var = StringVar()
    div_var.set('`')

    #GUN BG IMAGE
    gun_bg=ImageTk.PhotoImage(Image.open("images/bg_m_quest.png"))
    
    #victory images
    victory_mp=ImageTk.PhotoImage(Image.open("images/victory_bg_mp.png"))

    #GRADING VARIABLES
    num_correct=0
    num_wrong=0  
    question_num=1
    current_wrong=1

    def make_decision(value,math_sign_init):
        global num_correct
        global num_wrong
        global question_num
        global current_wrong
        if float(e_answer.get())==float(cor_ans):
            num_correct+=1
            question_num+=1
            current_wrong=1
            e_answer.delete(0,END)
            m_execute(value=value1,math_sign_init=math_sign_list)
            #Label(mwork,text=str(value1)+' '+str(math_sign_list)+' '+str(cor_ans)).place(x=100,y=300)
        else:
            num_wrong+=1
            if current_wrong==1:
                current_wrong+=1
                c.create_text(155,65,text='Incorrect Answer. Please try again.',fill='red')
            else:
                concentrate=messagebox.showerror('Incorrect Answer.','You got the answer wrong more than once. This is just a focus reminder.')

    def m_done():
        global num_correct
        global num_wrong
        global index_grades
        global math_area
        winsound.PlaySound('sounds/victory.wav', winsound.SND_FILENAME| winsound.SND_ASYNC )
        total_num=num_correct+num_wrong
        c = Canvas(mwork, width=500, height=500)
        c.place(x=0,y=0)
        c.create_image(0,0,image=victory_mp,anchor="nw")
        c.image=victory_mp
        restartBut=Button(mwork,text='Go back into the storm!', command=lambda: app_reset(app_root=mwork,where_from='math_work()'))
        c.create_window(250, 375,window=restartBut)
        c.create_text(250,200,font=('Castellar',9,'bold'),text='Number correct:\n\n\n\nTotal Number of Questions:\n\n\n\nPercent:',justify='center')
        c.create_text(250,162,font=('Cambria',20,'bold'),text=str(num_correct),justify='center')
        c.create_text(250,220,font=('Cambria',20,'bold'),text=str(total_num),justify='center')
        c.create_text(250,300,font=('Castellar',35,'bold'),text='{:.0%}'.format((num_correct/total_num)),justify='center')
        df=pd.read_excel('grading_book.xlsx', index_col='Entry')
        today=date.today()
        df_new_dict = {'Date': [today.strftime('%m/%d/%y')], 'Subject': ['Math'],'Area':[math_area], 'Grade': [int(round((num_correct/total_num)*100))], 'Correct':[num_correct], 'Incorrect':[num_wrong]}
        df_new=pd.DataFrame(data=df_new_dict)
        df2=pd.concat([df, df_new], sort=False,ignore_index=True)
        df2.index.name='Entry'
        is_math=df2['Subject']=='Math'
        df3=df2[is_math]
        df2['Math AVG'][0]=int(round(sum(df3['Grade'])/len(df3)))
        df2['Total AVG'][0]=int(round(sum(df2['Grade'])/len(df2)))
        df2.to_excel('grading_book.xlsx')        

    def m_execute(value,math_sign_init):
        global c
        global num1
        global num2
        global sign_choice
        global question_num
        global cor_ans
        global e_answer
        global math_area
        gun_list=['gun1.png', 'gun10.png', 'gun11.png', 'gun12.png', 'gun13.png', 'gun14.png', 'gun15.png', 'gun16.png', 'gun17.png', 'gun18.png', 'gun19.png', 'gun2.png', 'gun20.png', 'gun21.png', 'gun3.png', 'gun4.png', 'gun5.png', 'gun6.png', 'gun7.png', 'gun8.png', 'gun9.png']
        gun_choice_p=random.choice(gun_list)
        gun_choice=ImageTk.PhotoImage(Image.open("images/guns/"+gun_choice_p).resize((250,84), Image.ANTIALIAS))
        #gun_bg=ImageTk.PhotoImage(Image.open("images/bg_m_quest.png"))
        c = Canvas(mwork, width=250, height=84)
        c.place(x=65,y=175)
        c.create_image(0,0,image=gun_bg,anchor="nw")
        c.image=gun_bg
        c.create_image(0,0,image=gun_choice,anchor="nw")
        c.image=gun_choice
        
        num1=random.randint(0,value)
        num2=random.randint(0,value)
        num3=0
        sign_choice=random.choice(math_sign_init)
        cor_ans=0
        math_area=math_sign_init

        e_answer = Entry(mwork,fg='white',relief=SUNKEN,bg='black',font=('Cambria',40,'bold'),width=3)
        e_answer.place(x=336,y=189)

        if sign_choice=='+':
            cor_ans=num1+num2
        elif sign_choice=='-':
            cor_ans=max(num1,num2)-min(num1,num2)
        elif sign_choice=='×':
            cor_ans=num1*num2
        elif sign_choice=='÷':
            if num2==0:
                num2=random.randint(1,value)
            num3=num1*num2
            cor_ans=num3/num2

        if sign_choice=='÷':
            q_n=c.create_text(0,0,text=str(question_num)+'.',anchor='nw', fill='black',font=('Cambria',20))
            q_cont=c.create_text(125,35,text=str(num3)+sign_choice+str(num2), fill='white', font=('Cambria',40,'bold'))
            bbqn=c.bbox(q_n)
            qn_rec=c.create_rectangle(bbqn, outline="black", fill="white")
            c.tag_raise(q_n,qn_rec)
        elif sign_choice=='-':
            q_n=c.create_text(0,0,text=str(question_num)+'.',anchor='nw', fill='black',font=('Cambria',20))
            q_cont=c.create_text(125,35,text=str(max(num1,num2))+sign_choice+str(min(num1,num2)), fill='white', font=('Cambria',40,'bold'))
            bbqn=c.bbox(q_n)
            qn_rec=c.create_rectangle(bbqn, outline="black", fill="white")
            c.tag_raise(q_n,qn_rec)
        else:
            q_n=c.create_text(0,0,text=str(question_num)+'.',anchor='nw',fill='black', font=('Cambria',20))
            q_cont=c.create_text(125,35,text=str(num1)+sign_choice+str(num2), fill='white', font=('Cambria',40,'bold'))
            bbqn=c.bbox(q_n)
            qn_rec=c.create_rectangle(bbqn, outline="black", fill="white")
            c.tag_raise(q_n,qn_rec)

        doneBut=Button(mwork,text='Leave the storm.',command=m_done).place(x=200,y=350)
            
        mwork.bind('<Return>',lambda event: make_decision(value=value1,math_sign_init=math_sign_list))
        e_answer.focus_set()
    
    #WHEN GO! BUTTON IS CLICKED
    def clicked(value):
        global value1
        global math_sign_list
        value1=value
        math_sign_init1=[add_var.get(),sub_var.get(),mult_var.get(),div_var.get()] 
        math_sign_count=0
        math_sign_list=[]
        #ERROR FOR MISSING VALUES
        def missing_val():
            math_sign_count=0
            math_sign_list=[]
            errorBox=messagebox.showerror("Missing values.","You either didnt choose a maximum number, or you didn't choose any operators. Click OK to continue.")
        #CHECK FOR MISSING CHECKS IN OPERATORS SELECTIONS
        for i in math_sign_init1:
            if i == '`':
                math_sign_count+=1
            else:
                math_sign_list.append(i)
        if math_sign_count == 4 or value == 0:
            missing_val()
        #EXECUTE PRACTICE (ALL VALUES PRESENT)
        else:
            #GO GO GO!
            winsound.PlaySound('sounds/gogogo.wav', winsound.SND_FILENAME| winsound.SND_ASYNC)
            #CLEAR THE SCREEN
            for i in button_list2:
                i.destroy()
            #EXECUTE
            m_execute(value=value1,math_sign_init=math_sign_list)

    ##### OPENING LAYOUT #####
    #BOX SURROUNDING THE CHECKBOXES
    box1=Label(mwork, width=38, height=12, relief=SUNKEN, bd=3, bg='black')
    box1.place(x=127,y=120)
    #max number options
    chk5=Checkbutton(mwork,text='5',selectcolor='black',variable=max_var,onvalue=5,fg='white', bg='black')
    chk10=Checkbutton(mwork,text='10',selectcolor='black',variable=max_var,onvalue=10, fg='white', bg='black')
    chk20=Checkbutton(mwork,text='20',selectcolor='black',variable=max_var,onvalue=20, fg='white', bg='black')
    chk50=Checkbutton(mwork,text='50',selectcolor='black',variable=max_var,onvalue=50, fg='white', bg='black')
    chk100=Checkbutton(mwork,text='100',selectcolor='black',variable=max_var,onvalue=100, fg='white', bg='black')
    chk5.place(x=170,y=150)
    chk10.place(x=170,y=170)
    chk20.place(x=170,y=190)
    chk50.place(x=170,y=210)
    chk100.place(x=170,y=230)
    #math sign options
    addBut=Checkbutton(mwork,text='Addition (+)',selectcolor='black',variable=add_var,onvalue='+', fg='white', bg='black',offvalue='`')
    subBut=Checkbutton(mwork,text='Subtraction (-)',selectcolor='black',variable=sub_var,onvalue='-', fg='white', bg='black',offvalue='`')
    multBut=Checkbutton(mwork,text='Multiplication (×)',selectcolor='black',variable=mult_var,onvalue='×', fg='white', bg='black',offvalue='`')
    divBut=Checkbutton(mwork,text='Division (÷)',selectcolor='black',variable=div_var,onvalue='÷', fg='white', bg='black',offvalue='`')
    addBut.place(x=270,y=157)
    subBut.place(x=270,y=177)
    multBut.place(x=270,y=197)
    divBut.place(x=270,y=217)
    maxnumL=Label(mwork, text='Maximum Number:',fg='white', bg='black')
    maxnumL.place(x=137,y=130)
    mathopL=Label(mwork, text='Math Operator(s):',fg='white', bg='black')
    mathopL.place(x=270,y=137)

    #GO BUTTON
    goBut=Button(mwork,text='GO!', command=lambda: clicked(max_var.get()))
    goBut.place(x=249,y=270)

    #BUTTON LIST AND STATUS BAR
    button_list2=[box1,chk5,chk10,chk20,chk50,chk100,addBut,subBut,multBut,divBut,maxnumL,mathopL,goBut]
    status=Label(mwork, text='We love you Evelynn May Close.', bd=2, relief=SUNKEN, anchor=E)
    status.place(x=0,y=480, relwidth=1.0)

    #LOOP AND PROTOCOL OPTIONS
    mwork.protocol("WM_DELETE_WINDOW", lambda: on_closing(mwork))
    mwork.mainloop()

#MATH GAME
def math_game():
    return

#SPELLILNG PRACTICE
def spelling_work():
    global on_closing
    global button_list2
    global sp_work_bg
    global num_correct
    global num_wrong 
    global current_wrong
    global question_num
    global victory_sp
    swork = Toplevel()
    swork.title('Spelling Practice.')
    swork.iconbitmap('images/gun_icon.ico')
    swork.geometry('550x688')
    swork["cursor"]="@images/cursors/crosshair_green.cur"
    background_image3=ImageTk.PhotoImage(file='images/background3.jpg')
    background_label3 = Label(swork, image=background_image3)
    background_label3.place(x=0, y=0, relwidth=1, relheight=1)

    #Variables
    spell_opt=StringVar()
    spell_opt.set('nothing')
    num_correct=0
    num_wrong=0  
    question_num=1
    current_wrong=1

    #Images
    sp_work_bg=ImageTk.PhotoImage(Image.open("images/bg_sp_quest.png"))
    victory_sp=ImageTk.PhotoImage(Image.open("images/victory_bg_sp.png"))
    

    def make_decision(option):
        global c,sp_word,let_remove,num_correct,question_num,num_wrong,current_wrong,buttonlist_2, doneBut
        spell_op=option
        if spell_op == 'whole':
            if e_answer.get() == sp_word:
                num_correct+=1
                question_num+=1
                current_wrong=1
                for i in buttonlist_2:
                    i.destroy()
                s_execute(option=spell_op)
            else:
                num_wrong+=1
                if current_wrong==1:
                    current_wrong+=1
                    c.create_text(350,75,text='Incorrect Answer. Please try again.',fill='red',anchor='se')
                else:
                    concentrate=messagebox.showerror('Incorrect Answer.','You got the answer wrong more than once. This is just a focus reminder.')
        else:
            if e_answer.get() == let_remove:
                num_correct+=1
                question_num+=1
                current_wrong=1
                for i in buttonlist_2:
                    i.destroy()
                s_execute(option=spell_op)
            else:
                num_wrong+=1
                if current_wrong==1:
                    current_wrong+=1
                    c.create_text(350,75,text='Incorrect Answer. Please try again.',fill='red',anchor='se')
                else:
                    concentrate=messagebox.showerror('Incorrect Answer.','You got the answer wrong more than once. This is just a focus reminder.')
    def s_done():
        global num_correct
        global num_wrong
        global spell_op
        winsound.PlaySound('sounds/victory.wav', winsound.SND_FILENAME| winsound.SND_ASYNC )
        total_num=num_correct+num_wrong
        c = Canvas(swork, width=550, height=688)
        c.place(x=0,y=0)
        c.create_image(0,0,image=victory_sp,anchor="nw")
        c.image=victory_sp
        restartBut=Button(swork,text='Go back into the storm!', command=lambda: app_reset(app_root=swork,where_from='spelling_work()'))
        c.create_window(275,475,window=restartBut)
        c.create_text(275,300,font=('Castellar',9,'bold'),text='Number correct:\n\n\n\nTotal Number of Questions:\n\n\n\nPercent:',justify='center')
        c.create_text(275,262,font=('Cambria',20,'bold'),text=str(num_correct),justify='center')
        c.create_text(275,320,font=('Cambria',20,'bold'),text=str(total_num),justify='center')
        c.create_text(275,400,font=('Castellar',35,'bold'),text='{:.0%}'.format((num_correct/total_num)),justify='center')
        df=pd.read_excel('grading_book.xlsx', index_col='Entry')
        today=date.today()
        df_new_dict = {'Date': [today.strftime('%m/%d/%y')], 'Subject': ['Spelling'], 'Area': [spell_op], 'Grade': [int(round((num_correct/total_num)*100))], 'Correct':[num_correct], 'Incorrect':[num_wrong]}
        df_new=pd.DataFrame(data=df_new_dict)
        df2=pd.concat([df, df_new], sort=False,ignore_index=True)
        df2.index.name='Entry'
        is_spelling=df2['Subject']=='Spelling'
        df3=df2[is_spelling]
        df2['Spelling AVG'][0]=int(round(sum(df3['Grade'])/len(df3)))
        df2['Total AVG'][0]=int(round(sum(df2['Grade'])/len(df2)))
        df2.to_excel('grading_book.xlsx')

    def s_execute(option):
        global sp_images_list
        global spell_op
        global vowel_list
        global sp_word
        global e_answer
        global let_remove
        global question_num
        global buttonlist_2
        global c
        global doneBut
        spell_op=option
        vowel_list='aeiou'
        sp_word=''
        let_remove=''
        spell_dir_list=[]
        for i in os.listdir('images/spelling'):
            spell_dir_list.append(i)
        sp_image_random=random.choice(spell_dir_list)
        sp_image=ImageTk.PhotoImage(Image.open('images/spelling/'+sp_image_random))
        sp_image_label=Label(swork,image=sp_image)
        sp_image_label.image=sp_image
        sp_image_label.place(relx=0.5,y=250,anchor=CENTER)
        c = Canvas(swork, width=350, height=75)
        c.place(relx=0.5,y=425, anchor=CENTER)
        c.create_image(0,0,image=sp_work_bg,anchor="nw")        
        c.image=sp_work_bg
        q_n=c.create_text(0,0,text=str(question_num)+'.',anchor='nw', fill='black',font=('Cambria',20))
        bbqn=c.bbox(q_n)
        qn_rec=c.create_rectangle(bbqn, outline="black", fill="white")
        c.tag_raise(q_n,qn_rec)

        if spell_op=='vowels':
            sp_word=sp_image_random.split('.')[0]
            let_remove_pre=[]
            for i in sp_word:
                if i in vowel_list:
                    let_remove_pre.append(i)
            let_remove=random.choice(let_remove_pre)
            sp_word_change=sp_word.replace(let_remove,' __ ',1)
            c.create_text(172,33,text=sp_word_change, fill='white', font=('Cambria',40,'bold'))            
            e_answer = Entry(swork,fg='white',relief=SUNKEN,bg='black',font=('Cambria',40,'bold'),width=1)
            
        elif spell_op=='consonants':
            sp_word=sp_image_random.split('.')[0]
            let_remove_pre=[]            
            for i in sp_word:
                if i not in vowel_list:
                    let_remove_pre.append(i)
            let_remove=random.choice(let_remove_pre)
            sp_word_change=sp_word.replace(let_remove,' __ ',1)
            c.create_text(172,33,text=sp_word_change, fill='white', font=('Cambria',40,'bold'))
            e_answer = Entry(swork,fg='white',relief=SUNKEN,bg='black',font=('Cambria',40,'bold'),width=1)
            
        elif spell_op=='both':
            sp_word=sp_image_random.split('.')[0]
            let_remove=random.choice(sp_word)
            sp_word_change=sp_word.replace(let_remove,' __ ',1)
            c.create_text(172,33,text=sp_word_change, fill='white', font=('Cambria',40,'bold'))
            e_answer = Entry(swork,fg='white',relief=SUNKEN,bg='black',font=('Cambria',40,'bold'),width=1)
            
        else:
            sp_word=sp_image_random.split('.')[0]
            sp_word_change=''
            for i in sp_word:
                sp_word_change+=' __ '
            c.create_text(172,33,text=sp_word_change, fill='white', font=('Cambria',40,'bold'))
            e_answer = Entry(swork,fg='white',relief=SUNKEN,bg='black',font=('Cambria',40,'bold'),width=len(sp_word))
            
        e_answer.place(relx=0.5,y=530,anchor=CENTER)       

        doneBut=Button(swork,text='Leave the storm.',command=s_done).place(relx=0.5,y=600, anchor=CENTER)
        buttonlist_2=[e_answer,c,sp_image_label]
        swork.bind('<Return>',lambda event: make_decision(option=spell_op))
        e_answer.focus_set()
        
    def clicked(option):
        spell_op=option
        if option =='nothing':
            errorBox=messagebox.showerror("Didn't select an option.","You must check one of the options. Click OK to continue.")
        else:
            winsound.PlaySound('sounds/gogogo.wav', winsound.SND_FILENAME| winsound.SND_ASYNC )
            for i in button_list2:
                i.destroy()                
            s_execute(option=spell_op)

    ##### OPENING LAYOUT #####
    box1=Label(swork, width=27, height=12, relief=SUNKEN, bd=3, bg='black')
    box1.place(x=173,y=190)
    #max number options #550x668
    chk_word=Checkbutton(swork,text='Entire words',selectcolor='black',variable=spell_opt,onvalue='whole',offvalue='nothing',fg='white', bg='black')
    chk_vow=Checkbutton(swork,text='Missing vowels',selectcolor='black',variable=spell_opt,onvalue='vowels',offvalue='nothing', fg='white', bg='black')
    chk_con=Checkbutton(swork,text='Missing consonants',selectcolor='black',variable=spell_opt,onvalue='consonants',offvalue='nothing', fg='white', bg='black')
    chk_both=Checkbutton(swork,text='Missing letters',selectcolor='black',variable=spell_opt,onvalue='both',offvalue='nothing', fg='white', bg='black')    
    chk_word.place(x=205,y=220)
    chk_vow.place(x=205,y=240)
    chk_con.place(x=205,y=260)
    chk_both.place(x=205,y=280)
    spell_op=Label(swork, text='What would you like to practice?',fg='white', bg='black')
    spell_op.place(x=183,y=200)
    goBut=Button(swork,text='GO!', command=lambda: clicked(spell_opt.get()))
    goBut.place(x=258,y=327)

    #BUTTON LIST AND STATUS BAR
    button_list2=[box1,chk_word,chk_vow,chk_con,chk_both,spell_op,goBut]
    status= Label(swork, text='We love you Evelynn May Close!', bd=2, relief=SUNKEN, anchor=E)
    status.place(x=0,y=668, relwidth=1.0)

    #LOOP AND PROTOCOL OPTIONS
    swork.protocol("WM_DELETE_WINDOW", lambda: on_closing(swork))
    swork.mainloop()

#SPELLING GAME
def spelling_game():
    return
    


#make background image
background_image=ImageTk.PhotoImage(file='images/background.jpg')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#status label
status_label= Label(root, text='Hello Andrew! Welcome to home school! When you are able to read this, you get a present!', bd=2, relief=SUNKEN, anchor=E)
#make buttons
home_photo = PhotoImage(file = r"images/home_button.png")
home_photo_image = home_photo.subsample(5,5)
photo = PhotoImage(file = r"images/practice_button.png")
photoimage = photo.subsample(4,4)
math_photo = PhotoImage(file = r"images/math_button.png")
math_photo_image = math_photo.subsample(4,4)
spelling_photo = PhotoImage(file = r"images/spelling_button.png")
spelling_photo_image = spelling_photo.subsample(4,4)
game_photo = PhotoImage(file = r"images/game_button.png")
game_photo_image = game_photo.subsample(4,4)

math_button=Button(root,text = '', bg='black', image = math_photo_image, command=lambda: [playsound('sounds/shoot.wav',block=False),math_options()]) 
spelling_button=Button(root,text = '',bg='black', image = spelling_photo_image, command=lambda: [playsound('sounds/shoot.wav',block=False),spelling_options()]) 
home_button=Button(root,text='',bg='orange', image = home_photo_image, command=lambda: [playsound('sounds/shoot.wav',block=False),home()]) 
math_button.bind("<Enter>", lambda event: button_hover(math_button))
math_button.bind("<Leave>", lambda event: button_leave(math_button))
spelling_button.bind("<Enter>", lambda event: button_hover(spelling_button))
spelling_button.bind("<Leave>", lambda event: button_leave(spelling_button))
home_button.bind("<Enter>", lambda event: button_hover(home_button))
home_button.bind("<Leave>", lambda event: button_leave(home_button))
math_button.place(x=450, y=125)
spelling_button.place(x=450, y=230)
button_list=[math_button, spelling_button]
#place status bar
status_label.place(x=0,y=412, relwidth=1.0)
#playsound('sounds/bg_song.mp3', block=False)
winsound.PlaySound('sounds/bg_song.wav', winsound.SND_FILENAME| winsound.SND_ASYNC )
root.mainloop()
