import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# 資料設定
data = [
    ("201509", "202107", "大學+研究所（文史哲領域）"),
    ("202107", "202109", "協助學校教授工作"),
    ("202109", "202202", "台大資工系系辦助理"),
]

# 轉換時間格式為 datetime 物件
def convert_to_date(date_str):
    # 將 "YYYYMM" 格式轉換為 datetime 格式
    return datetime.strptime(date_str, "%Y%m")

# 建立甘特圖資料
tasks = []
for start, end, event in data:
    tasks.append((convert_to_date(start), convert_to_date(end), event))

# 創建圖表
fig, ax = plt.subplots(figsize=(10, 4))

# 依據每個任務繪製橫條圖
for i, (start, end, event) in enumerate(tasks):
    ax.barh(i, (end - start).days, left=start, height=0.4, align='center')
    ax.text(start, i, event, va='center', ha='left', color='black')

# 設定 Y 軸與 X 軸標籤
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task[2] for task in tasks])
ax.xaxis.set_major_locator(mdates.YearLocator())  # 設定 X 軸為每年標註一次
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # X 軸格式為 YYYY-MM
plt.xticks(rotation=45)

# 加入標題與調整排版
plt.title("生涯經歷甘特圖")
plt.xlabel("時間")
plt.tight_layout()

# 顯示圖表
st.pyplot(fig)
