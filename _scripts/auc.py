import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import auc
from scipy.interpolate import interp1d

# Example Data (Replace with real values) 
# X -> Num of recommendations |  Y -> average distance of recommendations
# num_recommendations = np.array([1, 2, 3, 5, 10, 15])  # Number of places recommended
# avg_distance = np.array([2.306889596397673, 1.4415367475383, 1.9510169997568079, 1.3681276455327742, 2.1385756882740434, 4.462730155951702])  # Average distance of recommended places for density range 0-100
# avg_distance = np.array([2.306889596397673,2.638433550295748,1.9510169997568079, 13.658833419925042, 13.658833419925042, 13.658833419925042 ])  # Average distance of recommended places for density range 20-80

# X -> Num of Recommendations | Y -> Preference/Ranking Score
num_recommendations = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])  # Number of places recommended
ranking_score = np.array([0.8880768259851184, 0.880814650903478, 0.862580029048869, 0.8529374910640772, 0.8466231411612956 ,0.8421796807918086, 0.8373840453932224, 0.8315012620570821, 0.825798429742096, 0.8205770782164923, 0.8103151589523562, 0.7951835257398187, 0.7755917651894789, 0.7425339629709102, 0.7027797367736758])

# auc_value = auc(num_recommendations, ranking_score)

# # Plot the AUC curve
# plt.figure(figsize=(7, 5))
# plt.plot(num_recommendations, ranking_score, marker='o', linestyle='-', label=f'AUC = {auc_value:.2f}')
# plt.fill_between(num_recommendations, ranking_score, alpha=0.2)
# plt.xlabel('Number of Recommended Places')
# # plt.ylabel('Average Distance to User (km)')
# plt.ylabel('Average Preference Score')
# plt.title('AUC Curve: Tourist Recommendation System Density range 0-80')
# plt.legend()
# plt.grid()
# plt.savefig('density0to80NumberOfRecommendationsToPreferenceScore.png', dpi=500)
# plt.show()



auc_value = auc(num_recommendations, ranking_score)

# Smooth curve using interpolation
smooth_x = np.linspace(num_recommendations.min(), num_recommendations.max(), 300)
smooth_y = interp1d(num_recommendations, ranking_score, kind='cubic')(smooth_x)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(smooth_x, smooth_y, linestyle='-', linewidth=2, color='#007acc', label=f'AUC = {auc_value:.3f}')
plt.scatter(num_recommendations, ranking_score, color='#cc3300', edgecolors='black', zorder=3, label='Data Points')  # Add points

# Fill area under curve
plt.fill_between(smooth_x, smooth_y, alpha=0.3, color='#007acc')

# Labels & Title
plt.xlabel('Number of Recommended Places')
plt.ylabel('Average Preference Score')
plt.title('AUC Curve: Tourist Recommendation System (Density Range 0-80)')

# Grid, Legend, and Styling
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(fontsize=10 )
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Save High-Resolution Image
plt.savefig('density0to80NumberOfRecommendationsToPreferenceScore.png', dpi=500)

# Show
plt.show()