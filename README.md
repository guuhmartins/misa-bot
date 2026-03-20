# 🎀 Misa Bot

Misa is a Discord bot created for the **Misa Community**.
She's not just a bot — she's a character. Fofa, engraçada, animada e às vezes estressada.
Misa helps manage the server, welcome new members and bring life to the community.

Created on **March 5, 2026**.

---

## ✨ Features

### 📋 Information
- `ping` — shows bot latency
- `userinfo [@member]` — shows user information
- `avatar [@member]` — shows user avatar
- `botinfo` — shows Misa's information
- `convite` — generates a server invite link

### 🎀 Misa's Personality
- `misa` — Misa responds based on her current mood
- `humor <state>` — changes Misa's mood *(Misa Owner only)*
- Mood states: `feliz`, `animada`, `cansada`, `estressada`, `curiosa`

### 🎭 Roleplay
- `hug`, `kiss`, `cafune`, `highfive`, `attack`, `dance`, `laugh`, `cry`
- All commands support optional member mention
- Powered by **Giphy API**

### 🍥 Anime
- `anime <name>` — search anime information
- Powered by **AniList GraphQL API**

### 🧰 Utilities
- `calcular <expression>` — math calculator
- `traduzir <text>` — auto-detect language and translate to Portuguese
- `remind <time> <message>` — set a reminder (supports `s`, `m`, `h`)

### 📜 Logs
Automatic logging to `#server-logs`:
- Deleted messages
- Edited messages
- Members joining/leaving
- Roles added/removed

### 🛡️ Moderation *(Misa Owner only)*
- `clear [amount]` — delete messages (default: 10)
- `slowmode <seconds>` — set slowmode (0 to disable)
- `lock` — lock a channel
- `unlock` — unlock a channel

### ⭐ XP System
- XP gained per message with 60s cooldown (anti-spam)
- Automatic level up system
- Level up notification in channel
- Powered by **MySQL**

---

## 📂 Project Structure

```
misa-bot/
│
├── cogs/
│   ├── commands.py
│   ├── events.py
│   ├── info.py
│   ├── logs.py
│   ├── misa.py
│   ├── moderation.py
│   ├── roleplay.py
│   ├── anime.py
│   ├── utils.py
│   ├── xp.py
│   └── slash.py
│
├── database.py
├── main.py
├── .env
└── requirements.txt
```

---

## 🚀 Setup

```bash
git clone https://github.com/guuhmartins/misa-bot
cd misa-bot
pip install -r requirements.txt
```

Crie um arquivo `.env`:

```env
DISCORD_TOKEN=your_token_here
GIPHY_KEY=your_giphy_key_here
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=misa_bot
```

```bash
python main.py
```

---

## 🗄️ Database

```sql
CREATE DATABASE misa_bot;
USE misa_bot;

CREATE TABLE xp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id BIGINT NOT NULL,
    servidor_id BIGINT NOT NULL,
    xp INT DEFAULT 0,
    nivel INT DEFAULT 1,
    ultima_mensagem DATETIME,
    UNIQUE KEY unique_usuario_servidor (usuario_id, servidor_id)
);
```

---

## 🛣️ Roadmap

- [x] Welcome system
- [x] Information commands
- [x] Misa's personality & mood system
- [x] Roleplay commands with GIFs
- [x] Anime search
- [x] Server logs
- [x] Basic moderation
- [x] Utility commands
- [x] XP & level system
- [ ] XP rank command
- [ ] Auto roles by level
- [ ] Music system
- [ ] Advanced moderation
- [ ] Web dashboard

---

## 🎀 About Misa

Misa was created to help manage and bring life to the **Misa Community** server. ≽(◉˕◉≼)マ

---

## 👨‍💻 Developers

Developed with 💕 by **Gustavo Henrique** & **Maria Clara**

GitHub: https://github.com/guuhmartins & https://github.com/bezzr
