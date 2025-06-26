import matplotlib.pyplot as plt
import seaborn as sns

def plot_malnutrition_by_country(df, country_column, value_column, top_n=10):
    """
    Plot the top N countries with the highest malnutrition values.
    """
    top_countries = df.groupby(country_column)[value_column].mean().nlargest(top_n).sort_values()
    
    plt.figure(figsize=(10, 6))
    top_countries.plot(kind='barh', color='coral')
    plt.xlabel("Average Malnutrition Value")
    plt.title(f"Top {top_n} Countries by Malnutrition")
    plt.tight_layout()
    plt.show()
