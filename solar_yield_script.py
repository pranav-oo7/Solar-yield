import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

annual_kwh = 4206
system_capacity_kw = 3.0
monthly_fraction = np.array([0.075,0.075,0.085,0.095,0.11,0.09,0.06,0.06,0.07,0.085,0.08,0.095])
monthly_fraction = monthly_fraction / monthly_fraction.sum()
monthly_kwh = (monthly_fraction * annual_kwh).round(1)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthly_series = pd.Series(monthly_kwh, index=months)

plt.figure(figsize=(10,5))
monthly_series.plot(kind='bar')
plt.ylabel('Energy (kWh)')
plt.title(f'Estimated monthly production — {system_capacity_kw} kW system (Annual {annual_kwh} kWh)')
plt.tight_layout()
plt.savefig('monthly_production_plot.png', dpi=150)
plt.show()

# Savings plot

tariff_rates = {'Low (₹2.03/kWh)':2.03, 'Mid (₹6.50/kWh)':6.50, 'High (₹11.00/kWh)':11.00}
savings = {k: annual_kwh * v for k,v in tariff_rates.items()}
co2_tonnes = (annual_kwh * 0.79) / 1000.0

plt.figure(figsize=(8,5))
names = list(savings.keys())
values = [savings[n] for n in names]
plt.bar(names, values)
plt.ylabel('Estimated yearly savings (₹)')
plt.title('Annual savings by tariff scenario')
plt.tight_layout()
plt.savefig('savings_by_tariff.png', dpi=150)
plt.show()

metrics = {
    'annual_kwh': annual_kwh,
    'co2_tonnes_per_year': round(co2_tonnes,3),
    'savings_low_rpy_per_year': round(savings['Low (₹2.03/kWh)'],2),
    'savings_mid_rpy_per_year': round(savings['Mid (₹6.50/kWh)'],2),
    'savings_high_rpy_per_year': round(savings['High (₹11.00/kWh)'],2),
}
metrics_df = pd.DataFrame([metrics])
metrics_df.to_csv('project_metrics_summary.csv', index=False)
with open('short_report_auto.md','w') as f:
    f.write(f"# Short Report (auto-generated)\n\n**Annual kWh:** {annual_kwh} kWh\n\n**CO2 avoided:** {metrics['co2_tonnes_per_year']} tonnes/year\n\n**Estimated yearly savings:**\n- Low (₹2.03/kWh): ₹{metrics['savings_low_rpy_per_year']:,}\n- Mid (₹6.50/kWh): ₹{metrics['savings_mid_rpy_per_year']:,}\n- High (₹11.00/kWh): ₹{metrics['savings_high_rpy_per_year']:,}\n")
print('Done')
