# =========================================================
# CAREERVERSE : STUDENT MISSION
# FULL FINAL PROFESSIONAL VERSION
# =========================================================

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
from datetime import datetime

# SOUND (WINDOWS ONLY)
try:
    import winsound
    SOUND_AVAILABLE = True
except:
    SOUND_AVAILABLE = False


# =========================================================
# MAIN CLASS
# =========================================================
class CareerAdventureGame:

    def __init__(self, root):

        self.root = root

        # FULL SCREEN
        self.root.title("CareerVerse: Student Mission")
        self.root.state("zoomed")
        self.root.minsize(1200, 700)
        self.root.configure(bg="#0b1020")
        self.root.resizable(True, True)

        # PLAYER STATS
        self.tech_score = 20
        self.biz_score = 20
        self.creative_score = 20

        self.xp_points = 0
        self.player_rank = "Novice Explorer"

        self.current_step = "START"

        self.story_animating = False
        self.story_index = 0

        self.create_styles()
        self.create_widgets()

        self.spawn_particles()
        self.animate_background()

        self.animate_title()
        self.glowing_buttons()
        self.update_clock()
        self.update_tips()

        self.load_scene()

        self.root.after(1000, self.show_welcome)

    # =====================================================
    # STYLE
    # =====================================================
    def create_styles(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Career.Horizontal.TProgressbar",
            troughcolor="#1f2740",
            background="#7c3aed",
            thickness=18
        )

    # =====================================================
    # CREATE WIDGETS
    # =====================================================
    def create_widgets(self):

        # BACKGROUND CANVAS
        self.bg_canvas = tk.Canvas(
            self.root,
            bg="#0b1020",
            highlightthickness=0
        )
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # =================================================
        # HEADER
        # =================================================
        self.header_frame = tk.Frame(
            self.root,
            bg="#111827",
            height=80
        )
        self.header_frame.place(x=0, y=0, relwidth=1)

        self.title_label = tk.Label(
            self.header_frame,
            text="🚀 CAREERVERSE : STUDENT MISSION",
            font=("Helvetica", 22, "bold"),
            fg="white",
            bg="#111827"
        )
        self.title_label.pack(pady=10)

        self.sub_label = tk.Label(
            self.header_frame,
            text="Interactive Career Guidance System",
            font=("Helvetica", 11),
            fg="#cbd5e1",
            bg="#111827"
        )
        self.sub_label.pack()

        # DIGITAL CLOCK
        self.clock_label = tk.Label(
            self.header_frame,
            text="",
            font=("Helvetica", 12, "bold"),
            fg="#86efac",
            bg="#111827"
        )
        self.clock_label.place(x=1200, y=20)

        # =================================================
        # MAIN FRAME
        # =================================================
        self.main_frame = tk.Frame(
            self.root,
            bg="#0b1020"
        )
        self.main_frame.place(x=20, y=100, width=1450, height=800)

        # LEFT PANEL
        self.left_panel = tk.Frame(
            self.main_frame,
            bg="#111827",
            bd=3,
            relief="ridge"
        )
        self.left_panel.place(x=0, y=0, width=850, height=720)

        # RIGHT PANEL
        self.right_panel = tk.Frame(
            self.main_frame,
            bg="#0f172a",
            bd=3,
            relief="ridge"
        )
        self.right_panel.place(x=880, y=0, width=500, height=720)

        # =================================================
        # HERO SECTION
        # =================================================
        self.hero_frame = tk.Frame(
            self.left_panel,
            bg="#1e293b"
        )
        self.hero_frame.place(x=25, y=20, width=790, height=130)

        self.hero_title = tk.Label(
            self.hero_frame,
            text="MISSION CONTROL",
            font=("Helvetica", 18, "bold"),
            fg="#93c5fd",
            bg="#1e293b"
        )
        self.hero_title.pack(pady=10)

        self.score_label = tk.Label(
            self.hero_frame,
            text=f"✨ XP: {self.xp_points} | RANK: {self.player_rank}",
            font=("Helvetica", 13, "bold"),
            fg="#fbbf24",
            bg="#1e293b"
        )
        self.score_label.pack()

        self.xp_bar = ttk.Progressbar(
            self.hero_frame,
            style="Career.Horizontal.TProgressbar",
            orient="horizontal",
            length=650,
            mode="determinate",
            maximum=1000
        )
        self.xp_bar.pack(pady=15)

        # =================================================
        # STORY CARD
        # =================================================
        self.story_card = tk.Frame(
            self.left_panel,
            bg="#0f172a",
            bd=2,
            relief="solid"
        )
        self.story_card.place(x=25, y=170, width=790, height=380)

        self.story_icon = tk.Label(
            self.story_card,
            text="🌟",
            font=("Helvetica", 35),
            fg="#facc15",
            bg="#0f172a"
        )
        self.story_icon.pack(pady=10)

        self.story_text = tk.Label(
            self.story_card,
            text="",
            font=("Helvetica", 13),
            fg="#e2e8f0",
            bg="#0f172a",
            wraplength=720,
            justify="left"
        )
        self.story_text.pack(pady=10)

        # =================================================
        # REWARD LABEL
        # =================================================
        self.reward_label = tk.Label(
            self.left_panel,
            text="",
            font=("Courier New", 13, "bold"),
            fg="#34d399",
            bg="#111827"
        )
        self.reward_label.place(x=25, y=570, width=790, height=40)

        # =================================================
        # BUTTON FRAME
        # =================================================
        self.btn_frame = tk.Frame(
            self.left_panel,
            bg="#111827"
        )
        self.btn_frame.place(x=25, y=620, width=790, height=80)

        # BUTTONS
        self.btnA = tk.Button(
            self.btn_frame,
            text="",
            width=55,
            font=("Helvetica", 11, "bold"),
            bg="#22c55e",
            fg="#111827",
            command=lambda: self.handle_choice("A")
        )

        self.btnB = tk.Button(
            self.btn_frame,
            text="",
            width=55,
            font=("Helvetica", 11, "bold"),
            bg="#3b82f6",
            fg="#111827",
            command=lambda: self.handle_choice("B")
        )

        self.btnC = tk.Button(
            self.btn_frame,
            text="",
            width=55,
            font=("Helvetica", 11, "bold"),
            bg="#f59e0b",
            fg="#111827",
            command=lambda: self.handle_choice("C")
        )

        self.btn_reset = tk.Button(
            self.btn_frame,
            text="🔄 Restart Mission",
            width=25,
            font=("Helvetica", 11, "bold"),
            bg="#ef4444",
            fg="white",
            command=self.reset_game
        )

        # =================================================
        # RIGHT PANEL
        # =================================================
        self.right_title = tk.Label(
            self.right_panel,
            text="📊 LIVE PROFILE ANALYTICS",
            font=("Helvetica", 15, "bold"),
            fg="#e2e8f0",
            bg="#0f172a"
        )
        self.right_title.pack(pady=15)

        self.canvas = tk.Canvas(
            self.right_panel,
            width=420,
            height=280,
            bg="#0f172a",
            highlightthickness=0
        )
        self.canvas.pack(pady=10)

        # CAREER TIPS
        self.tip_box = tk.Label(
            self.right_panel,
            text="",
            font=("Helvetica", 12),
            fg="#e2e8f0",
            bg="#111827",
            wraplength=380,
            justify="left",
            padx=15,
            pady=15
        )
        self.tip_box.pack(pady=20)

    # =====================================================
    # WELCOME POPUP
    # =====================================================
    def show_welcome(self):

        popup = tk.Toplevel(self.root)

        popup.title("Welcome")

        popup.geometry("500x250")

        popup.configure(bg="#111827")

        popup.grab_set()

        label = tk.Label(
            popup,
            text=
            "🚀 Welcome to CareerVerse!\n\n"
            "An Interactive Career Guidance System\n"
            "for students after 10th and 2nd PU.",
            font=("Helvetica", 15, "bold"),
            fg="white",
            bg="#111827",
            justify="center"
        )

        label.pack(expand=True)

        btn = tk.Button(
            popup,
            text="Start Mission",
            font=("Helvetica", 12, "bold"),
            bg="#22c55e",
            command=popup.destroy
        )

        btn.pack(pady=20)

    # =====================================================
    # PARTICLES
    # =====================================================
    def spawn_particles(self):

        self.particles = []

        for _ in range(120):

            x = random.randint(0, 1600)
            y = random.randint(0, 900)

            r = random.randint(1, 3)

            speed = random.uniform(0.5, 2)

            color = random.choice([
                "#93c5fd",
                "#f9a8d4",
                "#86efac",
                "#fcd34d",
                "#c4b5fd"
            ])

            particle = self.bg_canvas.create_oval(
                x, y, x + r, y + r,
                fill=color,
                outline=""
            )

            self.particles.append([particle, speed])

    def animate_background(self):

        for item, speed in self.particles:

            self.bg_canvas.move(item, 0, speed)

            coords = self.bg_canvas.coords(item)

            if coords[1] > 900:

                x = random.randint(0, 1600)

                self.bg_canvas.coords(item, x, 0, x + 2, 2)

        self.root.after(30, self.animate_background)

    # =====================================================
    # TITLE ANIMATION
    # =====================================================
    def animate_title(self):

        colors = [
            "#ffffff",
            "#93c5fd",
            "#fbbf24",
            "#86efac"
        ]

        self.title_label.config(
            fg=random.choice(colors)
        )

        self.root.after(700, self.animate_title)

    # =====================================================
    # GLOW BUTTONS
    # =====================================================
    def glowing_buttons(self):

        current = self.btnA.cget("bg")

        if current == "#22c55e":
            self.btnA.config(bg="#4ade80")
        else:
            self.btnA.config(bg="#22c55e")

        self.root.after(600, self.glowing_buttons)

    # =====================================================
    # CLOCK
    # =====================================================
    def update_clock(self):

        current = datetime.now().strftime("%I:%M:%S %p")

        self.clock_label.config(text=current)

        self.root.after(1000, self.update_clock)

    # =====================================================
    # TIPS
    # =====================================================
    def update_tips(self):

        tips = [

            "💡 Engineering needs logical thinking skills.",

            "💡 AI & Cybersecurity are future careers.",

            "💡 Commerce students can become entrepreneurs.",

            "💡 Communication skills help in every career.",

            "💡 Creative careers are highly demanded today.",

            "💡 Data Science is one of the highest paying fields.",

            "💡 Students should choose based on interest + skills."
        ]

        self.tip_box.config(
            text=random.choice(tips)
        )

        self.root.after(4000, self.update_tips)

    # =====================================================
    # TYPEWRITER EFFECT
    # =====================================================
    def type_story(self, text):

        self.story_animating = True

        self.story_text.config(text="")

        self.story_chars = list(text)

        self.story_index = 0

        self.type_next()

    def type_next(self):

        if self.story_index < len(self.story_chars):

            current = self.story_text.cget("text")

            self.story_text.config(
                text=current + self.story_chars[self.story_index]
            )

            self.story_index += 1

            self.root.after(10, self.type_next)

        else:

            self.story_animating = False

    # =====================================================
    # GRAPH
    # =====================================================
    def draw_live_graph(self):

        self.canvas.delete("all")

        self.canvas.create_text(
            210,
            20,
            text="SKILL MATRIX",
            fill="white",
            font=("Helvetica", 15, "bold")
        )

        base_y = 240

        def draw_bar(x, value, color, label):

            height = min(value * 1.5, 200)

            self.canvas.create_rectangle(
                x,
                base_y - height,
                x + 70,
                base_y,
                fill=color,
                outline=""
            )

            self.canvas.create_text(
                x + 35,
                base_y + 20,
                text=label,
                fill="white",
                font=("Helvetica", 11, "bold")
            )

        draw_bar(60, self.tech_score, "#fca5a5", "TECH")
        draw_bar(170, self.biz_score, "#93c5fd", "BUSINESS")
        draw_bar(280, self.creative_score, "#86efac", "CREATIVE")

        self.xp_bar["value"] = self.xp_points

    # =====================================================
    # UPDATE GAME
    # =====================================================
    def update_game(self, xp, rank, t_add, b_add, c_add):

        self.xp_points += xp

        self.player_rank = rank

        self.tech_score += t_add
        self.biz_score += b_add
        self.creative_score += c_add

        self.score_label.config(
            text=f"✨ XP: {self.xp_points} | RANK: {self.player_rank}"
        )

        self.draw_live_graph()

    # =====================================================
    # BUTTON CLEAR
    # =====================================================
    def clear_buttons(self):

        self.btnA.pack_forget()
        self.btnB.pack_forget()
        self.btnC.pack_forget()
        self.btn_reset.pack_forget()

    # =====================================================
    # LOAD SCENE
    # =====================================================
    def load_scene(self):

        self.clear_buttons()

        self.reward_label.config(text="")

        self.draw_live_graph()

        scenes = {

            "START": {
                "text":
                "🚀 Welcome to CareerVerse!\n\n"
                "This system helps students choose the right career path "
                "after 10th and 2nd PU.\n\n"
                "Select your education level.",

                "icon": "🌌",

                "buttons": [
                    ("🎓 After 10th Standard", "A"),
                    ("🏆 After 2nd PU", "B")
                ]
            },

            "10TH_MAIN": {
                "text":
                "🧭 AFTER 10TH OPTIONS\n\n"

                "💻 SCIENCE STREAM\n"
                "Subjects:\n"
                "Physics, Chemistry, Maths, Biology, Computer Science\n\n"

                "📊 COMMERCE STREAM\n"
                "Subjects:\n"
                "Accountancy, Economics, Business Studies\n\n"

                "🎨 TECHNICAL / CREATIVE\n"
                "Courses:\n"
                "ITI, Diploma, Animation, Designing\n\n"

                "Choose your area of interest.",

                "icon": "🧭",

                "buttons": [
                    ("💻 Science & Technology", "A"),
                    ("📊 Commerce & Business", "B"),
                    ("🎨 Technical / Creative", "C")
                ]
            },

            "10TH_SCIENCE": {
                "text":
                "🔬 SCIENCE STREAM DETAILS\n\n"

                "Career Options:\n"
                "• Engineering\n"
                "• Artificial Intelligence\n"
                "• Medical\n"
                "• Robotics\n"
                "• Software Development\n"
                "• Biotechnology\n\n"

                "Choose your specialization.",

                "icon": "⚙️",

                "buttons": [
                    ("⚡ Engineering & Computer Science", "A"),
                    ("🩺 Medical & Biology", "B")
                ]
            },

            "10TH_COMMERCE": {
                "text":
                "💼 COMMERCE STREAM DETAILS\n\n"

                "Career Options:\n"
                "• Chartered Accountant\n"
                "• Banking\n"
                "• Financial Analyst\n"
                "• Business Management\n"
                "• Entrepreneurship\n\n"

                "Choose your commerce goal.",

                "icon": "💎",

                "buttons": [
                    ("💎 Chartered Accountant / CS", "A"),
                    ("💡 Business Leadership / Startup", "B")
                ]
            },

            "PU_MAIN": {
                "text":
                "🎓 AFTER 2ND PU OPTIONS\n\n"

                "🔬 Science → Engineering / Medical / AI\n\n"

                "💸 Commerce → B.Com / BBA / CA\n\n"

                "🎨 Arts → Law / Journalism / Design\n\n"

                "Choose your stream.",

                "icon": "🎓",

                "buttons": [
                    ("🔬 Science Stream", "A"),
                    ("💸 Commerce Stream", "B"),
                    ("🎨 Arts / Design", "C")
                ]
            }
        }

        endings = {

            "END_VOCA":
            "🏅 Recommended Careers:\n\n"
            "• Polytechnic\n"
            "• ITI\n"
            "• Designing\n"
            "• Hardware Networking",

            "END_ENGG":
            "⚡ Recommended Careers:\n\n"
            "• Software Engineering\n"
            "• Artificial Intelligence\n"
            "• Robotics\n"
            "• Cybersecurity",

            "END_MED":
            "🩺 Recommended Careers:\n\n"
            "• MBBS\n"
            "• Pharmacy\n"
            "• Nursing\n"
            "• Biotechnology",

            "END_CA":
            "💎 Recommended Careers:\n\n"
            "• Chartered Accountant\n"
            "• Banking\n"
            "• Finance\n"
            "• Investment Banking",

            "END_CORP":
            "💼 Recommended Careers:\n\n"
            "• Entrepreneurship\n"
            "• Startup Founder\n"
            "• Marketing\n"
            "• Business Administration",

            "END_ARTS":
            "🎨 Recommended Careers:\n\n"
            "• Journalism\n"
            "• Fashion Designing\n"
            "• Animation\n"
            "• UI/UX Designing"
        }

        if self.current_step in scenes:

            scene = scenes[self.current_step]

            self.story_icon.config(text=scene["icon"])

            self.type_story(scene["text"])

            buttons = scene["buttons"]

            if len(buttons) >= 1:
                self.btnA.config(text=buttons[0][0])
                self.btnA.pack(pady=5)

            if len(buttons) >= 2:
                self.btnB.config(text=buttons[1][0])
                self.btnB.pack(pady=5)

            if len(buttons) >= 3:
                self.btnC.config(text=buttons[2][0])
                self.btnC.pack(pady=5)

        elif self.current_step in endings:

            self.story_icon.config(text="🏁")

            self.reward_label.config(
                text="🎉 CAREER ANALYSIS COMPLETED 🎉"
            )

            self.type_story(endings[self.current_step])

            self.btn_reset.pack(pady=15)

    # =====================================================
    # HANDLE CHOICE
    # =====================================================
    def handle_choice(self, choice):

        if SOUND_AVAILABLE:
            winsound.Beep(700, 100)

        if self.story_animating:
            return

        if self.current_step == "START":

            if choice == "A":
                self.current_step = "10TH_MAIN"
                self.update_game(100, "Initiate Voyager", 10, 10, 10)

            elif choice == "B":
                self.current_step = "PU_MAIN"
                self.update_game(150, "Advanced Navigator", 20, 20, 20)

        elif self.current_step == "10TH_MAIN":

            if choice == "A":
                self.current_step = "10TH_SCIENCE"
                self.update_game(100, "Logic Builder", 40, 0, 10)

            elif choice == "B":
                self.current_step = "10TH_COMMERCE"
                self.update_game(100, "Market Apprentice", 0, 40, 10)

            elif choice == "C":
                self.current_step = "END_VOCA"
                self.update_game(200, "Master Technician", 50, 20, 50)

        elif self.current_step == "10TH_SCIENCE":

            if choice == "A":
                self.current_step = "END_ENGG"
                self.update_game(250, "Cyber Architect", 80, 10, 20)

            else:
                self.current_step = "END_MED"
                self.update_game(250, "Elite Scientist", 70, 0, 40)

        elif self.current_step == "10TH_COMMERCE":

            if choice == "A":
                self.current_step = "END_CA"
                self.update_game(250, "Financial Mastermind", 10, 90, 0)

            else:
                self.current_step = "END_CORP"
                self.update_game(250, "Venture Captain", 30, 70, 40)

        elif self.current_step == "PU_MAIN":

            if choice == "A":
                self.current_step = "10TH_SCIENCE"
                self.update_game(100, "Logic Seeker", 30, 0, 10)

            elif choice == "B":
                self.current_step = "10TH_COMMERCE"
                self.update_game(100, "Asset Planner", 0, 30, 10)

            elif choice == "C":
                self.current_step = "END_ARTS"
                self.update_game(250, "Creative Mastermind", 10, 20, 90)

        self.load_scene()

    # =====================================================
    # RESET
    # =====================================================
    def reset_game(self):

        self.tech_score = 20
        self.biz_score = 20
        self.creative_score = 20

        self.xp_points = 0

        self.player_rank = "Novice Explorer"

        self.current_step = "START"

        self.load_scene()


# =========================================================
# RUN GAME
# =========================================================
if __name__ == "__main__":

    root = tk.Tk()

    app = CareerAdventureGame(root)

    root.mainloop()