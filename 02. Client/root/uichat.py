# ChatLine.OnIMETab icinde ara:
	def OnIMETab(self):
		interface = self.interface

# Altina ekle:
		if app.ENABLE_CHAT_TABS and interface and interface.wndChat:
			interface.wndChat.ToggleStopChat()
			return TRUE


# ChatInputSet.Open icinde ara:
	def Open(self):
		self.chatLine.Show()

# Altina ekle:
		if app.ENABLE_CHAT_TABS:
			self.chatLine.SetPosition(57, 5)
		elif app.ENABLE_EMOTICONS_SYSTEM:
			self.chatLine.SetPosition(77, 5)
		else:
			self.chatLine.SetPosition(57, 5)


# ChatInputSet.RefreshPosition icinde ara:
	def RefreshPosition(self):

# Altina ekle:
		if app.ENABLE_CHAT_TABS:
			self.chatLine.SetSize(self.GetWidth() - 194, 13)
			self.btnSend.SetPosition(self.GetWidth() - 125, 2)
		elif app.ENABLE_EMOTICONS_SYSTEM:
			self.chatLine.SetSize(self.GetWidth() - 113, 13)
			self.btnSend.SetPosition(self.GetWidth() - 25, 2)
		else:
			self.chatLine.SetSize(self.GetWidth() - 93, 13)
			self.btnSend.SetPosition(self.GetWidth() - 25, 2)


# ChatWindow icinde ara:
	EDIT_LINE_HEIGHT = 25
	CHAT_WINDOW_WIDTH = 600

# Altina ekle:
	if app.ENABLE_CHAT_TABS:
		CHAT_WINDOW_WIDTH = 650
		CHAT_LINE_STEP = 15


# ChatWindow.__init__ icinde ara:
		self.chatTabLineRight = None
		self.chatTabLineExtra = []

# Altina ekle:
		if app.ENABLE_CHAT_TABS:
			self.stopChatText = None
			self.chatTabSelected = [0]


# ChatWindow.__init__ icinde ara:
			chat.SetStep(self.chatID, 20)
			chat.SetFontNameChat("Tahoma:12")

# Altina ekle:
		if app.ENABLE_CHAT_TABS:
			chat.SetStep(self.chatID, self.CHAT_LINE_STEP)


# ChatWindow.__init__ icinde ara:
		chatInputSet.SetEscapeEvent(ui.__mem_func__(self.CloseChat))
		chatInputSet.SetReturnEvent(ui.__mem_func__(self.CloseChat))

# Altina ekle:
		if app.ENABLE_CHAT_TABS:
			chatInputSet.SetSize(self.CHAT_WINDOW_WIDTH, 25)
		else:
			chatInputSet.SetSize(550, 25)


# ChatWindow.__init__ icinde ara:
			btnEmoticonsOpen.SetOverVisual("d:/ymir work/ui/game/emoji/emoticons/gui/open_over.png")
			btnEmoticonsOpen.SetDownVisual("d:/ymir work/ui/game/emoji/emoticons/gui/open_down.png")

# Altina ekle:
			if app.ENABLE_CHAT_TABS:
				btnEmoticonsOpen.SetUpVisual("d:/ymir work/ui/game/taskbar/clr_emoji_btn_1.tga")
				btnEmoticonsOpen.SetOverVisual("d:/ymir work/ui/game/taskbar/clr_emoji_btn_2.tga")
				btnEmoticonsOpen.SetDownVisual("d:/ymir work/ui/game/taskbar/clr_emoji_btn_2.tga")
			else:
				btnEmoticonsOpen.SetButtonScale(0.29, 0.29)


# ChatWindow.__init__ icinde ara:
			btnEmoticonsOpen.SetPosition(51, 2)

# Altina ekle:
			if app.ENABLE_CHAT_TABS:
				btnEmoticonsOpen.SAFE_SetEvent(self.OpenEmojiPicker)
			else:
				btnEmoticonsOpen.SAFE_SetEvent(self.OpenEmoticons)


# ChatWindow.__init__ icinde ara:
			btnEmoticonsClose.SetOverVisual("d:/ymir work/ui/game/emoji/emoticons/gui/close_over.png")
			btnEmoticonsClose.SetDownVisual("d:/ymir work/ui/game/emoji/emoticons/gui/close_down.png")

