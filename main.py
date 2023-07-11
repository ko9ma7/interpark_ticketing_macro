from tkinter import *
from tkinter import messagebox
import pyautogui

class App:
    def __init__(self, root):
        bgcolor = "#F0FFFF"
        self.root = root
        self.root.title("인터파크 티켓팅 매크로")
        self.root.iconbitmap('macro.ico')
        self.root.geometry("850x600")
        self.root.configure(bg=bgcolor)  # 배경색 설정

        self.label_font = ("KIMM_bold", 12)  # 폰트 설정

        self.username_label = Label(self.root, text="아이디", font=self.label_font, bg=bgcolor)
        self.username_label.grid(row=0, column=0, sticky=E)

        self.username_entry = Entry(self.root, font=self.label_font)
        self.username_entry.grid(row=0, column=1, pady=5, padx=10, sticky=W)

        self.password_label = Label(self.root, text="비밀번호", font=self.label_font, bg=bgcolor)
        self.password_label.grid(row=1, column=0, sticky=E)

        self.password_entry = Entry(self.root, font=self.label_font)
        self.password_entry.grid(row=1, column=1, pady=(5, 20), padx=10, sticky=W)

        self.performance_code_label = Label(self.root, text="공연코드", font=self.label_font, bg=bgcolor)
        self.performance_code_label.grid(row=3, column=0, sticky=E)

        self.performance_code_entry = Entry(self.root, font=self.label_font)
        self.performance_code_entry.grid(row=3, column=1, pady=5, padx=10, sticky=W)

        self.performance_date_label = Label(self.root, text="공연날짜", font=self.label_font, bg=bgcolor)
        self.performance_date_label.grid(row=4, column=0, sticky=E)

        self.performance_date_entry = Entry(self.root, font=self.label_font)
        self.performance_date_entry.grid(row=4, column=1, pady=5, padx=10, sticky=W)

        self.code_number_label = Label(self.root, text="코드번호", font=self.label_font, bg=bgcolor)
        self.code_number_label.grid(row=5, column=0, sticky=E)

        self.code_number_entry = Entry(self.root, font=self.label_font)
        self.code_number_entry.grid(row=5, column=1, pady=5, padx=10, sticky=W)

        self.gate_address_label = Label(self.root, text="게이트 주소", font=self.label_font, bg=bgcolor)
        self.gate_address_label.grid(row=6, column=0, sticky=E)

        self.gate_address_entry = Entry(self.root, font=self.label_font)
        self.gate_address_entry.grid(row=6, column=1, pady=5, padx=10, sticky=W)

        self.seat_label = Label(self.root, text="좌석수", font=self.label_font, bg=bgcolor)
        self.seat_label.grid(row=0, column=2, padx=150, sticky=W)

        self.seat_value = StringVar()
        self.seat_value.set("1")  # 기본 선택값
        self.seat_radios = [("1석", "1"), ("2석", "2"), ("3석", "3"), ("4석", "4")]

        for i, (text, value) in enumerate(self.seat_radios):
            self.seat_radio = Radiobutton(
                self.root,
                text=text,
                variable=self.seat_value,
                value=value,
                font=self.label_font,
                bg=bgcolor
            )
            self.seat_radio.grid(row=i + 1, column=2, padx=100, sticky=W)

        self.check_value1 = BooleanVar()

        self.checkbutton1 = Checkbutton(self.root, text="안심예매문자 자동입력", variable=self.check_value1, font=self.label_font, bg=bgcolor)
        self.checkbutton1.grid(row=len(self.seat_radios) + 2, column=2, padx=100, pady=5, sticky=W)

        self.display_frame = Frame(self.root, bg="white", padx=10, pady=10)
        self.display_frame.grid(row=7, columnspan=2, sticky=W+E)

        self.save_button = Button(self.root, text="저장", command=self.save, font=self.label_font, bg="#87CEFA")
        self.save_button.grid(row=8, column=0, pady=10, padx=10, sticky=E)

        self.run_button = Button(self.root, text="실행", command=self.run_macro, font=self.label_font, bg="#87CEFA")
        self.run_button.grid(row=8, column=1, pady=10, padx=10, sticky=E)

        self.display_text = Text(self.display_frame, height=10, width=50)
        self.display_text.pack()
        self.display_text.config(state=DISABLED)

    def save(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.performance_code = self.performance_code_entry.get()
        self.performance_date = self.performance_date_entry.get()
        self.code_number = self.code_number_entry.get()
        self.gate_address = self.gate_address_entry.get()
        self.seat = self.seat_value.get()

        self.check1 = self.check_value1.get()

        self.display_text.config(state=NORMAL)
        self.display_text.delete("1.0", END)  # 기존 내용 삭제
        self.display_text.insert(END, f"아이디: {self.username}\n")
        self.display_text.insert(END, f"비밀번호: {self.password}\n")
        self.display_text.insert(END, f"공연코드: {self.performance_code}\n")
        self.display_text.insert(END, f"공연날짜: {self.performance_date}\n")
        self.display_text.insert(END, f"코드번호: {self.code_number}\n")
        self.display_text.insert(END, f"게이트 주소: {self.gate_address}\n")
        self.display_text.insert(END, f"좌석수: {self.seat}\n")
        self.display_text.insert(END, f"안심예매문자: {self.check1}\n")
        self.display_text.config(state=DISABLED)
        messagebox.showinfo("알림", "저장이 완료되었습니다.")

    def run_macro(self):
        # 실행 버튼이 눌렸을 때 수행할 동작
        pyautogui.alert('매크로 실행됨')

root = Tk()
app = App(root)
root.mainloop()
