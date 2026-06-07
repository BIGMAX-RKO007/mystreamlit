import streamlit as st

st.set_page_config(page_title="Fan Xiao | Global Select Shop", page_icon="🛒", layout="centered", initial_sidebar_state="collapsed")

# 1. 自动识别浏览器语言 (I18n)
# 读取浏览器的 Accept-Language 请求头，如果不包含 'zh'，则自动切换为英文环境
accept_lang = st.context.headers.get("Accept-Language", "zh")
is_en = "zh" not in accept_lang.lower()

# 中英文词典配置，保持简短以控制代码量
T = {
    "zh": {
        "title": "Fan Xiao Shop",
        "caption": "🌎 全球精选 & 本地结算 | ✈️ 全球配送",
        "intro": "欢迎来到我的社交平台导航！这里汇集了我分享中的所有视频教程详情、开源效率代码，以及我个人正在使用的数码外设与付费工具的第三方直达链接。我们支持各国主流本地化支付平台结算。",
        "social_title": "📱 关注我的社交平台 (Global Channels)",
        "product_title": "🛍️ 视频同款与教程详情 (Featured Tutorials & Shop)",
        "store_title": "🏪 我的官方平台店铺 (Our Official Stores)",
        "secure_checkout": "🔒 官方平台担保交易 | 🛡️ 售后无忧",
        "direct_buy": "**🛒 选择地区直购:**",
        "inquiry": "📬 售后与商务合作 (Inquiry)",
        "m_fans_val": "10W+", "m_fans_lbl": "👥 全网粉丝关注", "m_fans_hlp": "B站、小红书等社交平台总关注人数",
        "m_rate_val": "99.8%", "m_rate_lbl": "👌 用户真实好评", "m_rate_hlp": "各平台官方店铺真实买家好评整理",
        "m_resp_val": "<24小时", "m_resp_lbl": "⚡ 专属客服响应", "m_resp_hlp": "售后与商务合作邮件的平均回复时效",
        "guarantee_title": "🛡️ 官方双重安全与售后保障说明",
        "guarantee_text": "1. **官方渠道保证**：所有商品链接均为品牌官方旗舰店或作者本人的直达店铺，拒绝一切非官方的第三方代理。\n2. **资金担保安全**：交易均在淘宝、eBay、Gumroad 等主流知名电商平台内完成，资金不经过任何个人账户，100% 享受平台的消费者保障计划。"
    },
    "en": {
        "title": "Fan Xiao Shop",
        "caption": "🌎 GLOBAL SELECTION & LOCAL CHECKOUT | ✈️ GLOBAL SHIPPING",
        "intro": "Welcome to my navigation hub! Here you can find all my video tutorial details, open-source code, and direct links to digital gear and paid tools I personal use. We support mainstream localized payment methods worldwide.",
        "social_title": "📱 Follow My Social Channels",
        "product_title": "🛍️ Featured Tutorials & Shop",
        "store_title": "🏪 Our Official Stores",
        "secure_checkout": "🔒 Escrow Transaction | 🛡️ Worry-Free Support",
        "direct_buy": "**🛒 Choose Your Region to Buy:**",
        "inquiry": "📬 Business & Order Inquiry",
        "m_fans_val": "100K+", "m_fans_lbl": "👥 Total Followers", "m_fans_hlp": "Total followers across Bilibili, Xiaohongshu, Instagram, etc.",
        "m_rate_val": "99.8%", "m_rate_lbl": "👌 Positive Feedback", "m_rate_hlp": "Aggregated from official store customer ratings.",
        "m_resp_val": "<24h", "m_resp_lbl": "⚡ Support Response", "m_resp_hlp": "Average response time for support & business inquiry emails.",
        "guarantee_title": "🛡️ Official Security & Support Guarantee",
        "guarantee_text": "1. **Official Channels Only**: All product links lead directly to official flagship stores or the creator's verified stores. No unauthorized third-party agents.\n2. **Secure Checkout**: All transactions are processed through mainstream platforms (Taobao, eBay, Gumroad) with full consumer protection. Funds are never sent to personal accounts."
    }
}
t = T["en"] if is_en else T["zh"]

# 2. 顶部个人品牌与头像区域
col_avatar, col_title = st.columns([1, 4])
with col_avatar:
    # 使用中性、简约的默认用户头像（您可以把这行 URL 换成您自己的个人照片链接或本地路径，如 "avatar.png"）
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
with col_title:
    st.title(t["title"])
    st.caption(t["caption"])

st.markdown(t["intro"])

# 3. 信任背书与数据展示
st.divider()
c1, c2, c3 = st.columns(3)
c1.metric(label=t["m_fans_lbl"], value=t["m_fans_val"], help=t["m_fans_hlp"])
c2.metric(label=t["m_rate_lbl"], value=t["m_rate_val"], help=t["m_rate_hlp"])
c3.metric(label=t["m_resp_lbl"], value=t["m_resp_val"], help=t["m_resp_hlp"])

