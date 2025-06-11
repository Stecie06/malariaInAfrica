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

## 📦 Part 3: Python Library - `alumath_matrix`

Our team has successfully developed and published a Python library for matrix multiplication operations to PyPI.

**Group Name**: "matrix" (as in alumath\_**matrix**)  
**Library Name**: `alumath_matrix` (following required pattern: alumath[nameofgroup])

### 🚀 Installation Instructions for Coach

```bash
# Install our published library from PyPI
pip install alumath_matrix
```

### 🧪 Usage Examples - Different Matrix Dimensions

```python
from alumath_matrix.matrix_ops import Matrix

# Test 1: 2x2 matrices
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
result1 = A @ B
print("2x2 × 2x2:", result1.data)  # [[19, 22], [43, 50]]

# Test 2: 2x3 × 3x2 matrices
C = Matrix([[1, 2, 3], [4, 5, 6]])     # 2x3
D = Matrix([[7, 8], [9, 10], [11, 12]]) # 3x2
result2 = C @ D
print("2x3 × 3x2:", result2.data)  # [[58, 64], [139, 154]]

# Test 3: 3x3 × 3x1 matrices
E = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 3x3
F = Matrix([[1], [2], [3]])                      # 3x1
result3 = E @ F
print("3x3 × 3x1:", result3.data)  # [[14], [32], [50]]

# Test 4: 1x4 × 4x2 matrices
G = Matrix([[1, 2, 3, 4]])                       # 1x4
H = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])    # 4x2
result4 = G @ H
print("1x4 × 4x2:", result4.data)  # [[50, 60]]

# Test 5: 4x3 × 3x4 matrices
I = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # 4x3
J = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])    # 3x4
result5 = I @ J
print("4x3 × 3x4:", result5.data)
# Output: [[38, 44, 50, 56], [83, 98, 113, 128], [128, 152, 176, 200], [173, 206, 239, 272]]
```

### ✅ Library Features

- **✅ Published to PyPI**: Available worldwide via `pip install alumath_matrix`
- **✅ Matrix Multiplication**: Handles any compatible dimensions (m×n) × (n×p) → (m×p)
- **✅ Dimension Validation**: Automatic checking with clear error messages
- **✅ Clean API**: Uses Python's `@` operator for intuitive matrix multiplication
- **✅ Professional Packaging**: Proper PyPI metadata and documentation

### 🧪 Quick Verification Test for Coach

```python
# Quick test to verify installation works
from alumath_matrix.matrix_ops import Matrix

# Test case
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
result = A @ B

expected = [[19, 22], [43, 50]]
print("✅ Test passed!" if result.data == expected else "❌ Test failed!")
```

### 🌐 PyPI Package Information

- **Package Name**: `alumath_matrix`
- **Version**: 0.1.0
- **PyPI Page**: https://pypi.org/project/alumath-matrix/
- **Installation**: `pip install alumath_matrix`
- **Author**: Stecie Niyonzima
- **License**: MIT License

**Developed by Peer Group "matrix":**

- **Mitali Bela** - Data preprocessing and PCA implementation
- **Stecie Niyonzima** - Eigendecomposition and library development
- **Charlotte Kariza** - Principal component analysis
- **Elizabeth** - Visualization and results analysis

**GitHub Repository**: https://github.com/Stecie06/malariaInAfrica  
**Course**: Mathematics for Machine Learning - African Leadership University
