from datetime import date
import ephem

d = date.today()
moon = ephem.Moon(d)
print(f"Moon phase on {d}: {moon.phase:.1f}% illuminated")

