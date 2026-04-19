import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# --- ส่วนที่ 1: การตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="Mortgage Churn Dashboard", layout="wide")
st.title(" Mortgage Refinance Risk Dashboard")
st.markdown("ระบบวิเคราะห์ความเสี่ยงลูกค้าสินเชื่อบ้านเพื่อการรักษาฐานลูกค้า")

# --- ส่วนที่ 2: จำลองข้อมูลและโมเดล (เพื่อให้แอปทำงานได้) ---
@st.cache_data
def load_data():
    # ใช้โค้ดจำลองข้อมูลเดิมที่เราทำกันมา
    n = 1000
    np.random.seed(42)
    df = pd.DataFrame({
        'Customer_ID': [f'C-{i:04d}' for i in range(1, n+1)],
        'Credit_Score': np.random.randint(500, 850, n),
        'Loan_Amount': np.random.randint(1000000, 5000000, n),
        'Current_Rate': np.random.uniform(4.0, 7.0, n),
        'Years_With_Bank': np.random.randint(1, 15, n)
    })
    return df

df = load_data()

# --- ส่วนที่ 3: Sidebar - "What-If" Simulator ---
st.sidebar.header(" Market Simulator")
market_rate = st.sidebar.slider("ดอกเบี้ยคู่แข่งในตลาด (%)", 2.0, 5.0, 3.5, 0.1)

# คำนวณ Rate Spread ใหม่ตามตัวแปรที่ผู้ใช้ปรับ
df['Rate_Spread'] = df['Current_Rate'] - market_rate

# --- ส่วนที่ 4: Logic การทำนาย (จำลองโมเดล) ---
# ในงานจริงคุณจะโหลดไฟล์โมเดลที่ Save ไว้มาใช้ตรงนี้
df['Churn_Prob'] = (df['Rate_Spread'] * 0.5) + (df['Credit_Score'] / 850 * 0.3)
df['Churn_Prob'] = df['Churn_Prob'] / df['Churn_Prob'].max() # Normalize ให้เป็น 0-1
df['Risk_Level'] = pd.cut(df['Churn_Prob'], bins=[0, 0.6, 0.8, 1], labels=['Low', 'Medium', 'High'])

# --- ส่วนที่ 5: แสดงผล Metrics (ตัวเลขเด่น) ---
col1, col2, col3 = st.columns(3)
high_risk_df = df[df['Risk_Level'] == 'High']

with col1:
    st.metric("ลูกค้ากลุ่มเสี่ยงสูง", f"{len(high_risk_df)} คน")
with col2:
    total_val = high_risk_df['Loan_Amount'].sum() / 1e6
    st.metric("มูลค่าสินเชื่อที่เสี่ยงหลุดมือ", f"{total_val:.2f} ล้านบาท")
with col3:
    st.metric("ดอกเบี้ยตลาดปัจจุบัน", f"{market_rate}%")

# --- ส่วนที่ 6: Visualization ---
st.divider()
c1, c2 = st.columns(2)

with c1:
    st.subheader("จำนวนลูกค้าแบ่งตามระดับความเสี่ยง")
    fig = px.histogram(df, x='Risk_Level', color='Risk_Level', 
                       color_discrete_map={'Low':'green', 'Medium':'orange', 'High':'red'})
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("ความสัมพันธ์ของ Spread และความเสี่ยง")
    fig2 = px.scatter(df, x='Rate_Spread', y='Churn_Prob', color='Risk_Level',
                      hover_data=['Customer_ID'])
    st.plotly_chart(fig2, use_container_width=True)

# --- ส่วนที่ 7: ตารางรายชื่อลูกค้าที่ต้องโทรหา ---
st.divider()
st.subheader(" รายชื่อลูกค้าที่ต้องดำเนินการด่วน (High Risk)")
st.table(high_risk_df[['Customer_ID', 'Credit_Score', 'Current_Rate', 'Rate_Spread', 'Churn_Prob']].sort_values('Churn_Prob', ascending=False).head(10))