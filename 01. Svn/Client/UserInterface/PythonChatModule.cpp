// void initChat() icinde:
// Ara:
	PyModule_AddIntConstant(poModule, "CHAT_TYPE_MISSION", CHAT_TYPE_MISSION);

// Altina ekle:
#ifdef ENABLE_CHAT_TABS
	PyModule_AddIntConstant(poModule, "CHAT_TYPE_DUNGEON", CHAT_TYPE_DUNGEON);
	PyModule_AddIntConstant(poModule, "CHAT_TYPE_EXCHANGE", CHAT_TYPE_EXCHANGE);
	PyModule_AddIntConstant(poModule, "CHAT_TYPE_DROP", CHAT_TYPE_DROP);
#endif

