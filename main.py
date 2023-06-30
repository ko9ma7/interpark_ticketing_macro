from tkinter import *


class App:
    def __init__(self, root):
        bgcolor = "#F0FFFF"
        self.root = root
        self.root.title("인터파크 티켓팅 매크로")
        self.root.iconbitmap('macro.ico')
        self.root.geometry("800x600")
        self.root.configure(bg=bgcolor)  # 배경색 설정

        self.label_font = ("KIMM_bold", 12)  # 폰트 설정

        self.username_label = Label(self.root, text="아이디", font=self.label_font, bg=bgcolor)  # 폰트와 배경색 설정
        self.username_label.grid(row=0, column=0, sticky=E)

        self.username_entry = Entry(self.root, font=self.label_font)
        self.username_entry.grid(row=0, column=1, pady=5, padx=10, sticky=W)

        self.password_label = Label(self.root, text="비밀번호", font=self.label_font, bg=bgcolor)  # 폰트와 배경색 설정
        self.password_label.grid(row=1, column=0, sticky=E)

        self.password_entry = Entry(self.root, show="*", font=self.label_font)
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

        self.seat_label = Label(self.root, text="좌석수", font=self.label_font, bg=bgcolor)  # 폰트와 배경색 설정
        self.seat_label.grid(row=0, column=2, padx=150, sticky=W)

        self.seat_value = StringVar()
        self.seat_value.set("1석")  # 기본 선택값
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
            self.seat_radio.grid(row=i + 1, column=2, padx=150, sticky=W)

        self.seat_label = Label(self.root, text="안심예매문자 자동입력", font=self.label_font, bg=bgcolor)  # 폰트와 배경색 설정
        self.seat_label.grid(row=len(self.seat_radios) + 3, column=2, padx=150, sticky=W)

        self.check_value1 = BooleanVar()
        self.check_value2 = BooleanVar()

        self.checkbutton1 = Checkbutton(self.root, text="켜기", variable=self.check_value1, font=self.label_font, bg=bgcolor)
        self.checkbutton1.grid(row=len(self.seat_radios) + 4, column=2, padx=150, pady=5, sticky=W)

        self.checkbutton2 = Checkbutton(self.root, text="끄기", variable=self.check_value2, font=self.label_font, bg=bgcolor)
        self.checkbutton2.grid(row=len(self.seat_radios) + 5, column=2, padx=150, pady=5, sticky=W)

        self.save_button = Button(self.root, text="저장", command=self.save, font=self.label_font, bg="#87CEFA")
        self.save_button.grid(row=8, column=0, pady=10, padx=10, sticky=E)

        self.run_button = Button(self.root, text="실행", command=self.run_macro, font=self.label_font, bg="#87CEFA")
        self.run_button.grid(row=8, column=1, pady=10, padx=10, sticky=E)

    def save(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        performance_code = self.performance_code_entry.get()
        performance_date = self.performance_date_entry.get()
        code_number = self.code_number_entry.get()
        gate_address = self.gate_address_entry.get()
        seat = self.seat_value.get()

        check1 = self.check_value1.get()
        check2 = self.check_value2.get()

        print("아이디:", username)
        print("비밀번호:", password)
        print("공연코드:", performance_code)
        print("공연날짜:", performance_date)
        print("코드번호:", code_number)
        print("게이트 주소:", gate_address)
        print("좌석수:", seat)
        print("체크1:", check1)
        print("체크2:", check2)

    def run_macro(self):
        # 실행 버튼이 눌렸을 때 수행할 동작
        print("매크로 실행")


root = Tk()
app = App(root)
root.mainloop()
