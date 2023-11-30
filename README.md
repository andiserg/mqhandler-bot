# Message Queue Handler Bot
<p align="center">
    <img src="https://img.shields.io/badge/python-3.10.12-blue?logo=python" alt="Python Version">
    <a href="https://github.com/AndrewSergienko/simple-cdn-server/actions">
        <img src="https://github.com/AndrewSergienko/mqhandler/actions/workflows/docker.yml/badge.svg" alt="Actions">
    </a>
    <a href=https://results.pre-commit.ci/latest/github/AndrewSergienko/simple-cdn-server/master>
        <img src=https://results.pre-commit.ci/badge/github/AndrewSergienko/simple-cdn-server/master.svg>
    </a>
    <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code_style-black-black" alt="black"></a>
</p>

## [Головний репозиторій](https://github.com/AndrewSergienko/mqhandler-bot)

## Про проект:
**Message Queue Handler Bot** - це міні-бот, який пересилає отримані повідомлення телеграм в чергу повідомлень.

**Формат повідомлення:**
```json
{
  "username": "string",
  "text": "string",
  "time": "string (ISO format)"
}
```
