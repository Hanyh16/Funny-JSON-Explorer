# 图标族管理
class IconFamily:
    def __init__(self, families):
        self.families = families

    def get_icons(self, family_type):
        if family_type == 'poker':
            return self.families[0]
        elif family_type == 'sun':
            return self.families[1]
        elif family_type == 'star':
            return self.families[2]
        elif family_type == 'king':
            return self.families[3]
        elif family_type == 'snow':
            return self.families[4]