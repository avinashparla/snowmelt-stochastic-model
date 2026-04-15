import xarray as xr
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================

file_path = r"P:\snowmelt_stochastic_model\data\raw\era5_chandra_temp_2018_2022.nc"

ds = xr.open_dataset(file_path)

print("\nDataset summary:\n")
print(ds)

# =========================
# CONVERT TO CELSIUS
# =========================

temp = ds['t2m'] - 273.15

# =========================
# BASIN AVERAGE
# =========================

temp_mean = temp.mean(dim=['latitude', 'longitude'])

# =========================
# PLOT
# =========================

plt.figure(figsize=(10,5))
temp_mean.plot()
plt.title("ERA5 Temperature - Chandra Basin (2018–2022)")
plt.ylabel("Temperature (°C)")
plt.xlabel("Time")
plt.grid()

plt.show()
# =========================
# DEGREE-DAY MODEL
# =========================

DDF = 3.0   # mm/°C/day (reasonable starting value)
T0 = 0.0    # threshold temperature

# Apply melt condition
melt = DDF * (temp_mean - T0)

# No melt below freezing
melt = melt.where(temp_mean > T0, 0)

# =========================
# PLOT MELT
# =========================

plt.figure(figsize=(10,5))
melt.plot()
plt.title("Deterministic Snowmelt (Degree-Day Model)")
plt.ylabel("Melt (mm/day)")
plt.xlabel("Time")
plt.grid()

plt.show()
import numpy as np

# Random noise (standard normal)
epsilon = np.random.normal(0, 1, size=len(melt))
# Sigma increases with temperature
sigma = 0.3 * melt  # proportional to melt (simple & effective)
melt_stochastic = melt + sigma * epsilon

plt.figure(figsize=(10,5))

plt.plot(melt.time, melt, label="Deterministic", alpha=0.7)
plt.plot(melt.time, melt_stochastic, label="Stochastic", alpha=0.7)

plt.title("Deterministic vs Stochastic Snowmelt")
plt.ylabel("Melt (mm/day)")
plt.xlabel("Time")
plt.legend()
plt.grid()

plt.show()