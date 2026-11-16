# GuildWindow icinde ara:
		self.moneyDialog = None
		self.enemyGuildNameList = []

# Altina ekle:
	def DeleteGuild(self):
		self.RefreshGuildInfoPage()
		self.RefreshGuildBoardPage()
		self.RefreshGuildMemberPage()
		self.RefreshGuildSkillPage()
		self.RefreshGuildGradePage()
		self.Hide()

