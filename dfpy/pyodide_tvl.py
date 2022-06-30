from pyodide.http import pyfetch
import asyncio

async def main() :
    response = await pyfetch(url="https://jsonplaceholder.typicode.com/todos/1", method="GET")
    output = f"GET request=> status:{response.status}, json:{await response.json()}"
    print(f"request_output: {output}")

asyncio.run(main())