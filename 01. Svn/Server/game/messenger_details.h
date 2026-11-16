/*********************************************************************
 * File Name : messenger_details.cpp
 * Author    : BestStudio
 * Version   : 1.0.0
 * Date      : 04-11-2026  
 */

#pragma once

#include "../../common/service.h"

#ifdef ENABLE_MESSENGER_DETAILS
void MessengerDetails_OnLogin(LPCHARACTER ch);
void MessengerDetails_OnFriendLogin(const char* account, const char* companion);
#endif
