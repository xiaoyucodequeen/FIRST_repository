import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取清洗后的数据
file_path = "issues_data_cleaned.csv"
df = pd.read_csv(file_path)

# 检查并转换 'Update Time' 为 datetime 类型
if not pd.api.types.is_datetime64_any_dtype(df['Update Time']):
    df['Update Time'] = pd.to_datetime(df['Update Time'], errors='coerce')  # 无法解析的时间将被设置为 NaT

# 确保数据中没有无效日期
df = df.dropna(subset=['Update Time'])  # 删除 'Update Time' 中为 NaT 的行

# 设置 Seaborn 风格
sns.set_theme(style="darkgrid")

#更新类型分布
plt.figure(figsize=(8, 6))
sns.countplot(y="Update Type", data=df, order=df['Update Type'].value_counts().index)
plt.title("Distribution of Update Types", fontsize=18)
plt.xlabel("Count")
plt.ylabel("Update Type")
plt.show()

#浏览量分布
plt.figure(figsize=(8, 6))
#直方图
sns.histplot(df['View Count'], bins=20, kde=True, color='skyblue')
plt.title("Distribution of View Count", fontsize=18)
plt.xlabel("View Count")
plt.ylabel("Frequency")
plt.show()

#按时间的更新数量趋势
df['Month'] = df['Update Time'].dt.to_period('M')  # 按月份聚合
time_trend = df.groupby('Month').size()
plt.figure(figsize=(10, 6))
time_trend.plot(kind='line', marker='o', color='green')
plt.title("Update Count Trend Over Time", fontsize=18)
plt.xlabel("Time")
plt.ylabel("Number of Updates")
plt.grid()
plt.show()

#高浏览量的更新类型
top_viewed = df.sort_values(by='View Count', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="View Count", y="Update Content", data=top_viewed, palette="Blues_r")
plt.title("Top 10 Update Contents by View Count", fontsize=18)
plt.xlabel("View Count")
plt.ylabel("Update Content")
plt.show()

#浏览量与更新时间的关系
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Update Time", y="View Count", data=df, hue="Update Type", palette="tab10", s=100)
plt.title("Relationship between Update Time and View Count", fontsize=18)
plt.xlabel("Update Time")
plt.ylabel("View Count")
plt.show()

#浏览量与更新类型联合分析
plt.figure(figsize=(10, 6))
sns.boxplot(x="Update Type", y="View Count", data=df, palette="Set2")
plt.title("View Count Distribution by Update Type", fontsize=18)
plt.xlabel("Update Type")
plt.ylabel("View Count")
plt.xticks(rotation=80)
plt.show()
