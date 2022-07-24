#!/usr/bin/env python
# -*- coding: utf-8 -*-

import src.Main as main


"""
Beispieldatei zur Verwendung des Bots.
Alle Stellen die angepasst werden müssen sind mit TODO gekennzeichnet.
"""

#TODO: Login Daten eintragen
user = 'bongomedia'
pw = '3df5da34'
server = 46

#Login und Initialisierung des Bots
wurzelBot = main.initWurzelBot()
wurzelBot.launchBot(server, user, pw)

#TODO: Aktionen definieren
#Beispiel: Alles ernten, in allen Gärten Kürbis anbauen und alles gießen
wurzelBot.renewAllItemsInPark()
wurzelBot.collectCashFromPark()

#Deinitialisierung des Bots
wurzelBot.exitBot()




