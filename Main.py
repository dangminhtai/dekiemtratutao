import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import PhotoImage
import os
import webbrowser
# Hàm để thay đổi kích thước ảnh
def resize_image(image, scale_factor):
    width, height = image.size
    new_size = (int(width * scale_factor), int(height * scale_factor))
    return image.resize(new_size, Image.Resampling.LANCZOS)  # Sử dụng LANCZOS thay vì ANTIALIAS

# Hàm tạo button với hình ảnh và văn bản
def create_button_with_text(text_input, command):
    def create_image_with_text(image_path, text, font_path, font_size=30):
        try:
            img = Image.open(image_path)
            draw = ImageDraw.Draw(img)
            # Chọn font chữ
            if not os.path.exists(font_path):
                font = ImageFont.load_default()
                print(f"Không tìm thấy font tại {font_path}. Dùng font mặc định.")
            else:
                font = ImageFont.truetype(font_path, size=font_size)

            # Tính toán kích thước chữ
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            # Vị trí chữ căn giữa
            img_width, img_height = img.size
            text_position = ((img_width - text_width) // 2, (img_height - text_height) // 2)
            # Vẽ chữ lên ảnh
            draw.text(text_position, text, fill="black", font=font)  # Tùy chỉnh màu chữ
            scale_factor = 0.7  # Thay đổi tỉ lệ (0.5 là giảm một nửa, 2.0 là gấp đôi)
            img = resize_image(img, scale_factor)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Lỗi khi tạo ảnh: {e}")
            return None

    # Đường dẫn file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    button_image_path = os.path.join(base_dir, "button.png")
    button_hover_image_path = os.path.join(base_dir, "button_hover.png")
    font_path = os.path.join(base_dir, "ja-jp.ttf")

    # Tạo ảnh với chữ
    button_image = create_image_with_text(button_image_path, text_input, font_path)
    button_hover_image = create_image_with_text(button_hover_image_path, text_input, font_path)

    # Hàm thay đổi ảnh khi hover
    def on_enter(event):
        button.config(image=button_hover_image)

    def on_leave(event):
        button.config(image=button_image)

    # Tạo nút với ảnh và gán sự kiện click
    button = tk.Button(
        frame,
        image=button_image,
        borderwidth=0,           # Không viền
        highlightthickness=0,    # Không hiệu ứng viền
        command=command         # Gắn sự kiện khi nhấn nút
    )
    button.pack(pady=20)

    # Gắn sự kiện hover
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button


# Data cấu trúc đề thi
questions = {
    "Đề 1": {
        "Câu 1": {"question": "Câu 1", "answer": "Đáp án câu 1"},
        "Câu 2": {"question": "Câu 2", "answer": "Đáp án câu 2"},
        "Câu 3": {"question": "Câu 3", "answer": "Đáp án câu 3"},
        "Câu 4": {"question": "Câu 4", "answer": "Đáp án câu 4"},
        "Câu 5": {"question": "Câu 5", "answer": "Đáp án câu 5"},
        "Câu 6": {"question": "Câu 6", "answer": "Đáp án câu 6"},
        "Câu 7": {"question": "Câu 7", "answer": "Đáp án câu 7"}
    },
    "Đề 2": {
        "Câu 1": {"question": "Câu 1", "answer": "Đáp án câu 1"},
        "Câu 2": {"question": "Câu 2", "answer": "Đáp án câu 2"},
        "Câu 3": {"question": "Câu 3", "answer": "Đáp án câu 3"},
        "Câu 4": {"question": "Câu 4", "answer": "Đáp án câu 4"},
        "Câu 5": {"question": "Câu 5", "answer": "Đáp án câu 5"},
        "Câu 6": {"question": "Câu 6", "answer": "Đáp án câu 6"},
        "Câu 7": {"question": "Câu 7", "answer": "Đáp án câu 7"}
    },
    "Đề 3": {
        "Câu 1": {"question": "Câu 1", "answer": "Đáp án câu 1"},
        "Câu 2": {"question": "Câu 2", "answer": "Đáp án câu 2"},
        "Câu 3": {"question": "Câu 3", "answer": "Đáp án câu 3"},
        "Câu 4": {"question": "Câu 4", "answer": "Đáp án câu 4"},
        "Câu 5": {"question": "Câu 5", "answer": "Đáp án câu 5"},
        "Câu 6": {"question": "Câu 6", "answer": "Đáp án câu 6"},
        "Câu 7": {"question": "Câu 7", "answer": "Đáp án câu 7"}
    },
    "Đề 4": {
        "Câu 1": {"question": "Câu 1", "answer": "Đáp án câu 1"},
        "Câu 2": {"question": "Câu 2", "answer": "Đáp án câu 2"},
        "Câu 3": {"question": "Câu 3", "answer": "Đáp án câu 3"},
        "Câu 4": {"question": "Câu 4", "answer": "Đáp án câu 4"},
        "Câu 5": {"question": "Câu 5", "answer": "Đáp án câu 5"},
        "Câu 6": {"question": "Câu 6", "answer": "Đáp án câu 6"},
        "Câu 7": {"question": "Câu 7", "answer": "Đáp án câu 7"}
    },
    "Đề 5": {
        "Câu 1": {"question": "Câu 1", "answer": "Đáp án câu 1"},
        "Câu 2": {"question": "Câu 2", "answer": "Đáp án câu 2"},
        "Câu 3": {"question": "Câu 3", "answer": "Đáp án câu 3"},
        "Câu 4": {"question": "Câu 4", "answer": "Đáp án câu 4"},
        "Câu 5": {"question": "Câu 5", "answer": "Đáp án câu 5"},
        "Câu 6": {"question": "Câu 6", "answer": "Đáp án câu 6"},
        "Câu 7": {"question": "Câu 7", "answer": "Đáp án câu 7"}
    }
}
last_subject = None
last_question = None
# Giao diện chính khi nhấn vào một đề
def show_questions_buttons(subject):
    global last_subject
    last_subject = subject 
    # Ẩn các widget cũ
    for widget in frame.winfo_children():
        widget.destroy()
    # Tạo button các câu cho đề đã chọn
    for i in range(1, 8):
        button = create_button_with_text(f"Câu {i}", lambda i=i: show_question_or_answer(subject, i))
        button.pack(pady=5)

    # Thêm button "Undo" để quay lại màn hình chọn đề
    undo_button = create_button_with_text("Undo", show_subject_buttons)
    undo_button.pack(pady=5)

# Hiển thị câu hỏi và đáp án khi nhấn vào câu
def show_question_or_answer(subject, question_num):
    global last_question
    last_question = question_num  # Lưu lại câu hỏi đã chọn
    # Ẩn button câu và hiện button xem câu hỏi và đáp án
    for widget in frame.winfo_children():
        widget.destroy()
    # Tạo button xem câu hỏi và xem đáp án
    question_button = create_button_with_text(f"Xem Câu Hỏi", command=lambda : show_image(subject, question_num, "question"))
    question_button.pack(pady=5)

    answer_button = create_button_with_text(f"Xem Đáp Án", command=lambda : show_image(subject, question_num, "answer"))
    answer_button.pack(pady=5)

    # Thêm button "Undo" để quay lại màn hình chọn câu
    undo_button = create_button_with_text(f"Undo", command=lambda: show_questions_buttons(subject))
    undo_button.pack(pady=5)
def show_image(subject, question_num, type):
    # Lấy thư mục chứa script exam.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, "asset", type, f"{str(subject[-1])}{str(question_num)}.png")

    try:
        img = Image.open(image_path)
        img = img.resize((800, int(800 * img.height / img.width)))  # Giữ tỷ lệ ảnh nhưng thay đổi chiều rộng
        img = ImageTk.PhotoImage(img)

        # Tạo canvas với scrollbars
        canvas_frame = tk.Frame(frame)  # Tạo frame để chứa canvas và scrollbar
        canvas_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(canvas_frame, width=800, height=img.height())
        scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)  # Cuộn dọc
        canvas.config(yscrollcommand=scrollbar.set)

        # Cài đặt thanh cuộn dọc
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # Hiển thị ảnh trên canvas
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.image = img  # Giữ tham chiếu tới ảnh

        # Cập nhật chiều cao ảnh của canvas
        canvas.config(scrollregion=canvas.bbox("all"))

    except FileNotFoundError:
        messagebox.showerror("Lỗi", f"Không tìm thấy hình ảnh: {image_path}")
