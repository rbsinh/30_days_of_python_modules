import time
import asyncio
import requests

async def function1():
    URL="https://images6.alphacoders.com/337/thumb-1920-337780.jpg"
    response = requests.get(URL)
    open("instagram.ico","wb").write(response.content)
    await asyncio.sleep(3)
    print("func 1")

async def function2():
    URL="https://images6.alphacoders.com/337/thumb-1920-337780.jpg"
    response = requests.get(URL)
    open("instagram1.ico","wb").write(response.content)
    await asyncio.sleep(3)
    print("func 2")
    return "Harry"

async def function3():
    URL="https://images6.alphacoders.com/337/thumb-1920-337780.jpg"
    response = requests.get(URL)
    open("instagram2.ico","wb").write(response.content)
    await asyncio.sleep(3)
    print("func 3")

async def main():
    L= await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
asyncio.run(main())
    

