#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ゲームモジュール
クイズゲームのメインロジックを管理します
"""

import pygame
import random
from config import *
from ui import Button, UIManager
from data import QuestionManager

class QuizGame:
    """クイズゲームクラス"""
    
    def __init__(self, fonts, ui_manager, question_manager):
        """初期化"""
        self.fonts = fonts
        self.ui_manager = ui_manager
        self.question_manager = question_manager
        
        # 問題の初期化
        self.questions = self.question_manager.get_questions(QUESTIONS_PER_GAME)
        self.current_question = 0
        self.score = 0
        self.total_questions = len(self.questions)
        self.state = "question"  # question, correct, incorrect, result
        
        # 選択肢ボタンの初期化
        self.option_buttons = []
        self.initialize_options()
        
        # 次へボタンとリスタートボタン
        self.next_button = Button(
            WIDTH//2 - NEXT_BUTTON_WIDTH//2, 
            NEXT_BUTTON_Y, 
            NEXT_BUTTON_WIDTH, 
            NEXT_BUTTON_HEIGHT, 
            "次の問題へ", 
            GREEN, 
            LIGHT_GREEN
        )
        
        self.restart_button = Button(
            WIDTH//2 - RESTART_BUTTON_WIDTH//2, 
            HEIGHT//2 + 100, 
            RESTART_BUTTON_WIDTH, 
            RESTART_BUTTON_HEIGHT, 
            "もう一度プレイ", 
            BLUE, 
            LIGHT_BLUE
        )
        
        self.quit_button = Button(
            WIDTH//2 - QUIT_BUTTON_WIDTH//2, 
            HEIGHT//2 + 100 + QUIT_BUTTON_Y_OFFSET, 
            QUIT_BUTTON_WIDTH, 
            QUIT_BUTTON_HEIGHT, 
            "終了", 
            RED, 
            LIGHT_RED
        )
        
        self.selected_option = None
        self.correct_answer = None
        
    def initialize_options(self):
        """選択肢を初期化する"""
        # 現在の問題の選択肢をシャッフル
        if self.current_question < len(self.questions):
            options = self.questions[self.current_question]["options"].copy()
            random.shuffle(options)
            
            # 選択肢ボタンを作成
            self.option_buttons = []
            for i, option in enumerate(options):
                y_pos = OPTION_BUTTON_START_Y + i * OPTION_BUTTON_SPACING
                button = Button(
                    WIDTH//2 - OPTION_BUTTON_WIDTH//2, 
                    y_pos, 
                    OPTION_BUTTON_WIDTH, 
                    OPTION_BUTTON_HEIGHT, 
                    option, 
                    LIGHT_BLUE, 
                    BLUE
                )
                self.option_buttons.append(button)
                
            # 正解を記録
            self.correct_answer = self.questions[self.current_question]["correct"]
        
    def handle_events(self, events):
        """イベントを処理する"""
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
                    self.__init__(self.fonts, self.ui_manager, self.question_manager)  # ゲームをリセット
                    return "continue"
                
                if self.quit_button.is_clicked(mouse_pos, event):
                    return "quit"
        
        return "continue"
    
    def draw(self, surface):
        """ゲーム画面を描画する"""
        # 背景を描画
        self.ui_manager.draw_background(surface)
        
        # タイトルを描画
        self.ui_manager.draw_title(surface)
        
        # スコアを描画
        self.ui_manager.draw_score(surface, self.score, self.current_question)
        
        if self.state == "question":
            # 問題パネルを描画
            self.ui_manager.draw_question_panel(
                surface, 
                self.current_question, 
                self.total_questions, 
                self.questions[self.current_question]["question"]
            )
            
            # 選択肢ラベルを描画
            self.ui_manager.draw_options_label(surface)
            
            # 選択肢ボタンを描画
            for button in self.option_buttons:
                button.draw(surface, self.fonts["option"])
            
        elif self.state == "correct":
            # 正解パネルを描画
            self.ui_manager.draw_correct_panel(
                surface, 
                self.questions[self.current_question]["question"], 
                self.correct_answer
            )
            
            # 次へボタンを描画
            self.next_button.draw(surface, self.fonts["button"])
            
        elif self.state == "incorrect":
            # 不正解パネルを描画
            self.ui_manager.draw_incorrect_panel(
                surface, 
                self.questions[self.current_question]["question"], 
                self.correct_answer, 
                self.selected_option
            )
            
            # 次へボタンを描画
            self.next_button.draw(surface, self.fonts["button"])
            
        elif self.state == "result":
            # 結果パネルを描画
            self.ui_manager.draw_result_panel(surface, self.score, self.total_questions)
            
            # ボタンを描画
            self.restart_button.draw(surface, self.fonts["button"])
            self.quit_button.draw(surface, self.fonts["button"])
