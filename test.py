import tkinter as tk
import random
import sys
import os

# ensure single instance
def check_single_instance():
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("localhost", 12345))  # 使用一个端口号
        return True
    except:
        print("程序已在运行中！")
        return False

if not check_single_instance():
    sys.exit()


class TipApp:
    def __init__(self):
        self.batch_windows = []
        self.single_window = None

    #create single initial window
    def show_single_tip(self):
        self.single_window = tk.Tk()
        self.single_window.title("专属提示")

        screen_width = self.single_window.winfo_screenwidth()
        screen_height = self.single_window.winfo_screenheight()
        window_width = 350
        window_height = 120
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.single_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tip = "我是萧逸"
        bg = "light blue"
        tk.Label(
            self.single_window,
            text=tip,
            bg=bg,
            font=("宋体", 14),
            width=350,
            height=120,
            wraplength=320,
            justify="center"
        ).pack()

        self.single_window.bind('<space>', self.on_space_global)
        self.single_window.attributes('-topmost', True)

        self.single_window.protocol("WM_DELETE_WINDOW", self.start_batch_tips)
        self.single_window.mainloop()

    #create batch of windows
    def create_batch_window(self, count):
        if count <= 0:
            return
        window = tk.Toplevel()
        self.batch_windows.append(window)

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = 350
        window_height = 120
        x = random.randint(0, screen_width - window_width)
        y = random.randint(0, screen_height - window_height)
        window.title("提示")
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tips = [
            "记得多喝水。",
            "工作时要注意休息，保护眼睛。",
            "我们不能就这样算了。",
            "揉揉耳朵，不怕不怕。",
            "那天晚上风有点凉，我其实应该把外套给你的。",
            "无论山多高，海多宽，只要抬头就能看见，我的月亮。",
            "萧小五 记得开门。",
            "坏运气已经被我赶走了。",
            "和你在一起的日子在我这永久储存，在永久面前，所有事都像昨天一样新鲜。",
            "我想你了",
            "我爱你",
            "傻瓜，干嘛这么没自信。",
            "你就是你，干嘛要去和别人比。",
            "不管梦里还是现实，我都会一直陪在你身边。",
            "放我出去。",
            "我想见你。",
            "不论你在哪里，我都能找到你。"
        ]
        tip = random.choice(tips)
        
        # define colours
        colors = [
            "light blue",       
            "lavender",        
            "light pink",      
            "light yellow",   
            "honeydew",        
            "peach puff",       
            "pale green",      
            "light cyan",      
            "misty rose",      
            "thistle",         
            "light steel blue", 
            "khaki",         
            "pale green",       
            "sky blue",         
            "sandy brown",     
            "light green",      
            "powder blue",     
            "azure",            
            "mint cream",       
            "alice blue",      
        ]
        bg = random.choice(colors)

        tk.Label(
            window,
            text=tip,
            bg=bg,
            font=("宋体", 14),
            width=350,
            height=120,
            wraplength=320,
            justify="center"
        ).pack()

    
        window.protocol("WM_DELETE_WINDOW", self.close_all_windows)
        window.bind('<space>', self.on_space_global)
        window.attributes('-topmost', True)

        window.after(50, self.create_batch_window, count - 1)

    # close all windows
    def close_all_windows(self):
        
        for window in self.batch_windows:
            try:
                window.destroy()
            except:
                pass
        self.batch_windows.clear()

    # close the single window and start batch tips
    def start_batch_tips(self):
        if self.single_window:
            self.single_window.destroy()
            self.single_window = None
        self.create_batch_window(130)

    # press space to close all windows and exit
    def on_space_global(self, event):
        if self.single_window:
            self.single_window.destroy()
        self.close_all_windows()
        sys.exit()

if __name__ == "__main__":
    app = TipApp()
    app.show_single_tip()
        