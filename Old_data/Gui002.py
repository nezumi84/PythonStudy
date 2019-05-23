#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * Signal Slot의 기본 사용법

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
    def __init__(self): #폼의 생성자 (위젯임)
        QWidget.__init__(self, flags=Qt.Widget)
        self.dl = QDial()   #다이얼 새성
        self.sd = QSlider(Qt.Horizontal)    #슬라이더 생성
        self.init_widget()  ##윈도우 팝업 위젯초기화

    def init_widget(self):  ##위젯초기화 함수
        self.setWindowTitle("Signal Slot")  #윈도우 타이틀
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)  ##윈도우에 레이아웃 변수 설정
        self.setLayout(form_lbx)    #설정한 레이아웃을 폼에 설정

        # 시그널 슬롯 연결
        # 다이얼의 값이 변하면 슬라이더의 값을 변경하는 슬롯과 연결
        # 슬라이더의 값이 변화하면 다이얼의 값을 변경하는 슬롯과 연결
        # 두 위젯의 valueChange 시그널은 현재값을 int형으로 반환
        # 두 위젯의 setValue 슬롯은 int형만을 받는다.
        self.dl.valueChanged.connect(self.sd.setValue)  ##폼의 다이얼이 변할때 슬라이더의 값 변경과 연결
        self.sd.valueChanged.connect(self.dl.setValue)  ##슬라이더가 변할때 다이얼로그의 값 변경과 연결

        form_lbx.addWidget(self.dl)     #레이아웃에 위젯연결
        form_lbx.addWidget(self.sd)     #레이아웃에 슬라이더 연결


if __name__ == "__main__":
    app = QApplication(sys.argv)    #qty애플리케이션 수행
    form = Form()   #폼 객체 새성 및 실행 초기화 함수 수행
    form.show()     #폼 보여주기
    exit(app.exec_())   #애플리케이션 실행하고 끝나면 종료