# Standard Deviation Calculation Example

This example demonstrates how to calculate standard deviation and other statistical measures using the Wolfram MCP server.

## Prerequisites

- Wolfram MCP server configured in Claude Desktop
- Basic understanding of statistics

## Example 1: Basic Standard Deviation

**Question:** Calculate the standard deviation of {10, 20, 30, 40, 50}

**Using Wolfram MCP:**
```
Calculate the standard deviation of {10, 20, 30, 40, 50}
```

**Expected Response:**
Claude will use the `wolfram_statistics` tool with:
- Operation: `StandardDeviation`
- Data: `{10, 20, 30, 40, 50}`
- Result: `5√2` or approximately `14.142`

## Example 2: Complete Statistical Summary

**Wolfram Language Code:**
```wolfram
data = {10, 20, 30, 40, 50};
{
  Mean[data],
  StandardDeviation[data],
  Variance[data],
  Median[data],
  Min[data],
  Max[data]
}
```

**Using Claude:**
```
For the dataset {10, 20, 30, 40, 50}, calculate:
- Mean
- Standard Deviation
- Variance
- Median
- Min and Max values
```

**Expected Results:**
- Mean: 30
- Standard Deviation: 5√2 ≈ 14.142
- Variance: 200
- Median: 30
- Min: 10
- Max: 50

## Example 3: Large Dataset Analysis

**Wolfram Language Code:**
```wolfram
(* Generate random data *)
data = RandomReal[{0, 100}, 1000];

(* Calculate statistics *)
{
  "Count": Length[data],
  "Mean": Mean[data],
  "StandardDeviation": StandardDeviation[data],
  "Variance": Variance[data],
  "Median": Median[data],
  "Q1": Quartiles[data][[1]],
  "Q3": Quartiles[data][[3]],
  "IQR": InterquartileRange[data]
}
```

## Example 4: Population vs Sample Standard Deviation

**Population Standard Deviation:**
```wolfram
data = {10, 20, 30, 40, 50};
StandardDeviation[data]
(* Result: 5√2 ≈ 14.142 *)
```

**Sample Standard Deviation:**
```wolfram
data = {10, 20, 30, 40, 50};
StandardDeviation[data, 1]
(* Result: √250 ≈ 15.811 *)
```

**Note:** The second parameter (1) in `StandardDeviation[data, 1]` indicates sample standard deviation (n-1 in denominator).

## Example 5: Standard Deviation with Grouped Data

**Wolfram Language Code:**
```wolfram
(* Calculate mean and standard deviation for multiple groups *)
group1 = {10, 15, 20, 25, 30};
group2 = {50, 55, 60, 65, 70};
group3 = {100, 105, 110, 115, 120};

results = Table[
  {
    "Group": i,
    "Mean": Mean[data],
    "StdDev": StandardDeviation[data],
    "CV": StandardDeviation[data]/Mean[data] * 100  (* Coefficient of Variation *)
  },
  {i, 1, 3},
  {data, {group1, group2, group3}}
]
```

## Example 6: Z-Score Calculation

**Wolfram Language Code:**
```wolfram
data = {10, 20, 30, 40, 50};
mean = Mean[data];
stddev = StandardDeviation[data];

(* Calculate Z-scores for each value *)
zScores = (data - mean) / stddev

(* Result: {-√2, -(√2/2), 0, √2/2, √2} *)
(* Approximately: {-1.414, -0.707, 0, 0.707, 1.414} *)
```

## Example 7: Moving Standard Deviation

**Wolfram Language Code:**
```wolfram
(* Time series data *)
timeSeries = Table[Sin[x] + RandomReal[{-0.5, 0.5}], {x, 0, 10, 0.1}];

(* Calculate 10-point moving standard deviation *)
movingStdDev = MovingMap[StandardDeviation, timeSeries, 10];
```

## Interactive Usage with Claude

### Simple Query
```
What's the standard deviation of these test scores: {85, 92, 78, 95, 88, 91, 76, 89}?
```

### Advanced Query
```
I have sales data: {1200, 1350, 1180, 1420, 1390, 1250, 1180, 1400}
Calculate the mean, standard deviation, and coefficient of variation.
Also identify any outliers using the 1.5×IQR rule.
```

### Comparative Analysis
```
Compare these two datasets:
Dataset A: {10, 12, 15, 18, 20, 22, 25}
Dataset B: {5, 15, 20, 25, 30, 35, 45}

Which has higher variability? Calculate and compare:
- Range
- Standard Deviation
- Coefficient of Variation
```

## Visualization Example

After calculating standard deviation, you can visualize the data with normal distribution overlay:

```python
# Python visualization after getting Wolfram results
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = [10, 20, 30, 40, 50]
mean = 30
std_dev = 14.142

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=5, density=True, alpha=0.7, color='blue', edgecolor='black')

# Overlay normal distribution
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
plt.plot(x, stats.norm.pdf(x, mean, std_dev), 'r-', linewidth=2, 
         label=f'Normal(μ={mean}, σ={std_dev:.2f})')

# Mark mean and ±1σ, ±2σ, ±3σ
for i in range(-3, 4):
    x_val = mean + i * std_dev
    plt.axvline(x_val, color='gray', linestyle='--', alpha=0.5)
    plt.text(x_val, plt.ylim()[1] * 0.95, f'{i}σ', ha='center')

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Data Distribution with Standard Deviation Markers')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('standard_deviation_viz.png', dpi=150)
```

## Related Wolfram Functions

- `Mean[data]` - Arithmetic mean
- `Variance[data]` - Variance (σ²)
- `StandardDeviation[data]` - Standard deviation (σ)
- `Median[data]` - Middle value
- `Quartiles[data]` - Q1, Q2, Q3
- `InterquartileRange[data]` - IQR (Q3 - Q1)
- `MeanDeviation[data]` - Mean absolute deviation
- `CoefficientOfVariation[data]` - CV (σ/μ × 100)
- `Standardize[data]` - Convert to Z-scores

## Tips

1. **Use N[] for numerical results:**
   ```wolfram
   N[StandardDeviation[{10, 20, 30, 40, 50}]]
   (* Returns: 14.1421 instead of 5√2 *)
   ```

2. **Handle missing data:**
   ```wolfram
   data = {10, 20, Missing[], 40, 50};
   StandardDeviation[DeleteMissing[data]]
   ```

3. **Work with large datasets efficiently:**
   ```wolfram
   (* For large datasets, specify precision *)
   N[StandardDeviation[largeData], 5]
   ```

## Further Reading

- [Wolfram StandardDeviation Documentation](https://reference.wolfram.com/language/ref/StandardDeviation.html)
- [Statistical Distribution Functions](https://reference.wolfram.com/language/guide/StatisticalDistributions.html)
- [Data Manipulation Guide](https://reference.wolfram.com/language/guide/DataManipulation.html)

---

**Next Steps:**
- Try the examples above in your Claude conversation
- Experiment with your own datasets
- Combine with visualization tools (see `statistical_distributions.py`)
- Explore other statistical functions in Wolfram Language
