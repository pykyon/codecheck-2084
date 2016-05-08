#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import csv

class Program:
  def dp(self):
      for i, a in enumerate(self.memo):
          for j, v in enumerate(a):
              c = self.rows[i][0]
              x = self.rows[i][1]
              if i >= (self.memo[i-1][j][0] + cost):
                  self.memo[i][j] = self.memo[i-1][j][0] + cost
              else :
                  self.memo[i][j] = self.memo[i][j-1]
              self.memo[i][j] = self.memo[i][j] if vij[1] > self.memo[i-1][j][1]

  def build_deck(self, filename):
    # デッキを構築する関数
    # 引数 filename はカードのデータファイル
    # 返り値は文字列
    self.filename = filename
    self.memo = [[[0, ""] for _ in enumerate(10001)] for _ in enumerate(40001)]
    csvfile = open(filename)
    reader = csv.reader(csvfile)
    self.rows = [[row[0], row[1]] for row in reader]
    return "00000 00001 ..."

  def gacha(self, user_id):
    # ガチャを作成する
    # 変数 user_id はint型
    # 返り値はレアアイテムが当たったかどうかの true or false

    return True
