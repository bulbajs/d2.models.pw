from datetime import datetime

def get_duration(self):
    if self.complete:
        return round(self.time_in - self.time_out).total_seconds()//60
    else:
        return (datetime.now(timezone.utc)-self.time_in).total_seconds()//60

