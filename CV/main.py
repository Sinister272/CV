import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.pdfgen import canvas, pdfimages
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4

pdfmetrics.registerFont(TTFont("Vazir", "Vazir.ttf"))
pdfmetrics.registerFont(TTFont("Vazir-Bold", "Vazir-Bold.ttf"))

c = canvas.Canvas("resume.pdf")
c.setPageSize(A4)

width , height = A4


def reshape(text):
    reshaper = arabic_reshaper.reshape(text)
    reshaped = get_display(reshaper)
    return reshaped

def small_text():
    c.setFillColor("black")
    c.setFont("Vazir", 13)
    

c.setFillColorRGB(0.0039, 0.4509, 0.0196)
c.rect(410,0,200,1000,fill=1,stroke=1)
c.rect(0,680,700,30,fill=1,stroke=1)

c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(410,720,200,50,fill=1,stroke=1)

c.setFillColor("black")
c.setFont("Vazir-Bold",22)
c.drawString(235,810,reshape("محمد باقر ساکی"),mode=0, charSpace=0, direction= "RTL", wordSpace= 0)
c.setFont("Vazir",15)
c.drawString(40,825,reshape("سال تولد: 1377"),mode=0, charSpace=0, direction= "RTL", wordSpace= 0)
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/Date.png",143,820,15,15)
c.drawString(15,795,reshape("وضعیت تاهل: مجرد"),mode=0, charSpace=0, direction= "RTL", wordSpace= 0)
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/married.png",143,795,15,15)
#vertical green line
c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(175,778,10,200,fill=1,stroke=1)

c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(10,778,385,10,fill=1)
#about me
text0 = "مهندس مکانیک با ارشد آموزش زبان انگلیسی؛ ترکیبی از دانش فنی،مهارت زبانی"
text0_1 = " و توانایی برنامه‌نویسی پایتون که امکان فعالیت در حوزه‌های مختلف را فراهم"
text0_2 = "می‌آورد و همواره در پی گسترش مهارت‌ها در زمینه‌های جدید هستم."

