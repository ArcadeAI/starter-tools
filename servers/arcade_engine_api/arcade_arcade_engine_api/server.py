from arcade_mcp_server import MCPApp

import arcade_arcade_engine_api

app = MCPApp(
    name="ArcadeEngineApi",
    version="0.2.1",
)
app.add_tools_from_module(arcade_arcade_engine_api)

if __name__ == "__main__":
    app.run()