# Chọn màn hình ban đầu khi nhấn vào "Undo"
def show_subject_buttons():
    # Ẩn các widget cũ
    for widget in frame.winfo_children():
        widget.destroy()
    # Tạo button cho các đề thi
    for subject in questions.keys():
        button = create_button_with_text(subject, lambda subject=subject: show_questions_buttons(subject))
        button.pack(pady=5)
# Cửa sổ chính
window = tk.Tk()
window.title("Thu thập đề thi và đáp án")
window.iconbitmap("exam.ico")
window.geometry("1800x700")
# Frame chứa các button
frame = tk.Frame(window)
frame.pack(padx=20, pady=20)
image_path = "thongbao.png"  # Thay đổi đường dẫn đến hình ảnh của bạn
original_image = Image.open(image_path)
# Thay đổi kích thước hình ảnh (giảm xuống 50% so với kích thước ban đầu)
resized_image = resize_image(original_image, 0.3)
# Chuyển đổi hình ảnh đã thay đổi kích thước thành PhotoImage để Tkinter sử dụng
photo_image = ImageTk.PhotoImage(resized_image)
# Tạo Label để hiển thị hình ảnh
image_label = tk.Label(window, image=photo_image)
image_label.place(x=10, y=10)  # Đặt hình ảnh ở góc trên bên trái
# Tải hình ảnh và thay đổi kích thước
facebook_image = Image.open("facebook.png")  # Đường dẫn đến hình ảnh Facebook
github_image = Image.open("github.png")  # Đường dẫn đến hình ảnh Github

