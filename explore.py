import pandas as pd

df = pd.read_csv("Metro_Interstate_Traffic_Volume.csv")

print(df.head())
print(df.shape)
print(df.dtypes)
df["date_time"] = pd.to_datetime(df["date_time"])
df["hour"] = df["date_time"].dt.hour

hourly = df.groupby("hour")["traffic_volume"].mean()
print(hourly)
import matplotlib.pyplot as plt

hourly.plot(kind="line", marker="o")
plt.title("Average traffic volume by hour of day")
plt.xlabel("Hour of day")
plt.ylabel("Vehicles per hour")
plt.grid(True)
plt.show()
plt.savefig("traffic_by_hour.png", dpi=150)



