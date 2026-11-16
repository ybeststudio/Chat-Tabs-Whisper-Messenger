// Ara:
{
	return Py_BuildValue("i", GetCodePage());
}

// Altina ekle:
#ifdef ENABLE_CLIPBOARD_TEXT
PyObject* appSetClipboardText(PyObject* poSelf, PyObject* poArgs)
{
	char* szText;
	if (!PyTuple_GetString(poArgs, 0, &szText))
		return Py_BuildException();

	const int iLength = MultiByteToWideChar(GetCodePage(), 0, szText, -1, NULL, 0);
	if (iLength <= 0)
		return Py_BuildValue("i", 0);

	HGLOBAL hMemory = GlobalAlloc(GMEM_MOVEABLE, iLength * sizeof(wchar_t));
	if (!hMemory)
		return Py_BuildValue("i", 0);

	wchar_t* pwText = (wchar_t*)GlobalLock(hMemory);
	MultiByteToWideChar(GetCodePage(), 0, szText, -1, pwText, iLength);
	GlobalUnlock(hMemory);

	if (!OpenClipboard(NULL))
	{
		GlobalFree(hMemory);
		return Py_BuildValue("i", 0);
	}

	EmptyClipboard();
	if (!SetClipboardData(CF_UNICODETEXT, hMemory))
	{
		CloseClipboard();
		GlobalFree(hMemory);
		return Py_BuildValue("i", 0);
	}

	CloseClipboard();
	return Py_BuildValue("i", 1);
}
#endif


// void initapp() icinde:
// Ara:
		{ "LoadLocaleAddr",				appLoadLocaleAddr,				METH_VARARGS },
		{ "LoadLocaleData",				appLoadLocaleData,				METH_VARARGS },
		{ "GetDefaultCodePage",			appGetDefaultCodePage,			METH_VARARGS },

// Altina ekle:
#ifdef ENABLE_CLIPBOARD_TEXT
		{ "SetClipboardText",			appSetClipboardText,			METH_VARARGS },
#endif


// void initapp() icinde:
// Ara:
	PyModule_AddIntConstant(poModule, "ENABLE_BUFFI_CHANGE_SEX", 0);

// Altina ekle:
#ifdef ENABLE_WHISPER_MESSENGER
	PyModule_AddIntConstant(poModule, "ENABLE_WHISPER_MESSENGER", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_WHISPER_MESSENGER", 0);
#endif


// void initapp() icinde:
// Ara:
	PyModule_AddIntConstant(poModule, "ENABLE_GUILD_APPLICATION", 0);

// Altina ekle:
#ifdef ENABLE_MESSENGER_DETAILS
	PyModule_AddIntConstant(poModule, "ENABLE_MESSENGER_DETAILS", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_MESSENGER_DETAILS", 0);
#endif


// void initapp() icinde:
// Ara:
	PyModule_AddIntConstant(poModule, "ENABLE_AUTO_CHAT", 0);

// Altina ekle:
#ifdef ENABLE_CHAT_TABS
	PyModule_AddIntConstant(poModule, "ENABLE_CHAT_TABS", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_CHAT_TABS", 0);
#endif


// void initapp() icinde:
// Ara:
	PyModule_AddIntConstant(poModule, "ENABLE_DUNGEON_LIMIT_RENEWAL", 0);

// Altina ekle:
#ifdef ENABLE_CLIPBOARD_TEXT
	PyModule_AddIntConstant(poModule, "ENABLE_CLIPBOARD_TEXT", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_CLIPBOARD_TEXT", 0);
#endif

