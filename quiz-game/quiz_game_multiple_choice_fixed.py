#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
import random
import os
import copy

# Pygameの初期化
pygame.init()

# 画面設定
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("雑学クイズゲーム")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (200, 230, 255)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (255, 200, 200)
LIGHT_YELLOW = (255, 255, 200)
GRAY = (200, 200, 200)
DARK_BLUE = (0, 0, 128)

# フォント設定
font_path = None
# 一般的な日本語フォントのパスを確認
possible_font_paths = [
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf",
    "/usr/share/fonts/truetype/ipafont/ipag.ttf",
    "/usr/share/fonts/truetype/ipafont/ipam.ttf",
    "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf"
]

for path in possible_font_paths:
    if os.path.exists(path):
        font_path = path
        break

try:
    if font_path:
        title_font = pygame.font.Font(font_path, 60)
        question_font = pygame.font.Font(font_path, 36)
        option_font = pygame.font.Font(font_path, 28)
        button_font = pygame.font.Font(font_path, 32)
        score_font = pygame.font.Font(font_path, 28)
    else:
        # フォントが見つからない場合はシステムフォントを使用
        title_font = pygame.font.SysFont("notosanscjkjp", 60)
        question_font = pygame.font.SysFont("notosanscjkjp", 36)
        option_font = pygame.font.SysFont("notosanscjkjp", 28)
        button_font = pygame.font.SysFont("notosanscjkjp", 32)
        score_font = pygame.font.SysFont("notosanscjkjp", 28)
except:
    # それでもダメな場合はデフォルトフォントを使用
    title_font = pygame.font.SysFont(None, 60)
    question_font = pygame.font.SysFont(None, 36)
    option_font = pygame.font.SysFont(None, 28)
    button_font = pygame.font.SysFont(None, 32)
    score_font = pygame.font.SysFont(None, 28)

# クイズデータ
all_questions = [
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
    }
]

