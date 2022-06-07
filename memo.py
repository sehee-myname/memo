from tkinter import *
import os

root =Tk()
root.title("MEMO")
root.geometry("640x480")
#열기 저장 파일 이름
filename = "mynote.txt"

def open_file() :
    if os.path.isfile(filename): #파일이 있으면 T
        with open(filename, "r", encoding="utf-8") as file:
            txt.delete("1.0", END) #텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) #파일 본문에 입력

def save_file() :
    with open(filename, "w", encoding="utf-8") as file:
        file.write(txt.get("1.0", END))

menu= Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

#스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

#본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()