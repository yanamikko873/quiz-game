#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
メインモジュール
クイズゲームのエントリーポイントです
"""

import pygame
import sys
from config import WIDTH, HEIGHT, TITLE, FPS
from utils import load_fonts
from ui import UIManager
from game import QuizGame
from data import QuestionManager

def main():
    """メイン関数"""
    # Pygameの初期化
    pygame.init()
    
    # 画面設定
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    
    # フォントの読み込み
    fonts = load_fonts()
    
    # UIマネージャーの初期化
    ui_manager = UIManager(fonts)
    
    # 問題マネージャーの初期化
    question_manager = QuestionManager()
    
    # ゲームの初期化
    game = QuizGame(fonts, ui_manager, question_manager)
    
    # ゲームループ
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # イベント処理
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        # ゲームイベントの処理
        result = game.handle_events(events)
        if result == "quit":
            running = False
        
        # 描画
        game.draw(screen)
        pygame.display.flip()
        
        # フレームレート制御
        clock.tick(FPS)
    
    # 終了処理
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
