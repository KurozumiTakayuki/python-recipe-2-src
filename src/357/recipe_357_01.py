import asyncio


async def main():
    await asyncio.sleep(1)
    print('main')
    return "result value"

coroutine_obj = main()
result = asyncio.run(coroutine_obj)
print(result)
