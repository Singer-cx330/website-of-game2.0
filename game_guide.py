class GameGuide:
    def __init__(self):
        self.main_menu = {
            1: "游戏攻略",
            2: "意见征集",
            3: "工作室招募(暂时关闭)"
        }
        
        self.game_guide_submenu = {
            1: "游戏介绍",
            2: "职业状态",
            3: "梦灵",
            4: "基础属性介绍",
            5: "性格",
            6: "怪物BOSS",
            7: "装备",
            8: "饰品",
            9: "阵容推荐",
            10: "版本更新",
            11: "制作人列表"
        }
        
        self.feedback_submenu = {
            1: "职业意见",
            2: "装备意见",
            3: "怪物意见",
            4: "BOSS意见",
            5: "梦灵意见",
            6: "饰品意见"
        }

    def display_menu(self, menu_items):
        for key, value in menu_items.items():
            print(f"{key}. {value}")

    def main(self):
        while True:
            print("\n=== 游戏指引系统 ===")
            self.display_menu(self.main_menu)
            choice = input("\n请选择功能 (输入q退出): ")
            
            if choice.lower() == 'q':
                break
                
            try:
                choice = int(choice)
                if choice == 1:
                    self.game_guide_section()
                elif choice == 2:
                    self.feedback_section()
                elif choice == 3:
                    print("\n工作室招募功能暂时关闭")
                else:
                    print("\n无效选择，请重试")
            except ValueError:
                print("\n请输入有效的数字")

    def game_guide_section(self):
        while True:
            print("\n=== 游戏攻略 ===")
            self.display_menu(self.game_guide_submenu)
            choice = input("\n请选择内容 (输入b返回): ")
            
            if choice.lower() == 'b':
                break
                
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.game_guide_submenu):
                    print(f"\n显示{self.game_guide_submenu[choice]}的内容...")
                    # 这里可以添加具体内容的显示逻辑
                else:
                    print("\n无效选择，请重试")
            except ValueError:
                print("\n请输入有效的数字")

    def feedback_section(self):
        while True:
            print("\n=== 意见征集 ===")
            self.display_menu(self.feedback_submenu)
            choice = input("\n请选择内容 (输入b返回): ")
            
            if choice.lower() == 'b':
                break
                
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.feedback_submenu):
                    feedback = input(f"\n请输入您对{self.feedback_submenu[choice]}的意见: ")
                    print("\n感谢您的反馈！")
                else:
                    print("\n无效选择，请重试")
            except ValueError:
                print("\n请输入有效的数字")

if __name__ == "__main__":
    guide = GameGuide()
    guide.main() 