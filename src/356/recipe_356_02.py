import asyncio


async def main():
    print('main')
    return "result value"

result = asyncio.run(main())
print(result)
