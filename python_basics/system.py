import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SchoolManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("750x500")
        self.root.configure(bg="lightblue")

        # ===== Title =====
        title = tk.Label(root, text="School Management System", 
                         font=("Arial", 18, "bold"), bg="lightblue")
        title.pack(pady=10)

        # ===== Frame for Form =====
        form_frame = tk.Frame(root, bg="lightblue")
        form_frame.pack(pady=10)

        # Student ID
        tk.Label(form_frame, text="Student ID:", bg="lightblue", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.student_id = tk.Entry(form_frame, font=("Arial", 12))
        self.student_id.grid(row=0, column=1, padx=10, pady=5)

        # Student Name
        tk.Label(form_frame, text="Student Name:", bg="lightblue", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.student_name = tk.Entry(form_frame, font=("Arial", 12))
        self.student_name.grid(row=1, column=1, padx=10, pady=5)

        # Student Course
        tk.Label(form_frame, text="Student Course:", bg="lightblue", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.student_course = tk.Entry(form_frame, font=("Arial", 12))
        self.student_course.grid(row=2, column=1, padx=10, pady=5)

        # Student Phone
        tk.Label(form_frame, text="Student Phone:", bg="lightblue", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.student_phone = tk.Entry(form_frame, font=("Arial", 12))
        self.student_phone.grid(row=3, column=1, padx=10, pady=5)

        # ===== Buttons =====
        button_frame = tk.Frame(root, bg="lightblue")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Student", font=("Arial", 12), 
                  command=self.add_student, bg="green", fg="white").grid(row=0, column=0, padx=10)

        tk.Button(button_frame, text="Delete Selected", font=("Arial", 12), 
                  command=self.delete_student, bg="red", fg="white").grid(row=0, column=1, padx=10)

        tk.Button(button_frame, text="Clear Fields", font=("Arial", 12), 
                  command=self.clear_fields, bg="orange", fg="white").grid(row=0, column=2, padx=10)

        # ===== Table =====
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Course", "Phone"), show="headings")
        self.tree.pack(pady=20, fill="both", expand=True)

        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Student Name")
        self.tree.heading("Course", text="Student Course")
        self.tree.heading("Phone", text="Student Phone")

        self.tree.column("ID", width=100)
        self.tree.column("Name", width=150)
        self.tree.column("Course", width=150)
        self.tree.column("Phone", width=120)

    # ===== Functions =====
    def add_student(self):
        if (self.student_id.get() == "" or 
            self.student_name.get() == "" or 
            self.student_course.get() == "" or 
            self.student_phone.get() == ""):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        self.tree.insert("", "end", values=(
            self.student_id.get(),
            self.student_name.get(),
            self.student_course.get(),
            self.student_phone.get()
        ))

        messagebox.showinfo("Success", "Student added successfully!")
        self.clear_fields()

    def delete_student(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a student to delete.")
            return

        for item in selected_item:
            self.tree.delete(item)

        messagebox.showinfo("Deleted", "Student record deleted.")

    def clear_fields(self):
        self.student_id.delete(0, tk.END)
        self.student_name.delete(0, tk.END)
        self.student_course.delete(0, tk.END)
        self.student_phone.delete(0, tk.END)


# ===== Run Application =====
if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()