#*********************************************************************
# File Name : uiautochat.py
# Author    : BestStudio
# Version   : 1.0.0
# Date      : 13-11-2026
#
# Data/UserData/autochat/<name>.txt; slots always start disabled.
#*********************************************************************
if __USE_DYNAMIC_MODULE__:
	import pyapi

app = __import__(pyapi.GetModuleName("app"))
player = __import__(pyapi.GetModuleName("player"))
net = __import__(pyapi.GetModuleName("net"))

import chat
import ui
import localeInfo
import userdata

AUTO_CHAT_ASSET_PATH = "d:/ymir work/ui/game/auto_chat/"
AUTO_CHAT_INTERVAL_SEC = 15
AUTO_CHAT_MAX_MESSAGE_LEN = 511
AUTO_CHAT_SLOT_COUNT = 3

CHECKBOX_PATH = "d:/ymir work/ui/game/common/"

BOARD_WIDTH = 486
BOARD_HEIGHT = 216
SLOT_Y = 27
SLOT_STEP = 60
ITEM_X = 5
ITEM_W = 476
ITEM_H = 65
EDIT_BG_X = 14
EDIT_BG_Y = 8
EDIT_X = 6				# text inside editline_bg.png
EDIT_Y = 4
EDIT_W = 447
CHECK_X = 14
CHECK_Y = 37
STATE_X = 36
STATE_Y = 46
SHOP_BTN_X = 412
EMOJI_BTN_X = 444
BTN_Y = 31
PLACEHOLDER_COLOR = 0xff8a8178

SHOP_LINK = "|cffffc700|Hshop:%s|h[Shop-%s]|h|r"


class BoxToolTip(ui.ThinBoard):
	PADDING_X = 24
	HEIGHT = 36
	GAP = 5

	def __init__(self, text):
		ui.ThinBoard.__init__(self, "TOP_MOST")
		self.AddFlag("float")
		self.AddFlag("not_pick")
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.SetText(text)
		self.textLine.Show()
		(w, h) = self.textLine.GetTextSize()
		self.SetSize(w + self.PADDING_X * 2, self.HEIGHT)
		self.textLine.SetPosition(self.GetWidth() / 2, self.HEIGHT / 2)
		self.Hide()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def ShowAbove(self, button):
		(bx, by) = button.GetGlobalPosition()
		self.SetPosition(bx + button.GetWidth() / 2 - self.GetWidth() / 2, by - self.HEIGHT - self.GAP)
		self.Show()
		self.SetTop()


def BindBoxToolTip(button, text):
	toolTip = BoxToolTip(text)
	button.SetShowToolTipEvent(lambda b = button, t = toolTip: t.ShowAbove(b))
	button.SetHideToolTipEvent(lambda t = toolTip: t.Hide())
	return toolTip


