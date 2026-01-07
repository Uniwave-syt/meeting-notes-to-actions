# 📝 Meeting Notes → Action List

**一个使用 AI 自动把会议记录生成决策与行动列表的工具**  

[Streamlit 部署版演示](#)  ← （后续可以填 Streamlit Share 链接）

---

## 功能

- 粘贴会议记录（支持中文 / 英文）
- 自动生成：
  - 决策（Decisions Made）
  - 行动项（Action Items）
  - 待解决问题（Open Questions）
  - 风险与跟进（Risks / Follow-Ups）
- 输出结构清晰，方便直接执行或记录

---

## 技术栈

- **Python 3.10+**
- **Streamlit**：快速 Web 页面展示
- **OpenAI GPT-4o-mini**：核心 AI 文本处理
- **python-dotenv**：管理 API Key
- **Git + GitHub**：版本管理和展示

---

## 安装与运行

1. 克隆仓库
```bash
git clone https://github.com/你的用户名/meeting-notes-to-actions.git
cd meeting-notes-to-actions

2. 创建虚拟环境并激活
Windows:
python -m venv venv
venv\Scripts\activate

3. 安装依赖
pip install -r requirements.txt

4. 配置 API Key
OPENAI_API_KEY=你的OpenAI_API_KEY

5. 运行应用
streamlit run app.py
