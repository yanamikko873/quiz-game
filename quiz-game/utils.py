#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ユーティリティモジュール
ゲームの補助機能を提供します
"""

import os
import pygame
from config import POSSIBLE_FONT_PATHS, FONT_SIZES

def load_fonts():
    """フォントをロードする"""
    fonts = {}
    font_path = find_font_path()
    
    try:
        if font_path:
            fonts["title"] = pygame.font.Font(font_path, FONT_SIZES["title"])
            fonts["question"] = pygame.font.Font(font_path, FONT_SIZES["question"])
            fonts["option"] = pygame.font.Font(font_path, FONT_SIZES["option"])
            fonts["button"] = pygame.font.Font(font_path, FONT_SIZES["button"])
            fonts["score"] = pygame.font.Font(font_path, FONT_SIZES["score"])
        else:
            # フォントが見つからない場合はシステムフォントを使用
            fonts["title"] = pygame.font.SysFont("notosanscjkjp", FONT_SIZES["title"])
            fonts["question"] = pygame.font.SysFont("notosanscjkjp", FONT_SIZES["question"])
            fonts["option"] = pygame.font.SysFont("notosanscjkjp", FONT_SIZES["option"])
            fonts["button"] = pygame.font.SysFont("notosanscjkjp", FONT_SIZES["button"])
            fonts["score"] = pygame.font.SysFont("notosanscjkjp", FONT_SIZES["score"])
    except:
        # それでもダメな場合はデフォルトフォントを使用
        fonts["title"] = pygame.font.SysFont(None, FONT_SIZES["title"])
        fonts["question"] = pygame.font.SysFont(None, FONT_SIZES["question"])
        fonts["option"] = pygame.font.SysFont(None, FONT_SIZES["option"])
        fonts["button"] = pygame.font.SysFont(None, FONT_SIZES["button"])
        fonts["score"] = pygame.font.SysFont(None, FONT_SIZES["score"])
    
    return fonts

def find_font_path():
    """利用可能な日本語フォントのパスを探す"""
    for path in POSSIBLE_FONT_PATHS:
        if os.path.exists(path):
            return path
    return None
