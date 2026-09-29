import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os


# ==========================================================
#                    COLOR THEME
# ==========================================================

BG_COLOR = "#EEF4F8"
WHITE = "#FFFFFF"
PRIMARY = "#2F6F8F"
PRIMARY_DARK = "#24566F"
LIGHT_BLUE = "#DCECF4"
TEXT = "#263238"
SECONDARY = "#607D8B"
SUCCESS = "#3A9D70"
SUCCESS_DARK = "#2E805B"
DANGER = "#D9534F"
BORDER = "#D6E2E8"
ENTRY_BG = "#F8FBFD"


# ==========================================================
#                    MAIN WINDOW
# ==========================================================

root = tk.Tk()
root.title("Student Management System")
root.configure(bg=BG_COLOR)

try:
    root.state("zoomed")
except:
    root.attributes("-zoomed", True)


# ==========================================================
#                    GLOBAL VARIABLES
# ==========================================================

content = None
current_page = None


# ==========================================================
#                    UTILITY FUNCTIONS
# ==========================================================

def clear_root():
    """Remove all widgets from main window."""
    for widget in root.winfo_children():
        widget.destroy()


def create_entry(parent, width=35, show=None):
    entry = tk.Entry(
        parent,
        width=width,
        font=("Segoe UI", 12),
        bg=ENTRY_BG,
        fg=TEXT,
        insertbackground=TEXT,
        relief="solid",
        bd=1,
        show=show
    )
    return entry


def get_data():

    file = "student_admission.csv"

    if os.path.exists(file):
        try:
            return pd.read_csv(file, dtype=str)
        except:
            return pd.DataFrame()

    return pd.DataFrame()


# ==========================================================
#                    LOGIN PAGE
# ==========================================================

