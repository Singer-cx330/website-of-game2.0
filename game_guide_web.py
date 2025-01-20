import streamlit as st
from game_guide import GameGuide
from game_content import GAME_CONTENT
import time

class GameGuideWeb:
    def __init__(self):
        self.guide = GameGuide()
        
    def run(self):
        # 设置页面配置
        st.set_page_config(
            page_title="游戏指引系统",
            page_icon="🎮",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # 添加自定义CSS和JS效果
        st.markdown("""
        <style>
        /* 全局样式 */
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap');
        
        * {
            font-family: 'Noto Sans SC', sans-serif;
        }
        
        /* 渐变背景 */
        .stApp {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        }
        
        /* 卡片样式 */
        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        
        /* 动画按钮 */
        .stButton>button {
            background: linear-gradient(45deg, #2196F3, #00BCD4);
            border: none;
            border-radius: 25px;
            color: white;
            padding: 10px 25px;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(33, 150, 243, 0.4);
        }
        
        /* 标题动画 */
        @keyframes titleGlow {
            0% { text-shadow: 0 0 10px rgba(255,255,255,0.5); }
            50% { text-shadow: 0 0 20px rgba(255,255,255,0.8); }
            100% { text-shadow: 0 0 10px rgba(255,255,255,0.5); }
        }
        
        .title {
            color: white;
            animation: titleGlow 2s infinite;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 30px;
        }
        
        /* 导航菜单样式 */
        .nav-item {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            margin: 5px 0;
            padding: 10px;
            transition: all 0.3s ease;
        }
        
        .nav-item:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: scale(1.02);
        }
        
        /* 加载动画 */
        .loader {
            border: 4px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top: 4px solid #fff;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* 内容淡入效果 */
        .fade-in {
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
        
        <script>
        // 添加页面载入动画
        document.addEventListener('DOMContentLoaded', (event) => {
            document.body.classList.add('fade-in');
        });
        </script>
        """, unsafe_allow_html=True)
        
        # 显示加载动画
        with st.spinner('正在加载精彩内容...'):
            time.sleep(1)  # 模拟加载
            
        # 页面标题
        st.markdown('<h1 class="title">✨ 梦幻游戏指引 ✨</h1>', unsafe_allow_html=True)
        
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
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.markdown("## 🌟 游戏攻略")
        
        # 使用tabs来组织内容
        tabs = st.tabs([
            "🎮 基础指南", "⚔️ 职业系统", "✨ 特色玩法", "📝 更新日志"
        ])
        
        with tabs[0]:
            guide_selection = st.selectbox(
                "选择指南内容",
                list(self.guide.game_guide_submenu.values())
            )
            
            # 添加内容切换动画
            placeholder = st.empty()
            with st.spinner('加载中...'):
                time.sleep(0.5)
                with placeholder.container():
                    self.show_guide_content(guide_selection)
                    
    def show_guide_content(self, selection):
        st.markdown(f"""
        <div class="card">
            <h3>{selection}</h3>
            <div class="content">
                {GAME_CONTENT.get(selection, {}).get('content', '内容正在更新中...')}
            </div>
        </div>
        """, unsafe_allow_html=True)
            
    def show_feedback(self):
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        st.markdown("## 💫 意见征集")
        
        # 使用列来布局
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
                            time.sleep(1)
                            st.success("🎉 感谢您的反馈！")
                            st.balloons()
                    else:
                        st.error("❌ 请输入反馈内容")
        
        with col2:
            st.markdown("""
            <div class="card">
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
        
        # 添加订阅功能
        st.markdown("""
        <div class="card">
            <h4>✉️ 订阅招募通知</h4>
            <p>当有新的招募信息时，我们会第一时间通知您！</p>
        </div>
        """, unsafe_allow_html=True)
        
        email = st.text_input("邮箱地址")
        if st.button("🔔 订阅通知"):
            if email:
                with st.spinner('处理中...'):
                    time.sleep(1)
                    st.success("🎉 订阅成功！")
            else:
                st.error("请输入有效的邮箱地址")

if __name__ == "__main__":
    web_guide = GameGuideWeb()
    web_guide.run()