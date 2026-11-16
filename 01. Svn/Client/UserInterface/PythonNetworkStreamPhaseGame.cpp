// bool CPythonNetworkStream::RecvChatPacket() icinde:
// Ara:
		ServerCommand(buf);
		return true;
	}

// Altina ekle:
#ifdef ENABLE_WHISPER_MESSENGER
	if (CHAT_TYPE_GUILD == kChat.type)
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_WhisperMessengerGuildChat", Py_BuildValue("(s)", buf));
#endif


// bool CPythonNetworkStream::RecvChatPacket() icinde:
// Bul:
			kChat.type = CHAT_TYPE_NOTICE;

// Degistir:
#ifdef ENABLE_CHAT_TABS
			kChat.type = CHAT_TYPE_DUNGEON;
#else
			kChat.type = CHAT_TYPE_NOTICE;
#endif


// bool CPythonNetworkStream::RecvChatPacket() icinde:
// Ara:
		if (CHAT_TYPE_NOTICE == kChat.type

// Altina ekle:
#ifdef ENABLE_CHAT_TABS
			|| CHAT_TYPE_DUNGEON == kChat.type
#endif


// bool CPythonNetworkStream::RecvLocaleChatPacket() icinde:
// Ara:
		 && kLocaleChatPacket.type != CHAT_TYPE_CONTROL_NOTICE

// Altina ekle:
#ifdef ENABLE_CHAT_TABS
		 && kLocaleChatPacket.type != CHAT_TYPE_DUNGEON && kLocaleChatPacket.type != CHAT_TYPE_EXCHANGE && kLocaleChatPacket.type != CHAT_TYPE_DROP
#endif


// bool CPythonNetworkStream::RecvLocaleChatPacket() icinde:
// Ara:
			}
		}
		if (CHAT_TYPE_NOTICE == kLocaleChatPacket.type

// Altina ekle:
#ifdef ENABLE_CHAT_TABS
			|| CHAT_TYPE_DUNGEON == kLocaleChatPacket.type
#endif

