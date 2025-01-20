import streamlit as st
from game_guide import GameGuide
from game_content import GAME_CONTENT
import time
from api_handler import APIHandler

class GameGuideWeb:
    def __init__(self):
        self.guide = GameGuide()
        self.api = APIHandler()
        
    def run(self):
        # 设置页面配置
        st.set_page_config(
            page_title="游戏指南",
            page_icon="🎮",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # 更新CSS样式
        st.markdown("""
        <style>
        /* 全局样式 */
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap');
        
        * {
            font-family: 'Noto Sans SC', sans-serif;
        }
        
        /* 高级梦幻渐变背景 */
        .stApp {
            background: 
                linear-gradient(45deg, 
                    rgba(123, 198, 204, 0.5),
                    rgba(148, 126, 245, 0.5),
                    rgba(238, 156, 167, 0.5)),
                linear-gradient(135deg,
                    rgba(238, 174, 202, 0.5),
                    rgba(148, 187, 233, 0.5));
            background-size: 400% 400%, 300% 300%;
            animation: gradientBG 20s ease infinite;
        }
        
        @keyframes gradientBG {
            0% {
                background-position: 0% 50%, 100% 50%;
            }
            50% {
                background-position: 100% 50%, 0% 50%;
            }
            100% {
                background-position: 0% 50%, 100% 50%;
            }
        }
        
        /* 新拟态玻璃卡片 */
        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 24px;
            padding: 25px;
            margin: 15px 0;
            box-shadow: 
                0 4px 24px -1px rgba(0, 0, 0, 0.1),
                0 6px 10px -1px rgba(0, 0, 0, 0.04),
                inset 0 0 0 1px rgba(255, 255, 255, 0.1);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .glass-card:hover {
            transform: translateY(-5px) scale(1.01);
            box-shadow: 
                0 20px 40px -4px rgba(0, 0, 0, 0.15),
                0 12px 20px -4px rgba(0, 0, 0, 0.08),
                inset 0 0 0 1px rgba(255, 255, 255, 0.2);
        }
        
        /* 炫彩文字效果 */
        .rainbow-text {
            background: linear-gradient(
                to right,
                #ff6b6b,
                #f9844a,
                #fee440,
                #02c39a,
                #4361ee,
                #7209b7
            );
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: rainbow 8s linear infinite;
            background-size: 200% auto;
        }
        
        @keyframes rainbow {
            to {
                background-position: 200% center;
            }
        }
        
        /* 现代按钮样式 */
        .modern-button {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 50px;
            font-weight: 500;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
        }
        
        .modern-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                120deg,
                transparent,
                rgba(255,255,255,0.3),
                transparent
            );
            transition: 0.5s;
        }
        
        .modern-button:hover::before {
            left: 100%;
        }
        
        /* 3D卡片效果 */
        .card-3d {
            transform-style: preserve-3d;
            perspective: 1000px;
        }
        
        .card-3d:hover {
            transform: rotateX(5deg) rotateY(5deg);
        }
        
        /* 动态边框 */
        .animated-border {
            position: relative;
        }
        
        .animated-border::after {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 24px;
            padding: 2px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #a777e3);
            -webkit-mask: 
                linear-gradient(#fff 0 0) content-box, 
                linear-gradient(#fff 0 0);
            mask: 
                linear-gradient(#fff 0 0) content-box, 
                linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            animation: borderRotate 4s linear infinite;
        }
        
        @keyframes borderRotate {
            to {
                transform: rotate(360deg);
            }
        }
        
        /* 自定义滚动条 */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #6e8efb, #a777e3);
            border-radius: 4px;
            transition: all 0.3s ease;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, #a777e3, #6e8efb);
        }
        
        /* 输入框美化 */
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            color: white;
            padding: 12px 20px;
            transition: all 0.3s ease;
        }
        
        .stTextInput>div>div>input:focus,
        .stTextArea>div>div>textarea:focus {
            border-color: rgba(255, 255, 255, 0.3);
            box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.1);
        }
        
        /* 标签页样式优化 */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background: rgba(255, 255, 255, 0.05);
            padding: 10px;
            border-radius: 50px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: 50px;
            color: rgba(255, 255, 255, 0.7);
            padding: 10px 20px;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: rgba(255, 255, 255, 0.1);
            color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        /* 欢迎页面样式 */
        .welcome-container {
            width: 80%;
            max-width: 1200px;
            margin: 15vh auto;
            text-align: center;
            padding: 4rem;
            background: linear-gradient(135deg, 
                rgba(88, 216, 232, 0.8),
                rgba(187, 137, 255, 0.8));
            border-radius: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(10px);
        }
        
        .welcome-title {
            font-size: 4vw;
            color: white;
            text-shadow: 0 0 10px rgba(0,0,0,0.3);
            margin-bottom: 2rem;
            opacity: 0;
            transform: translateY(30px);
            animation: slideUp 0.8s ease 0.5s forwards;
        }
        
        .welcome-subtitle {
            font-size: 2vw;
            color: rgba(255,255,255,0.9);
            margin-bottom: 3rem;
            opacity: 0;
            transform: translateY(20px);
            animation: slideUp 0.8s ease 1s forwards;
        }
        
        /* 响应式调整 */
        @media (min-width: 1400px) {
            .welcome-title {
                font-size: 56px;
            }
            .welcome-subtitle {
                font-size: 28px;
            }
        }
        
        @media (max-width: 768px) {
            .welcome-container {
                width: 90%;
                padding: 2rem;
                margin: 10vh auto;
            }
            .welcome-title {
                font-size: 32px;
            }
            .welcome-subtitle {
                font-size: 18px;
            }
        }
        
        /* 进入按钮样式 */
        .stButton > button {
            margin-top: 2rem;
            padding: 0.8rem 3rem;
            font-size: 1.2rem;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border: 2px solid white;
            border-radius: 50px;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        @keyframes slideUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* 调整整体布局 */
        .main {
            padding: 0 !important;
            margin: 0 !important;
        }
        
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            margin: 0 !important;
        }
        
        /* 主标题样式 */
        .main-title {
            font-size: 2.5vw;
            text-align: center;
            margin-top: 3rem;
            padding: 2rem;
            background: linear-gradient(120deg, #ff6b6b, #4ecdc4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shine 3s linear infinite;
            position: relative;
            z-index: 100;
        }
        
        .content-container {
            width: 90%;
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        /* 标签页样式优化 */
        .stTabs {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 15px;
            margin-top: 2rem;
        }
        
        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        /* 内容区域样式 */
        .content-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }
        
        @media (min-width: 1400px) {
            .main-title {
                font-size: 36px;
            }
        }
        
        @media (max-width: 768px) {
            .main-title {
                font-size: 24px;
            }
            .content-container {
                width: 95%;
                padding: 1rem;
            }
        }
        
        /* 梦幻泡泡效果 */
        .bubble {
            position: fixed;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            animation: float-bubble 8s infinite ease-in-out;
            pointer-events: none;
        }
        
        @keyframes float-bubble {
            0%, 100% {
                transform: translateY(0) translateX(0);
            }
            50% {
                transform: translateY(-100px) translateX(20px);
            }
        }
        
        /* 流星效果 */
        .shooting-star {
            position: fixed;
            width: 100px;
            height: 2px;
            background: linear-gradient(90deg, #ffffff, transparent);
            animation: shooting 3s infinite ease-out;
            opacity: 0;
            pointer-events: none;
        }
        
        @keyframes shooting {
            0% {
                transform: translateX(-100%) translateY(0) rotate(-45deg);
                opacity: 1;
            }
            100% {
                transform: translateX(200%) translateY(200%) rotate(-45deg);
                opacity: 0;
            }
        }
        
        /* 光晕效果 */
        .glow {
            position: fixed;
            width: 150px;
            height: 150px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: glow-pulse 4s infinite ease-in-out;
            pointer-events: none;
        }
        
        @keyframes glow-pulse {
            0%, 100% { transform: scale(1); opacity: 0.3; }
            50% { transform: scale(1.2); opacity: 0.5; }
        }
        </style>
        
        <script>
        // 创建梦幻泡泡
        function createBubbles() {
            const container = document.body;
            for (let i = 0; i < 20; i++) {
                const bubble = document.createElement('div');
                bubble.className = 'bubble';
                bubble.style.width = Math.random() * 30 + 10 + 'px';
                bubble.style.height = bubble.style.width;
                bubble.style.left = Math.random() * 100 + 'vw';
                bubble.style.top = Math.random() * 100 + 'vh';
                bubble.style.animationDelay = Math.random() * 8 + 's';
                container.appendChild(bubble);
            }
        }
        
        // 创建流星
        function createShootingStars() {
            const container = document.body;
            setInterval(() => {
                const star = document.createElement('div');
                star.className = 'shooting-star';
                star.style.top = Math.random() * 50 + 'vh';
                star.style.left = '0';
                container.appendChild(star);
                setTimeout(() => star.remove(), 3000);
            }, 4000);
        }
        
        // 创建光晕
        function createGlows() {
            const container = document.body;
            for (let i = 0; i < 5; i++) {
                const glow = document.createElement('div');
                glow.className = 'glow';
                glow.style.left = Math.random() * 100 + 'vw';
                glow.style.top = Math.random() * 100 + 'vh';
                glow.style.animationDelay = Math.random() * 4 + 's';
                container.appendChild(glow);
            }
        }
        
        // 页面加载时创建效果
        document.addEventListener('DOMContentLoaded', () => {
            createBubbles();
            createShootingStars();
            createGlows();
        });
        </script>
        """, unsafe_allow_html=True)
        
        # 使用 session_state 控制欢迎页面的显示
        if 'show_welcome' not in st.session_state:
            st.session_state.show_welcome = True
        
        # 如果不是欢迎页面，显示固定标题
        if not st.session_state.get('show_welcome', True):
            # 添加一些空行来调整标题位置
            st.markdown("<br>" * 2, unsafe_allow_html=True)
            st.markdown('<h1 class="main-title">✨ 游戏指南 ✨</h1>', unsafe_allow_html=True)
        
        # 显示欢迎页面或主内容
        if st.session_state.show_welcome:
            # 移除默认的页面边距
            st.markdown("""
                <style>
                    .block-container {
                        padding: 0;
                    }
                </style>
            """, unsafe_allow_html=True)
            
            # 创建一个居中的欢迎内容
            st.markdown("""
                <div class="welcome-container">
                    <h1 class="welcome-title">✨ 欢迎来到梦幻世界 ✨</h1>
                    <p class="welcome-subtitle">开启你的奇幻之旅</p>
                </div>
            """, unsafe_allow_html=True)
            
            # 添加一个居中的按钮
            col1, col2, col3 = st.columns([2, 1, 2])
            with col2:
                if st.button("点击进入", use_container_width=True):
                    st.session_state.show_welcome = False
                    st.rerun()
        else:
            # 显示主页面内容
            with st.spinner('正在加载精彩内容...'):
                time.sleep(0.5)
            
            # 侧边栏
            with st.sidebar:
                st.markdown("""
                <div style="text-align: center; padding: 20px;">
                    <div style="width: 100px; height: 100px; margin: 0 auto; background: linear-gradient(45deg, #FF6B6B, #4ECDC4); border-radius: 50%; animation: pulse 2s infinite;">
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("### 🎮 导航菜单")
                selection = st.radio(
                    "",
                    list(self.guide.main_menu.values()),
                    format_func=lambda x: f"{'🎯' if x == '游戏攻略' else '💡' if x == '意见征集' else '🏢'} {x}"
                )
            
            # 主要内容区域
            if selection == "游戏攻略":
                self.show_game_guide()
            elif selection == "意见征集":
                self.show_feedback()
            else:
                self.show_recruitment()
            
    def show_game_guide(self):
        with st.container():
            # 内容容器
            with st.container():
                st.markdown('<div class="content-container">', unsafe_allow_html=True)
                
                # 使用tabs来组织内容
                tabs = st.tabs([
                    "🎮 基础指南", "⚔️ 职业系统", "✨ 特色玩法", "📝 更新日志"
                ])
                
                with tabs[0]:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        guide_selection = st.selectbox(
                            "选择指南内容",
                            list(self.guide.game_guide_submenu.values())
                        )
                
                # 添加内容切换动画
                with st.spinner('加载中...'):
                    time.sleep(0.3)
                    self.show_guide_content(guide_selection)
            
                st.markdown('</div>', unsafe_allow_html=True)

    def show_guide_content(self, selection):
        content = self.api.get_game_content(selection)
        st.markdown(f"""
        <div class="glass-card">
            <h3 style="color: white; margin-bottom: 1.5rem;">{selection}</h3>
            <div class="content-section">
                <div style="color: rgba(255,255,255,0.9);">
                    {content.get('content', '内容正在更新中...')}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
            
    def show_feedback(self):
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.markdown("## 💫 意见征集")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            with st.form("feedback_form"):
                feedback_type = st.selectbox(
                    "选择反馈类型",
                    list(self.guide.feedback_submenu.values())
                )
                
                feedback_text = st.text_area(
                    "分享您的想法",
                    height=200,
                    placeholder="您的意见对我们很重要..."
                )
                
                col_a, col_b = st.columns(2)
                with col_a:
                    name = st.text_input("昵称（选填）")
                with col_b:
                    contact = st.text_input("联系方式（选填）")
                
                submitted = st.form_submit_button("✨ 提交反馈")
                
                if submitted:
                    if feedback_text.strip():
                        with st.spinner('提交中...'):
                            # 保存反馈数据
                            feedback_data = {
                                'type': feedback_type,
                                'content': feedback_text,
                                'name': name or '匿名',
                                'contact': contact,
                            }
                            if self.api.save_feedback(feedback_data):
                                st.success("🎉 感谢您的反馈！")
                                st.balloons()
                            else:
                                st.error("保存失败，请稍后重试")
                    else:
                        st.error("❌ 请输入反馈内容")
        
        with col2:
            st.markdown("""
            <div class="glass-card">
                <h4>🌟 反馈指南</h4>
                <ul>
                    <li>清晰描述您的想法</li>
                    <li>可以附上截图说明</li>
                    <li>建议提供联系方式</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
    def show_recruitment(self):
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.markdown("## 🏢 工作室招募")
        
        st.warning("⚠️ 招募通道暂时关闭")
        
        st.markdown("""
        <div class="glass-card">
            <h4>✉️ 订阅招募通知</h4>
            <p>当有新的招募信息时，我们会第一时间通知您！</p>
        </div>
        """, unsafe_allow_html=True)
        
        email = st.text_input("邮箱地址")
        if st.button("🔔 订阅通知"):
            if email and '@' in email:
                with st.spinner('处理中...'):
                    if self.api.add_subscriber(email):
                        st.success("🎉 订阅成功！")
                    else:
                        st.info("您已经订阅过了")
            else:
                st.error("请输入有效的邮箱地址")

if __name__ == "__main__":
    web_guide = GameGuideWeb()
    web_guide.run()