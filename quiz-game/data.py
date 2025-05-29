#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
データモジュール
クイズの問題データを管理します
"""

# クイズデータ
QUESTIONS = [
    {
        "question": "日本で一番高い山は何ですか？",
        "correct": "富士山",
        "options": ["富士山", "北岳", "奥穂高岳", "槍ヶ岳"]
    },
    {
        "question": "人間の体で一番大きな臓器は何ですか？",
        "correct": "肝臓",
        "options": ["肝臓", "心臓", "肺", "脳"]
    },
    {
        "question": "1年は何日ですか？",
        "correct": "365日",
        "options": ["365日", "364日", "366日", "360日"]
    },
    {
        "question": "世界で最も多く話されている言語は何ですか？",
        "correct": "中国語",
        "options": ["中国語", "英語", "スペイン語", "ヒンディー語"]
    },
    {
        "question": "水の化学式は何ですか？",
        "correct": "H2O",
        "options": ["H2O", "CO2", "O2", "H2O2"]
    },
    {
        "question": "太陽系で一番大きな惑星は何ですか？",
        "correct": "木星",
        "options": ["木星", "土星", "海王星", "地球"]
    },
    {
        "question": "人間の正常な体温は約何度ですか？",
        "correct": "36.5度",
        "options": ["36.5度", "37.5度", "35.5度", "38.5度"]
    },
    {
        "question": "DNAの二重らせん構造を発見した科学者は誰ですか？",
        "correct": "ワトソンとクリック",
        "options": ["ワトソンとクリック", "アインシュタイン", "ニュートン", "ダーウィン"]
    },
    {
        "question": "地球の表面の何パーセントが水で覆われていますか？",
        "correct": "約70%",
        "options": ["約70%", "約50%", "約60%", "約80%"]
    },
    {
        "question": "「モナリザ」を描いた芸術家は誰ですか？",
        "correct": "レオナルド・ダ・ヴィンチ",
        "options": ["レオナルド・ダ・ヴィンチ", "ミケランジェロ", "ラファエロ", "ゴッホ"]
    },
    {
        "question": "日本の首都は何ですか？",
        "correct": "東京",
        "options": ["東京", "大阪", "京都", "名古屋"]
    },
    {
        "question": "人間の心臓は1分間に約何回鼓動しますか？",
        "correct": "約70回",
        "options": ["約70回", "約50回", "約100回", "約120回"]
    },
    {
        "question": "世界で最も人口の多い国はどこですか？",
        "correct": "インド",
        "options": ["インド", "中国", "アメリカ", "インドネシア"]
    },
    {
        "question": "光の速さは秒速何キロメートルですか？",
        "correct": "約30万キロメートル",
        "options": ["約30万キロメートル", "約10万キロメートル", "約50万キロメートル", "約100万キロメートル"]
    },
    {
        "question": "人間の体の中で最も大きな骨は何ですか？",
        "correct": "大腿骨",
        "options": ["大腿骨", "頭蓋骨", "肩甲骨", "骨盤"]
    },
    {
        "question": "世界最大の海洋は何ですか？",
        "correct": "太平洋",
        "options": ["太平洋", "大西洋", "インド洋", "北極海"]
    },
    {
        "question": "人間の体の中で最も小さな骨は何ですか？",
        "correct": "アブミ骨",
        "options": ["アブミ骨", "指骨", "鼻骨", "尾骨"]
    },
    {
        "question": "地球から最も近い恒星は何ですか？",
        "correct": "太陽",
        "options": ["太陽", "プロキシマ・ケンタウリ", "シリウス", "アルファ・ケンタウリ"]
    },
    {
        "question": "人間の体の中で最も大きな筋肉は何ですか？",
        "correct": "大臀筋",
        "options": ["大臀筋", "大胸筋", "広背筋", "大腿四頭筋"]
    },
    {
        "question": "世界で最も長い川は何ですか？",
        "correct": "ナイル川",
        "options": ["ナイル川", "アマゾン川", "ミシシッピ川", "長江"]
    },
    # 追加問題
    {
        "question": "元素記号「Au」は何の元素を表しますか？",
        "correct": "金",
        "options": ["金", "銀", "銅", "鉄"]
    },
    {
        "question": "世界で最も面積が大きい国はどこですか？",
        "correct": "ロシア",
        "options": ["ロシア", "カナダ", "中国", "アメリカ"]
    },
    {
        "question": "人間の体の中で最も大きな器官は何ですか？",
        "correct": "皮膚",
        "options": ["皮膚", "肝臓", "肺", "腸"]
    },
    {
        "question": "「ハムレット」を書いた劇作家は誰ですか？",
        "correct": "シェイクスピア",
        "options": ["シェイクスピア", "トルストイ", "ゲーテ", "ヘミングウェイ"]
    },
    {
        "question": "地球の大気の主成分は何ですか？",
        "correct": "窒素",
        "options": ["窒素", "酸素", "二酸化炭素", "水素"]
    }
]

class QuestionManager:
    """問題管理クラス"""
    
    def __init__(self):
        """初期化"""
        self.used_indices = set()
        
    def get_questions(self, count):
        """指定数の問題をランダムに取得する"""
        import copy
        import random
        
        # 使用可能な問題のインデックスを取得
        available_indices = [i for i in range(len(QUESTIONS)) if i not in self.used_indices]
        
        # 全ての問題を使い切った場合はリセット
        if len(available_indices) < count:
            self.used_indices = set()
            available_indices = list(range(len(QUESTIONS)))
        
        # ランダムに問題を選択
        selected_indices = random.sample(available_indices, min(count, len(available_indices)))
        
        # 選択した問題を使用済みとしてマーク
        self.used_indices.update(selected_indices)
        
        # 選択した問題を取得（ディープコピー）
        return [copy.deepcopy(QUESTIONS[i]) for i in selected_indices]
