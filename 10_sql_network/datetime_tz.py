"""Даты и часовые пояса. naive datetime (без tz) в API лучше не отдавать — путаница UTC/локаль."""

from datetime import UTC, date, datetime, timedelta, timezone

print(date.today(), date(2026, 10, 12).isoformat())   # 2026-10-12

now_utc = datetime.now(UTC)
print(now_utc.isoformat())

# zoneinfo — правильный путь (IANA: Europe/Moscow). На Windows: pip install tzdata
try:
    from zoneinfo import ZoneInfo
    msk = ZoneInfo("Europe/Moscow")
except Exception:
    msk = timezone(timedelta(hours=3), name="MSK")   # запасной фиксированный сдвиг

now_msk = now_utc.astimezone(msk)
print(now_msk.strftime("%d.%m.%Y %H:%M %Z"))

d = datetime.strptime("12.10.2026 21:00", "%d.%m.%Y %H:%M")  # naive!
aware = d.replace(tzinfo=msk)
print(aware.astimezone(UTC))

print(date.today() + timedelta(days=7))
print((date(2026, 10, 12) - date(2026, 10, 1)).days)  # 11

# JSON: dt.isoformat()  →  "2026-10-12T18:00:00+00:00"
# из JSON: datetime.fromisoformat(s)
# timestamp: datetime.fromtimestamp(ts, tz=UTC)
# понедельник = 0: date.today().weekday()
# не пиши datetime.now() без tz в серверном коде — возьми UTC и конвертируй на выводе