class AutoChatItem(ui.Window):
	def __init__(self, owner, index):
		ui.Window.__init__(self)
		self.owner = owner
		self.index = index
		self.enabled = False
		self.nextTime = 0.0
		self.__Build()

	def __del__(self):
		ui.Window.__del__(self)

	def __Build(self):
		self.SetSize(ITEM_W, ITEM_H)

		bg = ui.ExpandedImageBox()
		bg.SetParent(self)
		bg.AddFlag("not_pick")
		bg.LoadImage(AUTO_CHAT_ASSET_PATH + "item_bg.png")
		bg.SetScale(float(ITEM_W) / 478.0, 1.0)
		bg.SetPosition(0, 0)
		bg.Show()
		self.bg = bg

		editBg = ui.ImageBox()
		editBg.SetParent(self)
		editBg.LoadImage(AUTO_CHAT_ASSET_PATH + "editline_bg.png")
		editBg.SetPosition(EDIT_BG_X - ITEM_X, EDIT_BG_Y)
		editBg.Show()
		self.editBg = editBg

		editLine = ui.EditLine()
		editLine.SetParent(editBg)
		editLine.SetPosition(EDIT_X, EDIT_Y)
		editLine.SetSize(EDIT_W, 15)
		editLine.SetMax(AUTO_CHAT_MAX_MESSAGE_LEN)
		editLine.SetText("")
		editLine.SetEscapeEvent(ui.__mem_func__(self.__OnEditLineEscape))
		editLine.SetReturnEvent(ui.__mem_func__(self.__OnEditLineEscape))
		editLine.Show()
		self.editLine = editLine

		placeHolder = ui.TextLine()
		placeHolder.SetParent(editBg)
		placeHolder.AddFlag("not_pick")
		placeHolder.SetPosition(EDIT_X, EDIT_Y)
		placeHolder.SetPackedFontColor(PLACEHOLDER_COLOR)
		placeHolder.SetText(localeInfo.AUTO_CHAT_PLACEHOLDER)
		placeHolder.Show()
		self.placeHolder = placeHolder

		check = ui.Button()
		check.SetParent(self)
		check.SetPosition(CHECK_X - ITEM_X, CHECK_Y)
		check.SetEvent(ui.__mem_func__(self.__OnCheck))
		check.Show()
		self.check = check

		state = ui.TextLine()
		state.SetParent(self)
		state.SetPosition(STATE_X - ITEM_X, STATE_Y)
		state.SetVerticalAlignCenter()
		state.Show()
		self.state = state

		shopBtn = ui.Button()
		shopBtn.SetParent(self)
		shopBtn.SetUpVisual(AUTO_CHAT_ASSET_PATH + "btn_link_shop_norm.png")
		shopBtn.SetOverVisual(AUTO_CHAT_ASSET_PATH + "btn_link_shop_hover.png")
		shopBtn.SetDownVisual(AUTO_CHAT_ASSET_PATH + "btn_link_shop_select.png")
		shopBtn.SetPosition(SHOP_BTN_X - ITEM_X, BTN_Y)
		shopBtn.SetEvent(ui.__mem_func__(self.__OnClickShop))
		shopBtn.Show()
		self.shopBtn = shopBtn
		self.shopToolTip = BindBoxToolTip(shopBtn, localeInfo.AUTO_CHAT_ADD_SHOP_LINK)

		emojiBtn = ui.Button()
		emojiBtn.SetParent(self)
		emojiBtn.SetUpVisual(AUTO_CHAT_ASSET_PATH + "btn_emoji_norm.png")
		emojiBtn.SetOverVisual(AUTO_CHAT_ASSET_PATH + "btn_emoji_hover.png")
		emojiBtn.SetDownVisual(AUTO_CHAT_ASSET_PATH + "btn_emoji_select.png")
		emojiBtn.SetPosition(EMOJI_BTN_X - ITEM_X, BTN_Y)
		emojiBtn.SetEvent(ui.__mem_func__(self.__OnClickEmoji))
		emojiBtn.Show()
		self.emojiBtn = emojiBtn
		self.emojiToolTip = BindBoxToolTip(emojiBtn, localeInfo.AUTO_CHAT_ADD_EMOJI)

		self.RefreshCheck()
		self.RefreshStateText()

	def Destroy(self):
		self.shopToolTip.Hide()
		self.emojiToolTip.Hide()
		self.owner = None

	def SetData(self, enabled, message):
		self.enabled = enabled
		self.editLine.SetText(message)
		self.RefreshCheck()
		self.RefreshStateText()

	def GetMessage(self):
		return self.editLine.GetText().strip()

	def RefreshCheck(self):
		image = CHECKBOX_PATH + ("checkbox2_check.png" if self.enabled else "checkbox2_no.png")
		self.check.SetUpVisual(image)
		self.check.SetOverVisual(image)
		self.check.SetDownVisual(image)

	def RefreshStateText(self, secondsLeft = None):
		if not self.enabled:
			self.state.SetText(localeInfo.AUTO_CHAT_DISABLED)
		elif secondsLeft is None:
			self.state.SetText(localeInfo.AUTO_CHAT_ENABLED)
		else:
			self.state.SetText(localeInfo.AUTO_CHAT_NEXT % secondsLeft)

	def __OnCheck(self):
		if not self.enabled and not self.GetMessage():
			return
		self.enabled = not self.enabled
		self.nextTime = 0.0		# first message right away
		self.RefreshCheck()
		self.RefreshStateText()
		if self.owner:
			self.owner.OnItemChanged()

	def __OnEditLineEscape(self):
		self.editLine.KillFocus()
		if self.owner:
			self.owner.OnItemChanged()

	def __OnClickShop(self):
		name = player.GetName()
		link = SHOP_LINK % (name, name)
		text = self.editLine.GetText()
		if len(text) + len(link) > AUTO_CHAT_MAX_MESSAGE_LEN:
			return
		self.editLine.SetText(text + link)
		self.editLine.SetFocus()
		if self.owner:
			self.owner.OnItemChanged()

	def __OnClickEmoji(self):
		if self.owner:
			self.owner.OpenEmoji(self.editLine, self.emojiBtn)

	def Tick(self, now):
		if not self.enabled:
			return
		message = self.GetMessage()
		if not message:
			self.enabled = False
			self.RefreshCheck()
			self.RefreshStateText()
			return
		if now >= self.nextTime:
			self.nextTime = now + AUTO_CHAT_INTERVAL_SEC
			if net.IsChatInsultIn(message):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHAT_INSULT_STRING)
			elif app.ENABLE_MULTILANGUAGE_CHATTING:
				net.SendChatPacket(message, chat.CHAT_TYPE_SHOUT, 0)
			else:
				net.SendChatPacket(message, chat.CHAT_TYPE_SHOUT)
		self.RefreshStateText(max(0, int(self.nextTime - now + 0.999)))

	def OnUpdate(self):
		self.placeHolder.Show() if (not self.editLine.GetText() and not self.editLine.IsFocus()) else self.placeHolder.Hide()