small_text()
c.setFont("Vazir", 12)
c.drawRightString(390,763,reshape(text0), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawRightString(390,742,reshape(text0_1), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawRightString(390,720,reshape(text0_2), mode=0, charSpace=0, direction="RTL", wordSpace= 0)

#Title
c.setFillColor("White")
c.setFont("Vazir-Bold", 20)
c.drawString(120,690,reshape("تحصیلات و مدارک"), mode=0, charSpace=0, direction="RTL", wordSpace= 0)



#text
text1_1= "کارشناسی مهندسی مکانیک از دانشگاه دولتی صنعتی جندی شاپور دزفول"
text1_1_2= "تجربه شبیه‌سازی CFD و تحلیل ایرفویل با ANSYS Fluent"


small_text()
c.drawRightString(390,660,reshape(text1_1), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawRightString(390,635,reshape(text1_1_2), mode=0, charSpace=0, direction="RTL", wordSpace= 0)



c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(10,610,385,10,fill=1)

text2_1 = "کارشناسی ارشد زبان انگلیسی (گرایش آموزش زبان انگلیسی) از دانشگاه"
text2_2 = "آزاد اسلامی اهواز"
small_text()
c.drawRightString(390,585,reshape(text2_1), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawRightString(390,560,reshape(text2_2), mode=0, charSpace=0, direction="RTL", wordSpace= 0)

c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(10,535,385,10,fill=1)


text3 = "مدرک مهارت های 7 گانه (ICDL) از فنی و حرفه ای"
small_text()
c.drawRightString(390,515,reshape(text3), mode=0, charSpace=0, direction="RTL", wordSpace= 0)

c.setFillColorRGB(0.0039, 0.4509, 0.0196)
c.rect(0,475,410,30,fill=1,stroke=1)
c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(410,475,200,30,fill=1,stroke=1)


c.setFillColor("White")
c.setFont("Vazir-Bold", 20)
c.drawString(150,485,reshape("مهارت ها"), mode=0, charSpace=0, direction="RTL", wordSpace= 0)

text3_5 = "تسلط به زبان انگلیسی و مهارت در مطالعه، ترجمه و مکاتبات"
text3_6 = "آشنایی کاربردی با زبان عربی و مهارت در برقراری مکالمه"
text4= "Excel (Spreadsheets), Access (Data Base), Word (Word Processing)"
text5= "Network, PowerPoint (Slide Presentation)"
text6= "مسلط به زبان برنامه نویسی پایتون (Python)"
text7= "تجربه کار با کتابخانه های پرکاربرد پایتون:"
text8= "PySide6 (GUI ساخت), Matplotlib (ساخت نمودار بر اساس داده ها)"
text9= "Pandas (پردازش و مدیریت داده ها), Reportlab, Math, Numpy"
text10= "PyAutoGui (اتوماتیک کردن تمام کارها در کامپیوتر)"
small_text()
c.drawRightString(390,450,reshape(text3_5), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawRightString(390,425,reshape(text3_6), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(10,405,385,10,fill=1)
small_text()
c.drawRightString(400,390,reshape(text4), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawString(10,365,reshape(text5), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(10,345,385,10,fill=1)
small_text()
c.drawRightString(390,325,reshape(text6), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/Python logo.png",12,305,30,30)
c.drawRightString(390,300,reshape(text7), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawString(10,275,reshape(text8), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawString(10,250,reshape(text9), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawString(10,225,reshape(text10), mode=0, charSpace=0, direction="RTL", wordSpace= 0)

c.setFillColorRGB(0.0039, 0.4509, 0.0196)
c.rect(0,180,410,30,fill=1,stroke=1)
c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(410,180,200,30,fill=1,stroke=1)
c.setFillColor("White")
c.setFont("Vazir-Bold", 20)
c.drawString(125,190,reshape("اطلاعات تکمیلی"), mode=0, charSpace=0, direction="RTL", wordSpace= 0)

text11 = "وضعیت نظام وظیفه: معافیت دائم با 18 ماه سابقه خدمت در پدافند هوایی"
text12 = "فرزند فرهنگی (والدین شاغل در آموزش‌ و پرورش)"
text13 = "دارای سابقه فعالیت‌های داوطلبانه، فرهنگی و اجتماعی در بسیج"
text14 = "کسب رتبه اول مسابقات کشوری حفظ قرآن کریم ویژه دانش‌آموزان ایرانی"
text15 = "مقیم امارات در سال‌های ۱۳۸۷ و ۱۳۸۹"

small_text()
c.drawRightString(390,155,reshape(text11), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(10,135,385,10,fill=1)
small_text()
c.drawRightString(390,115,reshape(text12), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(10,95,385,10,fill=1)
small_text()
c.drawRightString(390,75,reshape(text13), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.setFillColorRGB(0.635, 0.960, 0.643)
c.rect(10,55,385,10,fill=1)
small_text()
c.drawRightString(390,35,reshape(text14), mode=0, charSpace=0, direction="RTL", wordSpace= 0)
c.drawRightString(390,15,reshape(text15), mode=0, charSpace=0, direction="RTL", wordSpace= 0)

#Call
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/Call.png", 420, 400, 20,20)
c.setFillColor("White")
c.setFont("Vazir", 13)
c.drawString(450,405,reshape("09351713158"), mode=0, charSpace=2, direction="RTL")
#Mail
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/mail.png", 420, 360, 20,20)
c.setFillColor("White")
c.setFont("Vazir", 13)
c.drawString(450,370,reshape("Baghersaki272"), mode=0, charSpace=2, direction="RTL")
c.drawString(450,350,reshape("@gmail.com"), mode=0, charSpace=2, direction="RTL")
#home
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/Home.jpg", 420, 310, 20,20)
c.setFillColor("White")
c.setFont("Vazir", 13)
c.drawString(450,315,reshape("Ahvaz"), mode=0, charSpace=2, direction="RTL")

#key skills
c.setFillColor("White")
c.setFont("Vazir-Bold", 13)
c.drawString(443,150,reshape("مهارت های کلیدی"), mode=0, charSpace=0, direction="RTL")
c.setFillColor("White")
c.setFont("Vazir", 13)
c.drawString(455,120,reshape("زبان انگلیسی"), mode=0, charSpace=0, direction="RTL")
c.drawString(455,95,reshape("Python"), mode=0, charSpace=0, direction="RTL")
c.drawString(455,70,reshape("مهندسی مکانیک"), mode=0, charSpace=0, direction="RTL")
c.drawString(455,45,reshape("کامپیوتر (ICDL)"), mode=0, charSpace=0, direction="RTL")
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/star.png", 420, 115, 30,20)
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/star.png", 420, 90, 30,20)
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/star.png", 420, 65, 30,20)
c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/star.png", 420, 40, 30,20)

c.drawImage("C:/Users/Sinister/Desktop/Python/CV/Utils/bagher-office-small - Copy.png",410,505,190,340)







c.save()