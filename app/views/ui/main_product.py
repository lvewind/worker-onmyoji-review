# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_product.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindowProduct(object):
    def setupUi(self, MainWindowProduct):
        if not MainWindowProduct.objectName():
            MainWindowProduct.setObjectName(u"MainWindowProduct")
        MainWindowProduct.resize(880, 436)
        MainWindowProduct.setMinimumSize(QSize(880, 436))
        MainWindowProduct.setMaximumSize(QSize(880, 436))
        self.centralwidget = QWidget(MainWindowProduct)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_play_list = QGroupBox(self.centralwidget)
        self.groupBox_play_list.setObjectName(u"groupBox_play_list")
        self.groupBox_play_list.setGeometry(QRect(10, 10, 851, 191))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(9)
        self.groupBox_play_list.setFont(font)
        self.tableWidget_products = QTableWidget(self.groupBox_play_list)
        self.tableWidget_products.setObjectName(u"tableWidget_products")
        self.tableWidget_products.setGeometry(QRect(0, 20, 851, 171))
        self.tableWidget_products.setFont(font)
        self.tableWidget_products.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_products.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_products.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_products.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_products.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_products.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_products.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget_products.horizontalHeader().setHighlightSections(False)
        self.tableWidget_products.verticalHeader().setVisible(False)
        self.tableWidget_products.verticalHeader().setMinimumSectionSize(18)
        self.tableWidget_products.verticalHeader().setDefaultSectionSize(18)
        self.groupBox_32 = QGroupBox(self.centralwidget)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.groupBox_32.setGeometry(QRect(790, 200, 71, 201))
        self.groupBox_32.setFont(font)
        self.checkBox_play_list_option_accept_jade_cooperation = QCheckBox(self.groupBox_32)
        self.checkBox_play_list_option_accept_jade_cooperation.setObjectName(u"checkBox_play_list_option_accept_jade_cooperation")
        self.checkBox_play_list_option_accept_jade_cooperation.setGeometry(QRect(10, 20, 61, 21))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.checkBox_play_list_option_accept_jade_cooperation.setFont(font1)
        self.checkBox_play_list_option_accept_ap_cooperation = QCheckBox(self.groupBox_32)
        self.checkBox_play_list_option_accept_ap_cooperation.setObjectName(u"checkBox_play_list_option_accept_ap_cooperation")
        self.checkBox_play_list_option_accept_ap_cooperation.setGeometry(QRect(10, 50, 61, 21))
        self.checkBox_play_list_option_accept_ap_cooperation.setFont(font1)
        self.checkBox_play_list_option_accept_coin_cooperation = QCheckBox(self.groupBox_32)
        self.checkBox_play_list_option_accept_coin_cooperation.setObjectName(u"checkBox_play_list_option_accept_coin_cooperation")
        self.checkBox_play_list_option_accept_coin_cooperation.setGeometry(QRect(10, 140, 61, 21))
        self.checkBox_play_list_option_accept_coin_cooperation.setFont(font1)
        self.checkBox_play_list_option_accept_pet_cooperation = QCheckBox(self.groupBox_32)
        self.checkBox_play_list_option_accept_pet_cooperation.setObjectName(u"checkBox_play_list_option_accept_pet_cooperation")
        self.checkBox_play_list_option_accept_pet_cooperation.setGeometry(QRect(10, 110, 61, 21))
        self.checkBox_play_list_option_accept_pet_cooperation.setFont(font1)
        self.checkBox_play_list_option_accept_yingbing_cooperation_2 = QCheckBox(self.groupBox_32)
        self.checkBox_play_list_option_accept_yingbing_cooperation_2.setObjectName(u"checkBox_play_list_option_accept_yingbing_cooperation_2")
        self.checkBox_play_list_option_accept_yingbing_cooperation_2.setGeometry(QRect(10, 80, 61, 21))
        self.checkBox_play_list_option_accept_yingbing_cooperation_2.setFont(font1)
        self.checkBox_play_list_option_accept_yingbing_cooperation = QCheckBox(self.groupBox_32)
        self.checkBox_play_list_option_accept_yingbing_cooperation.setObjectName(u"checkBox_play_list_option_accept_yingbing_cooperation")
        self.checkBox_play_list_option_accept_yingbing_cooperation.setGeometry(QRect(10, 170, 61, 21))
        self.checkBox_play_list_option_accept_yingbing_cooperation.setFont(font1)
        self.groupBox_play_list_setting = QGroupBox(self.centralwidget)
        self.groupBox_play_list_setting.setObjectName(u"groupBox_play_list_setting")
        self.groupBox_play_list_setting.setGeometry(QRect(170, 200, 611, 201))
        self.groupBox_play_list_setting.setFont(font1)
        self.groupBox_play_list_setting.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.checkBox_job_option_bonus_exp_100 = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_bonus_exp_100.setObjectName(u"checkBox_job_option_bonus_exp_100")
        self.checkBox_job_option_bonus_exp_100.setEnabled(True)
        self.checkBox_job_option_bonus_exp_100.setGeometry(QRect(10, 170, 71, 21))
        self.checkBox_job_option_bonus_exp_100.setFont(font1)
        self.checkBox_job_option_bonus_exp_50 = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_bonus_exp_50.setObjectName(u"checkBox_job_option_bonus_exp_50")
        self.checkBox_job_option_bonus_exp_50.setEnabled(True)
        self.checkBox_job_option_bonus_exp_50.setGeometry(QRect(10, 140, 71, 21))
        self.checkBox_job_option_bonus_exp_50.setFont(font1)
        self.checkBox_job_option_bonus_coin_100 = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_bonus_coin_100.setObjectName(u"checkBox_job_option_bonus_coin_100")
        self.checkBox_job_option_bonus_coin_100.setEnabled(True)
        self.checkBox_job_option_bonus_coin_100.setGeometry(QRect(10, 110, 71, 21))
        self.checkBox_job_option_bonus_coin_100.setFont(font1)
        self.checkBox_job_option_bonus_evolution = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_bonus_evolution.setObjectName(u"checkBox_job_option_bonus_evolution")
        self.checkBox_job_option_bonus_evolution.setEnabled(True)
        self.checkBox_job_option_bonus_evolution.setGeometry(QRect(10, 50, 71, 21))
        self.checkBox_job_option_bonus_evolution.setFont(font1)
        self.checkBox_job_option_bonus_coin_50 = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_bonus_coin_50.setObjectName(u"checkBox_job_option_bonus_coin_50")
        self.checkBox_job_option_bonus_coin_50.setEnabled(True)
        self.checkBox_job_option_bonus_coin_50.setGeometry(QRect(10, 80, 71, 21))
        self.checkBox_job_option_bonus_coin_50.setFont(font1)
        self.checkBox_job_option_bonus_soul = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_bonus_soul.setObjectName(u"checkBox_job_option_bonus_soul")
        self.checkBox_job_option_bonus_soul.setEnabled(True)
        self.checkBox_job_option_bonus_soul.setGeometry(QRect(10, 20, 71, 21))
        self.checkBox_job_option_bonus_soul.setFont(font1)
        self.checkBox_job_option_chapter_gift_spirit = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_chapter_gift_spirit.setObjectName(u"checkBox_job_option_chapter_gift_spirit")
        self.checkBox_job_option_chapter_gift_spirit.setGeometry(QRect(90, 110, 61, 21))
        self.checkBox_job_option_chapter_gift_spirit.setFont(font1)
        self.checkBox_job_option_chapter_gift_spirit.setChecked(False)
        self.checkBox_job_option_chapter_exp_spirit = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_chapter_exp_spirit.setObjectName(u"checkBox_job_option_chapter_exp_spirit")
        self.checkBox_job_option_chapter_exp_spirit.setGeometry(QRect(90, 50, 61, 21))
        self.checkBox_job_option_chapter_exp_spirit.setFont(font1)
        self.checkBox_job_option_chapter_exp_spirit.setChecked(False)
        self.checkBox_job_option_chapter_all_spirit = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_chapter_all_spirit.setObjectName(u"checkBox_job_option_chapter_all_spirit")
        self.checkBox_job_option_chapter_all_spirit.setGeometry(QRect(90, 20, 61, 21))
        self.checkBox_job_option_chapter_all_spirit.setFont(font1)
        self.checkBox_job_option_chapter_all_spirit.setChecked(False)
        self.checkBox_job_option_chapter_coin_spirit = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_chapter_coin_spirit.setObjectName(u"checkBox_job_option_chapter_coin_spirit")
        self.checkBox_job_option_chapter_coin_spirit.setGeometry(QRect(90, 80, 61, 21))
        self.checkBox_job_option_chapter_coin_spirit.setFont(font1)
        self.checkBox_job_option_chapter_coin_spirit.setChecked(False)
        self.checkBox_job_option_chapter_map_gift = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_chapter_map_gift.setObjectName(u"checkBox_job_option_chapter_map_gift")
        self.checkBox_job_option_chapter_map_gift.setGeometry(QRect(90, 140, 61, 21))
        self.checkBox_job_option_chapter_map_gift.setFont(font1)
        self.checkBox_job_option_chapter_map_seal = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_chapter_map_seal.setObjectName(u"checkBox_job_option_chapter_map_seal")
        self.checkBox_job_option_chapter_map_seal.setGeometry(QRect(90, 170, 61, 21))
        self.checkBox_job_option_chapter_map_seal.setFont(font1)
        self.groupBox_play_list_chapter = QGroupBox(self.groupBox_play_list_setting)
        self.groupBox_play_list_chapter.setObjectName(u"groupBox_play_list_chapter")
        self.groupBox_play_list_chapter.setGeometry(QRect(230, 20, 75, 51))
        self.radioButton_job_option_dog_food_m = QRadioButton(self.groupBox_play_list_chapter)
        self.radioButton_job_option_dog_food_m.setObjectName(u"radioButton_job_option_dog_food_m")
        self.radioButton_job_option_dog_food_m.setGeometry(QRect(0, 0, 71, 21))
        self.radioButton_job_option_dog_food_m.setFont(font1)
        self.radioButton_job_option_dog_food_n = QRadioButton(self.groupBox_play_list_chapter)
        self.radioButton_job_option_dog_food_n.setObjectName(u"radioButton_job_option_dog_food_n")
        self.radioButton_job_option_dog_food_n.setGeometry(QRect(0, 30, 71, 21))
        self.radioButton_job_option_dog_food_n.setFont(font1)
        self.radioButton_job_option_dog_food_n.setChecked(True)
        self.checkBox_job_option_lock_cast = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_lock_cast.setObjectName(u"checkBox_job_option_lock_cast")
        self.checkBox_job_option_lock_cast.setGeometry(QRect(310, 20, 71, 21))
        self.checkBox_job_option_lock_cast.setFont(font1)
        self.checkBox_job_option_use_yingbing = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_use_yingbing.setObjectName(u"checkBox_job_option_use_yingbing")
        self.checkBox_job_option_use_yingbing.setGeometry(QRect(310, 50, 71, 21))
        self.checkBox_job_option_use_yingbing.setFont(font1)
        self.checkBox_job_option_gymnasium_mass = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_gymnasium_mass.setObjectName(u"checkBox_job_option_gymnasium_mass")
        self.checkBox_job_option_gymnasium_mass.setGeometry(QRect(490, 140, 51, 21))
        self.checkBox_job_option_gymnasium_mass.setFont(font1)
        self.checkBox_job_option_gymnasium_only_watch = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_gymnasium_only_watch.setObjectName(u"checkBox_job_option_gymnasium_only_watch")
        self.checkBox_job_option_gymnasium_only_watch.setGeometry(QRect(490, 170, 61, 21))
        self.checkBox_job_option_gymnasium_only_watch.setFont(font1)
        self.checkBox_job_option_encounter_boss = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_encounter_boss.setObjectName(u"checkBox_job_option_encounter_boss")
        self.checkBox_job_option_encounter_boss.setGeometry(QRect(150, 170, 81, 21))
        self.checkBox_job_option_encounter_boss.setFont(font1)
        self.groupBox_6 = QGroupBox(self.groupBox_play_list_setting)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(150, 20, 71, 141))
        self.radioButton_job_option_chapter_0v3 = QRadioButton(self.groupBox_6)
        self.radioButton_job_option_chapter_0v3.setObjectName(u"radioButton_job_option_chapter_0v3")
        self.radioButton_job_option_chapter_0v3.setGeometry(QRect(0, 60, 71, 21))
        self.radioButton_job_option_chapter_0v3.setFont(font1)
        self.radioButton_job_option_chapter_1v3 = QRadioButton(self.groupBox_6)
        self.radioButton_job_option_chapter_1v3.setObjectName(u"radioButton_job_option_chapter_1v3")
        self.radioButton_job_option_chapter_1v3.setGeometry(QRect(0, 30, 71, 21))
        self.radioButton_job_option_chapter_1v3.setFont(font1)
        self.radioButton_job_option_chapter_1v3.setChecked(False)
        self.radioButton_job_option_chapter_1v2 = QRadioButton(self.groupBox_6)
        self.radioButton_job_option_chapter_1v2.setObjectName(u"radioButton_job_option_chapter_1v2")
        self.radioButton_job_option_chapter_1v2.setGeometry(QRect(0, 90, 71, 21))
        self.radioButton_job_option_chapter_1v2.setFont(font1)
        self.radioButton_job_option_chapter_2v2 = QRadioButton(self.groupBox_6)
        self.radioButton_job_option_chapter_2v2.setObjectName(u"radioButton_job_option_chapter_2v2")
        self.radioButton_job_option_chapter_2v2.setGeometry(QRect(0, 0, 71, 21))
        self.radioButton_job_option_chapter_2v2.setFont(font1)
        self.radioButton_job_option_chapter_2v2.setChecked(True)
        self.radioButton_job_option_chapter_0v0 = QRadioButton(self.groupBox_6)
        self.radioButton_job_option_chapter_0v0.setObjectName(u"radioButton_job_option_chapter_0v0")
        self.radioButton_job_option_chapter_0v0.setGeometry(QRect(0, 120, 71, 21))
        self.radioButton_job_option_chapter_0v0.setFont(font1)
        self.groupBox_7 = QGroupBox(self.groupBox_play_list_setting)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(230, 80, 75, 81))
        self.radioButton_job_option_dog_food_star_4 = QRadioButton(self.groupBox_7)
        self.radioButton_job_option_dog_food_star_4.setObjectName(u"radioButton_job_option_dog_food_star_4")
        self.radioButton_job_option_dog_food_star_4.setGeometry(QRect(0, 60, 71, 21))
        self.radioButton_job_option_dog_food_star_4.setFont(font1)
        self.radioButton_job_option_dog_food_star_4.setChecked(False)
        self.radioButton_job_option_dog_food_star_2 = QRadioButton(self.groupBox_7)
        self.radioButton_job_option_dog_food_star_2.setObjectName(u"radioButton_job_option_dog_food_star_2")
        self.radioButton_job_option_dog_food_star_2.setGeometry(QRect(0, 0, 71, 21))
        self.radioButton_job_option_dog_food_star_2.setFont(font1)
        self.radioButton_job_option_dog_food_star_2.setChecked(True)
        self.radioButton_job_option_dog_food_star_3 = QRadioButton(self.groupBox_7)
        self.radioButton_job_option_dog_food_star_3.setObjectName(u"radioButton_job_option_dog_food_star_3")
        self.radioButton_job_option_dog_food_star_3.setGeometry(QRect(0, 30, 71, 21))
        self.radioButton_job_option_dog_food_star_3.setFont(font1)
        self.radioButton_job_option_dog_food_star_3.setChecked(False)
        self.checkBox_job_option_guild_mall_amulet = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_mall_amulet.setObjectName(u"checkBox_job_option_guild_mall_amulet")
        self.checkBox_job_option_guild_mall_amulet.setGeometry(QRect(390, 80, 51, 21))
        self.checkBox_job_option_guild_mall_amulet.setFont(font1)
        self.checkBox_job_option_guild_mall_souls = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_mall_souls.setObjectName(u"checkBox_job_option_guild_mall_souls")
        self.checkBox_job_option_guild_mall_souls.setGeometry(QRect(390, 50, 51, 21))
        self.checkBox_job_option_guild_mall_souls.setFont(font1)
        self.checkBox_job_option_guild_mall_skill_daruma = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_mall_skill_daruma.setObjectName(u"checkBox_job_option_guild_mall_skill_daruma")
        self.checkBox_job_option_guild_mall_skill_daruma.setGeometry(QRect(390, 110, 51, 21))
        self.checkBox_job_option_guild_mall_skill_daruma.setFont(font1)
        self.checkBox_job_option_guild_mall_grade_daruma = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_mall_grade_daruma.setObjectName(u"checkBox_job_option_guild_mall_grade_daruma")
        self.checkBox_job_option_guild_mall_grade_daruma.setGeometry(QRect(390, 20, 51, 21))
        self.checkBox_job_option_guild_mall_grade_daruma.setFont(font1)
        self.checkBox_job_option_guild_mall_skin_ticket = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_mall_skin_ticket.setObjectName(u"checkBox_job_option_guild_mall_skin_ticket")
        self.checkBox_job_option_guild_mall_skin_ticket.setGeometry(QRect(390, 140, 51, 21))
        self.checkBox_job_option_guild_mall_skin_ticket.setFont(font1)
        self.checkBox_job_option_guild_mall_yingbing = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_mall_yingbing.setObjectName(u"checkBox_job_option_guild_mall_yingbing")
        self.checkBox_job_option_guild_mall_yingbing.setGeometry(QRect(390, 170, 51, 21))
        self.checkBox_job_option_guild_mall_yingbing.setFont(font1)
        self.checkBox_job_option_story_buy_ap = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_story_buy_ap.setObjectName(u"checkBox_job_option_story_buy_ap")
        self.checkBox_job_option_story_buy_ap.setGeometry(QRect(310, 110, 71, 21))
        self.checkBox_job_option_story_buy_ap.setFont(font1)
        self.checkBox_job_option_story_realm_raid = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_story_realm_raid.setObjectName(u"checkBox_job_option_story_realm_raid")
        self.checkBox_job_option_story_realm_raid.setGeometry(QRect(230, 170, 71, 21))
        self.checkBox_job_option_story_realm_raid.setFont(font1)
        self.checkBox_job_option_failed_stop = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_failed_stop.setObjectName(u"checkBox_job_option_failed_stop")
        self.checkBox_job_option_failed_stop.setGeometry(QRect(310, 80, 71, 21))
        self.checkBox_job_option_failed_stop.setFont(font1)
        self.checkBox_job_option_ap_use_up_restart = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_ap_use_up_restart.setObjectName(u"checkBox_job_option_ap_use_up_restart")
        self.checkBox_job_option_ap_use_up_restart.setGeometry(QRect(310, 170, 71, 21))
        self.checkBox_job_option_ap_use_up_restart.setFont(font1)
        self.checkBox_job_option_ap_use_up_close_game = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_ap_use_up_close_game.setObjectName(u"checkBox_job_option_ap_use_up_close_game")
        self.checkBox_job_option_ap_use_up_close_game.setGeometry(QRect(310, 140, 71, 21))
        self.checkBox_job_option_ap_use_up_close_game.setFont(font1)
        self.checkBox_job_option_guild_coin = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_coin.setObjectName(u"checkBox_job_option_guild_coin")
        self.checkBox_job_option_guild_coin.setGeometry(QRect(440, 20, 51, 21))
        self.checkBox_job_option_guild_coin.setFont(font1)
        self.checkBox_job_option_guild_contribute = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_contribute.setObjectName(u"checkBox_job_option_guild_contribute")
        self.checkBox_job_option_guild_contribute.setGeometry(QRect(440, 50, 51, 21))
        self.checkBox_job_option_guild_contribute.setFont(font1)
        self.checkBox_job_option_guild_invocation = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_invocation.setObjectName(u"checkBox_job_option_guild_invocation")
        self.checkBox_job_option_guild_invocation.setGeometry(QRect(440, 80, 51, 21))
        self.checkBox_job_option_guild_invocation.setFont(font1)
        self.checkBox_job_option_guild_task = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_task.setObjectName(u"checkBox_job_option_guild_task")
        self.checkBox_job_option_guild_task.setGeometry(QRect(440, 140, 51, 21))
        self.checkBox_job_option_guild_task.setFont(font1)
        self.checkBox_job_option_guild_realm_ap = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_realm_ap.setObjectName(u"checkBox_job_option_guild_realm_ap")
        self.checkBox_job_option_guild_realm_ap.setGeometry(QRect(440, 110, 51, 21))
        self.checkBox_job_option_guild_realm_ap.setFont(font1)
        self.checkBox_job_option_guild_foster_n = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_foster_n.setObjectName(u"checkBox_job_option_guild_foster_n")
        self.checkBox_job_option_guild_foster_n.setGeometry(QRect(490, 50, 61, 21))
        self.checkBox_job_option_guild_foster_n.setFont(font1)
        self.checkBox_job_option_guild_foster_m = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_foster_m.setObjectName(u"checkBox_job_option_guild_foster_m")
        self.checkBox_job_option_guild_foster_m.setGeometry(QRect(490, 20, 61, 21))
        self.checkBox_job_option_guild_foster_m.setFont(font1)
        self.checkBox_job_option_guild_cultivate_m = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_cultivate_m.setObjectName(u"checkBox_job_option_guild_cultivate_m")
        self.checkBox_job_option_guild_cultivate_m.setGeometry(QRect(490, 80, 61, 21))
        self.checkBox_job_option_guild_cultivate_m.setFont(font1)
        self.checkBox_job_option_guild_cultivate_n = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_cultivate_n.setObjectName(u"checkBox_job_option_guild_cultivate_n")
        self.checkBox_job_option_guild_cultivate_n.setGeometry(QRect(490, 110, 61, 21))
        self.checkBox_job_option_guild_cultivate_n.setFont(font1)
        self.checkBox_job_option_guild_task_contribute = QCheckBox(self.groupBox_play_list_setting)
        self.checkBox_job_option_guild_task_contribute.setObjectName(u"checkBox_job_option_guild_task_contribute")
        self.checkBox_job_option_guild_task_contribute.setGeometry(QRect(440, 170, 51, 21))
        self.checkBox_job_option_guild_task_contribute.setFont(font1)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 200, 161, 201))
        self.groupBox_3.setFont(font)
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 31, 21))
        self.label.setFont(font)
        self.comboBox_job_option_play = QComboBox(self.groupBox_3)
        self.comboBox_job_option_play.setObjectName(u"comboBox_job_option_play")
        self.comboBox_job_option_play.setGeometry(QRect(40, 20, 111, 20))
        self.comboBox_job_option_play.setFont(font)
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 31, 21))
        self.label_2.setFont(font)
        self.lineEdit_count = QLineEdit(self.groupBox_3)
        self.lineEdit_count.setObjectName(u"lineEdit_count")
        self.lineEdit_count.setGeometry(QRect(40, 110, 111, 20))
        self.lineEdit_count.setFont(font)
        self.lineEdit_count.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 31, 21))
        self.label_3.setFont(font)
        self.comboBox_job_option_stage = QComboBox(self.groupBox_3)
        self.comboBox_job_option_stage.setObjectName(u"comboBox_job_option_stage")
        self.comboBox_job_option_stage.setGeometry(QRect(40, 80, 111, 20))
        self.comboBox_job_option_stage.setFont(font)
        self.pushButton_save_job = QPushButton(self.groupBox_3)
        self.pushButton_save_job.setObjectName(u"pushButton_save_job")
        self.pushButton_save_job.setGeometry(QRect(100, 160, 51, 23))
        self.pushButton_save_job.setFont(font)
        self.pushButton_reset_job_option = QPushButton(self.groupBox_3)
        self.pushButton_reset_job_option.setObjectName(u"pushButton_reset_job_option")
        self.pushButton_reset_job_option.setGeometry(QRect(40, 160, 51, 23))
        self.pushButton_reset_job_option.setFont(font)
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 50, 31, 21))
        self.label_4.setFont(font)
        self.comboBox_job_option_play_sub = QComboBox(self.groupBox_3)
        self.comboBox_job_option_play_sub.setObjectName(u"comboBox_job_option_play_sub")
        self.comboBox_job_option_play_sub.setGeometry(QRect(40, 50, 111, 20))
        self.comboBox_job_option_play_sub.setFont(font)
        self.checkBox_job_option_approximate_count = QCheckBox(self.groupBox_3)
        self.checkBox_job_option_approximate_count.setObjectName(u"checkBox_job_option_approximate_count")
        self.checkBox_job_option_approximate_count.setEnabled(True)
        self.checkBox_job_option_approximate_count.setGeometry(QRect(40, 130, 111, 21))
        self.checkBox_job_option_approximate_count.setFont(font1)
        MainWindowProduct.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowProduct)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowProduct.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowProduct)

        QMetaObject.connectSlotsByName(MainWindowProduct)
    # setupUi

    def retranslateUi(self, MainWindowProduct):
        MainWindowProduct.setWindowTitle(QCoreApplication.translate("MainWindowProduct", u"\u4ea7\u54c1", None))
        self.groupBox_play_list.setTitle(QCoreApplication.translate("MainWindowProduct", u"\u4ea7\u54c1\u5217\u8868", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("MainWindowProduct", u"\u60ac\u8d4f\u5c01\u5370", None))
        self.checkBox_play_list_option_accept_jade_cooperation.setText(QCoreApplication.translate("MainWindowProduct", u"\u63a5\u52fe\u7389", None))
        self.checkBox_play_list_option_accept_ap_cooperation.setText(QCoreApplication.translate("MainWindowProduct", u"\u63a5\u4f53\u529b", None))
        self.checkBox_play_list_option_accept_coin_cooperation.setText(QCoreApplication.translate("MainWindowProduct", u"\u63a5\u91d1\u5e01", None))
        self.checkBox_play_list_option_accept_pet_cooperation.setText(QCoreApplication.translate("MainWindowProduct", u"\u63a5\u72d7\u7cae", None))
        self.checkBox_play_list_option_accept_yingbing_cooperation_2.setText(QCoreApplication.translate("MainWindowProduct", u"\u63a5\u73b0\u4e16", None))
        self.checkBox_play_list_option_accept_yingbing_cooperation.setText(QCoreApplication.translate("MainWindowProduct", u"\u63a5\u6a31\u997c", None))
        self.groupBox_play_list_setting.setTitle(QCoreApplication.translate("MainWindowProduct", u"\u53c2\u6570", None))
        self.checkBox_job_option_bonus_exp_100.setText(QCoreApplication.translate("MainWindowProduct", u"\u4e00\u767e\u7ecf\u9a8c", None))
        self.checkBox_job_option_bonus_exp_50.setText(QCoreApplication.translate("MainWindowProduct", u"\u4e94\u5341\u7ecf\u9a8c", None))
        self.checkBox_job_option_bonus_coin_100.setText(QCoreApplication.translate("MainWindowProduct", u"\u4e00\u767e\u91d1\u5e01", None))
        self.checkBox_job_option_bonus_evolution.setText(QCoreApplication.translate("MainWindowProduct", u"\u89c9\u9192\u52a0\u6210", None))
        self.checkBox_job_option_bonus_coin_50.setText(QCoreApplication.translate("MainWindowProduct", u"\u4e94\u5341\u91d1\u5e01", None))
        self.checkBox_job_option_bonus_soul.setText(QCoreApplication.translate("MainWindowProduct", u"\u5fa1\u9b42\u52a0\u6210", None))
        self.checkBox_job_option_chapter_gift_spirit.setText(QCoreApplication.translate("MainWindowProduct", u"\u7269\u54c1\u602a", None))
        self.checkBox_job_option_chapter_exp_spirit.setText(QCoreApplication.translate("MainWindowProduct", u"\u7ecf\u9a8c\u602a", None))
        self.checkBox_job_option_chapter_all_spirit.setText(QCoreApplication.translate("MainWindowProduct", u"\u6240\u6709\u602a", None))
        self.checkBox_job_option_chapter_coin_spirit.setText(QCoreApplication.translate("MainWindowProduct", u"\u91d1\u5e01\u602a", None))
        self.checkBox_job_option_chapter_map_gift.setText(QCoreApplication.translate("MainWindowProduct", u"\u5730\u56fe\u5956", None))
        self.checkBox_job_option_chapter_map_seal.setText(QCoreApplication.translate("MainWindowProduct", u"\u5996\u6c14\u5c01", None))
        self.groupBox_play_list_chapter.setTitle("")
        self.radioButton_job_option_dog_food_m.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b7\u767d\u86cb", None))
        self.radioButton_job_option_dog_food_n.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b7N\u5361", None))
        self.checkBox_job_option_lock_cast.setText(QCoreApplication.translate("MainWindowProduct", u"\u9501\u5b9a\u9635\u5bb9", None))
        self.checkBox_job_option_use_yingbing.setText(QCoreApplication.translate("MainWindowProduct", u"\u4f7f\u7528\u6a31\u997c", None))
        self.checkBox_job_option_gymnasium_mass.setText(QCoreApplication.translate("MainWindowProduct", u"\u96c6\u7ed3", None))
        self.checkBox_job_option_gymnasium_only_watch.setText(QCoreApplication.translate("MainWindowProduct", u"\u4ec5\u89c2\u6218", None))
        self.checkBox_job_option_encounter_boss.setText(QCoreApplication.translate("MainWindowProduct", u"\u9022\u9b54\u00b7Boss", None))
        self.groupBox_6.setTitle("")
        self.radioButton_job_option_chapter_0v3.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b70v3", None))
        self.radioButton_job_option_chapter_1v3.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b71v3", None))
        self.radioButton_job_option_chapter_1v2.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b71v2", None))
        self.radioButton_job_option_chapter_2v2.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b72v2", None))
        self.radioButton_job_option_chapter_0v0.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b70v0", None))
        self.groupBox_7.setTitle("")
        self.radioButton_job_option_dog_food_star_4.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b7\u56db\u661f", None))
        self.radioButton_job_option_dog_food_star_2.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b7\u4e8c\u661f", None))
        self.radioButton_job_option_dog_food_star_3.setText(QCoreApplication.translate("MainWindowProduct", u"\u72d7\u7cae\u00b7\u4e09\u661f", None))
        self.checkBox_job_option_guild_mall_amulet.setText(QCoreApplication.translate("MainWindowProduct", u"\u84dd\u7968", None))
        self.checkBox_job_option_guild_mall_souls.setText(QCoreApplication.translate("MainWindowProduct", u"\u5fa1\u9b42", None))
        self.checkBox_job_option_guild_mall_skill_daruma.setText(QCoreApplication.translate("MainWindowProduct", u"\u9ed1\u76ae", None))
        self.checkBox_job_option_guild_mall_grade_daruma.setText(QCoreApplication.translate("MainWindowProduct", u"\u767d\u86cb", None))
        self.checkBox_job_option_guild_mall_skin_ticket.setText(QCoreApplication.translate("MainWindowProduct", u"\u76ae\u5238", None))
        self.checkBox_job_option_guild_mall_yingbing.setText(QCoreApplication.translate("MainWindowProduct", u"\u6a31\u997c", None))
        self.checkBox_job_option_story_buy_ap.setText(QCoreApplication.translate("MainWindowProduct", u"\u5267\u60c5\u00b7\u4e70\u4f53", None))
        self.checkBox_job_option_story_realm_raid.setText(QCoreApplication.translate("MainWindowProduct", u"\u5267\u60c5\u00b7\u7a81\u7834", None))
        self.checkBox_job_option_failed_stop.setText(QCoreApplication.translate("MainWindowProduct", u"\u5931\u8d25\u00b7\u505c\u6b62", None))
        self.checkBox_job_option_ap_use_up_restart.setText(QCoreApplication.translate("MainWindowProduct", u"\u65e0\u4f53\u00b7\u91cd\u5f00", None))
        self.checkBox_job_option_ap_use_up_close_game.setText(QCoreApplication.translate("MainWindowProduct", u"\u65e0\u4f53\u00b7\u5173\u6e38", None))
        self.checkBox_job_option_guild_coin.setText(QCoreApplication.translate("MainWindowProduct", u"\u91d1\u5e01", None))
        self.checkBox_job_option_guild_contribute.setText(QCoreApplication.translate("MainWindowProduct", u"\u6350\u52fe", None))
        self.checkBox_job_option_guild_invocation.setText(QCoreApplication.translate("MainWindowProduct", u"\u7948\u613f", None))
        self.checkBox_job_option_guild_task.setText(QCoreApplication.translate("MainWindowProduct", u"\u7ed3\u4f34", None))
        self.checkBox_job_option_guild_realm_ap.setText(QCoreApplication.translate("MainWindowProduct", u"\u4f53\u529b", None))
        self.checkBox_job_option_guild_foster_n.setText(QCoreApplication.translate("MainWindowProduct", u"\u5bc4\u517b\u00b7N", None))
        self.checkBox_job_option_guild_foster_m.setText(QCoreApplication.translate("MainWindowProduct", u"\u5bc4\u517b\u00b7M", None))
        self.checkBox_job_option_guild_cultivate_m.setText(QCoreApplication.translate("MainWindowProduct", u"\u80b2\u6210\u00b7M", None))
        self.checkBox_job_option_guild_cultivate_n.setText(QCoreApplication.translate("MainWindowProduct", u"\u80b2\u6210\u00b7N", None))
        self.checkBox_job_option_guild_task_contribute.setText(QCoreApplication.translate("MainWindowProduct", u"\u6350\u6750", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindowProduct", u"\u73a9\u6cd5", None))
        self.label.setText(QCoreApplication.translate("MainWindowProduct", u"\u5185\u5bb9", None))
        self.label_2.setText(QCoreApplication.translate("MainWindowProduct", u"\u6b21\u6570", None))
        self.label_3.setText(QCoreApplication.translate("MainWindowProduct", u"\u96be\u5ea6", None))
        self.pushButton_save_job.setText(QCoreApplication.translate("MainWindowProduct", u"\u4fdd\u5b58", None))
        self.pushButton_reset_job_option.setText(QCoreApplication.translate("MainWindowProduct", u"\u91cd\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindowProduct", u"\u5b50\u9879", None))
        self.checkBox_job_option_approximate_count.setText(QCoreApplication.translate("MainWindowProduct", u"\u6b21\u6570\u8fd1\u4f3c\u6a21\u5f0f", None))
    # retranslateUi

