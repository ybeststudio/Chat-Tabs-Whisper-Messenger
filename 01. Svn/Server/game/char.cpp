// void CHARACTER::ChatPacket (BYTE type, const char* format, ...) icinde:
// Ara:
	// Sistem mesajlarini aliciya gelen oyuncunun diline cevir (per-player multilanguage)
	if (type == CHAT_TYPE_INFO || type == CHAT_TYPE_NOTICE || type == CHAT_TYPE_BIG_NOTICE || type == CHAT_TYPE_TALKING

// Altina ekle:
#ifdef ENABLE_CHAT_TABS
		|| type == CHAT_TYPE_DUNGEON || type == CHAT_TYPE_EXCHANGE || type == CHAT_TYPE_DROP
#endif


// void CHARACTER::LocaleChatPacket(BYTE type, DWORD index, const char* format, ...) icinde:
// Ara:
		&& type != CHAT_TYPE_CONTROL_NOTICE

// Altina ekle:
#ifdef ENABLE_CHAT_TABS
		&& type != CHAT_TYPE_DUNGEON && type != CHAT_TYPE_EXCHANGE && type != CHAT_TYPE_DROP
#endif

