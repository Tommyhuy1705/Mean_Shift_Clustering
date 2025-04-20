# **Mean_Shift_Clustering**

## Introduction  

- Mean Shift Clustering is a density-based unsupervised learning algorithm that groups data points by shifting them toward regions of higher density. Unlike k-means, it does not require specifying the number of clusters beforehand, making it useful for identifying arbitrary cluster shapes.
The algorithm iteratively moves data points to the mean of nearby points within a defined bandwidth, converging to dense regions in the feature space. The choice of bandwidth significantly impacts clustering performance.
Mean Shift is widely used in image segmentation, object tracking, and anomaly detection. Despite its flexibility, its computational cost can be high for large datasets. This study explores its theoretical foundations, implementation, and optimization techniques.
---

## **Features**
- **Density-Based Approach**: Finds clusters based on high-density regions without assuming a specific number of clusters.
- **Adaptive Cluster Shape**: Identifies arbitrarily shaped clusters, unlike k-means which assumes spherical clusters.
- **Bandwidth Sensitivity**: The choice of bandwidth affects the clustering outcome, influencing the number and shape of clusters.
- **Non-Parametric**: Does not require prior knowledge about the data distribution or the number of clusters.
- **Robust to Noise**: Can handle outliers better than some other clustering methods.
- **High Computational Cost**: Computationally expensive for large datasets due to its iterative nature.

---

## Project Structure  
```plaintext
├── data/                           # Input data
│   ├── Iris.csv                    # Iris dataset
│   ├── Mall_Customers.csv          # Customers dataset
│
├── Output/                         # Model storage
│   ├── MeanShift_dataset1.mdl      # Mean Shift for Iris dataset
│   ├── MeanShift_dataset2.mdl      # Mean Shift for Customers dataset
│
├── MeanShift.ipynb                 # Main source code
│
├── Evaluation.ipynb                # Clustering model evaluation using Silhouette Scores, Davies-Bouldin Index, Calinski-Harabasz Index.
│
├── mean_shift_utils.py             # Utility functions for running and evaluating Mean Shift clustering.
│
├── Solution.ipynb                  # Clustering model comparison: Mean Shift vs K-Means, DBSCAN, and Hierarchical Agglomerative Clustering.
│
├── Simulation.ipynb                # Theoretical simulation of the Mean Shift algorithm
|
└── README.md                       # Project documentation
```

---

## **Installation**
Follow the steps below to set up the project:

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/Tommyhuy1705/Mean_Shift_Clustering.git
   cd your-repo-name
   ```

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:  
   ```bash
   python src/main.py
   ```

---

## **Usage**
1. Place input test images or videos into the `data/images/` or `data/videos/` directories. --> Changes
2. Modify configurations in `experiments/experiment.md` to set up desired experiments.
3. Execute the `main.py` script to run the desired algorithm.
4. Analyze results in the `results/` folder:
   - CSV files provide performance metrics.
   - Plots visualized in `.ipynb` notebooks or saved in the `plots/` folder.

---

## **Results**
### Key Findings:
1. **___**:
   - 
 

### Result Visualization:
 

---

## **Contributions**
- Implemented Mean Shift Clustering with flexible bandwidth selection.
- Evaluated clustering quality using multiple metrics.
- Provided visualization tools for cluster analysis.
- Designed a structured pipeline for data preprocessing and model training.

---

## **Future Work**
- Optimize algorithm efficiency for large-scale datasets.
- Experiment with adaptive bandwidth selection techniques.
- Apply Mean Shift to real-world applications such as image segmentation and anomaly detection.
- Integrate additional evaluation methods for better clustering assessment.

---

## **Acknowledgments**
Special thanks to the contributors and open-source community for providing tools and resources.

--- 

