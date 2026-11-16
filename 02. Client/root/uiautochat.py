# AutoChatWindow.OpenEmoji icinde ara:
	def OpenEmoji(self, editLine, anchorBtn):

# Altina ekle:
		import uiemojipicker


# AutoChatWindow.OpenEmoji icinde ara:
		if not self.emojiPicker:

# Altina ekle:
			self.emojiPicker = uiemojipicker.EmojiSelectorWindow()


# AutoChatWindow.OpenEmoji icinde ara:
		self.emojiPicker.SetChatLine(editLine)
		(bx, by) = anchorBtn.GetGlobalPosition()

# Altina ekle:
		self.emojiPicker.Toggle(bx + anchorBtn.GetWidth() - uiemojipicker.WIDTH, by - uiemojipicker.HEIGHT - 4)

