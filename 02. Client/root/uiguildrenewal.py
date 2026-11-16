# Ara:
import ime
import uiGuild

# Altina ekle:
import uiMessengerRenewal


# _IsMemberOnline icinde ara:
		return True
	interface = constInfo.GetInterfaceInstance()

# Altina ekle:
	wnd = interface.wndMessenger if interface else None
	if wnd and app.ENABLE_MESSENGER_DETAILS:
		return wnd.IsGuildMemberOnline(name)


# InfoPage.__init__ icinde ara:
		self.blessingHover.Show()
		self.isBlessingHover = False

# Altina ekle:
		self.blessingScroll = uiMessengerRenewal.ThinScrollBar()


# ShopPage.__init__ icinde ara:
		self.view.SetInsideRender(True)
		self.view.Show()

# Altina ekle:
		self.scrollBar = uiMessengerRenewal.ThinScrollBar()


# Ara:
	def OnPressEscapeKey(self):
		return self.Close()

# Altina ekle:
class HitWindow(uiMessengerRenewal.HitWindow):
	def __init__(self, parent):
		self.onRightClick = None
		uiMessengerRenewal.HitWindow.__init__(self, parent)

	def Place(self, x, y, width, height):
		top = max(0, y)
		bottom = min(MEMBER_VIEW_HEIGHT, y + height)
		if bottom <= top:
			self.Hide()
			return
		self.SetPosition(x, top)
		self.SetSize(width, bottom - top)
		self.Show()

	def OnMouseRightButtonDown(self):
		if self.onRightClick:
			self.onRightClick()
		return True


# MemberPage.__init__ icinde ara:
		self.content.SetSize(MEMBER_VIEW_WIDTH, MEMBER_VIEW_HEIGHT)
		self.content.Show()

# Altina ekle:
		self.scrollBar = uiMessengerRenewal.ThinScrollBar()


# GuildWindow icinde ara:
		if self.legacy:
			self.legacy.Destroy()

# Altina ekle:
	def DeleteGuild(self):
		self.legacy.DeleteGuild()
		self.SetQuestInfo(0, 0, 0, 0, 0, 0, 0, 0, 0)
		self.Close()


# GuildWindow.OnRightClickMember icinde ara:
			entries.append((localeInfo.GUILD_WINDOW_MENU_EXCLUDE, "menu_exclude.png", lambda : self.__AskExclude(name, member["pid"])))
		if not self.contextMenu:

# Altina ekle:
			import uiWhisperMessenger
			self.contextMenu = uiWhisperMessenger.MessageContextMenu()

