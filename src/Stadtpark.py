#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from src.HTTPCommunication import HTTPConnection

class Park():

    def __init__(self, httpConnection: HTTPConnection):
        self._httpConn = httpConnection
        self._logPark = logging.getLogger('bot.Park')
        self._logPark.setLevel(logging.DEBUG)

    def collectCashFromCashpoint(self):
        try:
            cashpoints = self._httpConn.collectCashPointsFromPark()
        except:
            self._logPark.error("Es konnte kein Geld oder Punkte abgeholt werden.")
        else:
            self._logPark.info("Es wurden {points} Punkte, {money} Wurzeltaler, {parkpoints} Gartenpunkte abgeholt".format(points = cashpoints["points"], money = cashpoints["money"], parkpoints=cashpoints["parkpoints"]))

    def getRenewableItemsFromPark(self):
        return self._httpConn.getRenewableDekoFromPark()

    def renewAllItemsInPark(self):
        try:
            renewableItems = self.getRenewableItemsFromPark()
            for itemID in renewableItems.keys():
                self._httpConn.renewItemsInPark(itemID)
        except:
            self._logPark.error("Es konnten keine Items erneuert werden")
        else:
            self._logPark.info("Es wurden {} Items erneuert".format(len(renewableItems)))