st.divider()
with st.expander(t["social_title"], expanded=True):
    links = [
        ("📺 Bilibili (B站)" if not is_en else "📺 Bilibili", "https://space.bilibili.com"), 
        ("📕 小红书 (Xiaohongshu)" if not is_en else "📕 Xiaohongshu", "https://www.xiaohongshu.com"), 
        ("📸 Instagram", "https://instagram.com"), 
        ("💬 LINE / Twitter" if not is_en else "💬 LINE / X", "https://line.me")
    ]
    for i in range(0, len(links), 2):
        for col, (name, url) in zip(st.columns(2), links[i:i+2]):
            col.link_button(name, url, use_container_width=True)

st.divider()
with st.expander(t["product_title"]):
    # 商品定义，如果是英文模式，描述和按钮标签微调为英文
    products = [
        (
            "⌨️ 机械键盘" if not is_en else "⌨️ Mechanical Keyboard",
            "视频同款外设 / CUSTOM GEAR" if not is_en else "VIDEO RECOMMENDED / CUSTOM GEAR",
            "75%极简桌面布局，定制奶油轴，全铝客制化机身。" if not is_en else "75% minimal layout, custom linear switches, full CNC aluminum body.",
            [("淘宝直购 (CN)" if not is_en else "Taobao (CN)", "https://taobao.com"), 
             ("煤炉小铺 (JP)" if not is_en else "Mercari (JP)", "https://jp.mercari.com"), 
             ("eBay Store (Global)" if not is_en else "eBay (Global)", "https://ebay.com")]
        ),
        (
            "💡 护眼挂灯" if not is_en else "💡 Monitor Light",
            "视频同款硬件 / MONITOR LIGHT" if not is_en else "VIDEO RECOMMENDED / MONITOR LIGHT",
            "非对称光源设计，无线桌面旋钮控制器，无极调光。" if not is_en else "Asymmetric optical design, wireless desktop dial controller, stepless dimming.",
            [("淘宝直购 (CN)" if not is_en else "Taobao (CN)", "https://taobao.com"), 
             ("拼多多 (CN)" if not is_en else "Pinduoduo (CN)", "https://pinduoduo.com"), 
             ("eBay Store (Global)" if not is_en else "eBay (Global)", "https://ebay.com")]
        ),
        (
            "📚 AI 效率手册" if not is_en else "📚 AI Playbook",
            "数字商品 / CREATOR BLUEPRINT" if not is_en else "DIGITAL PRODUCT / CREATOR BLUEPRINT",
            "一键自动化创作分发脚本，附赠详细Prompt实操手册。" if not is_en else "One-click automated publishing script with detailed Prompt guide.",
            [("面包多店铺 (CN)" if not is_en else "Miandian (CN)", "https://mianbaoduo.com"), 
             ("爱发电赞助 (CN)" if not is_en else "Afdian (CN)", "https://afdian.com"), 
             ("Gumroad (Global)", "https://gumroad.com")]
        )
    ]
    for col, (title, tag, desc, links_list) in zip(st.columns(3), products):
        with col.container(border=True):
            st.subheader(title)
            st.caption(tag)
            st.write(desc)
            st.caption(t["secure_checkout"])
            st.divider()
            st.markdown(t["direct_buy"])
            for name, url in links_list: st.link_button(name, url, use_container_width=True)

st.divider()
with st.expander(t["store_title"]):
    stores = [
        ("**淘宝旗舰店**" if not is_en else "**Taobao Shop**", "China Taobao", "🛍️ 进店逛逛" if not is_en else "🛍️ Visit Store", "https://taobao.com"),
        ("**咸鱼闲置主页**" if not is_en else "**Xianyu Used**", "China Xianyu", "📦 前往淘货" if not is_en else "📦 Browse Items", "https://goofish.com"),
        ("**煤炉 JP 小铺**" if not is_en else "**Mercari Shop**", "Japan Mercari", "🇯🇵 前往煤炉" if not is_en else "🇯🇵 Visit Shop", "https://jp.mercari.com"),
        ("**eBay 跨国商铺**" if not is_en else "**eBay Store**", "Global eBay", "🌎 前往eBay" if not is_en else "🌎 Visit Store", "https://ebay.com")
    ]
    for col, (title, sub, btn, url) in zip(st.columns(4), stores):
        with col.container(border=True):
            st.write(title); st.caption(sub); st.link_button(btn, url, use_container_width=True)

# 4. 官方安全与售后保障卡
st.divider()
with st.container(border=True):
    st.markdown(f"### {t['guarantee_title']}")
    st.write(t['guarantee_text'])

st.divider()
f1, f2 = st.columns([2, 1])
f1.caption("© 2026 Fan Xiao Shop. All rights reserved. Globally Shipped & Engineered by Fan Xiao")
f2.link_button(t["inquiry"], "mailto:369246926@qq.com?subject=【Order & Business Support】", use_container_width=True)
