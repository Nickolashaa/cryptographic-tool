import asyncio
from bot.main import main


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot Stopped.")
    except Exception as e:
        print(f"ERROR\n{e}")
