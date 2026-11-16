# BiologistWindow.CheckTime icinde ara:
		if self.notifyPending and self.__Left() <= 0:
			self.notifyPending = False

# Altina ekle:
			if self.checkCall.GetCheckStatus() and self.interface and app.ENABLE_WHISPER_MESSENGER:
				self.interface.RecvWhisperMessenger(localeInfo.BIOLOG_SENDER, localeInfo.BIOLOG_SENDER + " : " + localeInfo.BIOLOG_READY)

