# Ara:
import ui
import uiWhisper

# Altina ekle:
if app.ENABLE_WHISPER_MESSENGER:
	import uiWhisperMessenger


# Interface.__init__ icinde ara:
		self.wndShopSoldNotice = None
		self._dropInfoGold = None

# Altina ekle:
		self.wndWhisperMessenger = None


# Interface.__init__ icinde ara:
		self.wndChat = None
		self.wndAutoChat = None

# Altina ekle:
		self.wndMessenger = None


# Interface icinde ara:
		else:
			self.wndExpandedMoney = uiTaskBar.ExpandedMoneyTaskBar()

# Altina ekle:
	def __MakeMessengerWindow(self):
		if app.ENABLE_MESSENGER_DETAILS:
			import uiMessengerRenewal
			self.wndMessenger = uiMessengerRenewal.MessengerWindow()
		else:
			self.wndMessenger = uiMessenger.MessengerWindow()

		from _weakref import proxy
		self.wndMessenger.SetWhisperButtonEvent(lambda n,i=proxy(self):i.OpenWhisperDialog(n))
		self.wndMessenger.SetGuildButtonEvent(ui.__mem_func__(self.ToggleGuildWindow))


# Interface.__MakeTaskBar icinde ara:
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_CHARACTER, ui.__mem_func__(self.ToggleCharacterWindowStatusPage))
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_INVENTORY, ui.__mem_func__(self.ToggleInventoryWindow))

# Altina ekle:
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_MESSENGER, ui.__mem_func__(self.ToggleMessenger))


# Interface.__MakeWindows icinde ara:
	def __MakeWindows(self):

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER:
			try:
				self.wndWhisperMessenger = uiWhisperMessenger.WhisperMessenger()
				self.wndWhisperMessenger.BindInterface(self)
				self.wndWhisperMessenger.Hide()
				self.wndMessengerButton = uiWhisper.WhisperButton()
				self.wndMessengerButton.SetUpVisual("d:/ymir work/ui/game/whisper/mp_close.png")
				self.wndMessengerButton.SetOverVisual("d:/ymir work/ui/game/whisper/mp_open.png")
				self.wndMessengerButton.SetDownVisual("d:/ymir work/ui/game/whisper/mp_open.png")
				self.wndMessengerButton.SetToolTipText(localeInfo.WHISPER_MESSENGER_ENVELOPE)
				self.wndMessengerButton.ToolTipText.SetHorizontalAlignCenter()
				self.wndMessengerButton.SetEvent(ui.__mem_func__(self.__OnClickMessengerButton))
				self.messengerQuickCloseTip = uiToolTip.ToolTip()
				self.messengerQuickCloseTip.SetIconTextLine(localeInfo.WHISPER_TOOLTIP_CLOSE_SHORTCUT)
				self.messengerQuickCloseTip.Hide()
				self.wndMessengerButton.SetHoverEvent(ui.__mem_func__(self.ShowMessengerQuickCloseTip), ui.__mem_func__(self.HideMessengerQuickCloseTip))
				self.wndMessengerButton.badge = uiWhisperMessenger.UnreadBadge(self.wndMessengerButton)
				if not constInfo.MESSENGER_BUTTON_CLOSED:
					self.wndMessengerButton.Show()
			except:
				import dbg, traceback
				dbg.TraceError("WhisperMessenger init failed: " + traceback.format_exc())
				self.wndWhisperMessenger = None


# Interface.MakeInterface icinde ara:
	def MakeInterface(self):

# Altina ekle:
		self.__MakeMessengerWindow()


# Interface.MakeInterface icinde ara:
		self.whisperButtonList = []
		self.whisperDialogDict = {}

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER:
			self.__ArrangeWhisperButton()


# Interface.Close icinde ara:
				self.wndTableDungeonInfo.Close()
				self.wndTableDungeonInfo.Destroy()

# Altina ekle:
		if self.wndMessenger:
			self.wndMessenger.Destroy()


# Interface.Close icinde ara:
		for dlg in self.whisperDialogDict.itervalues():
			dlg.Destroy()

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER and self.wndWhisperMessenger:
			self.wndWhisperMessenger.Destroy()
			self.wndWhisperMessenger.Hide()
			self.wndWhisperMessenger = None
		if app.ENABLE_WHISPER_MESSENGER and self.wndMessengerButton:
			self.wndMessengerButton.SetEvent(0)
			self.wndMessengerButton.Hide()
			self.wndMessengerButton = None


# Interface.Close icinde ara:
		# END_OF_ITEM_MALL
		del self.wndGuild