def show_login():

    global current_page

    clear_root()

    current_page = "login"

    root.title("Student Management System - Login")
    root.configure(bg=BG_COLOR)

    # ------------------------------------------------------
    # MAIN CONTAINER
    # ------------------------------------------------------

    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )

    # ------------------------------------------------------
    # LEFT PANEL
    # ------------------------------------------------------

    left = tk.Frame(
        main,
        bg=PRIMARY,
        width=550
    )

    left.pack(
        side="left",
        fill="y"
    )

    left.pack_propagate(False)

    tk.Label(
        left,
        text="🎓",
        font=("Segoe UI", 60),
        bg=PRIMARY,
        fg=WHITE
    ).pack(
        pady=(150, 20)
    )

    tk.Label(
        left,
        text="STUDENT",
        font=("Segoe UI", 32, "bold"),
        bg=PRIMARY,
        fg=WHITE
    ).pack()

    tk.Label(
        left,
        text="MANAGEMENT SYSTEM",
        font=("Segoe UI", 22, "bold"),
        bg=PRIMARY,
        fg=WHITE
    ).pack(
        pady=(0, 20)
    )

    tk.Label(
        left,
        text="Manage student information\nquickly, securely and efficiently.",
        font=("Segoe UI", 13),
        bg=PRIMARY,
        fg="#E8F4F8",
        justify="center"
    ).pack(
        pady=10
    )

    tk.Label(
        left,
        text="Python for Data Science • PBL Project",
        font=("Segoe UI", 10),
        bg=PRIMARY,
        fg="#C9E1EA"
    ).pack(
        side="bottom",
        pady=40
    )

    # ------------------------------------------------------
    # RIGHT PANEL
    # ------------------------------------------------------

    right = tk.Frame(
        main,
        bg=BG_COLOR
    )

    right.pack(
        side="right",
        fill="both",
        expand=True
    )

    # Login Card
    login_card = tk.Frame(
        right,
        bg=WHITE,
        width=500,
        height=560,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    login_card.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    login_card.pack_propagate(False)

    tk.Label(
        login_card,
        text="Welcome Back",
        font=("Segoe UI", 28, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        pady=(55, 5)
    )

    tk.Label(
        login_card,
        text="Sign in to access the student portal",
        font=("Segoe UI", 11),
        bg=WHITE,
        fg=SECONDARY
    ).pack(
        pady=(0, 35)
    )

    # Username
    tk.Label(
        login_card,
        text="Username",
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=55
    )

    username_entry = create_entry(
        login_card,
        width=38
    )

    username_entry.pack(
        padx=55,
        pady=(8, 20),
        ipady=9,
        fill="x"
    )

    # Password
    tk.Label(
        login_card,
        text="Password",
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=55
    )

    password_frame = tk.Frame(
        login_card,
        bg=WHITE
    )

    password_frame.pack(
        padx=55,
        pady=(8, 8),
        fill="x"
    )

    password_entry = create_entry(
        password_frame,
        width=30,
        show="*"
    )

    password_entry.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=9
    )

    password_visible = [False]

    def toggle_password():

        if password_visible[0]:

            password_entry.config(show="*")
            show_button.config(text="Show")

            password_visible[0] = False

        else:

            password_entry.config(show="")
            show_button.config(text="Hide")

            password_visible[0] = True

    show_button = tk.Button(
        password_frame,
        text="Show",
        command=toggle_password,
        font=("Segoe UI", 9, "bold"),
        bg=LIGHT_BLUE,
        fg=PRIMARY_DARK,
        relief="flat",
        cursor="hand2",
        width=7
    )

    show_button.pack(
        side="right",
        padx=(5, 0),
        ipady=5
    )

    # Login
    def login():

        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if username == "" or password == "":

            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )

            return

        if username == "admin" and password == "1234":

            show_dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password."
            )

    tk.Button(
        login_card,
        text="LOGIN TO SYSTEM",
        command=login,
        font=("Segoe UI", 12, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        activebackground=PRIMARY_DARK,
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2"
    ).pack(
        padx=55,
        pady=(25, 15),
        fill="x",
        ipady=12
    )

    tk.Label(
        login_card,
        text="Demo Login",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=SECONDARY
    ).pack(
        pady=(10, 2)
    )

    tk.Label(
        login_card,
        text="Username: admin    |    Password: 1234",
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=SECONDARY
    ).pack()

    tk.Label(
        login_card,
        text="Authorized users only",
        font=("Segoe UI", 9),
        bg=WHITE,
        fg="#9AA7AD"
    ).pack(
        side="bottom",
        pady=25
    )

    username_entry.focus()


# ==========================================================
#                    DASHBOARD
# ==========================================================

def show_dashboard():

    global content
    global current_page

    clear_root()

    current_page = "dashboard"

    root.title("Student Management System - Dashboard")

    # ======================================================
    # HEADER
    # ======================================================

    header = tk.Frame(
        root,
        bg=PRIMARY,
        height=85
    )

    header.pack(
        fill="x"
    )

    header.pack_propagate(False)

    tk.Label(
        header,
        text="🎓  STUDENT MANAGEMENT SYSTEM",
        font=("Segoe UI", 22, "bold"),
        bg=PRIMARY,
        fg=WHITE
    ).pack(
        side="left",
        padx=35
    )

    tk.Label(
        header,
        text="ADMIN PORTAL",
        font=("Segoe UI", 11, "bold"),
        bg=PRIMARY,
        fg="#D8EDF4"
    ).pack(
        side="right",
        padx=40
    )

    # ======================================================
    # MAIN AREA
    # ======================================================

    main = tk.Frame(
        root,
        bg=BG_COLOR
    )

    main.pack(
        fill="both",
        expand=True
    )

    # ======================================================
    # SIDEBAR
    # ======================================================

    sidebar = tk.Frame(
        main,
        bg=WHITE,
        width=250,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)

    tk.Label(
        sidebar,
        text="MAIN MENU",
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=SECONDARY
    ).pack(
        anchor="w",
        padx=25,
        pady=(35, 20)
    )

    # ======================================================
    # CONTENT AREA
    # ======================================================

    content = tk.Frame(
        main,
        bg=BG_COLOR
    )

    content.pack(
        side="right",
        fill="both",
        expand=True
    )

    # ======================================================
    # MENU FUNCTIONS
    # ======================================================

    def clear_content():

        for widget in content.winfo_children():
            widget.destroy()

    # ------------------------------------------------------
    # STUDENT ADMISSION
    # ------------------------------------------------------

    def open_admission():

        clear_content()

        show_admission_page()

    # ------------------------------------------------------
    # STUDENT RECORDS
    # ------------------------------------------------------

    def open_records():

        clear_content()

        tk.Label(
            content,
            text="Student Records",
            font=("Segoe UI", 27, "bold"),
            bg=BG_COLOR,
            fg=TEXT
        ).pack(
            anchor="w",
            padx=45,
            pady=(35, 5)
        )

        tk.Label(
            content,
            text="View all registered student information",
            font=("Segoe UI", 11),
            bg=BG_COLOR,
            fg=SECONDARY
        ).pack(
            anchor="w",
            padx=45,
            pady=(0, 20)
        )

        data = get_data()

        if data.empty:

            tk.Label(
                content,
                text="No student records found.",
                font=("Segoe UI", 16),
                bg=BG_COLOR,
                fg=SECONDARY
            ).pack(
                pady=100
            )

            return

        # Table container
        table_frame = tk.Frame(
            content,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        table_frame.pack(
            padx=45,
            pady=10,
            fill="both",
            expand=True
        )

        # Treeview
        columns = list(data.columns)

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        # Scrollbars
        vertical_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )

        horizontal_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=tree.xview
        )

        tree.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        vertical_scroll.pack(
            side="right",
            fill="y"
        )

        horizontal_scroll.pack(
            side="bottom",
            fill="x"
        )

        tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Headings
        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=150,
                anchor="center"
            )

        # Data
        for _, row in data.iterrows():

            tree.insert(
                "",
                "end",
                values=list(row)
            )

        # Style
        style = ttk.Style()

        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=35
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background=PRIMARY,
            foreground=WHITE
        )

    # ------------------------------------------------------
    # DATA ANALYSIS
    # ------------------------------------------------------

    def open_analysis():

        clear_content()

        tk.Label(
            content,
            text="Data Analysis",
            font=("Segoe UI", 27, "bold"),
            bg=BG_COLOR,
            fg=TEXT
        ).pack(
            anchor="w",
            padx=45,
            pady=(35, 5)
        )

        tk.Label(
            content,
            text="Statistical analysis of student performance",
            font=("Segoe UI", 11),
            bg=BG_COLOR,
            fg=SECONDARY
        ).pack(
            anchor="w",
            padx=45,
            pady=(0, 25)
        )

        data = get_data()

        if data.empty:

            tk.Label(
                content,
                text="No data available for analysis.",
                font=("Segoe UI", 16),
                bg=BG_COLOR,
                fg=SECONDARY
            ).pack(
                pady=100
            )

            return

        # Percentage conversion
        data["Percentage"] = pd.to_numeric(
            data["Percentage"],
            errors="coerce"
        )

        total = len(data)

        average = data["Percentage"].mean()

        highest = data["Percentage"].max()

        lowest = data["Percentage"].min()

        # Cards
        cards_frame = tk.Frame(
            content,
            bg=BG_COLOR
        )

        cards_frame.pack(
            padx=45,
            pady=20,
            fill="x"
        )

        for i in range(4):

            cards_frame.columnconfigure(
                i,
                weight=1
            )

        def create_card(title, value, column):

            card = tk.Frame(
                cards_frame,
                bg=WHITE,
                highlightbackground=BORDER,
                highlightthickness=1
            )

            card.grid(
                row=0,
                column=column,
                padx=8,
                sticky="nsew"
            )

            tk.Label(
                card,
                text=title,
                font=("Segoe UI", 11),
                bg=WHITE,
                fg=SECONDARY
            ).pack(
                pady=(25, 5)
            )

            tk.Label(
                card,
                text=value,
                font=("Segoe UI", 25, "bold"),
                bg=WHITE,
                fg=PRIMARY
            ).pack(
                pady=(0, 25)
            )

        create_card(
            "Total Students",
            str(total),
            0
        )

        create_card(
            "Average %",
            f"{average:.2f}%",
            1
        )

        create_card(
            "Highest %",
            f"{highest:.2f}%",
            2
        )

        create_card(
            "Lowest %",
            f"{lowest:.2f}%",
            3
        )

        # Summary
        summary = tk.Frame(
            content,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        summary.pack(
            padx=45,
            pady=20,
            fill="x"
        )

        tk.Label(
            summary,
            text="Performance Summary",
            font=("Segoe UI", 18, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(
            anchor="w",
            padx=30,
            pady=(25, 15)
        )

        summary_text = (
            f"Total students registered: {total}\n\n"
            f"Average percentage: {average:.2f}%\n\n"
            f"Highest percentage: {highest:.2f}%\n\n"
            f"Lowest percentage: {lowest:.2f}%"
        )

        tk.Label(
            summary,
            text=summary_text,
            font=("Segoe UI", 12),
            bg=WHITE,
            fg=SECONDARY,
            justify="left"
        ).pack(
            anchor="w",
            padx=30,
            pady=(0, 30)
        )

    # ------------------------------------------------------
    # REPORTS
    # ------------------------------------------------------

    def open_reports():

        clear_content()

        tk.Label(
            content,
            text="Reports",
            font=("Segoe UI", 27, "bold"),
            bg=BG_COLOR,
            fg=TEXT
        ).pack(
            anchor="w",
            padx=45,
            pady=(35, 5)
        )

        tk.Label(
            content,
            text="Student management system report",
            font=("Segoe UI", 11),
            bg=BG_COLOR,
            fg=SECONDARY
        ).pack(
            anchor="w",
            padx=45,
            pady=(0, 25)
        )

        data = get_data()

        if data.empty:

            tk.Label(
                content,
                text="No student data available.",
                font=("Segoe UI", 16),
                bg=BG_COLOR,
                fg=SECONDARY
            ).pack(
                pady=100
            )

            return

        data["Percentage"] = pd.to_numeric(
            data["Percentage"],
            errors="coerce"
        )

        total = len(data)

        average = data["Percentage"].mean()

        highest = data["Percentage"].max()

        lowest = data["Percentage"].min()

        # Report Card
        report_card = tk.Frame(
            content,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        report_card.pack(
            padx=45,
            fill="x"
        )

        tk.Label(
            report_card,
            text="Student Report Summary",
            font=("Segoe UI", 20, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(
            anchor="w",
            padx=35,
            pady=(30, 25)
        )

        report_text = (
            f"Total Registered Students : {total}\n\n"
            f"Average Percentage       : {average:.2f}%\n\n"
            f"Highest Percentage       : {highest:.2f}%\n\n"
            f"Lowest Percentage        : {lowest:.2f}%"
        )

        tk.Label(
            report_card,
            text=report_text,
            font=("Segoe UI", 12),
            bg=WHITE,
            fg=TEXT,
            justify="left"
        ).pack(
            anchor="w",
            padx=35,
            pady=(0, 25)
        )

        tk.Label(
            report_card,
            text="✓ Report generated successfully",
            font=("Segoe UI", 11, "bold"),
            bg=WHITE,
            fg=SUCCESS
        ).pack(
            anchor="w",
            padx=35,
            pady=(0, 25)
        )

        # Save Report
        def save_report():

            report_file = "student_report.txt"

            report_content = (
                "========================================\n"
                "       STUDENT MANAGEMENT SYSTEM\n"
                "             STUDENT REPORT\n"
                "========================================\n\n"
                f"Total Students : {total}\n"
                f"Average %      : {average:.2f}%\n"
                f"Highest %      : {highest:.2f}%\n"
                f"Lowest %       : {lowest:.2f}%\n\n"
                "========================================\n"
            )

            with open(
                report_file,
                "w"
            ) as file:

                file.write(
                    report_content
                )

            messagebox.showinfo(
                "Report Saved",
                "Student report saved as student_report.txt"
            )

        tk.Button(
            report_card,
            text="SAVE REPORT",
            command=save_report,
            font=("Segoe UI", 11, "bold"),
            bg=SUCCESS,
            fg=WHITE,
            activebackground=SUCCESS_DARK,
            relief="flat",
            cursor="hand2",
            width=20
        ).pack(
            padx=35,
            pady=(5, 30),
            ipady=10
        )

    # ======================================================
    # SIDEBAR BUTTONS
    # ======================================================

    def menu_button(
        text,
        command,
        active=False
    ):

        button = tk.Button(
            sidebar,
            text=text,
            command=command,
            font=("Segoe UI", 11, "bold" if active else "normal"),
            bg=LIGHT_BLUE if active else WHITE,
            fg=PRIMARY_DARK if active else SECONDARY,
            activebackground=LIGHT_BLUE,
            activeforeground=PRIMARY_DARK,
            relief="flat",
            anchor="w",
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=15,
            pady=5,
            ipady=10
        )

        return button

    menu_button(
        "   📝   Student Admission",
        open_admission,
        True
    )

    menu_button(
        "   👤   Student Records",
        open_records
    )

    menu_button(
        "   📊   Data Analysis",
        open_analysis
    )

    menu_button(
        "   📈   Reports",
        open_reports
    )

    # ======================================================
    # LOGOUT
    # ======================================================

    def logout():

        answer = messagebox.askyesno(
            "Logout",
            "Do you want to logout?"
        )

        if answer:

            show_login()

    tk.Button(
        sidebar,
        text="LOGOUT",
        command=logout,
        font=("Segoe UI", 10, "bold"),
        bg="#FDECEC",
        fg=DANGER,
        activebackground="#F8D7D7",
        relief="flat",
        cursor="hand2"
    ).pack(
        side="bottom",
        fill="x",
        padx=25,
        pady=30,
        ipady=10
    )

    # Show admission by default
    show_admission_page()


# ==========================================================
#                 STUDENT ADMISSION PAGE
# ==========================================================

def show_admission_page():

    global content

    # Clear content
    for widget in content.winfo_children():
        widget.destroy()

    # Page heading
    tk.Label(
        content,
        text="Student Admission",
        font=("Segoe UI", 27, "bold"),
        bg=BG_COLOR,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=45,
        pady=(35, 5)
    )

    tk.Label(
        content,
        text="Register a new student in the system",
        font=("Segoe UI", 11),
        bg=BG_COLOR,
        fg=SECONDARY
    ).pack(
        anchor="w",
        padx=45,
        pady=(0, 25)
    )

    # Form card
    form_card = tk.Frame(
        content,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    form_card.pack(
        padx=45,
        fill="x"
    )

    form_card.columnconfigure(
        0,
        weight=1
    )

    form_card.columnconfigure(
        1,
        weight=1
    )

    tk.Label(
        form_card,
        text="Student Information",
        font=("Segoe UI", 18, "bold"),
        bg=WHITE,
        fg=TEXT
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="w",
        padx=35,
        pady=(30, 5)
    )

    tk.Label(
        form_card,
        text="Please enter accurate student information",
        font=("Segoe UI", 10),
        bg=WHITE,
        fg=SECONDARY
    ).grid(
        row=1,
        column=0,
        columnspan=2,
        sticky="w",
        padx=35,
        pady=(0, 20)
    )

    # Field function
    def add_field(
        label_text,
        row,
        column
    ):

        frame = tk.Frame(
            form_card,
            bg=WHITE
        )

        frame.grid(
            row=row,
            column=column,
            sticky="ew",
            padx=35,
            pady=8
        )

        tk.Label(
            frame,
            text=label_text,
            font=("Segoe UI", 10, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(
            anchor="w"
        )

        entry = tk.Entry(
            frame,
            font=("Segoe UI", 11),
            bg=ENTRY_BG,
            fg=TEXT,
            insertbackground=TEXT,
            relief="solid",
            bd=1
        )

        entry.pack(
            fill="x",
            pady=(7, 0),
            ipady=8
        )

        return entry

    # Fields
    id_entry = add_field(
        "Student ID *",
        2,
        0
    )

    name_entry = add_field(
        "Student Name *",
        2,
        1
    )

    email_entry = add_field(
        "Email Address *",
        3,
        0
    )

    phone_entry = add_field(
        "Phone Number *",
        3,
        1
    )

    branch_entry = add_field(
        "Branch *",
        4,
        0
    )

    semester_entry = add_field(
        "Semester *",
        4,
        1
    )

    percentage_entry = add_field(
        "Percentage *",
        5,
        0
    )

    # ======================================================
    # ADD STUDENT
    # ======================================================

    def add_student():

        student_id = id_entry.get().strip()
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        branch = branch_entry.get().strip()
        semester = semester_entry.get().strip()
        percentage = percentage_entry.get().strip()

        # Empty check
        if not all([
            student_id,
            name,
            email,
            phone,
            branch,
            semester,
            percentage
        ]):

            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields."
            )

            return

        # Phone check
        if not phone.isdigit():

            messagebox.showerror(
                "Invalid Phone Number",
                "Phone number must contain only digits."
            )

            return

        if len(phone) != 10:

            messagebox.showerror(
                "Invalid Phone Number",
                "Phone number must contain exactly 10 digits."
            )

            return

        # Percentage check
        try:

            percentage_value = float(
                percentage
            )

            if (
                percentage_value < 0
                or percentage_value > 100
            ):

                raise ValueError

        except:

            messagebox.showerror(
                "Invalid Percentage",
                "Percentage must be between 0 and 100."
            )

            return

        # New student
        new_student = pd.DataFrame({

            "Student_ID": [str(student_id)],

            "Name": [str(name)],

            "Email": [str(email)],

            "Phone": [str(phone)],

            "Branch": [str(branch)],

            "Semester": [str(semester)],

            "Percentage": [str(percentage)]

        })

        file = "student_admission.csv"

        # Existing data
        if os.path.exists(file):

            old_data = pd.read_csv(
                file,
                dtype=str
            )

            # Duplicate ID
            if "Student_ID" in old_data.columns:

                if student_id in old_data[
                    "Student_ID"
                ].astype(str).values:

                    messagebox.showerror(
                        "Duplicate Student ID",
                        "This Student ID already exists."
                    )

                    return

            data = pd.concat(
                [
                    old_data,
                    new_student
                ],
                ignore_index=True
            )

        else:

            data = new_student

        # Save as text
        data = data.astype(str)

        data.to_csv(
            file,
            index=False
        )

        messagebox.showinfo(
            "Success",
            "Student admission added successfully!"
        )

        clear_form()

    # ======================================================
    # CLEAR FORM
    # ======================================================

    def clear_form():

        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        branch_entry.delete(0, tk.END)
        semester_entry.delete(0, tk.END)
        percentage_entry.delete(0, tk.END)

        id_entry.focus()

    # Buttons
    button_frame = tk.Frame(
        form_card,
        bg=WHITE
    )

    button_frame.grid(
        row=6,
        column=0,
        columnspan=2,
        pady=(20, 30)
    )

    tk.Button(
        button_frame,
        text="ADD STUDENT",
        command=add_student,
        font=("Segoe UI", 11, "bold"),
        bg=SUCCESS,
        fg=WHITE,
        activebackground=SUCCESS_DARK,
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        width=20
    ).pack(
        side="left",
        padx=10,
        ipady=10
    )

    tk.Button(
        button_frame,
        text="CLEAR FORM",
        command=clear_form,
        font=("Segoe UI", 11, "bold"),
        bg=LIGHT_BLUE,
        fg=PRIMARY_DARK,
        activebackground="#C7E1EC",
        relief="flat",
        cursor="hand2",
        width=20
    ).pack(
        side="left",
        padx=10,
        ipady=10
    )


# ==========================================================
#                    START PROGRAM
# ==========================================================

show_login()

root.mainloop()