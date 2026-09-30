from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from arabic_reshaper import reshape
from bidi.algorithm import get_display


def fa(text):
    return get_display(reshape(text))


pdfmetrics.registerFont(
    TTFont("Vazir", "Vazir.ttf")
)

c = canvas.Canvas("resumee.pdf", pagesize=A4)

width, height = A4

# =========================
# RIGHT SIDEBAR
# =========================

sidebar_width = 170

c.setFillColor(colors.darkgreen)

c.rect(
    width - sidebar_width,
    0,
    sidebar_width,
    height,
    fill=1,
    stroke=0
)

# =========================
# PHOTO
# =========================

c.drawImage(
    "C:/Users/Sinister/Desktop/Python/CV/1778685938181.jpg",
    width - 150,
    height - 170,
    width=120,
    height=120,
    mask="auto"
)

# =========================
# NAME
# =========================

c.setFillColor(colors.black)
c.setFont("Vazir", 24)

c.drawRightString(
    width - 200,
    height - 70,
    fa("احمد محمدی")
)

# =========================
# SUMMARY
# =========================

c.setFont("Vazir", 11)

c.drawRightString(
    width - 200,
    height - 100,
    fa("برنامه نویس پایتون با علاقه به توسعه نرم افزار")
)

c.drawRightString(
    width - 200,
    height - 120,
    fa("مسلط به PySide6 و طراحی رابط کاربری")
)

# =========================
# SECTION FUNCTION
# =========================

def section(title, y):

    c.setFillColorRGB(
        0.65,
        0.72,
        0.65
    )

    c.rect(
        30,
        y,
        width - sidebar_width - 50,
        28,
        fill=1,
        stroke=0
    )

    c.setFillColor(colors.white)

    c.setFont(
        "Vazir",
        14
    )

    c.drawRightString(
        width - sidebar_width - 20,
        y + 8,
        fa(title)
    )

    c.setFillColor(colors.black)


# =========================
# CONTACT
# =========================

c.setFillColor(colors.white)

c.setFont(
    "Vazir",
    16
)

c.drawRightString(
    width - 20,
    520,
    fa("اطلاعات تماس")
)

c.setFont(
    "Vazir",
    11
)

c.drawRightString(
    width - 20,
    480,
    fa("09123456789")
)

c.drawRightString(
    width - 20,
    455,
    fa("example@gmail.com")
)

c.drawRightString(
    width - 20,
    430,
    fa("تهران")
)

# =========================
# SKILLS
# =========================

c.setFont(
    "Vazir",
    16
)

c.drawRightString(
    width - 20,
    350,
    fa("مهارت ها")
)

skills = [
    "Python",
    "PySide6",
    "SQL",
    "Git"
]

y = 320

c.setFont(
    "Vazir",
    11
)

for skill in skills:

    c.drawRightString(
        width - 20,
        y,
        fa(f"• {skill}")
    )

    y -= 25

# =========================
# EXPERIENCE
# =========================

section(
    "سوابق شغلی",
    600
)

c.setFont(
    "Vazir",
    12
)

c.drawRightString(
    width - sidebar_width - 20,
    570,
    fa("توسعه دهنده پایتون")
)

c.setFont(
    "Vazir",
    10
)

c.drawRightString(
    width - sidebar_width - 20,
    545,
    fa("1403 تا کنون")
)

c.drawRightString(
    width - sidebar_width - 20,
    520,
    fa("طراحی نرم افزارهای دسکتاپ با PySide6")
)

c.drawRightString(
    width - sidebar_width - 20,
    500,
    fa("پیاده سازی سیستم مدیریت دانلود")
)

# =========================
# EDUCATION
# =========================

section(
    "تحصیلات",
    400
)

c.setFont(
    "Vazir",
    12
)

c.drawRightString(
    width - sidebar_width - 20,
    370,
    fa("کارشناسی مهندسی کامپیوتر")
)

c.setFont(
    "Vazir",
    10
)

c.drawRightString(
    width - sidebar_width - 20,
    345,
    fa("دانشگاه نمونه")
)

c.drawRightString(
    width - sidebar_width - 20,
    325,
    fa("1400 تا 1404")
)

c.save()