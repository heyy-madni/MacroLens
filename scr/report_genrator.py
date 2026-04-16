
from matplotlib import pyplot as plt





def __():
# def genrate_charts():


#     fig, ax = plt.subplots(figsize=(14, 6))

#     fig.patch.set_facecolor('#0f0f0f')
#     ax.set_facecolor('#1a1a1a')

#     # filter anomalies before plotting
#     clean = df[df['GDP_Growth'].between(-20, 40)]
#     country = clean[clean["Country"] == "India"]
#     # clean = df
#     ax.plot(clean['Year'], country['GDP_Growth'], color="#1fd50f", linewidth=2,
#             marker='o', markersize=3, label='GDP Growth (%)', zorder=3)
#     ax.plot(clean['Year'], country['Inflation'], color="#bd2b06", linewidth=2,
#             marker='o', markersize=3, label='Inflation (%)', zorder=3)
#     ax.plot(clean['Year'], country['Economic_Score'], color="#06bdbd", linewidth=2,
#                 marker='o', markersize=3, label='Economic Score', zorder=3   )
#     # shade recession years
#     recessions = [ (2008, 2009), (2020, 2021)]
#     for start, end in recessions:
#         ax.axvspan(start, end, color='#ff5252', alpha=0.12, zorder=1)

#     ax.axhline(0, color='#555555', linewidth=0.8, linestyle='--')
    
#     ax.set_title('India Economic Indicators', fontsize=16,
#                  fontweight='bold', color='white', pad=16)
#     ax.set_xlabel('Year', color='#aaaaaa', fontsize=12)
#     ax.set_ylabel('Percentage (%)', color='#aaaaaa', fontsize=12)

#     ax.tick_params(colors='#aaaaaa')
#     ax.spines['bottom'].set_color('#333333')
#     ax.spines['left'].set_color('#333333')
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
#     ax.grid(color='#2a2a2a', linewidth=0.6)

#     ax.legend(facecolor='#2a2a2a', edgecolor='#444444',
#               labelcolor='white', fontsize=10)

#     plt.tight_layout()
#     plt.show()
    pass




def over_view_of_economy_chart(df, choice="India"):
    from data_manager import df
    clean = df[df['GDP_Growth'].between(-20, 25)]
    fig, ax = plt.subplots(figsize=(14, 6))

    # background
    
    fig.patch.set_facecolor('#0f0f0f')
    ax.set_facecolor('#1a1a1a')
    ax.axhline(0, color='#555555', linewidth=0.9, linestyle='--')
   
    plt.grid(color='#2a2a2a', linewidth=0.6)
    # todo
   
    country = clean[clean["Country"] == choice]

    # labkels and title
    ax.set_title('Country Economic Indicators', fontsize=16,
                 fontweight='bold', color='white', pad=16)
    ax.set_xlabel(f'Year                              country:{choice}', color='#aaaaaa', fontsize=12)
    ax.set_ylabel('Percentage (%)', color='#aaaaaa', fontsize=12)


    # background
    x_ticks = country['Year'][::2].tolist()
    ax.set_xticks(x_ticks)
    ax.tick_params(colors='#aaaaaa')
    ax.spines['bottom'].set_color('#333333')
    ax.spines['left'].set_color('#333333')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)







      # plot lines
    ax.plot(country['Year'], country['GDP_Growth'], color="#1cd40b", linewidth=2,
            marker='o', markersize=3, label='GDP Growth (%)', zorder=3)

    ax.plot(country['Year'], country['Inflation'], color="#bd2b06", linewidth=2,
            marker='o', markersize=3, label='Inflation (%)', zorder=3)
   
    ax.plot(country['Year'], country['Unemployment_Change'], color="#06bdbd", linewidth=2,
                marker='o', markersize=3, label='Unemployment', zorder=3   )






    plt.legend(facecolor='#2a2a2a', edgecolor='#444444',labelcolor='white', fontsize=10)
    
    plt.show()




def genrate_report(df):
    lines = []
    lines.append("ECONOMIC REPORT\n")
    for _, row in df.iterrows():
        lines.append(f"• {int(row['Year'])} [{row['Country']}]: {row['Condition']} — {row['Contradiction']}")
    print("\n".join(lines))


if __name__ == "__main__":
    # genrate_report()
    over_view_of_economy_chart("USA")

