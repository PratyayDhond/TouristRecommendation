import numpy as np
import matplotlib.pyplot as plt

# Data
num_recommendations = np.array([1, 2, 3, 5, 10, 15])  # Number of places recommended
time_sectors = np.array([1,2,3,4])
avg_distance_sec_1 = np.array([0.8024560242742227, 0.6893199614765748, 0.7020096880095403, 1.5982029935755722, 2.192063692941522, 4.462730155951702])
avg_distance_sec_2 = np.array([2.306889596397673, 1.4415367475383, 1.9510169997568079, 1.3681276455327742, 2.1385756882740434, 4.462730155951702 ])
avg_distance_sec_3 = np.array([0.8024560242742227, 0.6893199614765748, 1.6522454101349056, 1.8699759193167735, 2.857292600383551, 4.462730155951702])
avg_distance_sec_4 = np.array([0.576183898678927, 0.6517865198771993, 1.203487545384024, 2.1708626337414634, 2.1920636929415225, 4.462730155951702]) 

# Mapping
sector_labels = ["Morning", "Afternoon", "Evening", "Night"]
sector_data = [avg_distance_sec_1, avg_distance_sec_2, avg_distance_sec_3, avg_distance_sec_4]
colors = ['#007acc', '#cc3300', '#009933', '#9933ff']

# Plotting
plt.figure(figsize=(9, 6))

for label, distances, color in zip(sector_labels, sector_data, colors):
    plt.plot(num_recommendations, distances, linestyle='-', linewidth=2, color=color, label=label)
    plt.fill_between(num_recommendations, distances, alpha=0.2, color=color)
    plt.scatter(num_recommendations, distances, color=color, edgecolors='black', zorder=3)

# Labels & Title
plt.xlabel('Number of Recommended Places')
plt.ylabel('Average Distance (km)')
plt.title('Average Distance vs Number of Recommendations (Straight Line AUC Style)')

# Styling
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(title='Time of Day', fontsize=10, loc='lower right')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Save High-Resolution Image
plt.savefig('straightLine_AUC_Distance_vs_Recommendations.png', dpi=500)

# Show
plt.show()

# num_recommendations = np.array([1, 2, 3, 4,5,6,7,8,9,10,11,12])
# avg_preference_sector_1 = np.array([0.9634892135770062, 0.9511388364148993, 0.9192560416019783, 0.9025236146364376, 0.8888603741515485, 0.8778180100322138, 0.8688112778206989, 0.8496851902348055, 0.8232076532287269, 0.7853712979743854, 0.7187585962446565, 0.7187585962446565])
# avg_preference_sector_2 = np.array([0.9186823783256219, 0.8641411314345455, 0.8399007670230839, 0.8053882780610928, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508, 0.6497987490979508])
# avg_preference_sector_3 = np.array([0.9624095914447526, 0.9487096866173285, 0.9235445406273195, 0.9062709872684270, 0.8946122517234422, 0.8850154909139053, 0.8758155482795164, 0.8684548708465913, 0.8398918137725366, 0.7896537990989918, 0.7275018997248022, 0.7275018997248022])
# avg_preference_sector_4 = np.array([0.9545268343166657, 0.9223330735530235, 0.9110240542074722, 0.8995593216789349, 0.8918061990635533, 0.8858539689912753, 0.8760429492322377, 0.8558936726057816, 0.8044454613083484, 0.7240009151775135, 0.7240009151775135, 0.7240009151775135])