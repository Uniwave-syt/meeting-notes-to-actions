import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# ------------------------
# 1. 加载 API Key
# ------------------------
load_dotenv()  # 从 .env 文件读取 OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ------------------------
# 2. Streamlit 页面设置
# ------------------------
st.set_page_config(
    page_title="Meeting Notes → Action List",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Meeting Notes → Action List")
st.write("把会议记录粘贴到下面，生成决策和行动列表。")

# ------------------------
# 3. 输入区域
# ------------------------
notes = st.text_area(
    "粘贴会议记录",
    height=250,
    placeholder="在这里粘贴你的会议记录或 Zoom transcript..."
)

# ------------------------
# 4. 点击按钮生成结果
# ------------------------
if st.button("生成 Action List"):
    if not notes.strip():
        st.warning("请先粘贴会议记录")
    else:
        with st.spinner("AI 正在分析..."):
            # ------------------------
            # 4a. 构造 Prompt
            # ------------------------
            prompt = f"""
你是一个高效的行政助理，请将以下会议记录整理为固定格式：
- 只提取关键信息
- 不要编造内容
- 如果负责人或截止日期不明确，写 "未指定"

会议记录：
{notes}

输出格式：
DECISIONS MADE:
- ...

ACTION ITEMS:
- Task:
  Owner:
  Deadline:
"""
            # ------------------------
            # 4b. 调用 OpenAI API
            # ------------------------
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt}
                ]
            )
            
            # ------------------------
            # 4c. 显示结果
            # ------------------------
            st.write(response.choices[0].message.content)