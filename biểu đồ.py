import matplotlib.pyplot as plt

# Dữ liệu bandwidth và chỉ số thực nghiệm
bandwidths = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
silhouette_scores = [0.3969, 0.3621, 0.4247, 0.5158, 0.5324, 0.5266, 0.5520, 0.4882]
db_scores = [0.6411, 0.6555, 0.7685, 0.7064, 0.5846, 0.6523, 0.5685, 0.7136]
ch_scores = [224.3, 189.1, 208.4, 224.0, 236.5, 243.0, 248.6, 171.6]


import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(figsize=(10, 6))

# Silhouette Score - trục trái
ax1.set_xlabel('Bandwidth')
ax1.set_ylabel('Silhouette Score', color='blue')
line1, = ax1.plot(bandwidths, silhouette_scores, marker='o', color='blue', label='Silhouette Score')
ax1.tick_params(axis='y', labelcolor='blue')

# Trục phải: DBI và CHI
ax2 = ax1.twinx()
line2, = ax2.plot(bandwidths, db_scores, marker='s', color='red', label='Davies-Bouldin Index')
line3, = ax2.plot(bandwidths, ch_scores, marker='^', color='green', label='Calinski-Harabasz Index')
ax2.set_ylabel('DBI / CHI')

# Gộp legend
lines = [line1, line2, line3]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper center')

plt.title("Biểu đồ đánh giá Mean Shift theo Bandwidth")
plt.grid(True)
plt.tight_layout()
plt.show()

