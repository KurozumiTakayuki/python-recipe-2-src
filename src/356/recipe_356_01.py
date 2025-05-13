import asyncio


async def main():
    print('main')
    return "result value"

coroutine_obj = main()
result = asyncio.run(coroutine_obj)
print(result)
