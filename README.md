# 🧸ྀི Mortgage Refinance Risk Dashboard 💗💍🦢

[![˚‧｡⋆🌻⋆｡‧˚Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mortgage-churn-dashboard.streamlit.app/)

## 🦢 Project Overview
Interactive Web Application สำหรับวิเคราะห์และจำลองความเสี่ยงของลูกค้าสินเชื่อที่อยู่อาศัยที่มีโอกาส **"ปิดบัญชีเพื่อรีไฟแนนซ์ (Prepayment Churn)"** ไปยังธนาคารคู่แข่ง โปรเจกต์นี้ผสานรวมแนวคิดทางการเงินเข้ากับ Data Science เพื่อช่วยผู้บริหารรักษาฐานรายได้ดอกเบี้ย (Net Interest Income) ของธนาคารอย่างมีประสิทธิภาพ

## 🐻‍❄️ྀིྀ The Business Problem
ในธุรกิจ Retail Banking เมื่อลูกค้าสินเชื่อบ้านหมดระยะเวลาโปรโมชั่นดอกเบี้ยต่ำ (มักจะช่วง 3 ปีแรก) ลูกค้ามักจะมีความอ่อนไหวต่ออัตราดอกเบี้ยสูงและมีแนวโน้มจะรีไฟแนนซ์หนี หากธนาคารแก้ปัญหาโดยการ "ลดดอกเบี้ยให้ทุกคนเพื่อรั้งไว้" จะทำให้สูญเสีย Margin มหาศาล 

**Objective:** ระบุตัวลูกค้ากลุ่มเสี่ยงล่วงหน้า (Predictive) เพื่อให้ทีม Retention หรือ Relationship Manager (RM) สามารถนำเสนอแคมเปญได้อย่างตรงจุดและคุ้มค่าต้นทุนที่สุด (Cost-effective Strategy)

## 🌸 The Solution & Key Features
แอปพลิเคชันนี้ออกแบบมาให้เป็น **"Strategic Simulator"** สำหรับทีม Business โดยมีฟีเจอร์เด่นดังนี้:
* **Interactive Market Simulator:** แถบสไลเดอร์ที่ให้ผู้ใช้จำลองการปรับ "อัตราดอกเบี้ยตลาด (Market Rate)" และดูผลกระทบแบบ Real-time ว่าพอร์ตสินเชื่อจะมีความเสี่ยงย้ายหนีเพิ่มขึ้นเท่าใด
* **Risk Segmentation:** แบ่งกลุ่มลูกค้าตามความน่าจะเป็น (Low, Medium, High Risk) โดยวิเคราะห์จากปัจจัยหลักคือ **Rate Spread** (ส่วนต่างดอกเบี้ยปัจจุบันกับตลาด) และ **Credit Score**
* **Financial Impact Metrics:** แสดงตัวเลขมูลค่าสินเชื่อ (Loan Amount) ที่กำลังตกอยู่ในความเสี่ยง เพื่อจัดลำดับความสำคัญทางธุรกิจ
* **Actionable Client List:** ตารางรายชื่อลูกค้ากลุ่มเสี่ยงสูงที่พร้อมนำไปใช้ปฏิบัติงานต่อได้ทันที

## 🩰 Technical Stack
* **Frontend / Web App:** `Streamlit`
* **Data Processing:** `Pandas`, `NumPy`
* **Data Visualization:** `Plotly` (สำหรับ Interactive Charts)
* **Underlying ML Concepts:** จำลองลอจิกความเสี่ยงโดยอิงจากโครงสร้างการทำนายของ **XGBoost Classifier** และผ่านกระบวนการคิดเรื่อง Class Imbalance ด้วย **SMOTE** (จากขั้นตอน Model Development)

## 🪞 How to Run Locally
หากต้องการรันโปรเจกต์นี้บนเครื่องคอมพิวเตอร์ของคุณเอง:
1. Clone repository นี้: `git clone [your-repo-link]`
2. ติดตั้ง Packages ที่จำเป็น: `pip install -r requirements.txt`
3. สั่งรัน Dashboard: `streamlit run app.py`
