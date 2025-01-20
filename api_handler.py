import json
import os
from datetime import datetime

class APIHandler:
    def __init__(self):
        # 创建数据存储目录
        self.data_dir = "data"
        self.feedback_file = os.path.join(self.data_dir, "feedback.json")
        self.subscribers_file = os.path.join(self.data_dir, "subscribers.json")
        self._init_data_files()
    
    def _init_data_files(self):
        """初始化数据文件"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        # 初始化反馈数据文件
        if not os.path.exists(self.feedback_file):
            self._save_json(self.feedback_file, [])
        
        # 初始化订阅者数据文件
        if not os.path.exists(self.subscribers_file):
            self._save_json(self.subscribers_file, [])
    
    def _save_json(self, file_path, data):
        """保存JSON数据"""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def _load_json(self, file_path):
        """加载JSON数据"""
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save_feedback(self, feedback_data):
        """保存用户反馈"""
        feedback_list = self._load_json(self.feedback_file)
        feedback_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        feedback_list.append(feedback_data)
        self._save_json(self.feedback_file, feedback_list)
        return True
    
    def add_subscriber(self, email):
        """添加订阅者"""
        subscribers = self._load_json(self.subscribers_file)
        if email not in subscribers:
            subscribers.append({
                'email': email,
                'subscribed_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            self._save_json(self.subscribers_file, subscribers)
            return True
        return False
    
    def get_game_content(self, section):
        """获取游戏内容"""
        from game_content import GAME_CONTENT
        return GAME_CONTENT.get(section, {}) 