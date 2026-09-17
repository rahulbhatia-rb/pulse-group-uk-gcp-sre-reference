from dataclasses import dataclass
@dataclass(frozen=True)
class Window: errors:int; requests:int; minutes:int
def burn_rate(window: Window, slo: float) -> float:
 if window.requests < 1 or window.errors < 0 or window.errors > window.requests or window.minutes < 1: raise ValueError("invalid window")
 if not 0 < slo < 1: raise ValueError("invalid slo")
 return (window.errors/window.requests)/(1-slo)
def response(short: Window, long: Window, slo: float) -> str:
 short_burn,long_burn=burn_rate(short,slo),burn_rate(long,slo)
 if short_burn >= 14 and long_burn >= 6: return "page_and_pause_risky_rollouts"
 if short_burn >= 2: return "investigate_and_increase_observation"
 return "within_policy"
