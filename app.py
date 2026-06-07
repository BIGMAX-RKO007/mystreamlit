import streamlit as st

st.set_page_config(page_title="Fan Xiao | Global Select Shop", page_icon="🛒", layout="centered", initial_sidebar_state="collapsed")
st.title("Fan Xiao Shop 全球个人好物铺")
st.caption("🌎 GLOBAL SELECTION & LOCAL CHECKOUT | ✈️ 全球配送")
st.markdown("欢迎来到我的社交平台导航！这里汇集了我分享中的所有视频教程详情、开源效率代码，以及我个人正在使用的数码外设与付费工具的第三方直达链接。我们支持各国主流本地化支付平台结算。")

st.divider()
with st.expander("📱 关注我的社交平台 (Global Channels)", expanded=True):
    links = [
        ("📺 Bilibili (B站)", "https://space.bilibili.com"), ("📕 小红书 (Xiaohongshu)", "https://www.xiaohongshu.com"), 
        ("📸 Instagram", "https://instagram.com"), ("💬 LINE / Twitter", "https://line.me")
    ]
    for i in range(0, len(links), 2):
        for col, (name, url) in zip(st.columns(2), links[i:i+2]):
            col.link_button(name, url, use_container_width=True)

st.divider()
with st.expander("🛍️ 视频同款与教程详情 (Featured Tutorials & Shop)"):
    for col, (title, tag, desc, links) in zip(st.columns(3), [
        ("⌨️ 机械键盘", "视频同款外设 / CUSTOM GEAR", "75%极简桌面布局，定制奶油轴，全铝客制化机身。", [("淘宝直购 (CN)", "https://taobao.com"), ("煤炉小铺 (JP)", "https://jp.mercari.com"), ("eBay Store (Global)", "https://ebay.com")]),
        ("💡 护眼挂灯", "视频同款硬件 / MONITOR LIGHT", "非对称光源设计，无线桌面旋钮控制器，无极调光。", [("淘宝直购 (CN)", "https://taobao.com"), ("拼多多 (CN)", "https://pinduoduo.com"), ("eBay Store (Global)", "https://ebay.com")]),
        ("📚 AI 效率手册", "数字商品 / CREATOR BLUEPRINT", "一键自动化创作分发脚本，附赠详细Prompt实操手册。", [("面包多店铺 (CN)", "https://mianbaoduo.com"), ("爱发电赞助 (CN)", "https://afdian.com"), ("Gumroad (Global)", "https://gumroad.com")])
    ]):
        with col.container(border=True):
            st.subheader(title); st.caption(tag); st.write(desc); st.divider(); st.markdown("**🛒 选择地区直购:**")
            for name, url in links: st.link_button(name, url, use_container_width=True)

st.divider()
with st.expander("🏪 我的官方平台店铺 (Our Official Stores)"):
    for col, (title, sub, btn, url) in zip(st.columns(4), [
        ("**淘宝旗舰店**", "China Taobao", "🛍️ 进店逛逛", "https://taobao.com"),
        ("**咸鱼闲置主页**", "China Xianyu", "📦 前往淘货", "https://goofish.com"),
        ("**煤炉 JP 小铺**", "Japan Mercari", "🇯🇵 前往煤炉", "https://jp.mercari.com"),
        ("**eBay 跨国商铺**", "Global eBay", "🌎 前往eBay", "https://ebay.com")
    ]):
        with col.container(border=True):
            st.write(title); st.caption(sub); st.link_button(btn, url, use_container_width=True)

st.divider()
f1, f2 = st.columns([2, 1])
f1.caption("© 2026 Fan Xiao Shop. All rights reserved. Globally Shipped & Engineered by Fan Xiao")
f2.link_button("📬 售后与商务合作 (Inquiry)", "mailto:369246926@qq.com?subject=【Order & Business Support】", use_container_width=True)