# Altina ekle:
			if app.ENABLE_CHAT_TABS:
				btnEmoticonsClose.SetUpVisual("d:/ymir work/ui/game/taskbar/clr_emoji_btn_2.tga")
				btnEmoticonsClose.SetOverVisual("d:/ymir work/ui/game/taskbar/clr_emoji_btn_2.tga")
				btnEmoticonsClose.SetDownVisual("d:/ymir work/ui/game/taskbar/clr_emoji_btn_1.tga")
			else:
				btnEmoticonsClose.SetButtonScale(0.29, 0.29)


# ChatWindow.__init__ icinde ara:
		self.imgChatBarMiddle = imgChatBarMiddle
		self.interface = None

# Altina ekle:
		if app.ENABLE_CHAT_TABS:
			self.__CreateChatTabs()


# ChatWindow.__RegisterChatColorDict icinde ara:
		if app.ENABLE_DICE_SYSTEM:
			CHAT_COLOR_DICT.update({chat.CHAT_TYPE_DICE_INFO : colorInfo.CHAT_RGB_DICE_INFO,})

# Altina ekle:
		if app.ENABLE_CHAT_TABS:
			CHAT_COLOR_DICT.update({
				chat.CHAT_TYPE_DUNGEON : colorInfo.CHAT_RGB_NOTICE,
				chat.CHAT_TYPE_EXCHANGE : colorInfo.CHAT_RGB_INFO,
				chat.CHAT_TYPE_DROP : colorInfo.CHAT_RGB_INFO,
			})


# ChatWindow.OpenEmoticons icinde ara:
			self.btnSendWhisper.SetPosition(self.GetWidth() - 50, 2 + self.LINE_HEIGHT)
			self.btnChatLog.SetPosition(self.GetWidth() - 25, 2 + self.LINE_HEIGHT)

# Altina ekle:
			if app.ENABLE_CHAT_TABS:
				self.__PlaceInputButtons()


# ChatWindow.CloseEmoticons icinde ara:
			self.btnSendWhisper.SetPosition(self.GetWidth() - 50, 2 + self.LINE_HEIGHT)
			self.btnChatLog.SetPosition(self.GetWidth() - 25, 2 + self.LINE_HEIGHT)

# Altina ekle:
			if app.ENABLE_CHAT_TABS:
				self.__PlaceInputButtons()


# ChatWindow.OpenChat icinde ara:
		self.chatInputSet.SetTop()
		self.SetTop()

# Altina ekle:
		if app.ENABLE_CHAT_TABS:
			self.__PlaceInputButtons()
			self.__RefreshStopChat()


# ChatWindow.CloseChat icinde ara:
		if app.ENABLE_AUTO_CHAT and self.btnAutoChat:
			self.btnAutoChat.Hide()

# Altina ekle:
		if app.ENABLE_CHAT_TABS and self.emojiPicker:
			self.emojiPicker.Hide()


# ChatWindow.__RefreshSizingBar icinde ara:
		self.imgChatBarMiddle.SetPosition(64, 0)
		self.imgChatBarMiddle.SetRenderingRect(0.0, 0.0, float(width - 128) / 64.0 - 1.0, 0.0)

# Altina ekle:
		if app.ENABLE_CHAT_TABS and self.chatTabLine:
			self.__RefreshChatTabLine(width)


# ChatWindow.OnUpdate icinde ara:
		if app.ENABLE_AUTO_CHAT and self.interface and self.interface.wndAutoChat:
			self.interface.wndAutoChat.Tick()

# Altina ekle:
		if app.ENABLE_CHAT_TABS:
			self.__UpdateStopChat()


# ChatWindow.OnRender icinde ara:
		if self.boardState == chat.BOARD_STATE_EDIT:
			grp.SetColor(self.BOARD_MIDDLE_COLOR)

# Altina ekle:
			if app.ENABLE_CHAT_TABS:
				top = self.CHAT_TAB_LINE_Y + 2
				grp.RenderBar(self.xBar, self.yBar + (self.heightBar - self.curHeightBar) + top, self.widthBar, max(0, self.curHeightBar + 10 - top))
			else:
				grp.RenderBar(self.xBar, self.yBar + (self.heightBar - self.curHeightBar) + 10, self.widthBar, self.curHeightBar)


# ChatWindow icinde ara:
		self.interface = interface
		self.chatInputSet.BindInterface(interface)

