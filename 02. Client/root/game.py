# GameWindow icinde ara:
	def RefreshQuest(self):
		self.interface.RefreshQuest()

# Altina ekle:
	def RefreshMessenger(self):
		self.interface.RefreshMessenger()


# GameWindow.BINARY_AdvancedGuildChat icinde ara:
	def BINARY_AdvancedGuildChat(self, line):

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER:
			return


# GameWindow icinde ara:
		chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, "[Guild]", line)
		self.interface.RecvWhisper("[Guild]")

# Altina ekle:
	def BINARY_WhisperMessengerGuildChat(self, line):
		if app.ENABLE_WHISPER_MESSENGER and self.interface:
			self.interface.RecvWhisperMessenger("[Guild]", line)


# GameWindow.OnRecvWhisper icinde ara:
		def OnRecvWhisper(self, mode, name, line, codepage = 0):

# Altina ekle:
			if app.ENABLE_WHISPER_MESSENGER:
				line = self.interface.PrepareGuildWhisper(name, line)


# GameWindow.OnRecvWhisper icinde ara:
				self.interface.RegisterGameMasterName(name)
			chat.AppendWhisper(mode, name, line, codepage)

# Altina ekle:
			if app.ENABLE_WHISPER_MESSENGER:
				self.interface.RecvWhisperMessenger(name, line)
				return


# GameWindow.OnRecvWhisper icinde ara:
		def OnRecvWhisper(self, mode, name, line):

# Altina ekle:
			if app.ENABLE_WHISPER_MESSENGER:
				line = self.interface.PrepareGuildWhisper(name, line)


# GameWindow.OnRecvWhisper icinde ara:
				self.interface.RegisterGameMasterName(name)
			chat.AppendWhisper(mode, name, line)

# Altina ekle:
			if app.ENABLE_WHISPER_MESSENGER:
				self.interface.RecvWhisperMessenger(name, line)
				return


# GameWindow.OnRecvWhisperSystemMessage icinde ara:
	def OnRecvWhisperSystemMessage(self, mode, name, line):
		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, line)

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER:
			self.interface.RecvWhisperMessenger(name, line, TRUE)
			return


# GameWindow.OnRecvWhisperError icinde ara:
			errorText = "Whisper Unknown Error(mode=%d, name=%s)" % (mode, name)
		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, errorText)

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER:
			if mode == 1 and self.interface.HandleWhisperNotLogon(name):
				return
			self.interface.RecvWhisperMessenger(name, errorText, TRUE)
			return


# GameWindow icinde ara:
		self.guildInviteQuestionDialog.Close()
		self.guildInviteQuestionDialog = None

# Altina ekle:
	def DeleteGuild(self):
		self.interface.DeleteGuild()


# GameWindow.__HideMapItemToolTip icinde ara:
		windowList = [self.interface.wndInventory, self.interface.wndSafebox, self.interface.wndMall, self.interface.wndCube,
			self.interface.dlgShop, self.interface.dlgExchange, self.interface.wndItemSelect, self.interface.wndCharacter,

# Altina ekle:
			self.interface.wndTaskBar, self.interface.wndGuild, self.interface.wndMessenger, self.interface.wndMiniMap,


# GameWindow icinde ara:
				self.affectShower.SetSungMaAffectImage(str, hp, move, immune)
	# WEDDING

# Altina ekle:
	def BINARY_LoverInfo(self, name, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnAddLover(name, lovePoint)
		if self.affectShower:
			self.affectShower.SetLoverInfo(name, lovePoint)

	def BINARY_UpdateLovePoint(self, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnUpdateLovePoint(lovePoint)
		if self.affectShower:
			self.affectShower.OnUpdateLovePoint(lovePoint)


# GameWindow icinde ara:
		except ValueError:
			pass

# Altina ekle:
	def AnkaGlobalChat(self, payload):
		if app.ENABLE_WHISPER_MESSENGER and self.interface:
			self.interface.RecvGlobalChat(payload)

	def AnkaWhisperInfo(self, name, found, empire, race, online, guildName):
		if app.ENABLE_WHISPER_MESSENGER and self.interface:
			self.interface.RecvWhisperPlayerInfo(name, int(found), int(empire), int(race), int(online), guildName.replace("\x1f", " "))

	def AnkaOfflineMsg(self, sender, sentAt, text):
		if app.ENABLE_WHISPER_MESSENGER and self.interface:
			self.interface.RecvOfflineWhisper(sender, int(sentAt), text.replace("\x1f", " "))

	def AnkaOfflineMsgResult(self, result, name):
		if app.ENABLE_WHISPER_MESSENGER and self.interface:
			self.interface.RecvOfflineWhisperResult(int(result), name)


# GameWindow icinde ara:
			import uiGuildApplication
			self.interface.OpenGuildJoinNotification(int(GID), name.replace("\x1f", " "), uiGuildApplication.Decode(desc))

# Altina ekle:
	def ServerCommand_MessengerInfo(self, group, name, level, race, channel, mapIndex, lastSeen, countryFlag = "-"):
		if app.ENABLE_MESSENGER_DETAILS and self.interface and self.interface.wndMessenger:
			self.interface.wndMessenger.OnMemberInfo(int(group), name, int(level), int(race), int(channel), int(mapIndex), int(lastSeen))

	def AnkaGlobalCooldown(self, seconds):
		if app.ENABLE_WHISPER_MESSENGER and self.interface:
			self.interface.RecvGlobalChatCooldown(seconds)


# GameWindow.__ServerCommand_Build icinde ara:
			"SetBraveCapeStatus" : self.SetBraveCapeStatus,
			"CharacterStats" : self.CharacterStats,

# Altina ekle:
			"AnkaGlobalChat" : self.AnkaGlobalChat,
			"AnkaGlobalCooldown" : self.AnkaGlobalCooldown,
			"AnkaWhisperInfo" : self.AnkaWhisperInfo,
			"AnkaOfflineMsg" : self.AnkaOfflineMsg,
			"AnkaOfflineMsgResult" : self.AnkaOfflineMsgResult,


# GameWindow.__ServerCommand_Build icinde ara:
			"GuildAppNewRequest" : self.GuildAppNewRequest,
			"Guild_JoinNotify" : self.ServerCommand_Guild_JoinNotify,

# Altina ekle:
			"MessengerInfo" : self.ServerCommand_MessengerInfo,


# GameWindow.__ServerCommand_Build icinde ara:
			"test_server"									: self.__EnableTestServerFlag,
			"mall"											: self.__InGameShop_Show,

# Altina ekle:
			"lover_login"									: self.__LoginLover,
			"lover_logout"									: self.__LogoutLover,


# GameWindow.__ServerCommand_Build icinde ara:
			"lover_near"									: self.__LoverNear,
			"lover_far"										: self.__LoverFar,

# Altina ekle:
			"lover_divorce"									: self.__LoverDivorce,


# GameWindow icinde ara:
			self.interface.OpenWebWindow(url)
	# WEDDING

# Altina ekle:
	def __LoginLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLoginLover()

	def __LogoutLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogoutLover()
		if self.affectShower:
			self.affectShower.HideLoverState()


# GameWindow icinde ara:
		if self.affectShower:
			self.affectShower.HideLoverState()

# Altina ekle:
	def __LoverDivorce(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.ClearLoverInfo()
		if self.affectShower:
			self.affectShower.ClearLoverState()


# GameWindow.RecvReadWiki icinde ara:
	def RecvReadWiki(self):

# Altina ekle:
		if app.ENABLE_WHISPER_MESSENGER:
			return

