from datetime import date, datetime, time, timedelta

from databento import Historical

from tastytrade.utils import TZ

exp = date(2025, 12, 19)
client = Historical(key="db-QaSpSyNRRfFAcf7XLsP5cXiFvFx9e")
# Get definition data
symbols = client.symbology.resolve(
    dataset="OPRA.PILLAR",
    symbols="SPXW.OPT",
    stype_in="parent",
    stype_out="instrument_id",
    start_date=exp,
    end_date=exp + timedelta(days=1),
)
iids = sorted(
    {
        m["s"]
        for sym, mappings in symbols["result"].items()
        if sym[6:12] == exp.strftime("%y%m%d")
        for m in mappings
    }
)
print(f"fetched chain with {len(iids)} symbols")
data = client.metadata.get_cost(
    dataset="OPRA.PILLAR",
    schema="cbbo-1s",
    symbols=iids,
    stype_in="instrument_id",
    start=datetime.combine(exp, time(9, 30), TZ),
    end=datetime.combine(exp, time(16, 0), TZ),
)
print(data)
client.batch.submit_job(
    dataset="OPRA.PILLAR",
    schema="cbbo-1s",
    symbols=iids,
    stype_in="instrument_id",
    start=datetime.combine(exp, time(9, 30), TZ),
    end=datetime.combine(exp, time(16, 0), TZ),
)
