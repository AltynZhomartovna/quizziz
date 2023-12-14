import psycopg2
from tkinter import *
from tkinter import messagebox
import importlib
import ast
import tkinter as tk
from CALCULATOR import calcu
from INVENTIONTABLE import invention
from DIFFERENTBRANCHESOFSCIENCE import diff
from BOOKSAUTHOR import bookss
from PERIODICTABLE import period
from ACRONYM import acro
from faq import create_faq_app
username = ""
subject = ""
main = Tk()
main.title('Main Page')
main.config(background='#fff')
main.geometry('1920x1080')
main.resizable(True,True)
def connect_to_database():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="2005",
            host="localhost",
            port="5432",
            database="postgres",
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

def sign():
        main.destroy()
img=PhotoImage(file='mainpage.png')
Label(main,image=img,bg='white').place(x=0,y=0)


def sign_in():
    root = Toplevel(main)
    root.title('Registation Form')
    root.config(background='#fff')
    root.geometry('1920x1080')
    root.resizable(True,True)
    
    def signin():
        global username,subject
        username=user.get()
        password=code.get()
        connection = connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                # Replace "users" with your actual table name
                cursor.execute("SELECT * FROM Usertable WHERE Username=%s AND Password=%s", (username, password))

                user_data = cursor.fetchone()
                if user_data:
                    # User exists, do something
                    print("User authenticated")
                else:
                    # User not found or invalid credentials
                    messagebox.showerror("Invalid", "Invalid username and password")
            except (Exception, psycopg2.Error) as error:
                print("Error executing SQL query", error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
        screen=Toplevel(root)
        screen.title("Quiz")
        screen.geometry('1920x1080')
        screen.config(bg='white')
        screen.resizable(True,True)
        img=PhotoImage(file='1.png')
        Label(screen,image=img,bg='white').place(x=0,y=0)
        s=Button(screen,width=10,text='Get started',border=0,bg='white',cursor='hand2',fg='black',font=('Garet',18),command=search)
        s.place(x=465,y=670)
        login=Button(screen,width=6,text='Log out',border=0,bg='white',cursor='hand2',fg='black',font=('Garet',12,'bold'),command=sign)
        login.place(x=1080,y=37)
        screen.mainloop()
        
    def search():
        scren=Toplevel(root)
        scren.title("Search")
        scren.geometry('1920x1080')
        scren.config(bg='black')
        scren.resizable(True,True)
        img=PhotoImage(file='2.png')
        Label(scren,image=img,bg='white').place(x=0,y=0)
        def load_quiz_data(subject):
                try:
                    quiz_module = importlib.import_module(f"{subject.lower()}_quiz")
                    return quiz_module.quiz_data
                except ImportError:
                    messagebox.showerror("Error", f"No quiz data available for subject: {subject}")
        def on_enter(e):
            subject_entry.delete(0,'end')

        def on_leave(e):
            subject=subject_entry.get()
            if subject_entry.get()=='':
                subject_entry.insert(0,'Search')
        def start_quiz():
            subject = subject_entry.get()
            global quiz_data
            quiz_data = load_quiz_data(subject)
            if quiz_data:
                global score, current_question
                score = 0
                quiz()
                current_question = 0
                mainpage.config(state="disabled")
        subject_entry=Entry(scren,width=25,fg='grey',bg='#F2F2F2',border=0,font=('Garet',16,'bold'))
        subject_entry.place(x=420,y=160)
        subject_entry.insert(0,'Search')
        subject_entry.bind('<FocusIn>',on_enter)
        subject_entry.bind('<FocusOut>',on_leave)
        def quiz():
            global current_question,quiz_data
    
            def show_question():
                question_number_label.config(text="Question {}".format(current_question + 1))
                question = quiz_data[current_question]
                qs_label.config(text=question["question"])

                choices = question["choices"]
                for i in range(4):
                    choice_btns[i].config(text=choices[i], state="normal")

                feedback_label.config(text="")
                next_btn.config(state="disabled")

            def check_answer(choice):
                question = quiz_data[current_question]
                selected_choice = choice_btns[choice].cget("text")
                if selected_choice == question["answer"]:
                    global score
                    score += 1
                    score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
                    feedback_label.config(text="Correct!", foreground="green", font=('Arial', 14))
                else:
                    feedback_label.config(text="Incorrect!", foreground="red", font=('Arial', 14))
                    feedback_label.place(x=20, y=550)
                for button in choice_btns:
                    button.config(state="disabled")
                next_btn.config(state="normal")
            current_question = 0
            def next_question():
                global current_question,score, username,subject
                current_question += 1
                if current_question < len(quiz_data):
                    show_question()
                else:
                    messagebox.showinfo("Quiz Completed",
                                        "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
                    connection = connect_to_database()
                    if connection:
                        try:
                            cursor = connection.cursor()
                            cursor.execute("SELECT * FROM UserTable WHERE Username=%s AND Subject=%s", (username))
                            existing_score = cursor.fetchone()

                            if existing_score:
                                if score > existing_score[2]:
                                    cursor.execute("UPDATE Usertable SET Score=%s WHERE Subject=%s AND Username=%s",
                                                   (score, subject, username))
                            else: 
                                cursor.execute("INSERT INTO Usertable (Username, Subject, Score) VALUES (%s, %s, %s)",
                                               (username, subject, score))


                            connection.commit()
                            print("Score stored successfully")
                        except (Exception, psycopg2.Error) as error:
                            print("Error executing SQL query", error)
                        finally:
                            if connection:
                                connection.close()
                    new.destroy()

            def calculator():
                calcu()

            def invent():
                invention()

            def sci():
                diff()

            def books():
                bookss()

            def per():
                period()

            def apo():
                acro()

            def sign():
                confirmation = messagebox.askquestion("Confirmation", "Are you sure you want to leave? Your score will be deleted")
                if confirmation == 'yes':
                    new.destroy()
                else:
                    pass

            new = Toplevel(scren)
            new.title("Quiz App")
            new.config(bg='white')
            new.geometry("1920x1080")
            img = tk.PhotoImage(file='3.png')
            tk.Label(new, image=img, bg='white').place(x=0, y=0)
            question_number_label = tk.Label(new, text="Question 1", fg='black', border=0, bg='white', font=('Arial', 14))
            question_number_label.place(x=20, y=150)
           

            choice_btns = []
            button_height = 70
            for i in range(4):
                button = tk.Button(new, command=lambda i=i: check_answer(i), fg='black', border=0, bg='#DCDCDC', anchor='center',
                                   font=('Arial', 12), pady=5)
                button.place(x=20, y=(i * button_height) + 250)
                choice_btns.append(button)

            feedback_label = tk.Label(new, fg='black', bg='white')
            feedback_label.place(x=20, y=550)
            score = 0
            score_label = tk.Label(new, text="Score: 0/0", fg='black', border=0, bg='white', font=('Arial', 14))
            score_label.place(x=20, y=630)
            next_btn = tk.Button(new, text="Next", command=next_question, state="disabled", font=('Arial', 14))
            next_btn.place(x=20, y=700)
            qs_label = tk.Label(new, fg='black', border=0, bg='white', font=('Arial', 14), wraplength=800)
            qs_label.place(x=20, y=180)
            frame = tk.Frame(new, width=1000, height=2, bg='black')
            frame.place(x=0, y=100)

            calc_btn = tk.Button(new, width=10, text='Calculator', border=0, bg='black', cursor='hand2', fg='white',font=('Arial', 12, 'bold'), justify='left', command=calculator)
            calc_btn.place(x=1035, y=300)
            tk.Frame(new, width=200, height=2, bg='white').place(x=1030, y=325)
            period_btn = tk.Button(new, width=13, text='Periodic Table', border=0, bg='black', cursor='hand2', fg='white',font=('Arial', 12, 'bold'), justify='left', command=per)
            period_btn.place(x=1035, y=350)
            tk.Frame(new, width=200, height=2, bg='white').place(x=1030, y=375)
            apo_btn = tk.Button(new, width=10, text='Aporonyms', border=0, bg='black', cursor='hand2', fg='white',font=('Arial', 12, 'bold'), justify='left', command=apo)
            apo_btn.place(x=1035, y=400)
            tk.Frame(new, width=200, height=2, bg='white').place(x=1030, y=425)
            inv_btn = tk.Button(new, width=13, text='Invention Table', border=0, bg='black', cursor='hand2', fg='white',font=('Arial', 12, 'bold'), justify='left', command=invent)
            inv_btn.place(x=1035, y=450)
            tk.Frame(new, width=200, height=2, bg='white').place(x=1030, y=475)
            books_btn = tk.Button(new, width=15, text='Books and authors', border=0, bg='black', cursor='hand2', fg='white',font=('Arial', 12, 'bold'), justify='left', command=books)
            books_btn.place(x=1035, y=500)
            tk.Frame(new, width=200, height=2, bg='white').place(x=1030, y=525)
            sci_btn = tk.Button(new, width=17, text='Different branches of Science', border=0, bg='black', cursor='hand2',fg='white', font=('Arial', 12, 'bold'), wraplength=200, justify='left', command=sci)
            sci_btn.place(x=1035, y=550)
            tk.Frame(new, width=200, height=2, bg='white').place(x=1030, y=595)
            leave_btn = tk.Button(new, width=6, text='Leave', border=0, bg='grey', cursor='hand2', fg='white',font=('Arial', 18), command=sign)
            leave_btn.place(x=1000, y=680)

            current_question = 0
            show_question()
            new.mainloop()

        mainpage=Button(scren,width=6,text='OK',border=0,cursor='hand2',fg='black',bg='grey',font=('Garet',15,'bold'),command=start_quiz)
        mainpage.place(x=1000,y=160)
        login=Button(scren,width=6,text='Exit',border=0,bg='black',cursor='hand2',fg='white',font=('Garet',12,'bold'),command=sign)
        login.place(x=1150,y=37)
        scren.mainloop()


    def signup_command():
        window=Toplevel(root)
        window.title('SignUp')
        window.config(background='#fff')
        window.geometry('1920x1080')
        window.resizable(True,True)
        def signup():
            username=user.get()
            password=code.get()
            urname=myname.get()
            conform_password=conform_code.get()
            connection = connect_to_database()
            if connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO Usertable (Username, Name, Password) VALUES (%s, %s, %s)", (username, urname, password))

                    connection.commit()
                    print("User registered successfully")
                except (Exception, psycopg2.Error) as error:
                    print("Error executing SQL query", error)
                    connection.rollback()
                finally:
                    # Close the database connection
                    if connection:
                        cursor.close()
                        connection.close()


        def sign():
            window.destroy()
            
        img=PhotoImage(file='register.png')
        Label(window,image=img,bg='white').place(x=0,y=0)

        def on_enter(e):
            user.delete(0,'end')

        def on_leave(e):
            name=user.get()
            if name=='':
                user.insert(0,'Username')
        user=Entry(window,width=25,fg='black',border=0,bg='white',font=('Garet',14))
        user.place(x=750,y=210)
        user.insert(0,'Username')
        user.bind('<FocusIn>',on_enter)
        user.bind('<FocusOut>',on_leave)
        Frame(window,width=440,height=2,bg='black').place(x=710,y=233)

        def on_enter(e):
            code.delete(0,'end')

        def on_leave(e):
            name=code.get()
            if name=='':
                code.insert(0,'Password')
        code=Entry(window,width=25,fg='black',border=0,bg='white',font=('Garet',14))
        code.place(x=750,y=350)
        code.insert(0,'Password')
        code.bind('<FocusIn>',on_enter)
        code.bind('<FocusOut>',on_leave)
        Frame(window,width=440,height=2,bg='black').place(x=710,y=373)

        def on_enter(e):
            myname.delete(0,'end')

        def on_leave(e):
            name=myname.get()
            if name=='':
                code.insert(0,'Name')
        myname=Entry(window,width=25,fg='black',border=0,bg='white',font=('Garet',14))
        myname.place(x=750,y=280)
        myname.insert(0,'Name')
        myname.bind('<FocusIn>',on_enter)
        myname.bind('<FocusOut>',on_leave)
        Frame(window,width=440,height=2,bg='black').place(x=710,y=303)
        def on_enter(e):
            conform_code.delete(0,'end')

        def on_leave(e):
            name=conform_code.get()
            if name=='':
                conform_code.insert(0,'Conform Password')
        conform_code=Entry(window,width=25,fg='black',border=0,bg='white',font=('Garet',14))
        conform_code.place(x=750,y=420)
        conform_code.insert(0,'Conform Password')
        conform_code.bind('<FocusIn>',on_enter)
        conform_code.bind('<FocusOut>',on_leave)
        Frame(window,width=440,height=2,bg='black').place(x=710,y=443)
        Button(window,width=60,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=710,y=480)
        signin=Button(window,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#262626',command=signup,font=('Garet',14))
        signin.place(x=990,y=625)
        
        window.mainloop()

   
    img=PhotoImage(file='sign.png')
    Label(root,image=img,bg='white').place(x=0,y=0)
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(root,width=25,fg='white',border=0,bg='#262626',font=('Garet',14))
    user.place(x=220,y=290)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(root,width=400,height=2,bg='white').place(x=180,y=320)

    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    code=Entry(root,width=25,fg='white',border=0,bg='#262626',font=('Garet',14))
    code.place(x=220,y=390)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)
    Frame(root,width=400,height=2,bg='white').place(x=180,y=420)

    Button(root,width=35,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin,font=('Garet',14)).place(x=180,y=490)
    sign_up=Button(root,width=10,text='Sign up',bg='#262626',fg='#57a1f8',border=0,command=signup_command).place(x=420,y=570)
    root.mainloop()
def cont():
    c = tk.Tk()
    c.title("CONTACT US")
    c.config(bg='white')
    info_text = (
        "At EduExplore, we're committed to providing you with a seamless experience. "
        "If you're in search of guides and resources or have any feedback to share, "
        "we are here to listen and help.\n\n"
        "Feel free to browse through a comprehensive set of articles, user guides, "
        "and FAQs hosted on our Main page. You may find answers to commonly asked "
        "questions on this platform. When you're logged into EduExplore, you can access "
        "the Help Center by clicking on the purple '?' icon () at the bottom-right "
        "corner of your screen.\n\n"
        "For quick assistance and troubleshooting, you can reach out to us at "
        "support@eduexplore.com. Our dedicated team of support agents is here to address "
        "your queries. You can also reach our support team by filling out this form "
        "and submitting a request."
    )

    label_info = tk.Label(c,bg='white', fg='black',text=info_text, justify="left", wraplength=600, padx=20, pady=20)
    label_info.pack()

    c.mainloop()

apply=Button(main,width=15,text='Join for',border=0,bg='black',cursor='hand2',fg='white',font=('Garet',12,'bold'))
apply.place(x=200,y=505)
appl=Button(main,width=12,text='Log in',border=0,bg='white',cursor='hand2',fg='black',font=('Garet',12,'bold'),command=sign_in)
appl.place(x=430,y=505)
login=Button(main,width=6,text='Leave',border=0,bg='grey',cursor='hand2',fg='white',font=('Garet',12,'bold'),command=sign)
login.place(x=1080,y=37)
faq=Button(main,width=3,text='FAQ',border=0,bg='white',cursor='hand2',fg='black',font=('Garet',12,'bold'),command=create_faq_app)
faq.place(x=650,y=40)
con=Button(main,width=9,text='Contact us',border=0,bg='white',cursor='hand2',fg='black',font=('Garet',12,'bold'),command=cont)
con.place(x=700,y=40)
main.mainloop()
