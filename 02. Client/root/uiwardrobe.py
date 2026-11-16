# WardrobeWindow.__CopyOutfitLink icinde ara:
		looks = self.draft if self.__IsEditing() else self.controller.activeLooks
		text = "outfit:1:" + ":".join(["%d" % v for v in looks])

# Altina ekle:
		copied = app.ENABLE_CLIPBOARD_TEXT and app.SetClipboardText(text) == 1

