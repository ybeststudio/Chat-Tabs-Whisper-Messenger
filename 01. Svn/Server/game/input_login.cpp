// void CInputLogin::Entergame(LPDESC d, const char * data) icinde:
// Ara:
	GuildQuest_OnLogin(ch);

// Altina ekle:
#ifdef ENABLE_MESSENGER_DETAILS
	MessengerDetails_OnLogin(ch);
#endif

