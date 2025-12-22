# Data Visualization with Matplotlib, Seaborn & Plotly

**Author:** Mohamed Zahran          
**Date:** December , 2025  
**Purpose:** Comprehensive guide to data visualization using Python's Matplotlib, Seaborn, and Plotly libraries

---

## Table of Contents

1. [Introduction](#introduction)
2. [Setup & Imports](#setup--imports)
3. [Matplotlib Fundamentals](#matplotlib-fundamentals)
   - [Scatter Plots](#scatter-plots)
   - [Line Plots](#line-plots)
   - [Histograms](#histograms)
   - [Box Plots](#box-plots)
   - [Bar Plots](#bar-plots)
   - [Pie Charts](#pie-charts)
   - [Subplots](#subplots)
4. [Seaborn Statistical Visualization](#seaborn-statistical-visualization)
   - [Count Plots](#count-plots)
   - [Box Plots](#seaborn-box-plots)
   - [Scatter Plots](#seaborn-scatter-plots)
   - [Relational Plots](#relational-plots)
   - [Histograms](#seaborn-histograms)
   - [Line Plots](#seaborn-line-plots)
5. [Plotly Interactive Visualization](#plotly-interactive-visualization)
   - [Scatter Plots](#plotly-scatter-plots)
   - [Line Plots](#plotly-line-plots)
   - [Bar Charts](#plotly-bar-charts)
   - [Histograms](#plotly-histograms)
   - [Box Plots](#plotly-box-plots)
   - [Pie Charts](#plotly-pie-charts)
   - [3D Plots](#plotly-3d-plots)
   - [Subplots](#plotly-subplots)
   - [Geographic Maps](#plotly-maps)
6. [Summary & Best Practices](#summary--best-practices)
7. [Resources](#resources)

---

## Introduction

Data visualization is a crucial skill for data analysis, allowing us to:
- Explore and understand data patterns
- Communicate insights effectively
- Identify outliers and anomalies
- Make data-driven decisions
- Create interactive dashboards

This notebook covers three essential Python visualization libraries:
- **Matplotlib**: Low-level, highly customizable plotting library
- **Seaborn**: High-level statistical visualization built on Matplotlib
- **Plotly**: Interactive, web-based visualizations with hover effects and zooming

---

## Setup & Imports

### Essential Libraries
```python
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
```

**Library Purposes:**
- `numpy`: Numerical computations and array operations
- `pandas`: Data manipulation with DataFrames
- `matplotlib.pyplot`: Core plotting functionality
- `seaborn`: Statistical visualizations with beautiful defaults

### Plot Styles
```python
# Set plotting style
plt.style.use('default')
# plt.style.use('ggplot')  # Alternative R-style theme
```

**Available Styles:**
- `default` - Standard Matplotlib
- `ggplot` - R's ggplot2 style
- `seaborn` - Clean modern look
- `fivethirtyeight` - Blog style
- `dark_background` - Dark theme

**Explore more:** [Matplotlib Style Sheets Reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

---

## Matplotlib Fundamentals

### Loading Data
```python
path = os.path.join(os.getcwd(), 'dataset', 'housing.csv')
df = pd.read_csv(path)
df.head()
df.info()
df.columns
```

---

### Scatter Plots

**Purpose:** Visualize relationships between two numerical variables

#### Basic Scatter Plot
```python
plt.scatter(df['longitude'], df['latitude'])
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title('Longitude vs. Latitude of Housing Dataset')
plt.show()
```

#### Advanced Customization
```python
plt.figure(figsize=(10, 6))
plt.scatter(x=df['longitude'], y=df['latitude'], 
            marker='o', color='black', alpha=0.5)
plt.xlabel('Longitude', fontsize=14, color='red')
plt.ylabel('Latitude', fontsize=14, color='red')
plt.title('Longitude vs. Latitude of Housing Dataset', fontsize=15, color='red')
plt.show()
```

#### Multi-dimensional Encoding
```python
plt.figure(figsize=(14, 8))
sc = plt.scatter(x=df['longitude'], y=df['latitude'], 
                 marker='o', 
                 c=df['median_house_value'],  # Color by value
                 cmap=plt.get_cmap('jet'), 
                 alpha=0.4, 
                 s=df['population']/100,  # Size by population
                 label='Population')
plt.colorbar(sc)
plt.xlabel('Longitude', fontsize=14)
plt.ylabel('Latitude', fontsize=14)
plt.title('Longitude vs. Latitude of Housing Dataset', fontsize=15)
plt.legend()
plt.show()
```

**Key Parameters:**
- `marker` - Point shape ('o', '+', 'x', 's', etc.)
- `c` - Color mapping to variable
- `cmap` - Color palette ('jet', 'viridis', 'plasma')
- `alpha` - Transparency (0-1)
- `s` - Point size

#### Pandas Shortcut
```python
df.plot(kind='scatter', x='longitude', y='latitude', 
        c='median_house_value', cmap='jet', alpha=0.4,
        s=df['population']/100, figsize=(14, 8), 
        colorbar=True, xlabel='Longitude', ylabel='Latitude',
        title='Longitude vs. Latitude of Housing Dataset')
plt.show()
```

---

### Line Plots

**Purpose:** Show trends and changes over continuous data

#### Creating Test Data
```python
x = np.linspace(1, 5, 100)  # 100 points from 1 to 5
y = np.exp(x)  # Exponential function
z = np.log2(x)  # Logarithmic function
```

#### Basic Line Plot
```python
plt.plot(x, y)
plt.title('x vs. y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

#### Multiple Lines with Styling
```python
plt.plot(x, y, marker='o', color='r', markersize=2, label='exp(x)')
plt.plot(x, z, marker='+', color='g', markersize=2, label='log2(x)')
plt.title('x vs. y')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
```

#### Dual Y-Axes (twinx)
```python
fig, ax = plt.subplots()

# Primary y-axis
ax.plot(x, y, color='blue', label='exp(x)')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', color='blue', fontsize=14)

# Secondary y-axis
ax2 = ax.twinx()
ax2.plot(x, z, color='red', label='log2(x)')
ax2.set_ylabel('z', color='red', fontsize=14)

plt.title('x vs. y & x vs. z', fontsize=14)
plt.show()
```

**When to use twinx:**
- Comparing variables with different scales
- Showing correlation between disparate metrics
- Economic/financial data (price vs volume)

#### Annotations
```python
plt.plot(x, y)
plt.title('x vs. y')
plt.xlabel('x')
plt.ylabel('y')
plt.annotate('max value', 
             xy=(5, 140),  # Point to annotate
             xytext=(4, 20),  # Label position
             arrowprops={"arrowstyle":"->", "color":"red"})
plt.show()
```

---

### Histograms

**Purpose:** Display distribution of numerical data

#### Basic Histogram
```python
plt.figure(figsize=(10, 6))
plt.hist(df['housing_median_age'], bins=50)
plt.title('Histogram Distr. for Houses ages', fontsize=12)
plt.xlabel('Housing median age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()
```

#### Normalized Histogram with Outline
```python
plt.figure(figsize=(10, 6))
plt.hist(df['housing_median_age'], 
         bins=50, 
         density=True,  # Normalize to probability density
         histtype='step')  # Outline only
plt.title('Histogram Distr. for Houses ages', fontsize=12)
plt.xlabel('Housing median age', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.show()
```

**Key Parameters:**
- `bins` - Number of intervals (more = finer detail)
- `density` - Normalize to probability (area = 1)
- `histtype` - 'bar' (default), 'step' (outline), 'stepfilled'

---

### Box Plots

**Purpose:** Show distribution summary and outliers

#### Basic Box Plot
```python
plt.figure(figsize=(10, 6))
plt.boxplot(df['median_income'])
plt.title('Boxplot for median_income variable', fontsize=12)
plt.xlabel('median_income', fontsize=12)
plt.ylabel('values', fontsize=12)
plt.show()
```

**Box Plot Components:**
- **Box**: Interquartile range (IQR) - middle 50%
- **Line in box**: Median (50th percentile)
- **Whiskers**: Extend to 1.5 × IQR
- **Points**: Outliers beyond whiskers

**Parameters:**
```python
plt.boxplot(df['median_income'], whis=1.5)  # Whisker multiplier
```

---

### Bar Plots

**Purpose:** Compare values across categories

#### Using Pandas
```python
df['ocean_proximity'].value_counts().plot(kind='bar')
plt.show()
```

#### Using Matplotlib with Customization
```python
vals = df['ocean_proximity'].value_counts().values
idx = df['ocean_proximity'].value_counts().index

plt.figure(figsize=(10, 6))
plt.bar(x=idx, height=vals)
plt.title('Distribution for ocean_proximity in Dataset', fontsize=14)
plt.xlabel('Ocean Proximity', fontsize=12)
plt.ylabel('Counts', fontsize=12)
plt.xticks(rotation=90)  # Rotate labels
plt.show()
```

---

### Pie Charts

**Purpose:** Show proportions of a whole

#### Using Pandas
```python
df['ocean_proximity'].value_counts().plot(
    kind='pie', 
    figsize=(10, 6),
    explode=(0.1, 0.2, 0.05, 0.4, 0.2),  # Separate slices
    autopct='%1.2f%%',  # Show percentages
    shadow=True,
    colors=('orange', 'cyan', 'brown', 'grey', 'indigo'))
plt.show()
```

#### Using Matplotlib
```python
vals = df['ocean_proximity'].value_counts().values
idx = df['ocean_proximity'].value_counts().index

plt.figure(figsize=(10, 6))
plt.pie(x=vals, labels=idx, 
        explode=(0.1, 0.2, 0.05, 0.4, 0.2),
        autopct='%1.2f%%', 
        shadow=True,
        colors=('orange', 'cyan', 'brown', 'grey', 'indigo'))
plt.title('Pie Chart for Ocean Proximity variable')
plt.show()
```

**Learn more:** [GeeksforGeeks Pie Chart Guide](https://www.geeksforgeeks.org/plot-a-pie-chart-in-python-using-matplotlib/)

---

### Subplots

**Purpose:** Display multiple plots in grid layout

#### Manual Approach
```python
fig, ax = plt.subplots(2, 2, figsize=(20, 10))
fig.tight_layout(pad=5)

# Top-left
plt.sca(ax[0, 0])
to_plot = df[df['ocean_proximity']=='<1H OCEAN']['median_house_value']
plt.hist(to_plot, bins=50)
plt.title('Distr. of Houses Prices at ocean_proximity=<1H OCEAN', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Top-right
plt.sca(ax[0, 1])
to_plot = df[df['ocean_proximity']=='INLAND']['median_house_value']
plt.hist(to_plot, bins=50)
plt.title('Distr. of Houses Prices at ocean_proximity=INLAND', fontsize=14)

# Bottom-left
plt.sca(ax[1, 0])
to_plot = df[df['ocean_proximity']=='NEAR OCEAN']['median_house_value']
plt.hist(to_plot, bins=50)
plt.title('Distr. of Houses Prices at ocean_proximity=NEAR OCEAN', fontsize=14)
plt.xlabel('Houses Prices', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Bottom-right
plt.sca(ax[1, 1])
to_plot = df[df['ocean_proximity']=='NEAR BAY']['median_house_value']
plt.hist(to_plot, bins=50)
plt.title('Distr. of Houses Prices at ocean_proximity=NEAR BAY', fontsize=14)
plt.xlabel('Houses Prices', fontsize=14)

plt.show()
```

#### Optimized with Loops
```python
fig, ax = plt.subplots(2, 2, figsize=(20, 10))
fig.tight_layout(pad=5)

# Get top 4 categories
ocean_vals = df['ocean_proximity'].value_counts().index[:4].tolist()
ocean_vals = np.array(ocean_vals).reshape(2, 2)

for row in range(2):
    for col in range(2):
        plt.sca(ax[row, col])
        to_plot = df[df['ocean_proximity']==ocean_vals[row, col]]['median_house_value']
        plt.hist(to_plot, bins=50)
        plt.title(f'Distr. of Houses Prices at ocean_proximity={ocean_vals[row, col]}', 
                  fontsize=14)
        
        if row != 0:
            plt.xlabel('Houses Prices', fontsize=14)
        if col != 1:
            plt.ylabel('Frequency', fontsize=14)

plt.show()
```

**Best Practices:**
- Use loops to avoid code repetition
- Apply labels only where needed (edges)
- Use `tight_layout()` to prevent overlap

---

## Mission Complete! 🎉

**Matplotlib Section Achievements:**
✅ Scatter plots with multi-dimensional encoding  
✅ Line plots and dual y-axes  
✅ Histograms and distributions  
✅ Box plots for outlier detection  
✅ Bar charts and pie charts  
✅ Subplots and annotations  

---

## Seaborn Statistical Visualization

### Introduction

**What is Seaborn?**
- High-level interface built on Matplotlib
- Beautiful default styles
- Automatic statistical aggregation
- Easy categorical grouping
- Seamless pandas integration

### Setup
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import os
```

### Loading Built-in Dataset
```python
df_tips = sns.load_dataset('tips')
df_tips.head()
```

**Tips Dataset Variables:**
- `total_bill` - Bill amount
- `tip` - Tip amount
- `sex` - Customer gender
- `smoker` - Smoking section (Yes/No)
- `day` - Day of week
- `time` - Lunch/Dinner
- `size` - Party size

---

### Count Plots - Bar Plot

**Purpose:** Automatically count and visualize categorical frequencies

**Check more styles:** [Matplotlib Style Sheets](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

#### Basic Count Plot
```python
plt.figure(figsize=(10, 8))
sns.countplot(x='time', data=df_tips, hue='time')
plt.title('Distr. of time variable in Dataset', fontsize=14)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.show()
```

#### Grouped Count Plot
```python
plt.figure(figsize=(10, 8))
sns.countplot(x='time', data=df_tips, hue='sex')
plt.title('Distr. of time variable in Dataset', fontsize=12)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(loc='upper left')
plt.show()
```

#### Using catplot (Figure-level)
```python
# Note: plt.figure() not needed with catplot
sns.catplot(kind='count', x='time', data=df_tips, hue='sex')
plt.title('Distr. of time variable in Dataset', fontsize=12)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()
```

**Key Difference:**
- `countplot()` - Axes-level (add to existing figure)
- `catplot()` - Figure-level (creates own figure)

---

### Seaborn Box Plots

**Purpose:** Enhanced box plots with easier grouping

#### Simple Box Plot
```python
plt.figure(figsize=(10, 8))
sns.boxplot(y='total_bill', data=df_tips)
plt.title('Distr of total bill', fontsize=14)
plt.xlabel('Total bill', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.show()
```

#### Grouped by Gender
```python
sns.catplot(y='total_bill', x='sex', data=df_tips, 
            kind='box', hue='sex')
plt.title('Distr of total bill', fontsize=14)
plt.xlabel('Sex', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.show()
```

#### Grouped by Time
```python
plt.figure(figsize=(12, 8))
sns.catplot(y='total_bill', x='time', data=df_tips, 
            kind='box', hue='time')
plt.title('Distr of total bill', fontsize=14)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.show()
```

---

### Seaborn Scatter Plots

**Purpose:** Enhanced scatter plots with easy grouping

#### Basic Scatter Plot
```python
plt.figure(figsize=(10, 8))
sns.scatterplot(x='total_bill', y='tip', data=df_tips)
plt.title('Relation between total bill and tip', fontsize=14)
plt.xlabel('Total bill', fontsize=14)
plt.ylabel('Tip', fontsize=14)
plt.show()
```

#### Grouped by Gender
```python
plt.figure(figsize=(10, 8))
sns.scatterplot(x='total_bill', y='tip', data=df_tips, hue='sex')
plt.title('Relation between total bill and tip', fontsize=14)
plt.xlabel('Total bill', fontsize=14)
plt.ylabel('Tip', fontsize=14)
plt.show()
```

---

### Relational Plots (relplot)

**Purpose:** Scatter/line plots with automatic faceting

#### Faceting by Columns
```python
sns.relplot(x='total_bill', y='tip', data=df_tips, 
            kind='scatter', col='smoker')
plt.show()
```

#### Faceting by Rows
```python
sns.relplot(x='total_bill', y='tip', data=df_tips, 
            kind='scatter', row='smoker')
plt.show()
```

#### 2D Faceting (Rows + Columns)
```python
sns.relplot(x='total_bill', y='tip', data=df_tips, 
            kind='scatter', col='smoker', row='time')
plt.show()
```

#### Multi-dimensional Encoding
```python
sns.relplot(x='total_bill', y='tip', data=df_tips, 
            kind='scatter', 
            col='smoker', row='time',
            size='size', hue='size')
plt.show()
```

**Encodes 5 Variables:**
1. Total bill (x-axis)
2. Tip (y-axis)
3. Smoker (columns)
4. Time (rows)
5. Party size (point size + color)

#### Style and Transparency
```python
sns.relplot(x='total_bill', y='tip', data=df_tips, 
            kind='scatter', 
            style='smoker', hue='smoker', alpha=0.4)
plt.title('Relation between total bill and tips with smoker', fontsize=14)
plt.xlabel('Total bill', fontsize=14)
plt.ylabel('Tip', fontsize=14)
plt.show()
```

---

### Seaborn Histograms

**Purpose:** Distribution plots with KDE curves

#### Grouped by Gender
```python
plt.figure(figsize=(12, 8))
sns.histplot(x='total_bill', data=df_tips, 
             bins=50, kde=True, hue='sex')
plt.title('Distr. of total bill in Dataset', fontsize=14)
plt.xlabel('Total Bill', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.show()
```

#### Grouped by Smoker Status
```python
plt.figure(figsize=(12, 8))
sns.histplot(x='total_bill', data=df_tips, 
             bins=50, kde=True, hue='smoker')
plt.title('Distr. of total bill in Dataset', fontsize=14)
plt.xlabel('Total Bill', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.show()
```

**Key Features:**
- `kde=True` - Adds smooth density curve
- `hue` - Creates overlapping distributions
- Automatic legend generation

---

### Seaborn Line Plots

**Purpose:** Trends with automatic aggregation

#### Loading Air Quality Data
```python
path = os.path.join(os.getcwd(), 'dataset', 'AirQuality.csv')
df_air = pd.read_csv(path, sep=';')
df_air.head()
```

#### Data Preprocessing
```python
# Remove null times
df_air = df_air[~df_air['Time'].isna()]

# Extract hour from time string
time_lst = []
for i in range(len(df_air)):
    time_lst.append(df_air['Time'][i][:2])

df_air['Time'] = time_lst
df_air.head()
```

#### Line Plot with Automatic Aggregation
```python
plt.figure(figsize=(14, 8))
sns.relplot(x='Time', y='NO2(GT)', data=df_air, 
            kind='line', markers=True)
plt.title('Relation between Time and NO2', fontsize=14)
plt.xlabel('Time', fontsize=14)
plt.ylabel('NO2(GT)', fontsize=14)
plt.xticks(rotation=90)
plt.show()
```

**Automatic Features:**
- Aggregates multiple values per x-value (computes mean)
- Shows confidence interval as shaded region
- Handles uncertainty visualization

---

## Seaborn Complete! 🎉

### What You've Mastered:

✅ **Count Plots** - Automatic categorical frequency  
✅ **Box Plots** - Distribution comparison with grouping  
✅ **Scatter Plots** - Relationship exploration  
✅ **Relational Plots** - Faceted visualizations  
✅ **Histograms** - Distributions with KDE  
✅ **Line Plots** - Time series with aggregation  

---

## Plotly Interactive Visualization

### Introduction

**What is Plotly?**
- Interactive, web-based visualization library
- Built-in hover tooltips, zooming, panning
- Export to HTML for sharing
- Publication-quality static images
- 3D plotting capabilities
- Geographic mapping support

**Key Advantages:**
🖱️ **Interactive by default** - Hover, zoom, pan, select  
📱 **Responsive** - Works on desktop and mobile  
🌐 **Web-ready** - Export as standalone HTML  
🎨 **Beautiful themes** - Modern, professional styling  
📊 **Dashboard-ready** - Perfect for Dash apps  

### Setup
```python
# Install Plotly if needed
# !pip install plotly

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
```

**Two Main APIs:**
- **Plotly Express (px)**: High-level, concise syntax (recommended for most cases)
- **Graph Objects (go)**: Low-level, detailed control

### Loading Data
```python
# Load tips dataset
df_tips = px.data.tips()
df_tips.head()

# Load housing dataset
import os
path = os.path.join(os.getcwd(), 'dataset', 'housing.csv')
df = pd.read_csv(path)
```

---

### Plotly Scatter Plots

**Purpose:** Interactive exploration of relationships

#### Basic Scatter Plot
```python
# Using Plotly Express (recommended)
fig = px.scatter(df_tips, 
                 x='total_bill', 
                 y='tip',
                 title='Relationship between Total Bill and Tip')
fig.show()
```

**Interactive Features:**
- Hover to see exact values
- Click and drag to zoom
- Double-click to reset view
- Click legend to hide/show series

#### Scatter with Color Grouping
```python
fig = px.scatter(df_tips, 
                 x='total_bill', 
                 y='tip',
                 color='sex',  # Color by category
                 title='Tips by Gender',
                 labels={'total_bill': 'Total Bill ($)', 
                         'tip': 'Tip ($)'})
fig.show()
```

#### Multi-dimensional Scatter
```python
fig = px.scatter(df_tips, 
                 x='total_bill', 
                 y='tip',
                 color='time',  # Color by meal time
                 size='size',  # Size by party size
                 hover_data=['day', 'smoker'],  # Additional hover info
                 title='Multi-dimensional Tip Analysis',
                 labels={'total_bill': 'Total Bill ($)', 
                         'tip': 'Tip ($)',
                         'size': 'Party Size'})
fig.show()
```

#### Customized with Trendline
```python
fig = px.scatter(df_tips, 
                 x='total_bill', 
                 y='tip',
                 color='smoker',
                 trendline='ols',  # Add regression line
                 title='Tips with Trendline by Smoking Status')
fig.show()
```

#### Using Graph Objects (Advanced)
```python
fig = go.Figure()

# Add trace for males
males = df_tips[df_tips['sex'] == 'Male']
fig.add_trace(go.Scatter(
    x=males['total_bill'],
    y=males['tip'],
    mode='markers',
    name='Male',
    marker=dict(size=8, color='blue', opacity=0.6)
))

# Add trace for females
females = df_tips[df_tips['sex'] == 'Female']
fig.add_trace(go.Scatter(
    x=females['total_bill'],
    y=females['tip'],
    mode='markers',
    name='Female',
    marker=dict(size=8, color='red', opacity=0.6)
))

fig.update_layout(
    title='Tips by Gender (Graph Objects)',
    xaxis_title='Total Bill ($)',
    yaxis_title='Tip ($)',
    hovermode='closest'
)

fig.show()
```

---

### Plotly Line Plots

**Purpose:** Interactive time series and trends

#### Basic Line Plot
```python
# Create sample time series data
dates = pd.date_range('2024-01-01', periods=100)
values = np.cumsum(np.random.randn(100))
df_time = pd.DataFrame({'date': dates, 'value': values})

fig = px.line(df_time, 
              x='date', 
              y='value',
              title='Time Series Example')
fig.show()
```

#### Multiple Lines
```python
# Create data with multiple series
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100)
df_multi = pd.DataFrame({
    'date': dates,
    'series_1': np.cumsum(np.random.randn(100)),
    'series_2': np.cumsum(np.random.randn(100)),
    'series_3': np.cumsum(np.random.randn(100))
})

# Melt for Plotly Express format
df_melted = df_multi.melt(id_vars='date', 
                           var_name='series', 
                           value_name='value')

fig = px.line(df_melted, 
              x='date', 
              y='value',
              color='series',
              title='Multiple Time Series')
fig.show()
```

#### Line with Markers and Custom Styling
```python
fig = px.line(df_time, 
              x='date', 
              y='value',
              title='Styled Line Plot',
              markers=True)  # Add markers at data points

fig.update_traces(line_color='darkblue', 
                  line_width=2,
                  marker=dict(size=8, color='red'))

fig.update_layout(
    plot_bgcolor='lightgray',
    hovermode='x unified'  # Unified hover across all series
)

fig.show()
```

---

### Plotly Bar Charts

**Purpose:** Interactive categorical comparisons

#### Basic Bar Chart
```python
# Count by category
count_data = df_tips['time'].value_counts().reset_index()
count_data.columns = ['time', 'count']

fig = px.bar(count_data, 
             x='time', 
             y='count',
             title='Meal Time Distribution',
             color='time')
fig.show()
```

#### Grouped Bar Chart
```python
# Group by two categories
grouped = df_tips.groupby(['time', 'sex']).size().reset_index(name='count')

fig = px.bar(grouped, 
             x='time', 
             y='count',
             color='sex',
             barmode='group',  # 'group' for side-by-side, 'stack' for stacked
             title='Meal Time by Gender')
fig.show()
```

#### Horizontal Bar Chart
```python
# Sort by value for better readability
ocean_counts = df['ocean_proximity'].value_counts().reset_index()
ocean_counts.columns = ['ocean_proximity', 'count']

fig = px.bar(ocean_counts, 
             x='count', 
             y='ocean_proximity',
             orientation='h',  # Horizontal bars
             title='Housing by Ocean Proximity',
             color='count',
             color_continuous_scale='Blues')
fig.show()
```

---

### Plotly Histograms

**Purpose:** Interactive distribution exploration

#### Basic Histogram
```python
fig = px.histogram(df_tips, 
                   x='total_bill',
                   nbins=30,
                   title='Distribution of Total Bills')
fig.show()
```
#### Histogram with Overlay

```python
fig = px.histogram(df_tips, 
                   x='total_bill',
                   color='sex',
                   nbins=30,
                   barmode='overlay',  # Overlay instead of stack
                   opacity=0.7,
                   title='Bill Distribution by Gender')
fig.show()
```

#### Histogram with Marginal Plot

```python
fig = px.histogram(df_tips, 
                   x='total_bill',
                   color='time',
                   marginal='box',  # Add box plot on top
                   # marginal='violin' or 'rug' also available
                   title='Bill Distribution with Box Plot')
fig.show()
```

---

### Plotly Box Plots

**Purpose:** Interactive statistical summaries

#### Basic Box Plot

```python
fig = px.box(df_tips, 
             y='total_bill',
             title='Total Bill Distribution')
fig.show()
```

#### Grouped Box Plot

```python
fig = px.box(df_tips, 
             x='time', 
             y='total_bill',
             color='smoker',
             title='Bill Distribution by Time and Smoking Status')
fig.show()
```

#### Box Plot with Points

```python
fig = px.box(df_tips, 
             x='day', 
             y='tip',
             color='sex',
             points='all',  # Show all points
             # points='outliers' shows only outliers
             title='Tips by Day with Individual Points')
fig.show()
```

#### Violin Plot (Enhanced Box Plot)

```python
fig = px.violin(df_tips, 
                x='time', 
                y='total_bill',
                color='sex',
                box=True,  # Show box plot inside
                points='all',  # Show all points
                title='Bill Distribution - Violin Plot')
fig.show()
```

---

### Plotly Pie Charts

**Purpose:** Interactive proportions

#### Basic Pie Chart

```python
ocean_counts = df['ocean_proximity'].value_counts().reset_index()
ocean_counts.columns = ['category', 'count']

fig = px.pie(ocean_counts, 
             values='count', 
             names='category',
             title='Housing by Ocean Proximity')
fig.show()
```

#### Pie Chart with Custom Colors and Pull

```python
fig = px.pie(ocean_counts, 
             values='count', 
             names='category',
             title='Housing Distribution',
             color_discrete_sequence=px.colors.qualitative.Set3)

# Pull out a slice
fig.update_traces(pull=[0.1, 0, 0, 0, 0],  # Pull first slice
                  textposition='inside',
                  textinfo='percent+label')

fig.show()
```

#### Donut Chart

```python
fig = px.pie(ocean_counts, 
             values='count', 
             names='category',
             title='Housing Distribution - Donut Chart',
             hole=0.4)  # Creates donut effect

fig.show()
```

---

### Plotly 3D Plots

**Purpose:** Visualize three-dimensional relationships

#### 3D Scatter Plot

```python
# Create sample 3D data
np.random.seed(42)
n = 200
df_3d = pd.DataFrame({
    'x': np.random.randn(n),
    'y': np.random.randn(n),
    'z': np.random.randn(n),
    'category': np.random.choice(['A', 'B', 'C'], n)
})

fig = px.scatter_3d(df_3d, 
                    x='x', 
                    y='y', 
                    z='z',
                    color='category',
                    title='3D Scatter Plot')
fig.show()
```

**Interactive Controls:**
- Click and drag to rotate
- Scroll to zoom
- Shift+drag to pan

#### 3D Surface Plot

```python
# Create surface data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Viridis')])

fig.update_layout(
    title='3D Surface Plot',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    )
)

fig.show()
```

#### 3D Line Plot

```python
# Create 3D spiral
t = np.linspace(0, 10, 100)
x = np.cos(t)
y = np.sin(t)
z = t

fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines',
    line=dict(color='blue', width=4)
)])

fig.update_layout(title='3D Spiral')
fig.show()
```

---

### Plotly Subplots

**Purpose:** Multiple plots in one figure

#### Basic Subplots

```python
from plotly.subplots import make_subplots

# Create 2x2 subplot grid
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Scatter', 'Bar', 'Box', 'Histogram')
)

# Add scatter plot
fig.add_trace(
    go.Scatter(x=df_tips['total_bill'], y=df_tips['tip'], mode='markers'),
    row=1, col=1
)

# Add bar chart
time_counts = df_tips['time'].value_counts()
fig.add_trace(
    go.Bar(x=time_counts.index, y=time_counts.values),
    row=1, col=2
)

# Add box plot
fig.add_trace(
    go.Box(y=df_tips['total_bill']),
    row=2, col=1
)

# Add histogram
fig.add_trace(
    go.Histogram(x=df_tips['tip'], nbinsx=20),
    row=2, col=2
)

fig.update_layout(height=800, showlegend=False, title_text="Multiple Plots")
fig.show()
```

#### Subplots with Different Types

```python
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "scatter"}, {"type": "pie"}]],
    subplot_titles=('Scatter Plot', 'Pie Chart')
)

# Scatter
fig.add_trace(
    go.Scatter(x=df_tips['total_bill'], y=df_tips['tip'], mode='markers'),
    row=1, col=1
)

# Pie
ocean_counts = df['ocean_proximity'].value_counts()
fig.add_trace(
    go.Pie(labels=ocean_counts.index, values=ocean_counts.values),
    row=1, col=2
)

fig.update_layout(height=500, title_text="Mixed Subplots")
fig.show()
```

#### Faceted Plots (Plotly Express)

```python
# Automatic faceting similar to Seaborn's relplot
fig = px.scatter(df_tips, 
                 x='total_bill', 
                 y='tip',
                 color='sex',
                 facet_col='time',  # Create columns
                 facet_row='smoker',  # Create rows
                 title='Faceted Scatter Plot')
fig.show()
```

---

### Plotly Geographic Maps

**Purpose:** Interactive geographic visualizations

#### Scatter Map with Geographic Coordinates

```python
# Using housing data with lat/lon
fig = px.scatter_mapbox(df, 
                        lat='latitude', 
                        lon='longitude',
                        color='median_house_value',
                        size='population',
                        hover_name='ocean_proximity',
                        color_continuous_scale='Viridis',
                        title='California Housing Map',
                        zoom=5,
                        height=600)

fig.update_layout(mapbox_style='open-street-map')
fig.show()
```

**Available Map Styles:**
- `'open-street-map'` - Free, no token required
- `'carto-positron'` - Light theme
- `'carto-darkmatter'` - Dark theme
- `'stamen-terrain'` - Terrain features
- `'stamen-toner'` - High contrast

#### Choropleth Map (Colored Regions)

```python
# Example with built-in geographic data
df_gapminder = px.data.gapminder().query("year==2007")

fig = px.choropleth(df_gapminder, 
                    locations="iso_alpha",
                    color="gdpPercap",
                    hover_name="country",
                    color_continuous_scale='Plasma',
                    title='GDP per Capita by Country (2007)')
fig.show()
```

#### Line Map (Geographic Routes)

```python
# Create sample route data
route = pd.DataFrame({
    'lat': [37.7749, 34.0522, 36.7783, 40.7128],
    'lon': [-122.4194, -118.2437, -119.4179, -74.0060],
    'city': ['San Francisco', 'Los Angeles', 'Fresno', 'New York']
})

fig = px.line_mapbox(route, 
                     lat='lat', 
                     lon='lon',
                     hover_name='city',
                     zoom=3,
                     height=500,
                     title='Route Map')

fig.update_layout(mapbox_style='open-street-map')
fig.show()
```

---

### Plotly Customization & Themes

#### Applying Themes

```python
# Available themes: 'plotly', 'plotly_white', 'plotly_dark', 'ggplot2', 
#                   'seaborn', 'simple_white', 'none'

fig = px.scatter(df_tips, x='total_bill', y='tip', color='time',
                 template='plotly_dark',  # Apply theme
                 title='Dark Theme Example')
fig.show()
```

#### Custom Color Scales

```python
# Sequential color scales
fig = px.scatter(df_tips, x='total_bill', y='tip', 
                 color='size',
                 color_continuous_scale='Blues',  # or 'Viridis', 'Plasma', 'Inferno'
                 title='Custom Color Scale')
fig.show()

# Discrete color sequences
fig = px.bar(df_tips.groupby('day').size().reset_index(name='count'),
             x='day', y='count',
             color='day',
             color_discrete_sequence=px.colors.qualitative.Pastel,
             title='Pastel Colors')
fig.show()
```

#### Advanced Layout Customization

```python
fig = px.scatter(df_tips, x='total_bill', y='tip', color='sex')

fig.update_layout(
    title={
        'text': 'Custom Layout Example',
        'x': 0.5,  # Center title
        'xanchor': 'center'
    },
    xaxis=dict(
        title='Total Bill ($)',
        gridcolor='lightgray',
        showgrid=True,
        zeroline=False
    ),
    yaxis=dict(
        title='Tip ($)',
        gridcolor='lightgray',
        showgrid=True
    ),
    plot_bgcolor='white',
    font=dict(family='Arial', size=12),
    hovermode='closest',
    legend=dict(
        orientation='h',  # Horizontal legend
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    )
)

fig.show()
```

#### Animation

```python
# Animated scatter plot (requires time-based data)
df_gapminder = px.data.gapminder()

fig = px.scatter(df_gapminder, 
                 x='gdpPercap', 
                 y='lifeExp',
                 animation_frame='year',  # Animate over years
                 animation_group='country',
                 size='pop',
                 color='continent',
                 hover_name='country',
                 log_x=True,
                 range_x=[100, 100000],
                 range_y=[25, 90],
                 title='Gapminder: Life Expectancy vs GDP')

fig.show()
```

#### Exporting

```python
# Save as HTML
fig.write_html('interactive_plot.html')

# Save as static image (requires kaleido)
# pip install kaleido
fig.write_image('plot.png', width=1200, height=800)
fig.write_image('plot.pdf')
fig.write_image('plot.svg')
```

---

## Plotly Complete! 🎉

### What You've Mastered:

✅ **Interactive Scatter Plots** - With hover, zoom, and selection  
✅ **Line Plots** - Time series with multiple series  
✅ **Bar Charts** - Grouped and stacked variations  
✅ **Histograms** - With overlays and marginal plots  
✅ **Box Plots & Violin Plots** - Statistical summaries  
✅ **Pie & Donut Charts** - Interactive proportions  
✅ **3D Plots** - Surface, scatter, and line in 3D  
✅ **Subplots** - Complex multi-plot layouts  
✅ **Geographic Maps** - Interactive maps with coordinates  
✅ **Customization** - Themes, colors, and styling  
✅ **Animations** - Time-based animated visualizations  

### Key Advantages:

🖱️ **Interactivity** - Built-in hover, zoom, pan  
🌐 **Web-Ready** - Export as standalone HTML  
📱 **Responsive** - Works on any device  
🎨 **Modern Design** - Beautiful default themes  
📊 **Dashboard-Ready** - Perfect for Dash apps  
🗺️ **Geographic** - Built-in mapping capabilities  

---

## Complete Summary

### Library Comparison

| Feature | Matplotlib | Seaborn | Plotly |
|---------|-----------|---------|---------|
| **Level** | Low-level | High-level | High-level |
| **Interactivity** | Static | Static | Interactive |
| **Syntax** | Verbose | Concise | Concise |
| **3D Support** | Basic | No | Excellent |
| **Web Export** | PNG/PDF | PNG/PDF | HTML |
| **Statistics** | Manual | Automatic | Some automatic |
| **Learning Curve** | Steep | Moderate | Easy |
| **Best For** | Publication | EDA/Stats | Dashboards/Web |

### When to Use Each Library

**Use Matplotlib when:**
- Need complete control over every element
- Creating publication-quality static figures
- Building custom visualizations
- Working with scientific papers
- Memory/performance is critical

**Use Seaborn when:**
- Exploratory data analysis (EDA)
- Statistical visualizations
- Quick categorical comparisons
- Need beautiful defaults fast
- Working with pandas DataFrames

**Use Plotly when:**
- Creating interactive dashboards
- Web-based applications
- Need hover/zoom/pan functionality
- Geographic/3D visualizations
- Sharing interactive HTML reports
- Building with Dash framework

### Function Quick Reference

#### Matplotlib
```python
plt.scatter()      # Scatter plot
plt.plot()         # Line plot
plt.hist()         # Histogram
plt.boxplot()      # Box plot
plt.bar()          # Bar chart
plt.pie()          # Pie chart
plt.subplots()     # Create subplots
```

#### Seaborn
```python
# Axes-level
sns.scatterplot()  # Scatter
sns.lineplot()     # Line
sns.histplot()     # Histogram
sns.boxplot()      # Box plot
sns.barplot()      # Bar chart
sns.countplot()    # Count plot

# Figure-level
sns.relplot()      # Relational (scatter/line)
sns.catplot()      # Categorical
sns.displot()      # Distribution
```

#### Plotly Express
```python
px.scatter()       # Scatter plot
px.line()          # Line plot
px.histogram()     # Histogram
px.box()           # Box plot
px.bar()           # Bar chart
px.pie()           # Pie chart
px.scatter_3d()    # 3D scatter
px.scatter_mapbox() # Geographic map
```

### Visual Encoding Effectiveness

**Order of Perceptual Accuracy:**
1. Position (x, y) - Most accurate
2. Length - Very accurate
3. Angle/Slope - Moderately accurate
4. Area - Less accurate
5. Volume - Least accurate
6. Color (hue) - Good for categories
7. Color (saturation) - Moderate for values

### Plot Selection Guide

| Data Type | Relationship | Best Plot(s) |
|-----------|-------------|--------------|
| 2 Numerical | Correlation | Scatter, Line |
| 1 Numerical | Distribution | Histogram, Box, Violin |
| 1 Categorical | Frequency | Bar, Count, Pie |
| Num + Cat | Comparison | Box, Violin, Bar |
| Time Series | Trend | Line, Area |
| Geographic | Spatial | Map, Choropleth |
| 3D Data | Multi-dim | 3D Scatter, Surface |

---

## Best Practices Summary

### 1. Data Preparation
```python
# Always check your data first
df.head()
df.info()
df.describe()

# Handle missing values
df = df.dropna()  # or df.fillna()

# Convert data types
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].astype('category')
```

### 2. Choose the Right Plot

**Distribution Analysis:**
- Single variable: Histogram, Box plot, Violin plot
- Multiple groups: Grouped box plot, Overlaid histograms

**Relationships:**
- Two variables: Scatter plot, Line plot
- Multiple variables: Faceted plots, 3D plots

**Comparisons:**
- Categories: Bar chart, Count plot
- Groups: Grouped/Stacked bars, Faceted plots

**Composition:**
- Parts of whole: Pie chart, Stacked bar
- Over time: Stacked area chart

### 3. Customization Checklist

✅ Clear, descriptive title  
✅ Labeled axes with units  
✅ Appropriate font sizes (10-14pt)  
✅ Legend when needed  
✅ Color-blind friendly palette  
✅ Consistent styling  
✅ Remove chart junk  
✅ Highlight key findings  

### 4. Color Guidelines

**Sequential:** Use for ordered data (low to high)
- Blues, Greens, Reds, Viridis, Plasma

**Diverging:** Use for data with meaningful midpoint
- RdBu, RdYlGn, Spectral

**Qualitative:** Use for categories (no order)
- Set1, Set2, Pastel, Dark2

**Accessibility:**
```python
# Avoid red-green combinations
# Use ColorBrewer palettes
# Test with colorblind simulators
```

### 5. Performance Tips

**For Large Datasets:**
```python
# Matplotlib: Use rasterization
plt.scatter(..., rasterized=True)

# Plotly: Use WebGL
fig = go.Figure(go.Scattergl(...))  # Note the 'gl'

# Downsample if necessary
df_sample = df.sample(n=10000)
```

**Memory Optimization:**
```python
# Close figures when done
plt.close('all')

# Use appropriate data types
df['category'] = df['category'].astype('category')
```

---

## Advanced Topics

### 1. Combining Libraries

```python
# Seaborn plot with Matplotlib customization
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='x', y='y', ax=ax)
ax.axhline(0, color='red', linestyle='--')
plt.title('Combined Approach')
plt.show()
```

### 2. Statistical Annotations

```python
# Matplotlib with statistics
from scipy import stats

x = df['x']
y = df['y']
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

plt.scatter(x, y)
plt.plot(x, slope * x + intercept, 'r', label=f'R² = {r_value**2:.3f}')
plt.legend()
plt.show()
```

### 3. Animation

```python
# Matplotlib animation
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
line, = ax.plot([], [])

def update(frame):
    line.set_data(range(frame), np.random.randn(frame))
    return line,

ani = FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
```

### 4. Dashboard Creation

```python
# Using Plotly Dash
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(id='interval', interval=1000)
])

@app.callback(Output('live-graph', 'figure'),
              Input('interval', 'n_intervals'))
def update_graph(n):
    fig = px.scatter(df, x='x', y='y')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```

---

## Resources & Further Learning

### Official Documentation

**Matplotlib:**
- [Documentation](https://matplotlib.org/)
- [Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Tutorials](https://matplotlib.org/stable/tutorials/index.html)

**Seaborn:**
- [Documentation](https://seaborn.pydata.org/)
- [Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Gallery](https://seaborn.pydata.org/examples/index.html)

**Plotly:**
- [Documentation](https://plotly.com/python/)
- [Gallery](https://plotly.com/python/plotly-express/)
- [Dash Documentation](https://dash.plotly.com/)

### Learning Resources

**Websites:**
- [Python Graph Gallery](https://www.python-graph-gallery.com/)
- [From Data to Viz](https://www.data-to-viz.com/)
- [Plotly Community](https://community.plotly.com/)

**Books:**
- "Fundamentals of Data Visualization" by Claus O. Wilke
- "Storytelling with Data" by Cole Nussbaumer Knaflic
- "The Visual Display of Quantitative Information" by Edward Tufte

**Courses:**
- DataCamp: Data Visualization in Python
- Coursera: Applied Plotting, Charting & Data Representation
- Udemy: Data Visualization with Python

### Practice Datasets

```python
# Seaborn built-in datasets
sns.load_dataset('tips')
sns.load_dataset('titanic')
sns.load_dataset('iris')
sns.load_dataset('flights')
sns.load_dataset('planets')

# Plotly built-in datasets
px.data.iris()
px.data.tips()
px.data.gapminder()
px.data.stocks()
px.data.wind()

# Other sources
# - Kaggle datasets
# - UCI Machine Learning Repository
# - data.gov
# - Google Dataset Search
```

---

## Congratulations! 🎊🎉

You've completed a comprehensive journey through **Python Data Visualization**!

### Your New Superpowers:

✅ **Matplotlib Mastery**
- Create any standard plot type
- Customize every visual element
- Build complex multi-panel figures
- Publication-quality static graphics

✅ **Seaborn Expertise**
- Quick exploratory analysis
- Statistical visualizations
- Automatic aggregation & CI
- Beautiful default styling

✅ **Plotly Proficiency**
- Interactive web-based plots
- 3D visualizations
- Geographic mapping
- Dashboard-ready components
- Animation capabilities

### You Can Now:

📊 Choose the right visualization for your data  
🎨 Create beautiful, effective charts  
📈 Tell compelling data stories  
🔍 Explore patterns and insights  
💻 Build interactive dashboards  
📱 Create web-ready visualizations  
🎯 Follow best practices  
🚀 Continue learning advanced techniques  

---

## Final Tips

1. **Practice Regularly**: Use real datasets and experiment
2. **Start Simple**: Master basics before advanced features
3. **Think About Your Audience**: Choose appropriate complexity
4. **Iterate**: First draft is never final
5. **Get Feedback**: Share and improve
6. **Stay Updated**: Libraries evolve constantly
7. **Combine Tools**: Use strengths of each library
8. **Focus on Story**: Visualization serves the message

---

**Happy Visualizing!** 📊🎨✨

*Remember: The best visualization is the one that clearly communicates your insight to your audience.*

---

**End of Complete Data Visualization Guide**

*Created with ❤️ for mastering Python visualization libraries*

---

## Quick Command Reference

### Installation
```bash
pip install matplotlib seaborn plotly pandas numpy
pip install kaleido  # For Plotly static image export
pip install dash  # For Plotly dashboards
```

### Imports
```python
# Standard imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Jupyter magic
%matplotlib inline
```

### File Operations
```python
# Save Matplotlib
plt.savefig('plot.png', dpi=300, bbox_inches='tight')

# Save Plotly
fig.write_html('plot.html')
fig.write_image('plot.png')
```

---

**Version Info:**
- Python: 3.8+
- Matplotlib: 3.5+
- Seaborn: 0.12+
- Plotly: 5.0+
- Pandas: 1.3+
- NumPy: 1.21+

Last Updated: December 2025
```
