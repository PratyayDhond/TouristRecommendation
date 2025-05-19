import numpy as np
import matplotlib.pyplot as plt

# Data
num_recommendations = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
num_recommendations = np.array([1, 2, 3, 4,5,6,7,8,9,10,11,12])
avg_preference_sector_1 = np.array([0.9634892135770062, 0.9511388364148993, 0.9192560416019783, 0.9025236146364376, 0.8888603741515485, 0.8778180100322138, 0.8688112778206989, 0.8496851902348055, 0.8232076532287269, 0.7853712979743854, 0.7187585962446565, 0.7187585962446565])
avg_preference_sector_2 = np.array([0.9186823783256219, 0.8641411314345455, 0.8399007670230839, 0.8053882780610928, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508])
avg_preference_sector_3 = np.array([0.9624095914447526, 0.9487096866173285, 0.9235445406273195, 0.9062709872684270, 0.8946122517234422, 0.8850154909139053, 0.8758155482795164, 0.8684548708465913, 0.8398918137725366, 0.7896537990989918, 0.7275018997248022, 0.7275018997248022])
avg_preference_sector_4 = np.array([0.9545268343166657, 0.9223330735530235, 0.9110240542074722, 0.8995593216789349, 0.8918061990635533, 0.8858539689912753, 0.8760429492322377, 0.8558936726057816, 0.8044454613083484, 0.7240009151775135, 0.7240009151775135, 0.7240009151775135])

# Mapping
sector_labels = ["Morning", "Afternoon", "Evening", "Night"]
sector_data = [avg_preference_sector_1, avg_preference_sector_2, avg_preference_sector_3, avg_preference_sector_4]
colors = ['#007acc', '#cc3300', '#009933', '#9933ff']

# Plot
plt.figure(figsize=(10, 6))

for label, preferences, color in zip(sector_labels, sector_data, colors):
    plt.plot(num_recommendations, preferences, linestyle='-', linewidth=2, color=color, label=label)
    plt.fill_between(num_recommendations, preferences, alpha=0.2, color=color)
    plt.scatter(num_recommendations, preferences, color=color, edgecolors='black', zorder=3)

# Labels & Title
plt.xlabel('Number of Recommended Places')
plt.ylabel('Average Preference Score')
plt.title('Preference Score vs Number of Recommendations (Time-Based Sectors)')

# Styling
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(title='Time of Day', fontsize=10, loc='lower right')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Save
plt.savefig('preference_vs_recommendations_straight_line_auc.png', dpi=500)

# Show
plt.show()