# Thay đổi kích thước hình ảnh (giảm xuống 50%)
facebook_image_resized = resize_image(facebook_image, 0.25)
github_image_resized = resize_image(github_image, 0.3)

# Chuyển đổi hình ảnh đã thay đổi kích thước thành PhotoImage để Tkinter sử dụng
facebook_photo = ImageTk.PhotoImage(facebook_image_resized)
github_photo = ImageTk.PhotoImage(github_image_resized)
def open_link(event, url):
    webbrowser.open(url, new=2)
# Lấy kích thước cửa sổ và hình ảnh
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
facebook_width = facebook_image_resized.width
facebook_height = facebook_image_resized.height
github_width = github_image_resized.width
github_height = github_image_resized.height

# Đặt các Label để hiển thị hình ảnh ở góc trên bên phải
facebook_label = tk.Label(window, image=facebook_photo)
facebook_label.place(x=window_width - facebook_width - 450, y=13)  # Đặt Facebook ở góc trên bên phải
facebook_caption = tk.Label(window, text="Facebook", font=("Arial", 8))
facebook_caption.place(x=window_width - facebook_width - 450 + facebook_width // 2 - 30, y=13 + facebook_height + 5)  # Phụ đề nằm dưới ảnh
github_label = tk.Label(window, image=github_photo)
github_label.place(x=window_width - github_width - 400, y=10)  # Đặt Github dưới Facebook
# Phụ đề cho Github
github_caption = tk.Label(window, text="Github", font=("Arial", 8))
github_caption.place(x=window_width - github_width - 400 + github_width // 2 - 20, y=11.5 + github_height)  # Phụ đề nằm dưới ảnh
# Gắn sự kiện click vào ảnh
facebook_label.bind("<Button-1>", lambda e: open_link(e,"https://web.facebook.com/tamidanopro"))
github_label.bind("<Button-1>", lambda e: open_link(e,"https://github.com/dangminhtai"))
show_subject_buttons()
# Chạy giao diện
window.mainloop()
