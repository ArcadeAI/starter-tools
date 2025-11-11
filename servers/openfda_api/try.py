import json
from arcade_openfda_api.tools import search_drug_adverse_events, ToolMode
from arcade_tdk import ToolContext


async def main():
    context = ToolContext()
    context.set_secret("OPENFDA_API_KEY", "")
    response = await search_drug_adverse_events(
        mode=ToolMode.EXECUTE,
        request_body=json.dumps({
            "search": "receivedate:[20140101+TO+20181231]",
            "limit": 1,
        }),
        context=context,
    )
    return response

if __name__ == "__main__":
    import asyncio
    response = asyncio.run(main())
    print(response)
