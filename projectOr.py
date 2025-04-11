# Project Name :-> Electricity Consumption Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv("CDCF.csv")    

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Interactive Menu
while True:
    print("\nChoose an option:")
    print("1. Exploratory Data Analysis (EDA)")
    print("2. View Pre-Designed Objectives")
    print("3. Create Your Own Analysis")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("\nPerforming EDA...")
        df.info()
        print(df.head())
        print(df.describe())
        # Correlation Heatmap
        plt.figure(figsize=(8, 6))
        numeric_cols = df.select_dtypes(include=['number']).drop(columns=['Category Code'], errors='ignore')
        numeric_corr = numeric_cols.corr()
        sns.heatmap(numeric_corr, annot=True, cmap='coolwarm', fmt='.2f')

        plt.title('Correlation Heatmap (Excluding Category Code)')
        plt.show()
    
    elif choice == "2":
        print("\nPre-Designed Objectives:")
        print("1. Analyze Relationship Between Load and Units Consumed")
        print("2. Identify Top 10 Areas with Highest Electricity Consumption")
        print("3. Compare Billed Services with Total Services")
        print("4. Analyze Electricity Consumption by Circle")
        print("5. Analyze Distribution of Billed Services")
        print("6. Analyze % Billed Services")
        print("7. Analyze Distribution of Electrical Load")
        obj_choice = input("Choose an objective (1-7): ")
        
        if obj_choice == "1":
            plt.figure(figsize=(8, 5))
            sns.scatterplot(x=df['Load'], y=df['Units'], alpha=0.5, color='brown')
            plt.title('Load vs Electricity Consumption')
            plt.xlabel('Load')
            plt.ylabel('Units Consumed')
            plt.show()
        elif obj_choice == "2":
            top_areas = df.groupby('Area')['Units'].sum().nlargest(10)
            plt.figure(figsize=(10, 6))
            top_areas.plot(kind='bar', color='darkred')
            plt.title('Top 10 Areas by Electricity Consumption')
            plt.xlabel('Area')
            plt.ylabel('Total Units')
            plt.xticks(rotation=45)
            plt.show()
        elif obj_choice == "3":
            plt.figure(figsize=(10, 5))
            sns.scatterplot(x=df['Total Services'], y=df['Billed Services'], alpha=0.6)
            plt.title('Total Services vs Billed Services')
            plt.xlabel('Total Services')
            plt.ylabel('Billed Services')
            plt.show()
        elif obj_choice == "4":
            plt.figure(figsize=(12, 6))
            sns.barplot(x=df['Circle'], y=df['Units'], hue=df['Circle'], estimator=sum, palette='viridis', legend=False)
            plt.xticks(rotation=45)
            plt.title('Total Electricity Consumption by Circle')
            plt.xlabel('Circle')
            plt.ylabel('Total Units')
            plt.show()
        elif obj_choice == "5":
            plt.figure(figsize=(8, 5))
            sns.boxplot(y=df['Billed Services'], color='purple')
            plt.title('Distribution of Billed Services')
            plt.ylabel('Billed Services')
            plt.show()
        elif obj_choice == "6":
            plt.figure(figsize=(7, 7))
            billed_percentage = (df['Billed Services'].sum() / df['Total Services'].sum()) * 100
            unbilled_percentage = 100 - billed_percentage
            labels = ['Billed Services', 'Unbilled Services']
            sizes = [billed_percentage, unbilled_percentage]
            colors = ['green', 'red']
            wedges, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'})
            plt.legend(wedges, labels, title="Service Status", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
            plt.title('% Billed vs. % Unbilled Services')
            plt.show()
        elif obj_choice == "7":
            plt.figure(figsize=(8, 5))
            sns.histplot(df['Load'], bins=30, kde=True, color='blue')
            plt.title('Distribution of Load')
            plt.xlabel('Load')
            plt.ylabel('Frequency')
            plt.show()
    
    elif choice == "3":
        print("\nCreate Your Own Analysis")
        column = input(f"Choose a column from {list(df.columns)}: ")
        graph_type = input("Choose a graph type (bar, scatter, hist, pie): ")
        
        if graph_type == "bar":
            plt.figure(figsize=(10, 5))
            sns.barplot(x=df[column], y=df['Units'], estimator=sum)
            plt.title(f'{column} vs Units')
            plt.xlabel(column)
            plt.ylabel('Units')
            plt.xticks(rotation=45)
            plt.show()
        elif graph_type == "scatter":
            x_col = input("Choose the X-axis column: ")
            y_col = input("Choose the Y-axis column: ")
            plt.figure(figsize=(8, 5))
            sns.scatterplot(x=df[x_col], y=df[y_col], alpha=0.5)
            plt.title(f'{x_col} vs {y_col}')
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()
        elif graph_type == "hist":
            plt.figure(figsize=(8, 5))
            sns.histplot(df[column], bins=30, kde=True)
            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()
        elif graph_type == "pie":
            df[column].value_counts().plot.pie(autopct='%1.1f%%')
            plt.title(f'Distribution of {column}')
            plt.show()
    
    elif choice == "4":
        print("Exiting...")
        break
