---
title: Usage
description: How to use LACC features
keywords: LACC usage, LACC guide
---

# Usage

The usage of this mod is pretty simple, talk in chat, it gets relayed to discord/other clustered map

#### Chat Commands

##### Players Commands


This mod adds several chat commands by default but server admins can also add their own, as can other ark mods. the default command prefix is `/`, each command can have a custom cooldown for usage, some have one by default

- `listcommands` - This will bring up a ingame UI with a list of all commands available to the player with discriptions (some commands might not show due to user group levels or not in admin mode)

- `ping` - Replies Pong in chat (not really much use)

- `suicide` - kills player like eating implant but without the need to wait

- `sethome` - Sets a home location for player

- `clearhome` - Removes set home location for player

- `home` - Teleports the player either to their set home or if ones not set the last bed spawned in

- `back` - Teleports the player to previous location from either Death or teleporting

- `waypoint` - Allows a player to quickly set a waypoint, takes a optional name and optional lat/lon flags, I.E `/waypoint crystal -lat=42 -lon=69`

- `whisper` - Allows two players to send a discreet message to each other, I.E `/whisper Survivor This is a cool test message`

- `tp` - Allows to players to teleport to each other, this has a few options, you can use request/r and here/h, request will move the person requester to requestee and here is the opposite way, the player receiveing the request has to use accept/a, if you are in admin mode you can add the `-force` flag to skip this, each request is only valid for 60 seconds. I.E player one `/tp r Survivor`, player two `/tp a`

- `listplayers` - This will bring up a UI of all Online and Offline players that is searchable

- `togglerelay` - This will allow each player to toggle whether messages are relayed to the api, takes `-global`, `-tribe` and `-ally` flags for each mode (This command is hard coded and cannot be edited)

##### Admin Commands

- `smite` - Allows a admin to smite a player/structure/dino. This command will also take some flags, `-ban`, `-destroy`, `-connected`. ban will ban the targetted player, destroy will destroy the targetted actor without dropping anything, connected will smite all connected structures (I.E someones whole base). This command takes an optional player name, if a player name is not provided it falls back to a line trace to get what the player is looking at

- `settings` - This is a admin only command that will allow some config options around the teleporting commands. This takes named args: tpcountdown(float) - Sets the time delay players have to stand still for teleporting - default is 5 seconds, AllowHomeInCave(bool) - Allows command use in cave, AllowBackInCave(bool) - Allows command use in cave, AllowTPInCave(bool) - Allows command use in cave, AllowHomeWhenEncumbered(bool) - Allows command use when encumbered, AllowBackWhenEncumbered(bool) - Allows command use when encumbered, AllowTPWhenEncumbered(bool) - Allows command use when encumbered, SetEncumberPoint(float) - sets the percentage to count as encumbered 0-1- default is 0.85, I.E `/settings -AllowTPInCave=false -tpcountdown=3.5`

- `bypasscd` - Toggle to allow admins to bypass any cooldown on commands