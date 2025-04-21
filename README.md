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
*1. Place input data files into the Data/ directory:*
The dataset files are required for the experiments. Place the following files in the Data/ folder:
- Iris.csv
- Mall_Customers.csv

*2. Execute the MeanShift.ipynb script to train the Mean Shift Clustering model:*
Run the MeanShift.ipynb notebook to implement and train the Mean Shift Clustering model using the provided data.

*3. Evaluate the model's clustering performance in Evaluation.ipynb:*
After training the model, evaluate the clustering quality using the following metrics:
- Silhouette Score
- Davies-Bouldin Index
- Calinski-Harabasz Index

*4. Compare clustering performance across algorithms in Solution.ipynb:*
In the Solution.ipynb notebook, compare the clustering performance of the following algorithms using the same evaluation metrics:
- Mean Shift
- KMeans
- DBSCAN
- Hierarchical Agglomerative Clustering (HAC)

---

## **Results**
### Key Findings:
1. **Mean Shift Clustering**:

- **Flexibility**: No need for a predefined number of clusters, adapts to the data's inherent structure.
- **Cluster Shape**: Effectively identifies arbitrarily shaped clusters, making it ideal for complex data distributions.
- **Bandwidth Sensitivity**: Performance is influenced by the bandwidth parameter; improper choice can affect clustering results.
- **Outlier Robustness**: Handles outliers better than K-Means but may still be affected by small bandwidth settings.
- **Computational Complexity**: Can be computationally expensive, especially with large datasets.
 
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

