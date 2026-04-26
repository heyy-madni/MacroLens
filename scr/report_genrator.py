#imports
from matplotlib import pyplot as plt





def over_view_of_economy_chart(df, choice="India"):
    from data_pipeline import df
    clean = df[df['gdp growth'].between(-20, 25)]
    fig, ax = plt.subplots(figsize=(14, 6))

    # background
    
    fig.patch.set_facecolor('#0f0f0f')
    ax.set_facecolor('#1a1a1a')
    ax.axhline(0, color='#555555', linewidth=0.9, linestyle='--')
   
    plt.grid(color='#2a2a2a', linewidth=0.6)
    # todo
   
    country = clean[clean["country"] == choice]

    # labkels and title
    ax.set_title('country Economic Indicators', fontsize=16,
                 fontweight='bold', color='white', pad=16)
    ax.set_xlabel(f'Year                              country:{choice}', color='#aaaaaa', fontsize=12)
    ax.set_ylabel('Percentage (%)', color='#aaaaaa', fontsize=12)


    # background
    x_ticks = country['Years'][country['Years'] % 5 == 0].tolist()
    ax.tick_params(axis='x', rotation=45)

    x_ticks.append(country['Years'].iloc[-1])  # Ensure the last year is included
    
    ax.set_xticks(x_ticks)


    ax.tick_params(colors='#aaaaaa')
    ax.spines['bottom'].set_color('#333333')
    ax.spines['left'].set_color('#333333')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)







      # plot lines
    ax.plot(country['Years'], country['gdp growth'], color="#1cd40b", linewidth=2,
            marker='o', markersize=3, label='GDP Growth (%)', zorder=3)

    ax.plot(country['Years'], country['inflation'], color="#bd2b06", linewidth=2,
            marker='o', markersize=3, label='Inflation (%)', zorder=3)
   
    ax.plot(country['Years'], country['unemployment'], color="#06bdbd", linewidth=2,
                marker='o', markersize=3, label='Unemployment', zorder=3   )






    plt.legend(facecolor='#2a2a2a', edgecolor='#444444',labelcolor='white', fontsize=10)
    
    plt.show()





def generate_report(df, country="India"):


    filtered = df[df['country'] == country]
    
    from functions import get_condition, detect_contradiction
    filtered["Condition"] = filtered.apply(get_condition, axis=1)
    filtered["Contradiction"] = filtered.apply(detect_contradiction, axis=1)
    if filtered.empty:
        print(f"No data found for: {country}")
        return
    
    lines = [f"ECONOMIC REPORT — {country}\n"]
    
    for _, row in filtered.iterrows():
        lines.append(f"• {int(row['Years'])} [{row['country']}]: {row['Condition']} — {row['Contradiction']}")
    
    print("\n".join(lines))


if __name__ == "__main__":
    from data_pipeline import df
    generate_report(df, "India")
    
    # over_view_of_economy_chart(df,choice="United States")

