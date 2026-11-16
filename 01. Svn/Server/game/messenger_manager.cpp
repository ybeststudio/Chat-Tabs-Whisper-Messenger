// Dosyanin uygun bir yerine ekle:
#ifdef ENABLE_MESSENGER_DETAILS
#include "messenger_details.h"
#endif


// void MessengerManager::SendLogin(MessengerManager::keyA account, MessengerManager::keyA companion) icinde:
// Ara:
	d->BufferedPacket(&pack, sizeof(TPacketGCMessenger));
	d->BufferedPacket(&bLen, sizeof(BYTE));
	d->Packet(companion.c_str(), companion.size());

// Altina ekle:
#ifdef ENABLE_MESSENGER_DETAILS
	MessengerDetails_OnFriendLogin(account.c_str(), companion.c_str());
#endif

