---
title: Installation
description: Installation guide for My ARK Mod
keywords: LACC API, API setup
---

# API

LACC requires either a webhook or an api to function. In this you have a few options:

Be sure to link your Discord and KoFi accounts to gain channel access. [See how to here](https://help.ko-fi.com/hc/en-us/articles/8664701197073-How-do-I-join-a-Creator-s-Discord#h_01H9FYE7RQD1RF4D4CN4S5JVE3)

If you purchase one of lily's options, there is setup instructions for both in discord and a help channel dedicated to the API

### Purchase Lily's API (Self Host)
Acquiring the api for self-hosting now has a distinct shop page for purchasing: [Buy Self-Hosted](https://ko-fi.com/s/aa9eeaa1bd)

You will need your own hardware or rent a cheap VPS to run this on.

### Rent Lily's API (Hosted)
You'll need an [active monthly membership on Kofi](https://ko-fi.com/delilaheve/tiers) with the LACC Api Hosted Access tier.


LACC Terms Of Service Agreement is here: [Terms Of Service](https://docs.google.com/document/d/147q8p2Ty4fJILHw2tM-YRSoxR20hOE1uSs0DRX1js20/edit)

### DIY Option:
If you prefer not to purchase the API, we've provided the minimum requirements below to build your own API. Support will not be provided for building your own solution.

#### Assumptions:

- LACC interacts via WebSockets, all communication with the api is done through them. HTTP communication will not be added because it lacks a full-duplex connection.
- The first frame sent by the sockets will be the authorization "handshake" where the client (Mod, Discord Bot, etc...) authorizes with the api by declaring a name, payload version, token and cluster key.
- The api will respond to the authorization `Handshake` with a `HandshakeResult`.
- If successfully connected, all following message frames should be a `ChatMessage`.
- Chat messages should be relayed by the api to all other connections upon successful receipt.

#### Message Structures:

##### Handshake (JSON String)
| PropertyName | Type      | Description                                              |
|--------------|-----------|----------------------------------------------------------|
| `name`       | `String`  | Declares the connecting client's "name" as an identifier |
| `token`      | `String`  | Declares the auth token                                  |
| `version`    | `Integer` | Declares the payload version                             |
| `clusterKey` | `String`  | Declares the cluster id of the connecting client.        |

##### HandshakeResult (Plaintext String)
| Response     | Description                     |
|--------------|---------------------------------|
| success      | Connection OK                   |
| fail_server  | API outdated                    |
| fail_client  | Mod/Client outdated             |
| bad_auth     | Client supplied bad token       |

##### ChatMessage (Json String)
| Property         | Type     | Description |
|------------------|----------|-------------------------------------------------|
| `sendMode`       | `Int`    | The mode in which the chat message was sent.    |
| `mapName`        | `String` | The name of the map where the message was sent. |
| `senderName`     | `String` | The name of the message sender.                 |
| `senderTribeId`  | `Int`    | The id of the sender's tribe.                   |
| `senderTribeName`| `String` | The name of the sender's tribe.                 |
| `senderId`       | `String` | The unique id of the sender.                    |
| `message`        | `String` | The content of the message.                     |
| `timeReceived`   | `Float`  | The time when the message was received.         |
| `isAdmin`        | `Boolean`| Indicates if the sender is an admin.            |
| `clusterKey`     | `String` | The key identifying the cluster.                |
| `platformPlayerName`     | `String` | The name provided by the platform       |
| `mapColour`      | `String` | The r,g,b,a value for map colour                |