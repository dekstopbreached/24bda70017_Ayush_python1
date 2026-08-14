import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

n_flips = 30      
p_heads = 0.65    
trials = 5000     

heads_counts = np.random.binomial(
    n=n_flips,
    p=p_heads,
    size=trials
)

exp_mean = np.mean(heads_counts)
exp_var = np.var(heads_counts)

theo_mean = n_flips * p_heads
theo_var = n_flips * p_heads * (1 - p_heads)

print("===== MEAN =====")
print(f"Theoretical Mean: {theo_mean}")
print(f"Experimental Mean: {exp_mean:.3f}")

print("\n===== VARIANCE =====")
print(f"Theoretical Variance: {theo_var}")
print(f"Experimental Variance: {exp_var:.3f}")

plt.figure(figsize=(10, 6))

sns.histplot(
    heads_counts,
    bins=31,
    kde=True,
    color="darkgreen",
    stat="probability"
)

plt.title("Probability Distribution of Heads in 30 Coin Flips (5,000 Trials)")
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.xticks(range(0, 31))
plt.grid(alpha=0.3)

plt.show()