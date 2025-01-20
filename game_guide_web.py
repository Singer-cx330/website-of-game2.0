import streamlit as st
from game_guide import GameGuide

class GameGuideWeb:
    def __init__(self):
        self.guide = GameGuide()
        
    def run(self):
        st.set_page_config(
            page_title="游戏指引系统",
            page_icon="🎮",
            layout="wide"
        )
        
        st.title("🎮 游戏指引系统")
        
        # 侧边栏导航
        with st.sidebar:
            st.header("主菜单")
            selection = st.radio(
                "选择功能",
                list(self.guide.main_menu.values())
            )
        
        # 主要内容区域
        if selection == "游戏攻略":
            self.show_game_guide()
        elif selection == "意见征集":
            self.show_feedback()
        else:
            st.warning("⚠️ 工作室招募功能暂时关闭")
            
    def show_game_guide(self):
        st.header("游戏攻略")
        
        guide_selection = st.selectbox(
            "选择攻略内容",
            list(self.guide.game_guide_submenu.values())
        )
        
        # 这里可以根据不同的选项显示具体内容
        if guide_selection == "游戏介绍":
            st.subheader("游戏介绍")
            st.write("这里是游戏的详细介绍...")
            
        elif guide_selection == "职业状态":
            st.subheader("职业状态")
            col1, col2 = st.columns(2)
            with col1:
                st.write("战士职业特点...")
            with col2:
                st.write("法师职业特点...")
                
        elif guide_selection == "梦灵":
            st.subheader("梦灵系统")
            st.write("梦灵相关内容...")
            
        # 可以继续添加其他选项的内容...
            
    def show_feedback(self):
        st.header("意见征集")
        
        feedback_type = st.selectbox(
            "选择反馈类型",
            list(self.guide.feedback_submenu.values())
        )
        
        feedback_text = st.text_area(
            f"请输入您对{feedback_type}的意见",
            height=200
        )
        
        if st.button("提交反馈"):
            if feedback_text.strip():
                # 这里可以添加保存反馈的逻辑
                st.success("感谢您的反馈！")
                
                # 示例：将反馈保存到文件
                with open("feedback.txt", "a", encoding="utf-8") as f:
                    f.write(f"\n类型: {feedback_type}\n")
                    f.write(f"内容: {feedback_text}\n")
                    f.write("-" * 50 + "\n")
            else:
                st.error("请输入反馈内容")

if __name__ == "__main__":
    web_guide = GameGuideWeb()
    web_guide.run() 