# Altina ekle:
		del self.wndMessenger


# Interface icinde ara:
		self.mallPageDlg.Open()
	# END_OF_ITEM_MALL

# Altina ekle:
	def RefreshMessenger(self):
		self.wndMessenger.RefreshMessenger()


# Interface icinde ara:
	def RefreshGuildGradePage(self):
		self.wndGuild.RefreshGuildGradePage()

# Altina ekle:
	def DeleteGuild(self):
		self.wndMessenger.ClearGuildMember()
		self.wndGuild.DeleteGuild()


# Interface.HideAllWindows icinde ara:
		if self.wndMiniMap:
			self.wndMiniMap.Hide()

# Altina ekle:
		if self.wndMessenger:
			self.wndMessenger.Hide()


# Interface icinde ara:
		self.dlgSystem.OpenDialog()
		self.dlgSystem.SetTop()

# Altina ekle:
	def ToggleMessenger(self):
		if self.wndMessenger.IsShow():
			self.wndMessenger.Hide()
		else:
			self.wndMessenger.SetTop()
			self.wndMessenger.Show()


# Interface.PressMKey icinde ara:
	def PressMKey(self):
		if app.IsPressed(app.DIK_LALT) or app.IsPressed(app.DIK_RALT):

# Altina ekle:
			self.ToggleMessenger()


# Interface.__HideWindows icinde ara:
						self.wndMiniMap,\
						self.wndGuild,\

# Altina ekle:
						self.wndMessenger,\


# Interface icinde ara:
	def __InitWhisper(self):
		chat.InitWhisper(self)

# Altina ekle:
	if app.ENABLE_WHISPER_MESSENGER:
		def __GetWhisperMessenger(self):
			return self.wndWhisperMessenger

		def PrepareGuildWhisper(self, name, line):
			if uiWhisperMessenger.GUILD_WHISPER_MARK not in line:
				return line
			messenger = self.__GetWhisperMessenger()
			if messenger:
				messenger.SetGuildSender(name)
			return line.replace(uiWhisperMessenger.GUILD_WHISPER_MARK, " : ", 1)

		def RecvWhisperMessenger(self, name, line, isSystem = FALSE):
			messenger = self.__GetWhisperMessenger()
			if not messenger:
				return
			if messenger.IsExcluded(name):
				return
			isOpen = messenger.RecvWhisperLine(name, line, isSystem)
			if self.IsGameMasterName(name):
				messenger.SetGameMaster(name)
			self.RefreshMessengerButton()
			if isOpen or isSystem or name == "[Guild]" or messenger.IsMuted(name):
				return
			self.__ReopenMessengerButton()
			if name.startswith("[") or messenger.IsGuildSender(name):
				btn = self.__FindWhisperButton(name)
				if 0 == btn:
					btn = self.__MakeSystemWhisperButton(name)
				btn.Flash()
			else:
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.RECEIVE_MESSAGE % (name))
			if app.ENABLE_BLINK_ALERT:
				app.FlashApplication()

		def HandleWhisperNotLogon(self, name):
			messenger = self.__GetWhisperMessenger()
			return messenger and messenger.OnWhisperNotLogon(name)

		def RecvOfflineWhisper(self, sender, sentAt, text):
			messenger = self.__GetWhisperMessenger()
			if not messenger:
				return
			isOpen = messenger.RecvOfflineMessage(sender, sentAt, text)
			self.RefreshMessengerButton()
			if not isOpen:
				self.__ReopenMessengerButton()
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.RECEIVE_MESSAGE % (sender))

		def RecvOfflineWhisperResult(self, result, name):
			messenger = self.__GetWhisperMessenger()
			if messenger:
				messenger.OnOfflineMessageResult(result, name)

		def RefreshMessengerButton(self):
			button = self.wndMessengerButton
			messenger = self.__GetWhisperMessenger()
			if button and messenger:
				button.badge.SetUnread(messenger.GetTotalUnreadCount())

		def ShowMessengerQuickCloseTip(self):
			tip = self.messengerQuickCloseTip
			if tip:
				tip.FitIconTextLine()
				tip.ShowToolTip()
				tip.SetTop()

		def HideMessengerQuickCloseTip(self):
			tip = self.messengerQuickCloseTip
			if tip:
				tip.HideToolTip()

		def __IsCtrlPressed(self):
			return app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)

		def __OnClickMessengerButton(self):
			self.HideMessengerQuickCloseTip()
			messenger = self.__GetWhisperMessenger()
			if messenger and self.__IsCtrlPressed():
				messenger.MarkAllRead()
				for btn in list(self.whisperButtonList):
					btn.Hide()
					self.__DestroyWhisperButton(btn)
				if messenger.IsShow():
					messenger.Close()
				self.RefreshMessengerButton()
				constInfo.MESSENGER_BUTTON_CLOSED = True
				self.wndMessengerButton.Hide()
				return
			self.ToggleWhisperMessenger()

		def __ReopenMessengerButton(self):
			button = self.wndMessengerButton
			if button and constInfo.MESSENGER_BUTTON_CLOSED:
				constInfo.MESSENGER_BUTTON_CLOSED = False
				button.Show()

		def __MakeSystemWhisperButton(self, name):
			button = uiWhisperMessenger.SystemWhisperButton(name)
			button.SetEvent(ui.__mem_func__(self.ShowWhisperDialog), button)
			button.SetHoverEvent(ui.__mem_func__(self.ShowMessengerQuickCloseTip), ui.__mem_func__(self.HideMessengerQuickCloseTip))
			button.Show()
			self.whisperButtonList.insert(0, button)
			self.__ArrangeWhisperButton()
			return button

		def RecvGlobalChat(self, payload):
			messenger = self.__GetWhisperMessenger()
			if messenger:
				messenger.RecvGlobalChat(payload)

		def RecvWhisperPlayerInfo(self, name, found, empire, race, online, guildName):
			messenger = self.__GetWhisperMessenger()
			if messenger:
				messenger.SetConversationInfo(name, found, empire, race, online, guildName)

		def RecvGlobalChatCooldown(self, seconds):
			messenger = self.__GetWhisperMessenger()
			if messenger:
				messenger.RecvGlobalCooldown(seconds)

		def OnWhisperConversationRead(self, name):
			btn = self.__FindWhisperButton(name)
			if 0 != btn:
				btn.Hide()
				self.__DestroyWhisperButton(btn)
				self.HideMessengerQuickCloseTip()
			self.RefreshMessengerButton()

		def ToggleWhisperMessenger(self):
			messenger = self.__GetWhisperMessenger()
			if messenger:
				messenger.Toggle()


