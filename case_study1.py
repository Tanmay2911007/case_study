import pandas as pd
import matplotlib.pyplot as plt

file_path = r"Divvy_Trips_2019_Q1.xlsx"  

try:
    df = pd.read_excel(file_path)
except:
    df = pd.read_csv(file_path, encoding='latin1')

print(" Data Loaded Successfully")
print("Rows, Columns:", df.shape)

print("\n--- INFO ---")
df.info()

print("\nDuplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after:", df.duplicated().sum())

print("\n--- Missing Values Before ---")
print(df.isnull().sum())

df = df.dropna()

print("\n--- Missing Values After ---")
print(df.isnull().sum())

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("\n Cleaned Column Names:")
print(df.columns.tolist())

if 'tripduration' in df.columns:
    invalid_count = (df['tripduration'] <= 0).sum()
    print(f"\nRemoving {invalid_count} invalid trip durations...")
    df = df[df['tripduration'] > 0]

if 'start_time' in df.columns:
    df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce')
    df['day_of_week'] = df['start_time'].dt.day_name()
    df['hour'] = df['start_time'].dt.hour

print("\n--- SUMMARY ---")
print(df.describe())

output_path = r"D:\JustDatasets\Divvy_Trips_2019_Q1_cleaned.csv"
df.to_csv(output_path, index=False)
print("\n Cleaned dataset saved successfully at:", output_path)

print("\n Data Cleaning Completed Successfully")
print("\n--- Generating Visualizations ---")

if 'day_of_week' in df.columns:
    plt.figure(figsize=(8, 5))
    df['day_of_week'].value_counts().reindex(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ).plot(kind='bar', color='steelblue', edgecolor='black')
    plt.title('Trips per Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Trip Count')
    plt.tight_layout()
    plt.show()

if 'hour' in df.columns:
    plt.figure(figsize=(8, 5))
    df['hour'].value_counts().sort_index().plot(kind='line', marker='o')
    plt.title('Trips by Hour of Day')
    plt.xlabel('Hour (24-hour format)')
    plt.ylabel('Trip Count')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if 'usertype' in df.columns:
    plt.figure(figsize=(6, 5))
    df['usertype'].value_counts().plot(kind='bar', color='darkcyan', edgecolor='black')
    plt.title('User Type Distribution')
    plt.xlabel('User Type')
    plt.ylabel('Number of Trips')
    plt.tight_layout()
    plt.show()

if 'tripduration' in df.columns:
    plt.figure(figsize=(8, 5))
    df['tripduration'].plot(kind='hist', bins=50, color='slategray', edgecolor='black')
    plt.title('Trip Duration Distribution')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

print("\n Visualization completed successfully.")

plt.savefig('output_graphs/trips_per_day.png')
