import tkinter as tk
import re

CHARS = {
    "C": [r"/\*.*?\*/", r"//.*"],
    "Python": [r"#.*", r"'''(.*?)'''", r'"""(.*?)"""'],
    "Java": [r"/\*.*?\*/", r"//.*"],
    "HTML": [r"<!--\s*[\S\s]*?\s*-->"],
    "CSS": [r"/\*\s*[\S\s]*?\s*\*/"],
    "JavaScript": [r"/\*.*?\*/", r"//.*"],
    "C++": [r"/\*.*?\*/", r"//.*"],
    "Rust": [r"/\*.*?\*/", r"//.*"],
    "Ruby": [r"#.*", r"=begin\s*([\S\s]*?)=end"],
    "Scala": [r"/\*.*?\*/", r"//.*"],
    "PHP": [r"/\*.*?\*/", r"//.*", r"#.*"],
    "Perl": [r"#.*"],
    "Go": [r"/\*.*?\*/", r"//.*"],
    "Zig": [r"//.*", r"/\*.*?\*/"],
    "Lua": [r"--\[\[\s*([\S\s]*?)\s*\]\]", r"--.*"],
    "VBA": [r"'.*"],
    "VBS": [r"'.*"],
    "SQL": [r"--.*"],
    "Kotlin": [r"/\*.*?\*/", r"//.*"],
    "Swift": [r"/\*.*?\*/", r"//.*"],
    "C#": [r"/\*.*?\*/", r"//.*"],
}
SUFFIX = "_nocomment"


class Remover:
    def remove(self, file, chars):
        with open(file, "r") as f:
            content = f.read()
        for pattern in chars:
            content = re.sub(pattern, "", content, flags=re.DOTALL | re.MULTILINE)
        return content

    def select_file(self):
        global chosen_file
        chosen_file = tk.filedialog.askopenfilename()

    def select_chars(self):
        global chosen_chars

    def remove_and_save(self):
        if chosen_file:
            new_file_content = self.remove(chosen_file, chosen_chars)
            with open(chosen_file + SUFFIX, "w") as f:
                f.write(new_file_content)
        else:
            print("请选择一个文件")


class GUI(tk.Frame, Remover):
    def __init__(self, master=None):
        super().__init__(master)
        self.var = tk.StringVar()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button_file = tk.Button(self, text="浏览", command=self.select_file)
        self.button_file.pack()
        for key, value in CHARS.items():
            tk.Radiobutton(
                self, text=key, variable=self.var, value=value, command=self.update_lang
            ).pack(anchor="w")

    def update_lang(self):
        option_key = self.var.get()
        option_value = CHARS[option_key]


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Comment Remover")
    gui = GUI(master=root)
    gui.mainloop()