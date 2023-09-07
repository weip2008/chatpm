import asyncio

async def simpleAsyncGeneratorFunc():
    value = await sleepFunc()
    yield value
    yield 2
    yield 3

async def main():
    g = simpleAsyncGeneratorFunc()
    print(g)
    async for i in g:
        print(i)

async def sleepFunc():
    await asyncio.sleep(10)
    return 1

if __name__ == '__main__':
    asyncio.run(main())