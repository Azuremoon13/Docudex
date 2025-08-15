---
title: Configuration
description: Config options for LACC
keywords: LACC Config, LACC setup
---

# Configuration

This mod **requires some setup** to work. At minimum, required options must be set in `GameUserSettings.ini` and an api/webhook should be available to connect to using the configured settings. info about API at bottom of the page.  
  
  
Options should be placed under the header `[LACC]` in `GameUserSettings.ini` or set in the ingame settings UI.

<span style="font-size: 1.5em; font-weight: bold;">Either  `URL` OR `DiscordWebhookURL` is required for this mod to function </span>

#### API

| Option Name          | Type   | Default | Description                                                                                       |
| -------------------- | ------ | ------- | ------------------------------------------------------------------------------------------------- |
| `URL`                | string | 		  | Optional URL for endpoint. Format: `ws://ip:port` or `wss://` if using SSL.                       |
| `Token`              | string | 		  | **Required** security token sent to backend API to establish connection (see Server API section). |
| `TribeAlliedChat`    | bool   | True    | Optional toggle for Tribe/Allied cross-chat.                                                      |
| `Name`               | string | 		  | Optional custom name for the map.                                                                 |
| `AutoReconnectDelay` | int    | 600     | Time in seconds before mod attempts autoreconnection if socket is dead.                           |
| `PassSystemMessages` | bool   | True    | Pass system messages to API (e.g., Welcome/Depart messages).                                      |
| `SystemName`         | string | 		  | Optional name for these messages to be sent by.                                                   |
| `MapColour`          | string | 		  | CSV string `r,g,b,a` for map colour in API messages (values 0–255).                               |
| `BlockedPrefixCSV`   | string | 		  | CSV list of blocked prefixes that will not be sent to the API.                                    |


#### Discord

| Option Name          | Type   | Default | Description                                                                 |
| -------------------- | ------ | ------- | --------------------------------------------------------------------------- |
| `DiscordWebhookURL`  | string | 		  | Optional URL for posting chat to a Discord channel.                         |
| `DiscordWebhookIcon` | string | 		  | Optional URL to override Discord webhook icon (only used for Discord post). |


This [guide](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) provided by Discord can instruct you in setting up a webhook

#### Chat

