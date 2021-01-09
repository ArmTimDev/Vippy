from rivescript import RiveScript

bot = RiveScript(utf8=True)
bot.load_directory("./scripts")
bot.sort_replies()


def reply(text: str) -> str:
    return bot.reply("localuser", text)


if __name__ == "__main__":
    while True:
        print(reply(input()))
