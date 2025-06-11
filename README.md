# Malaria in Africa - PCA Analysis

A collaborative Principal Component Analysis (PCA) implementation to analyze malaria data across African countries using the Africanized dataset.

## 👥 Team Members & Task Division

- **Mitali Bela** - Steps 1 & 3: Data Loading/Standardization & Covariance Matrix
- **Stecie Niyonzima** - Step 4: Eigendecomposition
- **Charlotte Kariza** - Steps 5 & 6: Component Sorting & Data Projection
- **Limpho Semakale** - Steps 7 & 8: Output Reduced Data & Visualization

## 📊 Dataset

- **Source**: Africanized malaria indicators across African countries
- **Original Size**: 594 samples, 27 features
- **Processed Size**: 594 samples, 15 numeric features after cleaning
- **Key Features**: Malaria incidence rates, bed net usage, water/sanitation access, population demographics, geographic coordinates

## 🔬 PCA Implementation Pipeline

### ✅ Steps 1 & 3: Data Loading & Covariance Matrix (Completed)

**Lead**: Mitali Bela

- [x] **Step 1**: Import libraries and load Africanized malaria dataset
- [x] Data cleaning and missing value handling (>50% threshold)
- [x] Feature standardization (mean=0, std=1) using NumPy only
- [x] **Step 3**: Calculate 15×15 covariance matrix from standardized data
- **Output**: 594×15 standardized dataset and covariance matrix ready for eigendecomposition

### 🚧 Step 4: Eigendecomposition (Assigned)

**Lead**: Stecie Niyonzima

- [x] **Step 4**: Perform eigendecomposition of covariance matrix
- [x] Extract eigenvalues and eigenvectors using NumPy
- [x] Display eigenvalues and eigenvector shapes
- **Expected Output**: Eigenvalues and eigenvectors for principal component analysis

### 🚧 Steps 5 & 6: Component Sorting & Data Projection (Assigned)

**Lead**: Charlotte Kariza

- [x] **Step 5**: Sort eigenvectors by eigenvalues (descending order)
- [x] Calculate explained variance ratios
- [x] Select optimal number of principal components
- [x] **Step 6**: Project original standardized data onto selected principal components
- **Expected Output**: Transformed data in reduced dimensionality

### 🚧 Steps 7 & 8: Results & Visualization (Assigned)

**Lead**: Limpho Semakale

- [x] **Step 7**: Display and analyze the reduced dataset
- [x] Output final PCA-transformed data
- [x] **Step 8**: Create before/after PCA visualizations
- [x] Compare original vs. transformed data dimensions
- **Expected Output**: Visual comparison and final analysis

## 🛠️ Setup Instructions

```bash
# Clone repository
git clone <repository-url>
cd malariaInAfrica

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install numpy pandas matplotlib jupyter ipykernel

# Launch Jupyter notebook
jupyter notebook Template_PCA_Formative_1[Peer_Pair_16].ipynb
```

## 📁 Project Structure

```
malariaInAfrica/
├── Template_PCA_Formative_1[Peer_Pair_16].ipynb    # Main PCA implementation
├── DatasetAfricaMalaria.csv                        # Africanized malaria dataset
├── README.md                                       # Project documentation
└── .venv/                                          # Virtual environment
```

## 🔄 Collaboration Workflow

1. **Sequential Development**: Each member builds upon previous steps
2. **Branch Strategy**: Create feature branches for assigned steps
3. **Code Review**: Submit pull requests for team review
4. **Integration**: Regular sync to ensure compatibility
5. **Documentation**: Include clear outputs for each step

## 📋 Progress Tracking

- [x] **Mitali**: Step 1 - Data loading and standardization
- [x] **Mitali**: Step 3 - Covariance matrix calculation
- [ ] **Stecie**: Step 4 - Eigendecomposition implementation
- [ ] **Charlotte**: Step 5 - Principal component sorting
- [ ] **Charlotte**: Step 6 - Data projection onto components
- [ ] **Limpho**: Step 7 - Reduced data output and analysis
- [ ] **Limpho**: Step 8 - Before/after PCA visualization

## 🎯 Learning Objectives

- Implement PCA algorithm from scratch using NumPy
- Apply linear algebra concepts to real African health data
- Practice collaborative software development with Git
- Analyze malaria patterns and relationships across countries
- Understand dimensionality reduction in data science

## 📊 Expected Deliverables

1. **Working PCA Implementation**: Complete Steps 1, 3-8 algorithm
2. **Data Analysis**: Insights from malaria data patterns
3. **Visualizations**: Before/after PCA comparison plots
4. **Documentation**: Clear code comments and outputs
5. **Collaboration Evidence**: Git history showing team contributions

## 🤝 Team Responsibilities

Each team member should:

- Complete assigned steps with clear, commented code
- Ensure outputs are displayed for grading
- Test code thoroughly before committing
- Coordinate with next team member for smooth handoff
- Document any challenges or insights discovered

## 📚 Resources

- [PCA Explained Variance Video](https://www.youtube.com/watch?v=vaF-1xUEXsA&t=17s)
- NumPy documentation for linear algebra functions
- Course materials on eigendecomposition and principal components

---

**Note**: This is Peer Pair 16's collaborative implementation of PCA for the Advanced Linear Algebra formative assignment.
