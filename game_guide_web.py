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
        
        /* 动态深蓝渐变背景 */
        .stApp {
            background: 
                linear-gradient(45deg, 
                    rgba(15, 23, 42, 0.95),   /* 深邃蓝 */
                    rgba(23, 37, 84, 0.95),   /* 靛蓝 */
                    rgba(30, 58, 138, 0.95)), /* 皇家蓝 */
                linear-gradient(135deg,
                    rgba(17, 24, 39, 0.97),   /* 暗蓝 */
                    rgba(29, 78, 216, 0.97));  /* 亮蓝 */
            background-size: 400% 400%, 300% 300%;
            animation: gradientBG 15s ease infinite;
        }
        
        @keyframes gradientBG {
            0% {
                background-position: 0% 50%, 100% 50%;
            }
            25% {
                background-position: 50% 100%, 50% 0%;
            }
            50% {
                background-position: 100% 50%, 0% 50%;
            }
            75% {
                background-position: 50% 0%, 50% 100%;
            }
            100% {
                background-position: 0% 50%, 100% 50%;
            }
        }
        
        /* 动态光效 */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 30%,
                    rgba(59, 130, 246, 0.1) 0%,
                    transparent 50%),
                radial-gradient(circle at 80% 70%,
                    rgba(37, 99, 235, 0.1) 0%,
                    transparent 50%);
            animation: lightEffect 20s ease-in-out infinite alternate;
        }
        
        @keyframes lightEffect {
            0% {
                opacity: 0.5;
                transform: scale(1);
            }
            50% {
                opacity: 0.8;
                transform: scale(1.2);
            }
            100% {
                opacity: 0.5;
                transform: scale(1);
            }
        }
        
        /* 动态玻璃卡片 */
        .glass-card {
            background: rgba(23, 37, 84, 0.4);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 24px;
            padding: 25px;
            margin: 15px 0;
            position: relative;
            overflow: hidden;
        }
        
        .glass-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(
                circle,
                rgba(59, 130, 246, 0.1) 0%,
                transparent 60%
            );
            animation: cardLight 8s ease-in-out infinite;
        }
        
        @keyframes cardLight {
            0% {
                transform: translate(-30%, -30%) rotate(0deg);
            }
            50% {
                transform: translate(30%, 30%) rotate(180deg);
            }
            100% {
                transform: translate(-30%, -30%) rotate(360deg);
            }
        }
        
        /* 炫彩文字效果 */
        .rainbow-text {
            background: linear-gradient(
                to right,
                #3b82f6,  /* 亮蓝色 */
                #60a5fa,  /* 天蓝色 */
                #93c5fd,  /* 浅蓝色 */
                #2563eb   /* 深蓝色 */
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
        
        /* 按钮样式 */
        .stButton > button {
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);  /* 蓝色渐变 */
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
        
        .stButton > button::before {
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
        
        .stButton > button:hover::before {
            left: 100%;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
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
        
        /* 滚动条样式 */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(23, 37, 84, 0.3);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(45deg, #3b82f6, #1d4ed8);
            border-radius: 4px;
            transition: all 0.3s ease;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(45deg, #a777e3, #6e8efb);
        }
        
        /* 输入框样式 */
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {
            background: rgba(23, 37, 84, 0.3);
            border: 1px solid rgba(59, 130, 246, 0.2);
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
        
        /* 标签页样式 */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background: rgba(23, 37, 84, 0.3);
            padding: 10px;
            border-radius: 50px;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: 50px;
            color: rgba(255, 255, 255, 0.7);
            padding: 10px 20px;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: rgba(59, 130, 246, 0.3);
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
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            border: none;
            border-radius: 50px;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
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
            background: rgba(30, 41, 59, 0.3);
            padding: 20px;
            border-radius: 15px;
            margin-top: 2rem;
        }
        
        .glass-card {
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            border: 1px solid rgba(78, 91, 112, 0.2);
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
        .shooting-stars {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }
        
        .shooting-star {
            position: absolute;
            width: 100px;
            height: 2px;
            background: linear-gradient(90deg, 
                rgba(59, 130, 246, 0.8), 
                rgba(37, 99, 235, 0.4), 
                transparent);
            animation: shootingStars 3s linear infinite;
        }
        
        @keyframes shootingStars {
            0% {
                transform: translateX(-100%) translateY(0) rotate(-45deg);
                opacity: 1;
            }
            100% {
                transform: translateX(200%) translateY(300%) rotate(-45deg);
                opacity: 0;
            }
        }
        
        /* 气泡效果 */
        .bubbles {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        }
        
        .bubble {
            position: absolute;
            background: radial-gradient(
                circle at 50% 50%,
                rgba(59, 130, 246, 0.2),
                rgba(37, 99, 235, 0.1)
            );
            border-radius: 50%;
            animation: floatBubble linear infinite;
        }
        
        @keyframes floatBubble {
            0% {
                transform: translateY(100vh) scale(0);
                opacity: 0;
            }
            50% {
                opacity: 0.5;
            }
            100% {
                transform: translateY(-100px) scale(1);
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
        
        /* 侧边栏样式 */
        .sidebar .sidebar-content {
            background: linear-gradient(
                180deg,
                rgba(15, 23, 42, 0.95),
                rgba(23, 37, 84, 0.95)
            );
            border-right: 1px solid rgba(59, 130, 246, 0.2);
            backdrop-filter: blur(10px);
        }
        
        .sidebar .sidebar-content > div {
            background: transparent !important;
        }
        
        /* 文字颜色 */
        p, li {
            color: rgba(226, 232, 240, 0.85);  /* 浅灰蓝色文字 */
        }
        
        h1, h2, h3, h4 {
            color: rgba(241, 245, 249, 0.95);  /* 近白色标题 */
        }
        
        /* 导航菜单项样式 */
        .stRadio > label {
            background: rgba(30, 58, 138, 0.3);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 10px;
            padding: 10px 15px;
            margin: 5px 0;
            transition: all 0.3s ease;
        }
        
        .stRadio > label:hover {
            background: rgba(30, 58, 138, 0.5);
            transform: translateX(5px);
        }
        
        /* 状态卡片样式 */
        .status-card {
            transition: all 0.3s ease;
            margin: 10px 0;
        }
        
        .status-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }
        
        .status-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
        }
        
        .status-icon {
            font-size: 1.5em;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: rgba(59, 130, 246, 0.1);
            border-radius: 50%;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }
        
        .status-desc {
            color: rgba(255, 255, 255, 0.8);
            margin: 0;
            font-size: 0.9em;
            line-height: 1.5;
        }
        
        .attribute-card {
            background: rgba(30, 58, 138, 0.4);
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 20px;
            text-align: center;
            border: 1px solid rgba(59, 130, 246, 0.3);
        }
        
        /* 导航菜单图标动画 */
        .sidebar .sidebar-content img,
        .sidebar .sidebar-content svg {
            transition: transform 0.3s ease;
        }
        
        .sidebar .sidebar-content img:hover,
        .sidebar .sidebar-content svg:hover {
            transform: scale(1.1);
        }
        
        /* 选中状态样式 */
        .stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {
            background-color: rgba(59, 130, 246, 0.3);
            border-color: rgba(59, 130, 246, 0.5);
        }
        
        .stRadio > div[role="radiogroup"] > label[data-baseweb="radio"][aria-checked="true"] {
            background: rgba(59, 130, 246, 0.2);
            border-color: rgba(59, 130, 246, 0.5);
            transform: translateX(10px);
        }
        
        /* 侧边栏头部样式 */
        .sidebar-header {
            text-align: center;
            padding: 2rem 1rem;
            margin-bottom: 2rem;
            border-bottom: 1px solid rgba(59, 130, 246, 0.2);
            background: rgba(30, 58, 138, 0.3);
        }
        
        .sidebar-header h2 {
            color: white;
            margin-top: 1rem;
            font-size: 1.5rem;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        /* 脉冲logo动画 */
        .logo-pulse {
            width: 80px;
            height: 80px;
            margin: 0 auto;
            background: linear-gradient(45deg, #3b82f6, #1d4ed8);
            border-radius: 50%;
            position: relative;
            animation: pulse 2s infinite;
        }
        
        .logo-pulse::before {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            background: inherit;
            border-radius: inherit;
            animation: pulse-ring 2s infinite;
        }
        
        @keyframes pulse {
            0% {
                transform: scale(0.95);
            }
            50% {
                transform: scale(1);
            }
            100% {
                transform: scale(0.95);
            }
        }
        
        @keyframes pulse-ring {
            0% {
                transform: scale(1);
                opacity: 0.8;
            }
            100% {
                transform: scale(1.5);
                opacity: 0;
            }
        }
        
        /* 导航菜单项样式 */
        .sidebar .sidebar-content [data-testid="stRadio"] > div {
            padding: 0.5rem;
        }
        
        .sidebar .sidebar-content [data-testid="stRadio"] label {
            background: rgba(30, 58, 138, 0.2);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 12px;
            padding: 1rem;
            margin: 0.5rem 0;
            transition: all 0.3s ease;
            cursor: pointer;
            display: flex;
            align-items: center;
        }
        
        .sidebar .sidebar-content [data-testid="stRadio"] label:hover {
            background: rgba(30, 58, 138, 0.4);
            transform: translateX(5px);
            border-color: rgba(59, 130, 246, 0.4);
        }
        
        /* 选中状态样式 */
        .sidebar .sidebar-content [data-testid="stRadio"] label[data-checked="true"] {
            background: rgba(59, 130, 246, 0.3);
            border-color: rgba(59, 130, 246, 0.6);
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.2);
        }
        
        /* 菜单图标样式 */
        .sidebar .sidebar-content [data-testid="stRadio"] label span {
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        /* 分割线样式 */
        .sidebar .sidebar-content hr {
            border-color: rgba(59, 130, 246, 0.2);
            margin: 2rem 0;
        }
        
        /* 滚动条样式 */
        .sidebar .sidebar-content::-webkit-scrollbar {
            width: 6px;
        }
        
        .sidebar .sidebar-content::-webkit-scrollbar-track {
            background: rgba(30, 58, 138, 0.1);
        }
        
        .sidebar .sidebar-content::-webkit-scrollbar-thumb {
            background: rgba(59, 130, 246, 0.3);
            border-radius: 3px;
        }
        
        .sidebar .sidebar-content::-webkit-scrollbar-thumb:hover {
            background: rgba(59, 130, 246, 0.5);
        }
        
        /* 导航菜单容器 */
        .nav-menu {
            padding: 1rem;
            margin-top: 1rem;
        }
        
        .nav-menu-items {
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
        }
        
        /* 导航菜单项 */
        .nav-item {
            display: flex;
            align-items: center;
            padding: 1rem 1.2rem;
            background: rgba(30, 58, 138, 0.2);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 12px;
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .nav-item:hover {
            background: rgba(30, 58, 138, 0.4);
            transform: translateX(5px);
            border-color: rgba(59, 130, 246, 0.4);
            color: white;
        }
        
        .nav-item.active {
            background: rgba(59, 130, 246, 0.3);
            border-color: rgba(59, 130, 246, 0.6);
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.2);
            color: white;
        }
        
        /* 导航图标 */
        .nav-icon {
            font-size: 1.2rem;
            margin-right: 0.8rem;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 2rem;
            height: 2rem;
            background: rgba(59, 130, 246, 0.1);
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        .nav-item:hover .nav-icon {
            background: rgba(59, 130, 246, 0.2);
            transform: scale(1.1);
        }
        
        /* 导航文字 */
        .nav-text {
            font-size: 1rem;
            font-weight: 500;
        }
        
        /* 移除原有的标题样式 */
        .sidebar .sidebar-content [data-testid="stMarkdown"] h3 {
            display: none;
        }
        
        /* 优化侧边栏整体样式 */
        .sidebar .sidebar-content {
            background: linear-gradient(
                180deg,
                rgba(15, 23, 42, 0.95),
                rgba(23, 37, 84, 0.95)
            );
            border-right: 1px solid rgba(59, 130, 246, 0.2);
            backdrop-filter: blur(10px);
        }
        
        /* 优化滚动条 */
        .sidebar .sidebar-content::-webkit-scrollbar {
            width: 6px;
        }
        
        .sidebar .sidebar-content::-webkit-scrollbar-track {
            background: rgba(30, 58, 138, 0.1);
        }
        
        .sidebar .sidebar-content::-webkit-scrollbar-thumb {
            background: rgba(59, 130, 246, 0.3);
            border-radius: 3px;
        }
        
        .sidebar .sidebar-content::-webkit-scrollbar-thumb:hover {
            background: rgba(59, 130, 246, 0.5);
        }
        
        /* 页面标题样式 */
        .page-header {
            text-align: center;
            margin-bottom: 2rem;
            padding: 2rem;
            background: rgba(30, 58, 138, 0.2);
            border-radius: 16px;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }
        
        .page-header h2 {
            color: white;
            margin-bottom: 0.5rem;
        }
        
        .page-header p {
            color: rgba(255, 255, 255, 0.8);
            font-size: 1.1rem;
        }
        
        /* 表单样式 */
        [data-testid="stForm"] {
            background: rgba(30, 58, 138, 0.2);
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }
        
        .stTextInput input, .stTextArea textarea {
            background: rgba(23, 37, 84, 0.3) !important;
            border: 1px solid rgba(59, 130, 246, 0.2) !important;
            color: white !important;
        }
        
        .stSelectbox [data-baseweb="select"] {
            background: rgba(23, 37, 84, 0.3) !important;
            border: 1px solid rgba(59, 130, 246, 0.2) !important;
        }
        
        /* 指南卡片样式 */
        .guide-card {
            height: 100%;
            padding: 1.5rem;
        }
        
        .guide-card h4 {
            color: white;
            margin-bottom: 1rem;
            border-bottom: 1px solid rgba(59, 130, 246, 0.2);
            padding-bottom: 0.5rem;
        }
        
        .guide-card ul {
            list-style: none;
            padding: 0;
            margin: 0 0 1.5rem 0;
        }
        
        .guide-card li {
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 0.5rem;
            padding-left: 1.5rem;
            position: relative;
        }
        
        .guide-card li:before {
            content: '•';
            color: #3b82f6;
            position: absolute;
            left: 0;
        }
        
        /* 提交按钮样式 */
        .stButton button {
            width: 100%;
            padding: 0.8rem !important;
            font-size: 1.1rem !important;
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        </style>
        
        <script>
        // 创建流星
        function createShootingStars() {
            const container = document.createElement('div');
            container.className = 'shooting-stars';
            document.body.appendChild(container);
            
            setInterval(() => {
                const star = document.createElement('div');
                star.className = 'shooting-star';
                star.style.top = Math.random() * 50 + 'vh';
                star.style.left = Math.random() * 100 + 'vw';
                container.appendChild(star);
                
                setTimeout(() => star.remove(), 3000);
            }, 2000);
        }
        
        // 创建气泡
        function createBubbles() {
            const container = document.createElement('div');
            container.className = 'bubbles';
            document.body.appendChild(container);
            
            setInterval(() => {
                const bubble = document.createElement('div');
                bubble.className = 'bubble';
                
                // 随机大小
                const size = Math.random() * 30 + 10;
                bubble.style.width = size + 'px';
                bubble.style.height = size + 'px';
                
                // 随机位置
                bubble.style.left = Math.random() * 100 + 'vw';
                
                // 随机动画时间
                const duration = Math.random() * 10 + 5;
                bubble.style.animation = `floatBubble ${duration}s linear infinite`;
                
                container.appendChild(bubble);
                setTimeout(() => bubble.remove(), duration * 1000);
            }, 500);
        }
        
        // 页面加载时初始化效果
        document.addEventListener('DOMContentLoaded', () => {
            createShootingStars();
            createBubbles();
        });
        
        // 添加导航菜单交互
        document.addEventListener('DOMContentLoaded', function() {
            const navItems = document.querySelectorAll('.nav-item');
            navItems.forEach(item => {
                item.addEventListener('click', function() {
                    navItems.forEach(i => i.classList.remove('active'));
                    this.classList.add('active');
                });
            });
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
                <div class="sidebar-header">
                    <div class="logo-pulse"></div>
                    <h2>✨ 梦幻指南</h2>
                </div>
                """, unsafe_allow_html=True)
                
                # 简单直接地使用 radio 按钮
                selection = st.radio(
                    "导航菜单",  # 添加标题
                    list(self.guide.main_menu.values()),
                    format_func=lambda x: {
                        "游戏攻略": "🎯 游戏攻略",
                        "意见征集": "💡 意见征集",
                        "工作室招募(暂时关闭)": "🏢 工作室招募"
                    }.get(x, x)
                )
                
                # 添加简单的样式
                st.markdown("""
                <style>
                .sidebar .sidebar-content {
                    background: linear-gradient(
                        180deg,
                        rgba(15, 23, 42, 0.95),
                        rgba(23, 37, 84, 0.95)
                    );
                }
                
                /* Radio按钮样式 */
                .stRadio > div {
                    background: rgba(30, 58, 138, 0.2);
                    padding: 1rem;
                    border-radius: 10px;
                }
                
                .stRadio > div > label {
                    background: rgba(30, 58, 138, 0.3);
                    border: 1px solid rgba(59, 130, 246, 0.2);
                    border-radius: 8px;
                    padding: 10px 15px;
                    margin: 5px 0;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
                
                .stRadio > div > label:hover {
                    background: rgba(59, 130, 246, 0.2);
                    transform: translateX(5px);
                }
                
                /* 选中状态 */
                .stRadio > div > label[data-checked="true"] {
                    background: rgba(59, 130, 246, 0.3);
                    border-color: rgba(59, 130, 246, 0.6);
                    box-shadow: 0 0 15px rgba(59, 130, 246, 0.2);
                }
                </style>
                """, unsafe_allow_html=True)
            
            # 主要内容区域
            if selection == "游戏攻略":
                self.show_game_guide()
            elif selection == "意见征集":
                self.show_feedback()
            else:
                self.show_recruitment()
            
    def show_game_guide(self):
        # 使用tabs来组织内容
        tabs = st.tabs([
            "🎮 基础指南", "⚔️ 职业系统", "💪 状态属性", "✨ 特色玩法", "📝 更新日志"
        ])
        
        with tabs[0]:
            col1, col2 = st.columns([3, 1])
            with col1:
                guide_selection = st.selectbox(
                    "选择指南内容",
                    list(self.guide.game_guide_submenu.values())
                )
        
        with st.spinner('加载中...'):
            time.sleep(0.3)
            self.show_guide_content(guide_selection)
        
        with tabs[1]:
            self.show_profession_content()
        
        with tabs[2]:
            self.show_status_content()

    def show_guide_content(self, selection):
        content = self.api.get_game_content(selection)
        st.markdown(f"""
        <div class="glass-card">
            <h3 style="color: white; margin-bottom: 1.5rem;">{selection}</h3>
            <div style="color: rgba(255,255,255,0.9);">
                {content.get('content', '内容正在更新中...')}
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_feedback(self):
        """显示意见征集页面"""
        st.markdown("""
        <div class="page-header">
            <h2>💡 意见征集</h2>
            <p>您的反馈对我们很重要，帮助我们打造更好的游戏体验！</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 创建两列布局
        col1, col2 = st.columns([2, 1])
        
        with col1:
            with st.form("feedback_form"):
                # 反馈类型选择
                feedback_type = st.selectbox(
                    "选择反馈类型",
                    list(self.guide.feedback_submenu.values()),
                    format_func=lambda x: {
                        "职业意见": "⚔️ 职业平衡",
                        "装备意见": "🛡️ 装备系统",
                        "怪物意见": "👾 怪物设计",
                        "BOSS意见": "👑 BOSS机制",
                        "梦灵意见": "✨ 梦灵系统",
                        "饰品意见": "💎 饰品系统"
                    }.get(x, x)
                )
                
                # 反馈内容
                feedback_text = st.text_area(
                    "详细描述",
                    height=200,
                    placeholder="请详细描述您的想法、建议或遇到的问题..."
                )
                
                # 联系方式（可选）
                contact = st.text_input(
                    "联系方式（选填）",
                    placeholder="QQ/微信/邮箱，方便我们与您进一步交流"
                )
                
                # 图片上传（可选）
                uploaded_file = st.file_uploader(
                    "上传截图（可选）",
                    type=['png', 'jpg', 'jpeg'],
                    help="支持PNG/JPG格式，大小不超过2MB"
                )
                
                # 提交按钮
                submit = st.form_submit_button("📮 提交反馈")
                
                if submit:
                    if feedback_text:
                        with st.spinner('正在提交...'):
                            feedback_data = {
                                'type': feedback_type,
                                'content': feedback_text,
                                'contact': contact,
                                'has_image': bool(uploaded_file)
                            }
                            if self.api.save_feedback(feedback_data):
                                st.success("🎉 感谢您的反馈！我们会认真考虑您的建议。")
                                st.balloons()
                    else:
                        st.error("请填写反馈内容")
        
        with col2:
            # 反馈指南
            st.markdown("### 📝 反馈指南")
            st.markdown("""
            • 请选择合适的反馈类型
            • 详细描述您的想法和建议
            • 可以附上截图以更好地说明问题
            • 留下联系方式以便我们进一步交流
            """)

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

    def show_profession_content(self):
        """显示职业系统内容"""
        content = self.api.get_game_content("职业系统")
        
        for profession, details in content.items():
            with st.expander(f"🎯 {profession}"):
                st.markdown(f"""
                <div class="glass-card">
                    <h4 style="color: white;">特点</h4>
                    <p>{details['特点']}</p>
                    
                    <h4 style="color: white;">技能</h4>
                    <ul>
                        {''.join(f'<li>{skill}</li>' for skill in details['技能'])}
                    </ul>
                    
                    <h4 style="color: white;">推荐装备</h4>
                    <ul>
                        {''.join(f'<li>{equip}</li>' for equip in details['装备推荐'])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

    def show_status_content(self):
        """显示状态属性内容"""
        content = self.api.get_game_content("状态属性")
        
        # 定义状态图标映射
        status_icons = {
            "生命值": "❤️",
            "魔法值": "🔮",
            "攻击力": "⚔️",
            "防御力": "🛡️",
            "眩晕": "💫",
            "中毒": "☠️",
            "虚弱": "😫",
            "加速": "⚡",
            "物理抗性": "🏰",
            "魔法抗性": "✨",
            "控制抗性": "🛑"
        }
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            st.markdown("""
            <div class="attribute-card">
                <h3 style="color: white;">基础属性</h3>
            </div>
            """, unsafe_allow_html=True)
            
            for attr, desc in content['基础属性'].items():
                st.markdown(f"""
                <div class="glass-card status-card">
                    <div class="status-header">
                        <span class="status-icon">{status_icons.get(attr, '🔹')}</span>
                        <h4 style="color: white; margin: 0;">{attr}</h4>
                    </div>
                    <p class="status-desc">{desc}</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="attribute-card">
                <h3 style="color: white;">特殊状态</h3>
            </div>
            """, unsafe_allow_html=True)
            
            for status, effect in content['特殊状态'].items():
                st.markdown(f"""
                <div class="glass-card status-card">
                    <div class="status-header">
                        <span class="status-icon">{status_icons.get(status, '🔸')}</span>
                        <h4 style="color: white; margin: 0;">{status}</h4>
                    </div>
                    <p class="status-desc">{effect}</p>
                </div>
                """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
            <div class="attribute-card">
                <h3 style="color: white;">抗性系统</h3>
            </div>
            """, unsafe_allow_html=True)
            
            for resistance, desc in content['抗性系统'].items():
                st.markdown(f"""
                <div class="glass-card status-card">
                    <div class="status-header">
                        <span class="status-icon">{status_icons.get(resistance, '🔰')}</span>
                        <h4 style="color: white; margin: 0;">{resistance}</h4>
                    </div>
                    <p class="status-desc">{desc}</p>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    web_guide = GameGuideWeb()
    web_guide.run()