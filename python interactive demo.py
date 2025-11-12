import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Generate two simulated groups (e.g., survival scores)
np.random.seed(42)
male = np.random.normal(0.45, 0.10, 200)     # mean 45%, some spread
female = np.random.normal(0.70, 0.10, 200)   # mean 70%, some spread

# Conduct t-test
t_stat, p_value = stats.ttest_ind(male, female)
print(f"t-statistic = {t_stat:.2f}, p-value = {p_value:.4f}")

# Plot overlapping distributions
sns.kdeplot(male, label='Male', fill=True, alpha=0.4)
sns.kdeplot(female, label='Female', fill=True, alpha=0.4)

# Annotate chart
plt.title(f"Visualizing p-value (p = {p_value:.4f})")
plt.xlabel('Survival Rate')
plt.ylabel('Density')
plt.legend()

# Highlight p-value interpretation zone
plt.text(0.5, 2.0, "Overlap = possible by chance (p-value region)", fontsize=10, color='gray')
plt.text(0.72, 1.5, "Separated = likely real difference", fontsize=10, color='darkgreen')

plt.show()


#-----
#⚙️ Common Uses of SciPy
#Module	Purpose	Example
#scipy.stats	Statistics & probability	t-tests, ANOVA, correlation, distributions
#scipy.optimize	Optimization	Minimizing or maximizing functions
#scipy.integrate	Integration	Calculating area under a curve
#scipy.signal	Signal processing	Filtering, Fourier transforms
#scipy.spatial	Spatial data	Distances, clustering, KD-trees
#scipy.interpolate	Interpolation	Estimating values between known data points
#scipy.fft	Fast Fourier Transforms	Frequency analysis
#scipy.linalg	Linear algebra	Solving systems of equations, matrix operations
