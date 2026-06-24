from anyio import run

from tastytrade import DXLinkStreamer, Session
from tastytrade.dxfeed import Trade


async def main():
    session = Session()
    async with DXLinkStreamer(session) as streamer:
        await streamer.subscribe(Trade, "RUT")
        print(await streamer.get_event(Trade))


run(main)