# Interface.OpenWhisperDialogWithoutTarget icinde ara:
	def OpenWhisperDialogWithoutTarget(self):

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER and self.__GetWhisperMessenger():
			self.wndWhisperMessenger.Open()
			self.wndWhisperMessenger.OpenNewConversation()
			return


# Interface.RecieveWhisperDetails icinde ara:
		def RecieveWhisperDetails(self, name, country, countryFlag = ""):

# Altina ekle:
			if app.ENABLE_COUNTRY_FLAG and self.wndWhisperMessenger:
				self.wndWhisperMessenger.SetCountryFlag(name, countryFlag)


# Interface.OpenWhisperWithText icinde ara:
		self.OpenWhisperDialog(name)
		line = None

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER and self.wndWhisperMessenger:
			line = self.wndWhisperMessenger.chatLine
		elif self.whisperDialogDict.has_key(name):
			line = self.whisperDialogDict[name].chatLine


# Interface.OpenWhisperDialog icinde ara:
	def OpenWhisperDialog(self, name):

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER and self.__GetWhisperMessenger():
			self.wndWhisperMessenger.Open(name)
			return


# Interface.ShowWhisperDialog icinde ara:
			self.OpenWikiWindow()
			return

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER and self.__GetWhisperMessenger():
			name = btn.name
			btn.Hide()
			self.__DestroyWhisperButton(btn)
			self.HideMessengerQuickCloseTip()
			if self.__IsCtrlPressed():
				self.wndWhisperMessenger.MarkRead(name)
				return
			self.wndWhisperMessenger.Open(name)
			return


# Interface.__ArrangeWhisperButton icinde ara:
		count = 0
		yShift = 0

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER and self.wndMessengerButton:
			yShift = -30
			self.wndMessengerButton.SetPosition(xPos, yPos + 63 + yShift)
			count = 2


# Interface.HideAllWhisperButton icinde ara:
		for btn in self.whisperButtonList:
			btn.Hide()

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER and self.wndMessengerButton:
			self.wndMessengerButton.Hide()


# Interface.ShowAllWhisperButton icinde ara:
		for btn in self.whisperButtonList:
			btn.Show()

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER and self.wndMessengerButton and not constInfo.MESSENGER_BUTTON_CLOSED:
			self.wndMessengerButton.Show()


# Interface.RecvReadWiki icinde ara:
		def RecvReadWiki(self):

# Altina ekle:
			if app.ENABLE_WHISPER_MESSENGER:
				return

