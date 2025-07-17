import tkinter as tk
from tkinter import ttk, messagebox
import json
import random
import time

class TravelSpinnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("暑假去哪玩 - 旅游目的地随机选择器")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f8ff")

        # 加载旅游目的地数据
        self.destinations = self.load_destinations()
        if not self.destinations:
            messagebox.showerror("错误", "无法加载旅游目的地数据")
            self.root.quit()

        # 创建UI组件
        self.create_widgets()

    def load_destinations(self):
        try:
            with open("travel_destinations.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"加载数据失败: {e}")
            return []

    def create_widgets(self):
        # 标题标签
        title_label = tk.Label(
            self.root,
            text="暑假去哪玩？",
            font=("SimHei", 24, "bold"),
            bg="#f0f8ff",
            fg="#2c3e50"
        )
        title_label.pack(pady=20)

        # 结果显示框
        self.result_frame = tk.Frame(self.root, width=500, height=200, bg="white", relief="ridge", bd=2)
        self.result_frame.pack(pady=10)
        self.result_frame.pack_propagate(False)

        self.name_label = tk.Label(
            self.result_frame,
            text="点击下方按钮开始选择",
            font=("SimHei", 18),
            bg="white",
            fg="#34495e"
        )
        self.name_label.pack(pady=10)

        self.scenery_label = tk.Label(
            self.result_frame,
            text="",
            font=("SimHei", 12),
            bg="white",
            fg="#7f8c8d",
            wraplength=450,
            justify="left"
        )
        self.scenery_label.pack(anchor="w", padx=20)

        self.food_label = tk.Label(
            self.result_frame,
            text="",
            font=("SimHei", 12),
            bg="white",
            fg="#e74c3c",
            wraplength=450,
            justify="left"
        )
        self.food_label.pack(anchor="w", padx=20, pady=5)

        # 按钮
        self.spin_button = ttk.Button(
            self.root,
            text="开始选择",
            command=self.spin,
            width=15
        )
        self.spin_button.pack(pady=20)

    def spin(self):
        # 禁用按钮防止重复点击
        self.spin_button.config(state="disabled")

        # 随机选择动画
        for _ in range(20):  # 动画帧数
            destination = random.choice(self.destinations)
            self.name_label.config(text=destination["name"])
            self.scenery_label.config(text=f"风景: {destination['scenery']}")
            self.food_label.config(text=f"美食: {destination['food']}")
            self.root.update()
            time.sleep(0.05)

        # 最终选择
        final_destination = random.choice(self.destinations)
        self.name_label.config(text=final_destination["name"])
        self.scenery_label.config(text=f"风景: {final_destination['scenery']}")
        self.food_label.config(text=f"美食: {final_destination['food']}")

        # 启用按钮
        self.spin_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelSpinnerApp(root)
    root.mainloop()