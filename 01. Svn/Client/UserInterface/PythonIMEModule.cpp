// Ara:
	CPythonIME::Instance().PasteTextFromClipBoard();
	return Py_BuildNone();
}

// Altina ekle:
#ifdef ENABLE_WHISPER_MESSENGER
PyObject *imeCopyTextToClipBoard(PyObject *poSelf, PyObject *poArgs)
{
	char * szText;
	if (!PyTuple_GetString(poArgs, 0, &szText))
		return Py_BuildException();

	const size_t len = strlen(szText);
	if (!::OpenClipboard(CPythonApplication::Instance().GetWindowHandle()))
		return Py_BuildValue("i", 0);

	::EmptyClipboard();
	HGLOBAL hMem = ::GlobalAlloc(GMEM_MOVEABLE, len + 1);
	if (hMem)
	{
		char * pDest = static_cast<char *>(::GlobalLock(hMem));
		if (pDest)
		{
			memcpy(pDest, szText, len + 1);
			::GlobalUnlock(hMem);
			if (!::SetClipboardData(CF_TEXT, hMem))
				::GlobalFree(hMem);
		}
		else
			::GlobalFree(hMem);
	}
	::CloseClipboard();
	return Py_BuildValue("i", 1);
}
#endif


// void initime() icinde:
// Ara:
		{ "PasteReturn",			imePasteReturn,				METH_VARARGS },
		{ "PasteTextFromClipBoard",	imePasteTextFromClipBoard,	METH_VARARGS },
		{ "EnablePaste",			imeEnablePaste,				METH_VARARGS },

// Altina ekle:
#ifdef ENABLE_WHISPER_MESSENGER
		{ "CopyTextToClipBoard",	imeCopyTextToClipBoard,		METH_VARARGS },
#endif

