// void CPythonChat::__Initialize() icinde:
// Ara:
	m_akD3DXClrChat[CHAT_TYPE_MISSION] = D3DXCOLOR(1.0f, 0.902f, 0.730f, 1.0f);

// Altina ekle:
#ifdef ENABLE_CHAT_TABS
	m_akD3DXClrChat[CHAT_TYPE_DUNGEON] = D3DXCOLOR(1.0f, 0.902f, 0.730f, 1.0f);	// notice colour
	m_akD3DXClrChat[CHAT_TYPE_EXCHANGE] = D3DXCOLOR(1.0f, 0.785f, 0.785f, 1.0f);	// info colour
	m_akD3DXClrChat[CHAT_TYPE_DROP] = D3DXCOLOR(1.0f, 0.785f, 0.785f, 1.0f);		// info colour
#endif

