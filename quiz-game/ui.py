#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UIモジュール
ゲームのUI要素を管理します
"""

import pygame
from config import *

class Button:
    """ボタンクラス"""
    
    def __init__(self, x, y, width, height, text, color, hover_color):
        """初期化"""
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.selected = False
        
    def draw(self, surface, font):
        """ボタンを描画する"""
        # 選択されている場合は別の色を使用
        if self.selected:
            color = DARK_BLUE
        else:
            color = self.hover_color if self.is_hovered else self.color
            
        pygame.draw.rect(surface, color, self.rect, border_radius=BUTTON_RADIUS)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=BUTTON_RADIUS)
        
        text_surface = font.render(self.text, True, WHITE if self.selected else BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        """マウスホバー状態をチェックする"""
        self.is_hovered = self.rect.collidepoint(pos)
        
    def is_clicked(self, pos, event):
        """クリックされたかどうかをチェックする"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

class UIManager:
    """UI管理クラス"""
    
    def __init__(self, fonts):
        """初期化"""
        self.fonts = fonts
        
    def draw_background(self, surface):
        """背景を描画する"""
        surface.fill(WHITE)
        
        # 背景に装飾を追加（透明度を下げて控えめに）
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        for decoration in DECORATIONS:
            color_with_alpha = (*decoration["color"], decoration["alpha"])
            pygame.draw.circle(s, color_with_alpha, decoration["pos"], decoration["radius"])
        surface.blit(s, (0, 0))
        
    def draw_title(self, surface):
        """タイトルを描画する"""
        title = self.fonts["title"].render(TITLE, True, BLACK)
        title_rect = title.get_rect(center=(WIDTH//2, TITLE_Y))
        surface.blit(title, title_rect)
        
    def draw_score(self, surface, score, current_question):
        """スコアを描画する"""
        score_text = self.fonts["score"].render(f"スコア: {score}/{current_question}", True, BLACK)
        score_rect = score_text.get_rect(topright=(WIDTH - SCORE_X_OFFSET, 30))
        surface.blit(score_text, score_rect)
        
    def draw_question_panel(self, surface, question_number, total_questions, question_text):
        """問題パネルを描画する"""
        # パネルの背景
        panel_rect = pygame.Rect(80, QUESTION_PANEL_Y, WIDTH-160, QUESTION_PANEL_HEIGHT)
        pygame.draw.rect(surface, LIGHT_BLUE, panel_rect, border_radius=PANEL_RADIUS)
        pygame.draw.rect(surface, BLACK, panel_rect, 2, border_radius=PANEL_RADIUS)
        
        # 問題番号を描画
        q_num = self.fonts["question"].render(f"問題 {question_number + 1}/{total_questions}", True, BLACK)
        q_num_rect = q_num.get_rect(topleft=(QUESTION_NUMBER_X, QUESTION_NUMBER_Y))
        surface.blit(q_num, q_num_rect)
        
        # 問題文を描画（長い場合は折り返す）
        self.draw_wrapped_text(surface, question_text, WIDTH//2, QUESTION_Y_OFFSET, self.fonts["question"], BLACK)
        
    def draw_options_label(self, surface):
        """選択肢ラベルを描画する"""
        options_label = self.fonts["question"].render("以下から選択してください:", True, BLACK)
        options_label_rect = options_label.get_rect(center=(WIDTH//2, OPTIONS_LABEL_Y))
        surface.blit(options_label, options_label_rect)
        
    def draw_correct_panel(self, surface, question_text, correct_answer):
        """正解パネルを描画する"""
        # 正解パネルの背景
        result_rect = pygame.Rect(100, HEIGHT//2 - RESULT_PANEL_Y_OFFSET, WIDTH-200, RESULT_PANEL_HEIGHT)
        pygame.draw.rect(surface, LIGHT_GREEN, result_rect, border_radius=RESULT_PANEL_RADIUS)
        pygame.draw.rect(surface, BLACK, result_rect, 2, border_radius=RESULT_PANEL_RADIUS)
        
        # 正解メッセージ
        result = self.fonts["question"].render("正解です！", True, GREEN)
        result_rect = result.get_rect(center=(WIDTH//2, HEIGHT//2 - 130))
        surface.blit(result, result_rect)
        
        # 問題文を表示
        q_text = self.fonts["question"].render(question_text, True, BLACK)
        q_rect = q_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
        surface.blit(q_text, q_rect)
        
        # 正解の表示
        answer = self.fonts["question"].render(f"答え: {correct_answer}", True, BLACK)
        answer_rect = answer.get_rect(center=(WIDTH//2, HEIGHT//2 - 30))
        surface.blit(answer, answer_rect)
        
    def draw_incorrect_panel(self, surface, question_text, correct_answer, selected_option):
        """不正解パネルを描画する"""
        # 不正解パネルの背景
        result_rect = pygame.Rect(100, HEIGHT//2 - RESULT_PANEL_Y_OFFSET, WIDTH-200, RESULT_PANEL_HEIGHT)
        pygame.draw.rect(surface, LIGHT_RED, result_rect, border_radius=RESULT_PANEL_RADIUS)
        pygame.draw.rect(surface, BLACK, result_rect, 2, border_radius=RESULT_PANEL_RADIUS)
        
        # 不正解メッセージ
        result = self.fonts["question"].render("不正解です", True, RED)
        result_rect = result.get_rect(center=(WIDTH//2, HEIGHT//2 - 130))
        surface.blit(result, result_rect)
        
        # 問題文を表示
        q_text = self.fonts["question"].render(question_text, True, BLACK)
        q_rect = q_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
        surface.blit(q_text, q_rect)
        
        # 正解の表示
        answer = self.fonts["question"].render(f"正解: {correct_answer}", True, BLACK)
        answer_rect = answer.get_rect(center=(WIDTH//2, HEIGHT//2 - 30))
        surface.blit(answer, answer_rect)
        
        # あなたの回答の表示
        your_answer = self.fonts["question"].render(f"あなたの回答: {selected_option}", True, BLACK)
        your_answer_rect = your_answer.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
        surface.blit(your_answer, your_answer_rect)
        
    def draw_result_panel(self, surface, score, total_questions):
        """結果パネルを描画する"""
        # 結果パネルの背景
        result_rect = pygame.Rect(100, HEIGHT//2 - 220, WIDTH-200, 400)
        pygame.draw.rect(surface, LIGHT_BLUE, result_rect, border_radius=RESULT_PANEL_RADIUS)
        pygame.draw.rect(surface, BLACK, result_rect, 2, border_radius=RESULT_PANEL_RADIUS)
        
        # 結果タイトル
        result_title = self.fonts["title"].render("クイズ終了！", True, BLACK)
        result_title_rect = result_title.get_rect(center=(WIDTH//2, HEIGHT//2 - 150))
        surface.blit(result_title, result_title_rect)
        
        # 最終スコア
        final_score = self.fonts["question"].render(f"あなたの最終スコア: {score}/{total_questions}", True, BLACK)
        final_score_rect = final_score.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
        surface.blit(final_score, final_score_rect)
        
        # 成績評価
        score_ratio = score / total_questions if total_questions > 0 else 0
        
        if score_ratio >= PERFECT_SCORE_THRESHOLD:
            evaluation = self.fonts["question"].render("素晴らしい！全問正解です！", True, GREEN)
        elif score_ratio >= GOOD_SCORE_THRESHOLD:
            evaluation = self.fonts["question"].render("よくできました！", True, GREEN)
        elif score_ratio >= AVERAGE_SCORE_THRESHOLD:
            evaluation = self.fonts["question"].render("まずまずの成績です。", True, BLUE)
        else:
            evaluation = self.fonts["question"].render("もう少し頑張りましょう！", True, RED)
        
        evaluation_rect = evaluation.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
        surface.blit(evaluation, evaluation_rect)
        
    def draw_wrapped_text(self, surface, text, x, y, font, color):
        """テキストを折り返して描画する"""
        # 日本語テキストの場合は文字単位で折り返す
        chars = list(text)
        lines = []
        current_line = ""
        max_width = WIDTH - 200  # 余白を確保
        
        for char in chars:
            test_line = current_line + char
            if font.size(test_line)[0] < max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = char
        
        if current_line:
            lines.append(current_line)
        
        # 問題文を中央に配置
        for i, line in enumerate(lines):
            line_surface = font.render(line, True, color)
            line_rect = line_surface.get_rect(center=(x, y + i * 40))
            surface.blit(line_surface, line_rect)
