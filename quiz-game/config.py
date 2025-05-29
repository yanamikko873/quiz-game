#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
設定ファイル
ゲームの設定や定数を管理します
"""

import os

# 画面設定
WIDTH = 1024
HEIGHT = 768
TITLE = "雑学クイズゲーム"
FPS = 60

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
FONT_SIZES = {
    "title": 60,
    "question": 36,
    "option": 28,
    "button": 32,
    "score": 28
}

# 一般的な日本語フォントのパス
POSSIBLE_FONT_PATHS = [
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
    "/usr/share/fonts/truetype/vlgothic/VL-Gothic-Regular.ttf",
    "/usr/share/fonts/truetype/ipafont/ipag.ttf",
    "/usr/share/fonts/truetype/ipafont/ipam.ttf",
    "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf"
]

# ゲーム設定
QUESTIONS_PER_GAME = 10  # 1ゲームあたりの問題数
BUTTON_RADIUS = 10       # ボタンの角の丸み
PANEL_RADIUS = 15        # パネルの角の丸み
RESULT_PANEL_RADIUS = 20 # 結果パネルの角の丸み

# 背景装飾の設定
DECORATIONS = [
    {"pos": (100, 100), "radius": 80, "color": LIGHT_BLUE, "alpha": 128},
    {"pos": (WIDTH-100, 200), "radius": 120, "color": LIGHT_GREEN, "alpha": 128},
    {"pos": (200, HEIGHT-100), "radius": 100, "color": LIGHT_YELLOW, "alpha": 128},
    {"pos": (WIDTH-150, HEIGHT-150), "radius": 70, "color": LIGHT_RED, "alpha": 128}
]

# ボタン設定
OPTION_BUTTON_WIDTH = 400
OPTION_BUTTON_HEIGHT = 60
OPTION_BUTTON_SPACING = 80
OPTION_BUTTON_START_Y = 350

NEXT_BUTTON_WIDTH = 200
NEXT_BUTTON_HEIGHT = 50
NEXT_BUTTON_Y = HEIGHT - 100

RESTART_BUTTON_WIDTH = 200
RESTART_BUTTON_HEIGHT = 50

QUIT_BUTTON_WIDTH = 200
QUIT_BUTTON_HEIGHT = 50
QUIT_BUTTON_Y_OFFSET = 70  # リスタートボタンからの距離

# パネル設定
QUESTION_PANEL_Y = 130
QUESTION_PANEL_HEIGHT = 180

RESULT_PANEL_Y_OFFSET = 200  # 画面中央からのオフセット
RESULT_PANEL_HEIGHT = 300

# テキスト設定
TITLE_Y = 70
SCORE_X_OFFSET = 50
QUESTION_NUMBER_X = 100
QUESTION_NUMBER_Y = 150
QUESTION_Y_OFFSET = 200
OPTIONS_LABEL_Y = 320

# 評価基準
PERFECT_SCORE_THRESHOLD = 1.0  # 100%
GOOD_SCORE_THRESHOLD = 0.7     # 70%
AVERAGE_SCORE_THRESHOLD = 0.4  # 40%
