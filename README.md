# Fan Xiao | Global Select Shop (全球个人好物铺)

🌎 **GLOBAL SELECTION & LOCAL CHECKOUT | ✈️ 全球配送**

这是一个极简且具有现代设计感的个人带货/社交引流导航页，基于 [Streamlit](https://streamlit.io/) 构建。

## 🌟 核心特性
- **社交媒体矩阵**：快速引流至 Bilibili, 小红书, Instagram, LINE/Twitter。
- **动态单品展示**：视频同款外设、效率手册的分类聚合与跨区购买链接分发。
- **官方店铺直达**：快速跳转淘宝、闲鱼、日本煤炉、eBay。
- **极简数据驱动**：采用 Python 原生数据结构驱动，维护成本极低（单文件 40 余行代码）。

## 🚀 如何在本地运行

1. 克隆或下载本项目到本地。
2. 创建并激活虚拟环境：
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Mac/Linux
   # 或者 .venv\Scripts\activate  # Windows
   ```
3. 安装依赖包：
   ```bash
   pip install -r requirements.txt
   ```
4. 运行 Streamlit 应用：
   ```bash
   streamlit run app.py
   ```
   *应用会自动在浏览器中打开 (默认地址：http://localhost:8501)。*

## 📦 自动构建测试 (CI)
本项目已配置 GitHub Actions。任何提交到主分支的代码都会自动运行基础依赖安装和测试，确保代码无严重语法错误。

---
© 2026 Fan Xiao Shop. All rights reserved. Globally Shipped & Engineered by Fan Xiao