# Altina ekle:
	if app.ENABLE_CHAT_TABS:
		CHAT_TAB_PATH = "d:/ymir work/ui/chat/"
		CHAT_TAB_X = 4
		CHAT_TAB_TEXT_Y = 8			# tab label centre (the engine centres text ~3 px low)
		CHAT_TAB_WIDTH = 57
		CHAT_TAB_LINE_Y = 18
		CHAT_TAB_OPEN_LEFT = 2
		CHAT_TAB_OPEN_RIGHT = 52		# ... to x=52
		CHAT_TAB_RIGHT_CORNER = (
			(4, 18, 4, 2, grp.GenerateColor(216 / 255.0, 202 / 255.0, 189 / 255.0, 1.0)),
			(2, 20, 2, 3, grp.GenerateColor(216 / 255.0, 202 / 255.0, 189 / 255.0, 1.0)),
			(1, 23, 1, 6, grp.GenerateColor(208 / 255.0, 194 / 255.0, 182 / 255.0, 0.96)),
			(2, 23, 1, 6, grp.GenerateColor(105 / 255.0, 99 / 255.0, 96 / 255.0, 0.91)),
		)

		STOP_KEY_WIDTH = 40
		STOP_KEY_HEIGHT = 16
		STOP_KEY_RIGHT = 117
		STOP_KEY_TEXT_COLOR = 0xffd2c6b6
		STOP_KEY_PARTS = (
			(0, 0, 40, 16, 0xff46413c),
			(1, 1, 38, 14, 0xff060100),
			(2, 2, 36, 3, 0xff41362b),
			(2, 5, 36, 3, 0xff3d3227),
			(2, 8, 36, 2, 0xff302820),
			(2, 10, 36, 2, 0xff25201b),
			(2, 12, 36, 2, 0xff1d1915),
		)

		## tab tooltip "[Ctrl] - Coklu secim icin basili tut": 200x39 board, key box 38x14 at (20, 13), text at x=61
		TAB_TOOLTIP_WIDTH = 200
		TAB_TOOLTIP_HEIGHT = 39
		TAB_TOOLTIP_GAP = 15			# tooltip bottom -> tab top
		TAB_TOOLTIP_X = -18
		TAB_TOOLTIP_KEY_X = 20
		TAB_TOOLTIP_KEY_Y = 13
		TAB_TOOLTIP_TEXT_X = 61
		CTRL_KEY_PARTS = (
			(0, 0, 38, 14, 0xff46413c),
			(1, 1, 36, 12, 0xff060100),
			(2, 2, 34, 3, 0xff41362b),
			(2, 5, 34, 2, 0xff3d3227),
			(2, 7, 34, 2, 0xff302820),
			(2, 9, 34, 2, 0xff25201b),
			(2, 11, 34, 2, 0xff1d1915),
		)

		def __CreateTabToolTip(self):
			board = ui.ThinBoard("TOP_MOST")
			board.AddFlag("float")
			board.AddFlag("not_pick")
			board.SetSize(self.TAB_TOOLTIP_WIDTH, self.TAB_TOOLTIP_HEIGHT)
			board.Hide()

			key = ui.Window()
			key.SetParent(board)
			key.AddFlag("not_pick")
			key.SetPosition(self.TAB_TOOLTIP_KEY_X, self.TAB_TOOLTIP_KEY_Y)
			key.SetSize(38, 14)
			key.Show()
			parts = []
			for (px, py, pw, ph, color) in self.CTRL_KEY_PARTS:
				part = ui.Bar()
				part.SetParent(key)
				part.AddFlag("not_pick")
				part.SetPosition(px, py)
				part.SetSize(pw, ph)
				part.SetColor(color)
				part.Show()
				parts.append(part)

			keyText = ui.TextLine()
			keyText.SetParent(key)
			keyText.SetPosition(19, 4)
			keyText.SetHorizontalAlignCenter()
			keyText.SetVerticalAlignCenter()
			keyText.SetPackedFontColor(self.STOP_KEY_TEXT_COLOR)
			keyText.SetText(localeInfo.AUTO_CTRL)
			keyText.Show()

			text = ui.TextLine()
			text.SetParent(board)
			text.SetPosition(self.TAB_TOOLTIP_TEXT_X, self.TAB_TOOLTIP_HEIGHT / 2 - 1)
			text.SetVerticalAlignCenter()
			text.SetText(localeInfo.CHAT_TAB_MULTI_SELECT)
			text.Show()

			self.tabToolTip = board
			self.tabToolTipParts = (key, parts, keyText, text)

		def __ShowTabToolTip(self, idx):
			if not self.tabToolTip:
				return
			(bx, by) = self.chatTabs[idx].GetGlobalPosition()
			self.tabToolTip.SetPosition(bx + self.TAB_TOOLTIP_X, by - self.TAB_TOOLTIP_GAP - self.TAB_TOOLTIP_HEIGHT)
			self.tabToolTip.Show()
			self.tabToolTip.SetTop()

		def __HideTabToolTip(self):
			if self.tabToolTip:
				self.tabToolTip.Hide()

		def __RefreshStopChat(self):
			if not self.stopChatText:
				return
			(x, y, width, height) = self.GetRect()
			self.stopKeyBox.SetPosition(width - self.STOP_KEY_RIGHT, -1)
			self.stopChatText.SetPosition(width - self.STOP_KEY_RIGHT + self.STOP_KEY_WIDTH + 4, -1)
			if self.chatStopped:
				self.stopChatText.SetText(localeInfo.CHAT_TAB_START_CHAT)
			else:
				self.stopChatText.SetText(localeInfo.CHAT_TAB_STOP_CHAT)

		def ToggleStopChat(self):
			self.chatStopped = not self.chatStopped
			if self.chatStopped:
				self.chatStopLineCount = chat.GetLineCount(self.chatID)
				self.chatStopLastCount = self.chatStopLineCount
			else:
				self.scrollBarPos = 1.0
				chat.SetEndPos(self.chatID, 1.0)
			self.__RefreshStopChat()

		def __UpdateStopChat(self):
			if not self.chatStopped:
				return
			lineCount = chat.GetLineCount(self.chatID)
			if lineCount == self.chatStopLastCount:
				return
			self.chatStopLastCount = lineCount
			visible = chat.GetVisibleLineCount(self.chatID)
			if lineCount - visible - 1 <= 0:
				return
			pos = float(self.chatStopLineCount - 1 - visible) / float(lineCount - visible - 1)
			chat.SetEndPos(self.chatID, max(0.0, min(1.0, pos)))

		def __PlaceInputButtons(self):
			lineHeight = 0
			if app.ENABLE_EMOTICONS_SYSTEM:
				lineHeight = self.LINE_HEIGHT
				self.btnEmoticonsOpen.SetPosition(self.GetWidth() - 100, 2 + lineHeight)
				self.btnEmoticonsClose.SetPosition(self.GetWidth() - 100, 2 + lineHeight)
			if app.ENABLE_AUTO_CHAT and self.btnAutoChat:
				self.btnAutoChat.SetPosition(self.GetWidth() - 75, 2 + lineHeight)
				self.btnAutoChat.Show()
			self.btnSendWhisper.SetPosition(self.GetWidth() - 50, 2 + lineHeight)
			self.btnChatLog.SetPosition(self.GetWidth() - 25, 2 + lineHeight)

		def __GetChatTabList(self):
			infoTypes = [chat.CHAT_TYPE_INFO, chat.CHAT_TYPE_NOTICE, chat.CHAT_TYPE_BIG_NOTICE]
			if app.ENABLE_DICE_SYSTEM:
				infoTypes.append(chat.CHAT_TYPE_DICE_INFO)
			return (
				(localeInfo.CHAT_TAB_ALL, None),
				(localeInfo.CHAT_TAB_NORMAL, (chat.CHAT_TYPE_TALKING, chat.CHAT_TYPE_PARTY)),
				(localeInfo.CHAT_TAB_GUILD, (chat.CHAT_TYPE_GUILD,)),
				(localeInfo.CHAT_TAB_GENERAL, (chat.CHAT_TYPE_SHOUT,)),
				(localeInfo.CHAT_TAB_EXCHANGE, (chat.CHAT_TYPE_EXCHANGE,)),
				(localeInfo.CHAT_TAB_INFO, tuple(infoTypes)),
				(localeInfo.CHAT_TAB_DROP, (chat.CHAT_TYPE_DROP,)),
				(localeInfo.CHAT_TAB_DUNGEON, (chat.CHAT_TYPE_DUNGEON,)),
			)

		def __CreateChatTabs(self):
			self.imgChatBarLeft.Hide()
			self.imgChatBarRight.Hide()
			self.imgChatBarMiddle.Hide()

			line = ui.ExpandedImageBox()
			line.SetParent(self.btnChatSizing)
			line.AddFlag("not_pick")
			line.LoadImage(self.CHAT_TAB_PATH + "chatmenutab_line.tga")
			line.Show()
			self.chatTabLine = line

			lineRight = ui.ExpandedImageBox()
			lineRight.SetParent(self.btnChatSizing)
			lineRight.AddFlag("not_pick")
			lineRight.LoadImage(self.CHAT_TAB_PATH + "chatmenutab_line.tga")
			lineRight.Show()
			self.chatTabLineRight = lineRight

			cornerLeft = ui.ImageBox()
			cornerLeft.SetParent(self.btnChatSizing)
			cornerLeft.AddFlag("not_pick")
			cornerLeft.LoadImage(self.CHAT_TAB_PATH + "chat_linebar_left.tga")
			cornerLeft.SetPosition(0, self.CHAT_TAB_LINE_Y - 1)
			cornerLeft.Show()
			self.chatTabCornerLeft = cornerLeft

			self.chatTabCornerRight = []
			for (cx, cy, cw, ch, color) in self.CHAT_TAB_RIGHT_CORNER:
				bar = ui.Bar()
				bar.SetParent(self.btnChatSizing)
				bar.AddFlag("not_pick")
				bar.SetSize(cw, ch)
				bar.SetColor(color)
				bar.Show()
				self.chatTabCornerRight.append((bar, cx, cy))

			keyBox = ui.Window()
			keyBox.SetParent(self.btnChatSizing)
			keyBox.AddFlag("not_pick")
			keyBox.SetSize(self.STOP_KEY_WIDTH, self.STOP_KEY_HEIGHT)
			keyBox.Show()
			self.stopKeyBox = keyBox

			self.stopKeyParts = []
			for (px, py, pw, ph, color) in self.STOP_KEY_PARTS:
				part = ui.Bar()
				part.SetParent(keyBox)
				part.AddFlag("not_pick")
				part.SetPosition(px, py)
				part.SetSize(pw, ph)
				part.SetColor(color)
				part.Show()
				self.stopKeyParts.append(part)

			keyText = ui.TextLine()
			keyText.SetParent(keyBox)
			keyText.SetPosition(self.STOP_KEY_WIDTH / 2, self.STOP_KEY_HEIGHT / 2)
			keyText.SetHorizontalAlignCenter()
			keyText.SetVerticalAlignCenter()
			keyText.SetPackedFontColor(self.STOP_KEY_TEXT_COLOR)
			keyText.SetText(localeInfo.AUTO_TAB)
			keyText.Show()
			self.stopKeyText = keyText

			stopText = ui.TextLine()
			stopText.SetParent(self.btnChatSizing)
			stopText.SetOutline()
			stopText.Show()
			self.stopChatText = stopText

			self.chatStopped = False
			self.chatStopLineCount = 0
			self.chatStopLastCount = 0
			self.__RefreshStopChat()

			self.chatTabList = self.__GetChatTabList()
			self.chatTabs = []
			for idx in xrange(len(self.chatTabList)):
				btn = ui.Button()
				btn.SetParent(self.btnChatSizing)
				btn.SetPosition(self.CHAT_TAB_X + idx * self.CHAT_TAB_WIDTH, 0)
				btn.SetEvent(ui.__mem_func__(self.OnChatTabClicked), idx)
				btn.SetShowToolTipEvent(ui.__mem_func__(self.__ShowTabToolTip), idx)
				btn.SetHideToolTipEvent(ui.__mem_func__(self.__HideTabToolTip))
				btn.Show()
				self.chatTabs.append(btn)

			self.__CreateTabToolTip()
			self.chatTabSelected = [0]
			self.chatTabIndex = 0
			self.__RefreshChatTabs()

		def __RefreshChatTabLine(self, width):
			if not self.chatTabLineRight:
				return
			selected = sorted(self.chatTabSelected)
			pieces = []
			start = 0
			for idx in selected:
				tabX = self.CHAT_TAB_X + idx * self.CHAT_TAB_WIDTH
				pieces.append((start, tabX + self.CHAT_TAB_OPEN_LEFT))
				start = tabX + self.CHAT_TAB_OPEN_RIGHT
			pieces.append((start, width))

			segments = [self.chatTabLine, self.chatTabLineRight] + self.chatTabLineExtra
			while len(segments) < len(pieces):
				seg = ui.ExpandedImageBox()
				seg.SetParent(self.btnChatSizing)
				seg.AddFlag("not_pick")
				seg.LoadImage(self.CHAT_TAB_PATH + "chatmenutab_line.tga")
				segments.append(seg)
				self.chatTabLineExtra = self.chatTabLineExtra + [seg]

			for i in xrange(len(segments)):
				seg = segments[i]
				if i < len(pieces) and pieces[i][1] > pieces[i][0]:
					(x0, x1) = pieces[i]
					seg.SetPosition(x0, 0)
					seg.SetRenderingRect(0.0, 0.0, float(x1 - x0) / float(self.CHAT_TAB_WIDTH) - 1.0, 0.0)
					seg.Show()
				else:
					seg.Hide()

			for (bar, cx, cy) in self.chatTabCornerRight:
				bar.SetPosition(width - cx, cy)

		def __RefreshChatTabs(self):
			selected = self.chatTabSelected
			for idx in xrange(len(self.chatTabs)):
				btn = self.chatTabs[idx]
				if idx in selected:
					image = self.CHAT_TAB_PATH + "chatmenutab_down.tga"
					btn.SetUpVisual(image)
					btn.SetOverVisual(image)
					btn.SetDownVisual(image)
				else:
					btn.SetUpVisual(self.CHAT_TAB_PATH + "chatmenutab_default.tga")
					btn.SetOverVisual(self.CHAT_TAB_PATH + "chatmenutab_drag.tga")
					btn.SetDownVisual(self.CHAT_TAB_PATH + "chatmenutab_down.tga")
				btn.SetText(self.chatTabList[idx][0])
				if btn.ButtonText:
					btn.ButtonText.SetPosition(btn.GetWidth() / 2, self.CHAT_TAB_TEXT_Y)

		def __GetAllChatTypes(self):
			return [chat.CHAT_TYPE_TALKING, chat.CHAT_TYPE_INFO, chat.CHAT_TYPE_NOTICE, chat.CHAT_TYPE_PARTY, chat.CHAT_TYPE_GUILD,
				chat.CHAT_TYPE_COMMAND, chat.CHAT_TYPE_SHOUT, chat.CHAT_TYPE_WHISPER, chat.CHAT_TYPE_BIG_NOTICE, chat.CHAT_TYPE_DICE_INFO,
				chat.CHAT_TYPE_CONTROL_NOTICE, chat.CHAT_TYPE_MISSION, chat.CHAT_TYPE_DUNGEON, chat.CHAT_TYPE_EXCHANGE, chat.CHAT_TYPE_DROP]

		def OnChatTabClicked(self, idx):
			if idx < 0 or idx >= len(self.chatTabList):
				return

			ctrl = app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)
			if ctrl and idx != 0:
				selected = [i for i in self.chatTabSelected if i != 0]
				if idx in selected:
					selected.remove(idx)
				else:
					selected.append(idx)
				if not selected:
					selected = [0]
			else:
				selected = [idx]
			self.chatTabSelected = selected
			self.chatTabIndex = idx

			modes = []
			for i in selected:
				if self.chatTabList[i][1] is None:
					modes = None
					break
				modes.extend(self.chatTabList[i][1])

			for chatType in self.__GetAllChatTypes():
				if modes is None or chatType in modes:
					chat.EnableChatMode(self.chatID, chatType)
				else:
					chat.DisableChatMode(self.chatID, chatType)

			chat.SetEndPos(self.chatID, 1.0)
			self.scrollBarPos = 1.0
			chat.ArrangeShowingChat(self.chatID)
			self.__RefreshChatTabs()
			self.__RefreshChatTabLine(self.GetWidth())
			self.Refresh()

	if app.ENABLE_CHAT_TABS:
		def OpenEmojiPicker(self):
			import uiemojipicker
			if not self.emojiPicker:
				self.emojiPicker = uiemojipicker.EmojiSelectorWindow()
			self.emojiPicker.SetChatLine(self.chatInputSet.chatLine)
			(bx, by) = self.btnEmoticonsOpen.GetGlobalPosition()
			self.emojiPicker.Toggle(bx + self.btnEmoticonsOpen.GetWidth() - uiemojipicker.WIDTH, by - uiemojipicker.HEIGHT - 4)