| Option Name               | Type   | Default            | Description                                                                                                                                                    |
| ------------------------- | ------ |:------------------:| -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CompatibilityMode`       | bool   | `False`            | Allows the mod to function with others when they have replaced chat (will lose some extra functions soon to be added, e.g., ChatCommands).                     |
| `AllowOnlineCountPvP`     | bool   | `False`            | Overrides the visibility for showing online player count in PvP.                                                                                               |
| `EmojiParseMode`          | int    | `0`                | Defines how the mod handles emojis and coloured messages (must match your custom message format).                                                              |
| `WelcomeMessage`          | string |                    | Optional message displayed in chat when a player joins.                                                                                                        |
| `WelcomeMessageMode`      | int    | `0`                | Mode for how the welcome message is sent.                                                                                                                      |
| `DepartMessage`           | string |			          | Optional message displayed in chat when a player leaves.                                                                                                       |
| `DepartMessageMode`       | int    | `0`                | Mode for how the depart message is sent.                                                                                                                       |
| `AdminOverridesMapColour` | bool   | `True`             | Uses the admin colour in chat instead of the set map colour.                                                                                                   |
| `DisableMapColour`        | bool   | `False`            | Removes the custom map colour from API messages and uses default ARK colours.                                                                                  |
| `MessageColourCSV`        | string | `1,1,1,1`          | Colour to change the messages from the API (default is white).                                                                                                 |
| `CustomMessageFormat`     | string | &lt;RichColor Color="$mapColour$"&gt;[$timestamp$] [$mapName$] $playerName$$tribeName$ $sendMode$&lt;/&gt;: $message$ | Custom message formatting for API messages. 			   |


`WelcomeMessage` has the following arguments (Note - This is optional but without this the first message sent in compatibility mode by a player could be missed):  
- `$playerName$` = Player Name  
- `$tribeName$`= Tribe Name  
- `$mapName$` = Map Name  
  
`WelcomeMessageMode` has the following options:  
- `0` = Off  
- `1` = Sent to Player  
- `2` = Sent to Tribe  
- `3` = Sent to Global  
  
`DepartMessage` has the following arguments:  
- `$playerName$` = Player Name  
- `$tribeName$` = Tribe Name  
- `$mapName$` = Map Name  
  
`DepartMessageMode` has the following options:  
- `0` = Off  
- `1` = Sent to Tribe  
- `2` = Sent to Global  
  
`CustomMessageFormat` has the following arguments:  
- `$mapColour$` = r,g,b,a value for map colour (Between 0 - 1)  
- `$messageColour$` = r,g,b,a value for message colour (Between 0 - 1)  
- `$timestamp$` = timestamp of message recieved (players local time)  
- `$mapName$` = Custom map name  
- `$playerName$` = Player name of sender  
- `$tribeName$` = Tribe name of sender  
- `$message$` = Message content  
- `$sendMode$` = Mode the chat was sent in  
- `$chatTypeColour$` =  r,g,b,a value for default ark message colours  

`EmojiParseMode` has the following options:  
- `0` = Off  
- `1` = messageColour  
- `2` = mapColour  
- `3` = chatTypeColour  

#### Core

| Option Name             | Type    | Default | Description                                         |
| ----------------------- | ------- | ------- | --------------------------------------------------- |
| `RemoteDebuggerWebhook` | string  |         | Accepts a Discord webhook to post logs to a channel |
| `VerboseLogging`        | boolean | False   | Optional toggle to log all messages received        |
| `BlockInGameSettings`   | boolean | False   | Blocks the in-game settings from being used/loaded  |
| `AnalyticLevel`         | integer | 1       | Used for some remote mod analytics                  |
| `UnredactAnalytics`     | boolean | False   | Used to de-anonymise analytics                      |

there is also a `PayloadVersion` option for anyone building their own API to integrate the mod with, by default it will send the version baked into the mod (`3` currently). Editing this is not advised unless you know what you're doing.  

#### Chat Commands

| Option Name                         | Type    | Default | Description                                           |
| ----------------------------------- | ------- | ------- | ----------------------------------------------------- |
| `ChatCommandPrefix`                 | string  | `/`     | Prefix for chat command activation                    |
| `AllowMCICCAddition`                | boolean | true    | Allows mods to use MCI to add chat commands           |
| `AllowMCICCAlteration`              | boolean | true    | Allows mods to use MCI to edit chat commands          |
| `AllowMCICCRemoval`                 | boolean | true    | Allows mods to use MCI to remove chat commands        |
| `MCICCAdditionOriginTagWhitelist`   | string  |         | CSV whitelist for mod tags allowed to add commands    |
| `MCICCAdditionOriginTagBlacklist`   | string  |         | CSV blacklist for mod tags allowed to add commands    |
| `MCICCAlterationOriginTagWhitelist` | string  |         | CSV whitelist for mod tags allowed to edit commands   |
| `MCICCAlterationOriginTagBlacklist` | string  |         | CSV blacklist for mod tags allowed to edit commands   |
| `MCICCRemovalOriginTagWhitelist`    | string  |         | CSV whitelist for mod tags allowed to remove commands |
| `MCICCRemovalOriginTagBlacklist`    | string  |         | CSV blacklist for mod tags allowed to remove commands |
| `DisabledChatCommandsCSV`           | string  |         | CSV list of command names to disable on boot          |
  
There is a config chat command called `settings` for some settings in [Player Usage](../players/usage.md){: .md-button .md-button--primary .btn-small }

For chat commands there is also two ingame UIs for setup, one to create user groups to allow certain commands per user and another to edit/create commands, these UIs can be opened via a scriptcommand

In the user group UI you can set levels for players, Level 500 is the lowest level and everyone has by default, level 1 is the highest level. Players of higher levels can run any commands below their set level, Admins with cheats enabled with bypass any rank restrictions on commands

In the Chat command UI you have the ability to edit any of the default commands and/or add custom ones, each commands has a few options:

- `Name` - Name for the command
- `Description` - Description to show in `listcommands` UI
- `Level` - User Group level - default is 500
- `Chat Response` - The message for the command to send to the player in chat
- `Console Command` - The console command to run for the player (These are run server side so bypass admin checks with owning players controller passed)
- `MCI Tag` - The Tag for a mods singleton for ModComm
- `MCI Key` - Key used for SendModData ModComm
- `MCI Data` - Json string for SendModData ModComm
- `Cooldown` - Cooldown for command usage in seconds
- `Enabled` - Whether this command is enabled for player use
- `URL` - a URL for the player to open on their device (Requires confirmation from player before opening)

`Chat Response`, `Console Command`, `MCI Data` and `URL` will take placeholders for `{playerName}`, `{playerID}`, `{eosID}`, `{tribeID}` and `{tribeName}`. These are case sensitive.
