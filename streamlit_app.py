import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# 設置matplotlib字體
matplotlib.font_manager.fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
matplotlib.rc('font', family='Taipei Sans TC Beta')

# 頁面標題跟寬度設定
st.set_page_config(page_title="蛇蛇工具箱🐍")

# 頁面樣式設定
st.markdown('<style>\
.st-emotion-cache-1dp5vir {\
position: absolute;\
top: 0px;\
right: 0px;\
left: 0px;\
height: 0.125rem;\
background-image: linear-gradient(90deg, #7E60BF, #E4B1F0);\
z-index: 999990;\
}\
</style>', unsafe_allow_html=True)

# 側欄render
menu_arr = ["甘特圖產生器"]
with st.sidebar:
    # 側欄分組與主要內容回填
    menu = option_menu("蛇蛇工具箱🐍", menu_arr,
        icons=[],
        menu_icon="cast", default_index=0)

if menu == "甘特圖產生器":
    try:
        st.subheader("甘特圖產生器")
        data_from_user = st.text_area("輸入事件與區間", placeholder = """201509,202107,大學+研究所（文史哲領域）
202107,202109,協助學校教授工作""")
        colors_from_user = st.text_input("甘特圖配色", value = "#917FB3,#E5BEEC,#FDE2F3", placeholder = "#917FB3,#E5BEEC,#FDE2F3")
        if st.button("生成甘特圖"):
            # 資料設定
            data = []
            for line in data_from_user.split("\n"):
                data.append(tuple(line.split(",")))

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

            colors = ["#917FB3", "#E5BEEC", "#FDE2F3"]
            # 依據每個任務繪製橫條圖
            for i, (start, end, event) in enumerate(tasks):
                ax.barh(i, (end - start).days, left=start, height=0.4, align='center', color=colors[i % len(colors)])
                ax.text(start, i, event, va='center', ha='left', color='black')

            # 設定 Y 軸與 X 軸標籤
            ax.set_yticks(range(len(tasks)))
            ax.set_yticklabels([task[2] for task in tasks])
            ax.xaxis.set_major_locator(mdates.YearLocator())  # 設定 X 軸為每年標註一次
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # X 軸格式為 YYYY-MM
            plt.xticks(rotation=45)

            # 加入標題與調整排版
            plt.title("甘特圖")
            plt.xlabel("時間")
            plt.tight_layout()

            # 顯示圖表
            st.pyplot(fig)
    except ValueError as ve:
        st.error("你是不是沒照我說的規則>\"<")