class AutoChatWindow(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.AddFlag("movable")
		self.AddFlag("float")
		self.SetSize(BOARD_WIDTH, BOARD_HEIGHT)
		self.SetTitleName(localeInfo.AUTO_CHAT_TITLE)
		self.SetCloseEvent(ui.__mem_func__(self.Close))
		self.interface = None
		self.emojiPicker = None
		self.loadedName = None
		self.items = []
		for i in xrange(AUTO_CHAT_SLOT_COUNT):
			item = AutoChatItem(self, i)
			item.SetParent(self)
			item.SetPosition(ITEM_X, SLOT_Y + i * SLOT_STEP)
			item.Show()
			self.items.append(item)
		self.SetCenterPosition()
		self.Hide()

	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def BindInterface(self, interface):
		self.interface = interface

	def Destroy(self):
		self.__Save()
		for item in self.items:
			item.Destroy()
		self.items = []
		if self.emojiPicker:
			self.emojiPicker.Hide()
		self.emojiPicker = None
		self.interface = None

	def Open(self):
		self.__Load()
		self.Show()
		self.SetTop()

	def Close(self):
		self.__Save()
		if self.emojiPicker:
			self.emojiPicker.Hide()
		self.Hide()

	def Toggle(self):
		if self.IsShow():
			self.Close()
		else:
			self.Open()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnItemChanged(self):
		self.__Save()

	def OpenEmoji(self, editLine, anchorBtn):
		import uiemojipicker
		if not self.emojiPicker:
			self.emojiPicker = uiemojipicker.EmojiSelectorWindow()
		self.emojiPicker.SetChatLine(editLine)
		(bx, by) = anchorBtn.GetGlobalPosition()
		self.emojiPicker.Toggle(bx + anchorBtn.GetWidth() - uiemojipicker.WIDTH, by - uiemojipicker.HEIGHT - 4)

	def Tick(self):
		self.__Load()
		now = app.GetTime()
		for item in self.items:
			item.Tick(now)

	def __FileName(self):
		name = player.GetName()
		if not name:
			return None
		return userdata.GetPath("%s.txt" % name, "autochat", "")

	def __Load(self):
		name = player.GetName()
		if not name or name == self.loadedName:
			return
		self.loadedName = name
		messages = [""] * AUTO_CHAT_SLOT_COUNT
		try:
			path = self.__FileName()
			if path:
				lines = open(path, "r").read().split("\n")
				for i in xrange(min(AUTO_CHAT_SLOT_COUNT, len(lines))):
					messages[i] = lines[i].rstrip("\r")
		except:
			pass
		for i in xrange(AUTO_CHAT_SLOT_COUNT):
			self.items[i].SetData(False, messages[i])

	def __Save(self):
		if not self.loadedName or self.loadedName != player.GetName():
			return
		try:
			path = self.__FileName()
			if path:
				f = open(path, "w")
				f.write("\n".join([item.editLine.GetText().replace("\n", " ") for item in self.items]))
				f.close()
		except:
			pass