# 使用済み問題を記録するグローバル変数
used_question_indices = set()

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.selected = False
        
    def draw(self, surface):
        # 選択されている場合は別の色を使用
        if self.selected:
            color = DARK_BLUE
        else:
            color = self.hover_color if self.is_hovered else self.color
            
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)
        
        text_surface = option_font.render(self.text, True, WHITE if self.selected else BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

class QuizGame:
    def __init__(self):
        global used_question_indices
        
        # 問題をシャッフルして選択
        available_indices = [i for i in range(len(all_questions)) if i not in used_question_indices]
        
        # 全ての問題を使い切った場合はリセット
        if len(available_indices) < 10:
            used_question_indices = set()
            available_indices = list(range(len(all_questions)))
        
        # ランダムに10問を選択
        selected_indices = random.sample(available_indices, min(10, len(available_indices)))
        
        # 選択した問題を使用済みとしてマーク
        used_question_indices.update(selected_indices)
        
        # 選択した問題を取得
        self.questions = [copy.deepcopy(all_questions[i]) for i in selected_indices]
        
        self.current_question = 0
        self.score = 0
        self.total_questions = len(self.questions)
        self.state = "question"  # question, correct, incorrect, result
        
        # 選択肢ボタンの初期化
        self.option_buttons = []
        self.initialize_options()
        
        # 次へボタンとリスタートボタン
        self.next_button = Button(WIDTH//2 - 100, HEIGHT - 100, 200, 50, "次の問題へ", GREEN, LIGHT_GREEN)
        self.restart_button = Button(WIDTH//2 - 100, HEIGHT//2 + 100, 200, 50, "もう一度プレイ", BLUE, LIGHT_BLUE)
        self.quit_button = Button(WIDTH//2 - 100, HEIGHT//2 + 170, 200, 50, "終了", RED, LIGHT_RED)
        
        self.selected_option = None
        self.correct_answer = None
        
    def initialize_options(self):
        # 現在の問題の選択肢をシャッフル
        if self.current_question < len(self.questions):
            options = self.questions[self.current_question]["options"].copy()
            random.shuffle(options)
            
            # 選択肢ボタンを作成
            self.option_buttons = []
            for i, option in enumerate(options):
                y_pos = 350 + i * 80
                button = Button(WIDTH//2 - 200, y_pos, 400, 60, option, LIGHT_BLUE, BLUE)
                self.option_buttons.append(button)
                
            # 正解を記録
            self.correct_answer = self.questions[self.current_question]["correct"]
        
    def handle_events(self, events):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in events:
            if event.type == pygame.QUIT:
                return "quit"
                
            if self.state == "question":
                # 選択肢ボタンのホバー状態を更新
                for button in self.option_buttons:
                    button.check_hover(mouse_pos)
                    
                    # ボタンがクリックされたら回答を処理
                    if button.is_clicked(mouse_pos, event):
                        self.selected_option = button.text
                        
                        # 全てのボタンの選択状態をリセット
                        for b in self.option_buttons:
                            b.selected = False
                        
                        # クリックされたボタンを選択状態にする
                        button.selected = True
                        
                        # 正解かどうかをチェック
                        if self.selected_option == self.correct_answer:
                            self.score += 1
                            self.state = "correct"
                        else:
                            self.state = "incorrect"
            
            elif self.state in ["correct", "incorrect"]:
                self.next_button.check_hover(mouse_pos)
                if self.next_button.is_clicked(mouse_pos, event):
                    self.current_question += 1
                    if self.current_question >= self.total_questions:
                        self.state = "result"
                    else:
                        self.state = "question"
                        self.selected_option = None
                        self.initialize_options()
            
            elif self.state == "result":
                self.restart_button.check_hover(mouse_pos)
                self.quit_button.check_hover(mouse_pos)
                
                if self.restart_button.is_clicked(mouse_pos, event):
                    self.__init__()  # ゲームをリセット
                    return "continue"
                
                if self.quit_button.is_clicked(mouse_pos, event):
                    return "quit"
        
        return "continue"
    
    def draw(self, surface):
        surface.fill(WHITE)
        
        # 背景に簡単な装飾を追加（透明度を下げて控えめに）
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.circle(s, (*LIGHT_BLUE, 128), (100, 100), 80)
        pygame.draw.circle(s, (*LIGHT_GREEN, 128), (WIDTH-100, 200), 120)
        pygame.draw.circle(s, (*LIGHT_YELLOW, 128), (200, HEIGHT-100), 100)
        pygame.draw.circle(s, (*LIGHT_RED, 128), (WIDTH-150, HEIGHT-150), 70)
        surface.blit(s, (0, 0))
        
        # タイトルを描画
        title = title_font.render("雑学クイズゲーム", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH//2, 70))
        surface.blit(title, title_rect)
        
        # スコアを描画
        score_text = score_font.render(f"スコア: {self.score}/{self.current_question}", True, BLACK)
        score_rect = score_text.get_rect(topright=(WIDTH - 50, 30))
        surface.blit(score_text, score_rect)
        
        if self.state == "question":
            # 問題パネルの背景
            panel_rect = pygame.Rect(80, 130, WIDTH-160, 180)
            pygame.draw.rect(surface, LIGHT_BLUE, panel_rect, border_radius=15)
            pygame.draw.rect(surface, BLACK, panel_rect, 2, border_radius=15)
            
            # 問題番号を描画
            q_num = question_font.render(f"問題 {self.current_question + 1}/{self.total_questions}", True, BLACK)
            q_num_rect = q_num.get_rect(topleft=(100, 150))
            surface.blit(q_num, q_num_rect)
            
            # 問題文を描画（長い場合は折り返す）
            question_text = self.questions[self.current_question]["question"]
            
            # 日本語テキストの場合は文字単位で折り返す
            chars = list(question_text)
            lines = []
            current_line = ""
            max_width = WIDTH - 200  # 余白を確保
            
            for char in chars:
                test_line = current_line + char
                if question_font.size(test_line)[0] < max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = char
            
            if current_line:
                lines.append(current_line)
            
            # 問題文を中央に配置
            y_offset = 200
            for i, line in enumerate(lines):
                q_line = question_font.render(line, True, BLACK)
                q_line_rect = q_line.get_rect(center=(WIDTH//2, y_offset + i * 40))
                surface.blit(q_line, q_line_rect)
            
            # 選択肢ラベルを描画
            options_label = question_font.render("以下から選択してください:", True, BLACK)
            options_label_rect = options_label.get_rect(center=(WIDTH//2, 320))
            surface.blit(options_label, options_label_rect)
            
            # 選択肢ボタンを描画
            for button in self.option_buttons:
                button.draw(surface)
            
        elif self.state == "correct":
            # 正解パネルの背景
            result_rect = pygame.Rect(100, HEIGHT//2 - 200, WIDTH-200, 300)
            pygame.draw.rect(surface, LIGHT_GREEN, result_rect, border_radius=20)
            pygame.draw.rect(surface, BLACK, result_rect, 2, border_radius=20)
            
            # 正解メッセージ
            result = question_font.render("正解です！", True, GREEN)
            result_rect = result.get_rect(center=(WIDTH//2, HEIGHT//2 - 130))
            surface.blit(result, result_rect)
            
            # 問題文を表示
            question_text = self.questions[self.current_question]["question"]
            q_text = question_font.render(question_text, True, BLACK)
            q_rect = q_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
            surface.blit(q_text, q_rect)
            
            # 正解の表示
            answer = question_font.render(f"答え: {self.correct_answer}", True, BLACK)
            answer_rect = answer.get_rect(center=(WIDTH//2, HEIGHT//2 - 30))
            surface.blit(answer, answer_rect)
            
            # 次へボタンを描画
            self.next_button.draw(surface)
            
        elif self.state == "incorrect":
            # 不正解パネルの背景
            result_rect = pygame.Rect(100, HEIGHT//2 - 200, WIDTH-200, 300)
            pygame.draw.rect(surface, LIGHT_RED, result_rect, border_radius=20)
            pygame.draw.rect(surface, BLACK, result_rect, 2, border_radius=20)
            
            # 不正解メッセージ
            result = question_font.render("不正解です", True, RED)
            result_rect = result.get_rect(center=(WIDTH//2, HEIGHT//2 - 130))
            surface.blit(result, result_rect)
            
            # 問題文を表示
            question_text = self.questions[self.current_question]["question"]
            q_text = question_font.render(question_text, True, BLACK)
            q_rect = q_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
            surface.blit(q_text, q_rect)
            
            # 正解の表示
            answer = question_font.render(f"正解: {self.correct_answer}", True, BLACK)
            answer_rect = answer.get_rect(center=(WIDTH//2, HEIGHT//2 - 30))
            surface.blit(answer, answer_rect)
            
            # あなたの回答の表示
            your_answer = question_font.render(f"あなたの回答: {self.selected_option}", True, BLACK)
            your_answer_rect = your_answer.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
            surface.blit(your_answer, your_answer_rect)
            
            # 次へボタンを描画
            self.next_button.draw(surface)
            
        elif self.state == "result":
            # 結果パネルの背景
            result_rect = pygame.Rect(100, HEIGHT//2 - 220, WIDTH-200, 400)
            pygame.draw.rect(surface, LIGHT_BLUE, result_rect, border_radius=20)
            pygame.draw.rect(surface, BLACK, result_rect, 2, border_radius=20)
            
            # 結果タイトル
            result_title = title_font.render("クイズ終了！", True, BLACK)
            result_title_rect = result_title.get_rect(center=(WIDTH//2, HEIGHT//2 - 150))
            surface.blit(result_title, result_title_rect)
            
            # 最終スコア
            final_score = question_font.render(f"あなたの最終スコア: {self.score}/{self.total_questions}", True, BLACK)
            final_score_rect = final_score.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
            surface.blit(final_score, final_score_rect)
            
            # 成績評価
            if self.score == self.total_questions:
                evaluation = question_font.render("素晴らしい！全問正解です！", True, GREEN)
            elif self.score >= self.total_questions * 0.7:
                evaluation = question_font.render("よくできました！", True, GREEN)
            elif self.score >= self.total_questions * 0.4:
                evaluation = question_font.render("まずまずの成績です。", True, BLUE)
            else:
                evaluation = question_font.render("もう少し頑張りましょう！", True, RED)
            
            evaluation_rect = evaluation.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
            surface.blit(evaluation, evaluation_rect)
            
            # ボタンを描画
            self.restart_button.draw(surface)
            self.quit_button.draw(surface)

# メインループ
def main():
    clock = pygame.time.Clock()
    game = QuizGame()
    
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        result = game.handle_events(events)
        if result == "quit":
            running = False
        
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
